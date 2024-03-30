cars = { 
    'BK3638BT': "Nissan Note", 
    'AA7690FR': "Renault Sandero",
    '|777|': "BMW X5",
    'AR4003CC': 'Toyota Avensis'    
}

print(cars['|777|'])

cars['|777|'] = "Tesla Model S"
print(cars)

del cars['AA7690FR']

print(len(cars))

cars['BA4667FF'] = "Range Rover Evoque"

print(cars.keys())
print(cars.values())

if 'AA7690FR' in cars: 
    print("Car is exists!")
else: print("Car does not exist")

for plate in cars:
    print(f"[{plate}] -  Model: {cars[plate]} ")