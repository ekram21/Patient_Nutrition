'''Contains functions to create database and tables - is a library'''

import sqlite3


def Create_All_Software_DatabaseAndTables():
	print ('Creating the databases for the software..')
	# conn= connection_to_database
	conn = Create_And_Connect_FixedDatabase()

	Create_PatientInformation(conn)

	Create_Recommendation(conn)

	conn.close()

def Create_And_Connect_FixedDatabase():
	conn = sqlite3.connect('fixedDatabase.db')
	return (conn)




def Create_GeneralNutrition_Table(conn):
	print("Creating GeneralNutrition database for the software..")
	c = conn.cursor()

	c.execute('''DROP TABLE IF EXISTS GeneralNutrition''')

	# Create table
	c.execute('''CREATE TABLE IF NOT EXISTS GeneralNutrition(Age INTEGER, 
															Weight INTEGER,
															Height INTEGER, 
															Protein INTEGER, 
															Carbohydrates INTEGER,  
															Fats INTEGER,  
															Sugar INTEGER)''')

	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	# conn.close()


def Create_DiseaseRestrictions_table(conn):

	print("Creating DiseaseRestrictions database for the software..")

	c = conn.cursor()

	c.execute('''DROP TABLE IF EXISTS DiseaseRestrictions''')

	c.execute('''CREATE TABLE IF NOT EXISTS DiseaseRestrictions(Disease_Name TEXT,Protein TEXT,Carbohydrates TEXT,Fats TEXT,Sugar TEXT)''')

	# Save (commit) the changes
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.


def Create_Recommendation(conn):

	print("Creating Recommendation database for the software..")

	c = conn.cursor()

	c.execute('''DROP TABLE IF EXISTS Recommendation''')

	c.execute('''CREATE TABLE IF NOT EXISTS Recommendation(NAME TEXT,
																	Protein TEXT,
																	Carbohydrates TEXT,
																	Fats TEXT,
																	DEE TEXT)''')
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.



def Create_PatientInformation(conn):

	print("Creating PatientInformation database for the software..")

	c = conn.cursor()

	c.execute('''DROP TABLE IF EXISTS PatientInformation''')

	c.execute('''CREATE TABLE IF NOT EXISTS PatientInformation(NAME TEXT,
																	GENDER TEXT,
																	AGE TEXT,
																	WEIGHT TEXT,
																	HEIGHT TEXT,
																	DISEASE TEXT)''')
	conn.commit()

	# We can also close the connection if we are done with it.
	# Just be sure any changes have been committed or they will be lost.
	







