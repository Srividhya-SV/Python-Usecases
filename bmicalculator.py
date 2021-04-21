import pandas as pd

df = pd.read_json('./input/data_file.json')
bmi_value = pd.Series([])
bmi_category = pd.Series([])
health_risk = pd.Series([])
noOfOverweightCount = 0

def bmi_calculate(height, weight):
    heightinmetre = height  / 100
    bmi = weight / heightinmetre
    return round(bmi, 2)

def bmi_category_healthrisk_finder(bmi):

        if bmi >= 40:
            bmi_category = "Very Severely Obese"
            health_risk = "Very High risk"
        elif (bmi>=35 and bmi<=39.9):
            bmi_category = "Severely Obese"
            health_risk = "High Risk"
        elif (bmi>=30 and bmi<=34.9):
            bmi_category = "Moderately Obese"
            health_risk = "Medium risk"
        elif (bmi>=25 and bmi<=29.9):
            bmi_category = "Overweight"
            health_risk = "Enhanced risk"
        elif (bmi>=18.5 and bmi <=24.9):
            bmi_category = "Normal weight"
            health_risk = "Low risk"
        elif (bmi<=18.4):
            bmi_category = "Underweight"
            health_risk = "Malnutrition risk"

        return bmi_category, health_risk

#Iterating the json data
for i in range(len(df)):
    bmi_value[i] = bmi_calculate(df["HeightCm"][i], df['WeightKg'][i])
    bmi_category[i], health_risk[i] = bmi_category_healthrisk_finder(bmi_value[i])

    if (bmi_category[i] == "Overweight") :
        noOfOverweightCount +=1

#Adding three columns to the table
df.insert(3, "BMI", bmi_value)
df.insert(4, "BMI Category", bmi_category)
df.insert(5, "Health risk", health_risk)

print(df)
print("Over weight people count:" , noOfOverweightCount)