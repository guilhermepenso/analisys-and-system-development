dic_01 = {"name": "Guilherme", "lastName": "Penso", "age": 25}
print(dic_01)

# add new 

dic_01["status"] = True
print(dic_01)

# op with dictionary
dic_01.pop("age")
print(dic_01)

# print keys and values list
print(dic_01.items())

# print only values list
print(dic_01.values())