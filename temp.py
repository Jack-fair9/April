# Temperature in degrees Fahrenheit (°F) = (Temperature in degrees Celsius (°C) * 9/5) + 32.
def celsius_to_fahrenheit (celsuius):
    ftemp = (celsuius * 9/5) + 32
    return ftemp

celsuius = 25
ftemp = celsius_to_fahrenheit(celsuius)
ftemp = round(ftemp)
print(f'25 degrees celsius to fahrenheit is {ftemp}')

fah = 82


def fahrenheit_to_celsius (fah):
    ctemp =  5/9 * (fah - 32)
    return ctemp

ctemp = fahrenheit_to_celsius(fah)
ctemp = round(ctemp)
print(f"fahrenheit of 82 is {ctemp} in celsius")






    