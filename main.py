person = {
    "name" : "alzahraa",
    "age" : 17 ,
    "hobbies" : ["karate and foot ball", 'eat'],
}
print(person["name"])
print(person["age"])

person["age"] = 18
person["country"] = "kuwait"

print(f"hi my name is {person['name']} , iam from {person['country']}, iam {person['age']} years old ,i hope to be a {person['hobbies']} playre")
print(f"{person}")


person["hobbies"].append("swimming")
print(person)



def check_hobbies(person):
    length = len(person['hobbies']) 
    if length >= 3:
        print("wow you are amazing")

check_hobbies(person)

