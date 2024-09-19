"""
To get User Information
Author: kanchan 
"""
def collect_user_id(id_counter=5000):
    name = input("Enter Your name: ")
    age = int(input("Enter your age: "))
    email = input("Enter your email address: ")
    unique_id = id_counter + 1
    
    
  user_info = {
        "ID": unique_id,
        "Name": name,
        "Age": age,
        "EMAIL": email
    }
    
    

def main(user_info):
    print(f"\n User Information")
    print(f"Unique ID: {user_info['ID']}")
    print(f"Name: {user_info['Name']}")
    print(f"Age: {user_info['Age']}")
    print(f"Email: {user_info['EMAIL']}")

# Collect user information
user_info = collect_user_id()

# Display the information using the main function
main(user_info)


explanation:
1.KISS (Keep It Simple, Stupid)
in this,it Emphasizes simplicity in design and implementation. Avoid unnecessary complexity to enhance readability and maintainability.

2. DRY (Don't Repeat Yourself)
it Encourages reducing duplication in code. Reuse code through functions, classes, or modules to avoid redundancy, making the codebase easier to maintain.

4. YAGNI (You Aren't Gonna Need It)
It Advises against adding functionality until it is necessary. This prevents over-engineering and helps keep the codebase simpler and more manageable.

4.SIngle Responsibility :
IN this,The Single Responsibility Principle states that a class or module should have one, and only one, reason to change. In other words, each class should focus on a single responsibility or functionality.


