class User: #Pascal case = fiirst letter of the class is UPPER case 
    # pass the empty class without throeing the error
    def __init__(self, user_id, username):
        print("the user is being created")
        self.id = user_id
        self.username = username

user_1 = User("001","anil kumble ")

user_new = User("0015", "Masti kkaka")
print(user_new.id)

#attributes of a class
user_1.id = "001"
user_1.username = "anirban"

print(user_1.username)

user_2 = User("002", "kaka")

user_2.id = "002"
print(user_2.id)  # Output: 002

user_2.username = "Angella "


#constructor _ what happen to our object 