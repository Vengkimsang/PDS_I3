def celsius_to_fahrenheit(celcius,round_t0=1):
    far = celcius * 9 / 5 + 32
    return far 
print(celsius_to_fahrenheit(43),"F")

def fahrenheit_to_celsius(fahr,round_to=1):
    celcius = (fahr - 32 ) * 5 / 9
    return celcius 
print(fahrenheit_to_celsius(20),"c")
print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celsius_to_fahrenheit(c):6}")
print("98.6 °F =", fahrenheit_to_celsius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))