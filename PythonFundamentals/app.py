print("Welcome to Learning and Masterying Python")

# Variables
# primitive types
student_count = 1000  # Int
rating = 4.99  # Float
is_published = False  # Boolean
course_name = "pyThon proGramming"  # String
# Varible names should be descriptive and meaningful
user_name = "Robert Doe"
user_message = f"""Hi {user_name}, 
Did you read the email regarding\n the changes to the payment feature"""
user_message_length = len(user_message)
print(user_message_length)
print(user_message[0:5])
print(user_message)

# String methods
print(course_name.lower())
print(course_name.capitalize())
print(course_name.find("pro"))
print(course_name.title())
print(course_name.replace("p", "j"))
print("pro" in course_name)  # this is an expression returning a value --> Boolean
print("swift" not in course_name)
