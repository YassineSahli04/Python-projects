#NAME: Yassine Sahli
#Student Number: 300383586
def celsius_en_fahrenheit(temp_Celsius):
    temp_Fahrenheit = temp_Celsius *(9/5) + 32
    return temp_Fahrenheit

temp_Celsius_1 = 25
temp_Fahrenheit_1 = celsius_en_fahrenheit(temp_Celsius_1)

temp_Celsius_2 = 35
temp_Fahrenheit_2 = celsius_en_fahrenheit(temp_Celsius_2)


print(f"La température de {temp_Celsius_1} en °C est de {temp_Fahrenheit_1} en fahrenheit")
print(f"La température de {temp_Celsius_2} en °C est de {temp_Fahrenheit_2} en fahrenheit")    
