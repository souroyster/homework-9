def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Invalid input. Please try again."

    return inner

contacts = {}

@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact '{name}' with phone '{phone}' added."

@input_error
def change_phone(name, new_phone):
    contacts[name] = new_phone
    return f"Phone number for '{name}' updated to '{new_phone}'."

@input_error
def get_phone(name):
    return f"The phone number for '{name}' is '{contacts[name]}'."

@input_error
def show_all_contacts():
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    while True:
        command = input("Enter a command: ").lower()

        if command == 'hello':
            print("How can I help you?")
        elif command.startswith('add'):
            _, name, phone = command.split()
            print(add_contact(name, phone))
        elif command.startswith('change'):
            _, name, new_phone = command.split()
            print(change_phone(name, new_phone))
        elif command.startswith('phone'):
            _, name = command.split()
            print(get_phone(name))
        elif command == 'show all':
            print(show_all_contacts())
        elif command in ['good bye', 'close']:
            print("Good bye!")
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
