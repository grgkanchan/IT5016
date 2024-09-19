"""
Author : kanchan 
"""

def collect_user_data(id_counter = 5000):
    #using input to create_user_data
    Name = input("Enter your username:")
    age = int(input("Enter your age:"))
    email = input("Enter your email address:")
    
    unique_id = id_counter +1
    #to display the user information
    user_info = {
        "ID":unique_id,
        "Name":Name,
        "Age":age, 
        "Email":email,       
        }
    return user_info


def main(user_info):
    print("user Information:")
    print(f"unique_ID:{user_info['ID']}")
    print(f"Name:{user_info['Name']}")
    print(f"Age:{user_info['Age']}")
    print(f"Email:{user_info['Email']}")
user_info =collect_user_data()
main(user_info) 

 































 
    
    
    




 
    
    
    