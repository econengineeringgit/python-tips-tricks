### MODEL

users = []


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


### VIEW
def show_users() -> None:
    for user in users:
        print(f"Name: {user.name}")
        print(f"Email: {user.email}")


def view():
    running = True
    while running:
        print("1. Add user")
        print("2. Show users")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            user = add_user(name, email)
            User
            users.append(user)
        elif choice == "2":
            show_users()
        elif choice == "3":
            running = False
        else:
            print("Invalid choice")


### CONTROLLER
def add_user(name: str, email: str) -> User:
    if "@" not in email:
        raise ValueError("Invalid email")
    user = User(name, email)
    return user


if __name__ == "__main__":
    view()
