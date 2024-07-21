"""task 4"""

from typing import Callable, Dict, List, Tuple


def input_error(func: Callable) -> Callable:
    """
    Decorator to handle common input errors for bot commands.

    Args:
        func (Callable): The function to decorate.

    Returns:
        Callable: The wrapped function with error handling.
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Name not found in contacts."
        except IndexError:
            return "Enter user name."

    return inner


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parse user input into a command and its arguments.

    Args:
        user_input (str): The raw input from the user.

    Returns:
        Tuple[str, List[str]]: The command and list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Add a new contact to the contacts dictionary.

    Args:
        args (List[str]): List containing name and phone number.
        contacts (Dict[str, str]): The contacts dictionary.

    Returns:
        str: Success message.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Change the phone number of an existing contact.

    Args:
        args (List[str]): List containing name and new phone number.
        contacts (Dict[str, str]): The contacts dictionary.

    Returns:
        str: Success or error message.
    """
    name, phone = args
    if contacts[name]:
        contacts[name] = phone
        return f"Contact {name} updated."


@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Show the phone number of a contact.

    Args:
        args (List[str]): List containing the name.
        contacts (Dict[str, str]): The contacts dictionary.

    Returns:Enter the argument for the command
        str: The phone number or an error message.
    """
    name = args[0]
    if contacts[name]:
        return f"{contacts[name]}"


@input_error
def show_all(contacts: Dict[str, str]) -> str:
    """
    Show all contacts.

    Args:
        contacts (Dict[str, str]): The contacts dictionary.

    Returns:
        str: All contacts formatted as a string, or an error message if empty.
    """
    if not contacts:
        return "Sorry, your phone book is empty."
    else:
        all_contacts = ""
        for name, phone in contacts.items():
            all_contacts += f"{name:<15} - {phone}\n"
        return all_contacts.strip()


def main():
    """
    Main function to run the assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
