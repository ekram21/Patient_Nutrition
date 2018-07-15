








def calculateMacro(age, weight, height, gender):
	'''
	returns an array of protein, Fats, carb
	'''
	NutrientArray = []
	if (gender.lower() == 'male'):
		DEE= 66.5 + 13.8* (weight) + 5* (height) + 6.8*(age)

	elif (gender.lower() == 'female'):
		DEE = 655.1 + 9.6* (weight) + 1.9* (height) + 4.7* (age)

	gp = 1.82* (weight)
	Protein = gp/4
	Protein = round(Protein, 2)
	NutrientArray.append(Protein)
	
	gf = (0.25*DEE)
	Fats = gf/9
	Fats = round(Fats, 2)
	NutrientArray.append(Fats)

	pf = gf+gp

	gc = DEE-pf
	Carbs = gc/4
	Carbs = round(Carbs, 2)
	NutrientArray.append(Carbs)

	return DEE,NutrientArray


def Cardiovascular(age, weight, height, gender):

	result_Macro = calculateMacro(age, weight, height, gender)
	DEE = result_Macro[0]
	Nutrient_Array = result_Macro[1]

	gp = 1.82* (weight)
	Protein = Nutrient_Array[0]
	Protein = round(Protein, 2)

	gf=(0.3*DEE) 
	Fats= gf/9
	Fats = round(Fats, 2)

	pf = gf +gp

	gc= DEE - pf
	Carbs= gc/4
	Carbs = round(Carbs, 2)

	return Protein, Fats, Carbs



def hypertension(age, weight, height, gender):

	result_Macro = calculateMacro(age, weight, height, gender)
	DEE = result_Macro[0]

	gp = 0.18* DEE
	Protein = gp/4
	Protein = round(Protein, 2)

	gf=(0.27*DEE) 
	Fats= gf/9
	Fats = round(Fats, 2)

	gc= (0.55*DEE)
	Carbs= gc/4
	Fats = round(Fats, 2)

	return Protein, Fats, Carbs


def DiabetesType1(age, weight, height, gender):

    result_Macro = calculateMacro(age, weight, height, gender)
    DEE = result_Macro[0]
    Nutrient_Array = result_Macro[1]

    gp = 1.82* (weight)
    Protein = Nutrient_Array[0]
    Protein = round(Protein, 2)

    gf=(0.275*DEE) 
    Fats= gf/9
    Fats = round(Fats, 2)

    pf = gf +gp

    gc= DEE - pf
    Carbs= gc/4
    Carbs = round(Carbs, 2)

    return Protein, Fats, Carbs

def DiabetesType2(age, weight, height, gender):

	result_Macro = calculateMacro(age, weight, height, gender)
	DEE = result_Macro[0]

	gp = 0.25* (DEE)
	Protein = gp/4
	Protein = round(Protein, 2)

	gf=(0.25*DEE) 
	Fats= gf/9
	Fats = round(Fats, 2)

	pf = gf +gp

	gc= DEE - pf
	Carbs= gc/4
	Carbs = round(Carbs, 2)

	return Protein, Fats, Carbs

def Kwashiorkor(age, weight, height, gender):

    result_Macro = calculateMacro(age, weight, height, gender)
    DEE = result_Macro[0]

    gp = (0.11*DEE)
    Protein = gp/4
    Protein = round(Protein, 2)

    gf=(0.25*DEE) 
    Fats= gf/9
    Fats = round(Fats, 2)

    pf = gf +gp

    gc= DEE - pf
    Carbs= gc/4
    Carbs = round(Carbs, 2)

    return Protein, Fats, Carbs

def KidneyDisease_Stage1_2(age, weight, height, gender):

    result_Macro = calculateMacro(age, weight, height, gender)
    DEE = result_Macro[0]

    gp = (0.18*DEE)
    Protein = gp/4
    Protein = round(Protein, 2)

    gf=(0.3*DEE) 
    Fats= gf/9
    Fats = round(Fats, 2)

    gc= (0.55*DEE)
    Carbs= gc/4
    Carbs = round(Carbs, 2)

    return Protein, Fats, Carbs

def KidneyDisease_Stage2_4(age, weight, height, gender):

    result_Macro = calculateMacro(age, weight, height, gender)
    DEE = result_Macro[0]

    gp = (0.10*DEE)
    Protein = gp/4
    Protein = round(Protein, 2)

    gf=(0.3*DEE) 
    Fats= gf/9
    Fats = round(Fats, 2)

    gc= (0.55*DEE)
    Carbs= gc/4
    Carbs = round(Carbs, 2)

    return Protein, Fats, Carbs


def ChooseDiseaseFunction(InputDisease, age, weight, height, gender):
	if InputDisease=="Cardiovascular":
		output = Cardiovascular(age, weight, height, gender)

		return output

	elif InputDisease=="Hypertension":
		output = hypertension(age, weight, height, gender)

		return output

	elif InputDisease=="DiabetesType1":
		output = DiabetesType1(age, weight, height, gender)

		return output

	elif InputDisease=="DiabetesType2":
		output = DiabetesType2(age, weight, height, gender)

		return output

	elif InputDisease=="Kwashiorkor":
		output = Kwashiorkor(age, weight, height, gender)

		return output

	elif InputDisease=="KidneyDisease_Stage1_2":
		output = KidneyDisease_Stage1_2(age, weight, height, gender)

		return output

	elif InputDisease=="KidneyDisease_Stage2_4":
		output = KidneyDisease_Stage2_4(age, weight, height, gender)

		return output




# if __name__ == '__main__':
# 	lol = calculateMacro(25, 80, 160, 'Male')
# 	print (lol)










