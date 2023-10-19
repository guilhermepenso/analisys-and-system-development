car = {}
car["brand"] = input("Write the brand: ")
car["model"] = input("Write the model: ")
car["value"] = float(input("Write the value: "))
car["renavam"] = input("Write the renavam: ")
car["owner"] = input("Write the owner: ")
car["year"] = int(input("Write the year: "))
car["chassis"] = input("Write the chassis: ")
print (car)

# change owner
car["owner"] = input("Write the new owner: ")
print (car)

# delete chassis
del(car["chassis"])
print (car)

# delete all
car.clear()
print (car)