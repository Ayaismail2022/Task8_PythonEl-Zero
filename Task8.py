"""
Task 8
"""
name = input("Enter your name: ").strip().capitalize()
print(f"Hello {name}, Happy To See You Here.")

print("-"*20)

age = int(input("Enter your age: "))

if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

print("-"*20)

first_name = input("Enter Your First Name: ").strip().capitalize()
last_name = input("Enter Your Last Name: ").strip().capitalize()
 # Example "Osama M."
print(f"Hello {first_name} {last_name:.1s}, Happy To See You Here.")

print("-"*20)

email = input("Enter Your Email: ").strip().lower()
print("Your name Is ", email[:email.index("@")].capitalize())
print("Email Service Provider Is ", email[email.index("@") + 1:email.index(".")])
print("Email Domain Is ", email[email.index(".") + 1:])
