from math import ceil

People = int(input("How many people need transporting?"))
TaxiCapacity = int(4)
TaxisNeeded = (People / TaxiCapacity)
TaxisNeeded = ceil(TaxisNeeded)
print(f"You will need {TaxisNeeded} taxis")