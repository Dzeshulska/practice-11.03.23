data_base = []



#   import random
#   print(random.randint(0, 1000))
#   print


def registration(user_name, user_age, user_wallet) :
    return{
        "name" : user_name,
        "age" : user_age,
        "wallet" : user_wallet
    }

user_name = input("Enter your name")
user_age = input("Enter your age")

if len(user_name ) > 2 and int(user_age) > 18 :    
    data_base.append([user_name] + [user_age] )
    print(data_base)
else:
    print("Error")

def autorization(array_of_date_base) :
    for user in array_of_date_base :
        print(user)
    



