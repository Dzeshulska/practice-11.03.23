data_base = [
    {
    "name": "Alla",
     "age" : "25",
     "Wallet" : "150"
     },
     {
    "name" : "Ivan",
     "age" : "35",
     "wallet" : "250"
     },
     {"login" : "tn@.",
      "password" : "12325"
     }
]

for user in data_base:
    print(user)

login = input("Enter your login")
password = input("Enter your password")
user = registration(login, pasword)
print(user)

if age < 18 and len(name) < 2 and wallet < 0:
    print("Error")
else:
    print("Great!")

    import random
    print(random.randint(0, 1000))
    print