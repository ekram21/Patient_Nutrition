'''
Author: Ekram
Date: June 20th 2018
A flask based html/JS application for database management of patient nutrition
Made for Brac Computer Engineering Thesis 2018
'''

#Importing all the relevant stuff
from flask import Flask, request, render_template
import os
import json
import socket
from misc import *
from Calculations import *

# Initialize the Flask application
app = Flask(__name__)

def ReturnOwnIpAddress():
    hostname = socket.gethostname()
    IP = socket.gethostbyname(hostname)
    return (str(IP))

global IP_Address
global Port_Number
 
IP_Address = '127.0.0.1'
Port_Number = 7000


@app.route('/')
def home():
	global IP_Address
	global Port_Number	

	return render_template('login.html', IP_Address=IP_Address, Port_Number=Port_Number)


@app.route('/Choose')
def Choose():

	global IP_Address
	global Port_Number

	Table_Names_Array = Get_All_TableNames('FixedDatabase')

	CraftedName_String = ''

	for elem in Table_Names_Array:
		CraftedName_String = CraftedName_String + elem + ';'

	return render_template('Table_Choose.html', CraftedName_String=CraftedName_String, IP_Address=IP_Address, Port_Number=Port_Number)

@app.route('/<TableName>')
def index(TableName):

	global IP_Address
	global Port_Number

	#Table Heading section
	Table_Headings = Get_Table_Headings_From_Table('FixedDatabase', TableName)
 
	CraftedHeading_String = ''

	for elem in Table_Headings:
		CraftedHeading_String = CraftedHeading_String + elem + ';'

	#tabe data section
	Table_Data = Get_Data_From_Table('FixedDatabase', TableName)

	CraftedFinalData_String = ''

	CraftedInterim_String = ''

	for row in Table_Data:
		for box in row:
			CraftedInterim_String = CraftedInterim_String + str(box) + ','

		CraftedFinalData_String = CraftedFinalData_String + CraftedInterim_String + ';'
		CraftedInterim_String = ''

	return render_template('table.html', TableName=TableName, CraftedHeading_String=CraftedHeading_String, CraftedFinalData_String=CraftedFinalData_String, IP_Address=IP_Address, Port_Number=Port_Number)


@app.route('/signUpUser', methods=['POST'])
def signUpUser():
	data_row_input_array = []
	MetaHeading_Data =  request.form['meta_Data']
	#Making the above into an array
	MetaHeading_Data_Array = MetaHeading_Data.split(',')[0:-1]

	#The last element was the table name
	Meta_Table_name = str(MetaHeading_Data.split(',')[-1]) 

	for heading in MetaHeading_Data_Array:
		current_data = request.form[str(heading)]
		data_row_input_array.append(current_data)

	#now insert this row of data into the sql table
	Insert_RowOFData_in_Table('fixedDatabase', Meta_Table_name, data_row_input_array)

	return json.dumps(data_row_input_array)

@app.route('/RecomInput_Response', methods=['POST'])
def RecomInput_Response():
	data_row_input_array = []
	recommendation_table_data = []
	#get the data from all the input forms..
	PatientName_Data =  request.form['PatientName']
	PatientAge_Data = request.form['PatientAge']
	PatientWeight_Data = request.form['PatientWeight']
	PatientHeight_Data = request.form['PatientHeight']
	PatientDisease_Data = request.form['meta_disease_data']
	PatientGender_Data = request.form['meta_gender_data']

	data_row_input_array.append(PatientName_Data)
	data_row_input_array.append(PatientGender_Data)
	data_row_input_array.append(PatientAge_Data)
	data_row_input_array.append(PatientWeight_Data)
	data_row_input_array.append(PatientHeight_Data)
	data_row_input_array.append(PatientDisease_Data)

	#now insert this row of data into the sql table
	Insert_RowOFData_in_Table('fixedDatabase', 'PatientInformation', data_row_input_array)

	#Run it through our calculation algorithm
	Result = ChooseDiseaseFunction(PatientDisease_Data, int(PatientAge_Data), int(PatientWeight_Data), int(PatientHeight_Data), PatientGender_Data)
	data_row_input_array.append(Result[0])
	data_row_input_array.append(Result[1])
	data_row_input_array.append(Result[2])

	#Update recommendation table
	recommendation_table_data.append(PatientName_Data)
	recommendation_table_data.append(Result[0])
	recommendation_table_data.append(Result[1])
	recommendation_table_data.append(Result[2])
	recommendation_table_data.append('Placeholder_DEE')

	Insert_RowOFData_in_Table('fixedDatabase', 'Recommendation', recommendation_table_data)

	return json.dumps(data_row_input_array)

@app.route('/Clear/<TableName>')
def Clear(TableName):

	#clear this current table of all data first
	Clear_Specified_Table('fixedDatabase', TableName)

	global IP_Address
	global Port_Number

	#Table Heading section
	Table_Headings = Get_Table_Headings_From_Table('FixedDatabase', TableName)
 
	CraftedHeading_String = ''

	for elem in Table_Headings:
		CraftedHeading_String = CraftedHeading_String + elem + ';'

	#tabe data section
	Table_Data = Get_Data_From_Table('FixedDatabase', TableName)

	CraftedFinalData_String = ''

	CraftedInterim_String = ''

	for row in Table_Data:
		for box in row:
			CraftedInterim_String = CraftedInterim_String + str(box) + ','

		CraftedFinalData_String = CraftedFinalData_String + CraftedInterim_String + ';'
		CraftedInterim_String = ''

	return render_template('table.html', TableName=TableName, CraftedHeading_String=CraftedHeading_String, CraftedFinalData_String=CraftedFinalData_String, IP_Address=IP_Address, Port_Number=Port_Number)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
	#Saving the submitted excel file locally
	if request.method == 'POST':
		f = request.files['Excel_File']
		MetaHeading_Data =  request.form['meta_import']
		f.save(MetaHeading_Data + '.xlsx')

	#extracting all data in excel file as a 2D array
	file_Name = str(MetaHeading_Data) + '.xlsx'
	dataSet = Get_All_Data_From_Excel_File(file_Name, 'Sheet1')

	global IP_Address
	global Port_Number

	TableName = MetaHeading_Data

	#Inserting the above obtained data from excel file into the sql table
	for row_ in dataSet:
		Insert_RowOFData_in_Table('FixedDatabase', TableName, row_)


	#Obtaining all data such as headings and cell data from sql tables

	#Table Heading section
	Table_Headings = Get_Table_Headings_From_Table('FixedDatabase', TableName)
 
	CraftedHeading_String = ''

	for elem in Table_Headings:
		CraftedHeading_String = CraftedHeading_String + elem + ';'

	#tabe data section
	Table_Data = Get_Data_From_Table('FixedDatabase', TableName)

	CraftedFinalData_String = ''

	CraftedInterim_String = ''

	for row in Table_Data:
		for box in row:
			CraftedInterim_String = CraftedInterim_String + str(box) + ','

		CraftedFinalData_String = CraftedFinalData_String + CraftedInterim_String + ';'
		CraftedInterim_String = ''

	#Delete the accepted excel file
	os.remove(file_Name)

	return render_template('table.html', TableName=TableName, CraftedHeading_String=CraftedHeading_String, CraftedFinalData_String=CraftedFinalData_String, IP_Address=IP_Address, Port_Number=Port_Number)


if __name__ == '__main__':

    app.run(host=IP_Address,port=Port_Number, debug=True)





