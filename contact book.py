class ContactBook:
    def __init__(self):
        self.contacts = {
            'Sekhar': {'phone': '9988665511', 'email': 'sekhar@gamail.com', 'address': 'tadipatri'},
            'Indra': {'phone': '9876543210', 'email': 'indra@gmail.com', 'address': 'ananthapur'},
            'Sai': {'phone': '8745698745', 'email': 'sai@gmail.com', 'address': 'tirupathi'}
        }

    def add_contact(self, name, phone, email, address):
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print(f"Contact {name} added successfully!")

    def view_contact(self, name):
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}")
        else:
            print(f"Contact {name} not found.")

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for name, contact in self.contacts.items():
                print(f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}\n")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"Contact {name} not found.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. List Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            address = input("Enter the address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            name = input("Enter the name to view: ")
            contact_book.view_contact(name)
        elif choice == '3':
            contact_book.list_contacts()
        elif choice == '4':
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
