import json

# Function to load users from a JSON file
def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


# Function to save users to a JSON file
def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Function to register a user
def register_user(users):
    username = input("Enter username: ")
    password = input("Enter password: ")
    users[username] = password
    save_users(users)  
    print("Registration successful.")

# Function to display registered users
def show_users(users):
    if not users:
        print("No registered users.")
    else:
        print("Registered users:")
        for username, password in users.items():
            print("Username:", username)
            print("Password:", password)
            print("---------------")

# Function for user login
def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful.")
    else:
        print("Incorrect username or password.")

# Load existing users from the JSON file
users = load_users()

# Main menu
while True:
    print("1. Register User")
    print("2. Show Registered Users")
    print("3. Login")
    print("4. Exit")
    option = input("Select an option: ")

    if option == "1":
        register_user(users)
    elif option == "2":
        show_users(users)
    elif option == "3":
        login(users)
    elif option == "4":
        save_users(users)
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")