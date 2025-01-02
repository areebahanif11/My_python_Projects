contact_book = {"areeba":12388748, "laiba":237637647,
                "amna":2376478747, "papa":162763774,
                 "mama":7367467646, "bhai":6358746876,
                  "czn":7848684898, "friend":76478638787}

def contact_list():
    # print(contact_book.keys())
    print("Contact names:")
    for name in contact_book.keys():
        print(name)

def search_contact():
    name = input("Enter name to find phone number : ").lower()
    if name in contact_book:
        print(f"Phone no : {contact_book.get(name)}")
    else:
        print("Not found this name")

def update_contact():
    new_name = input("Enter name you want to update :").lower()
    new_number = int(input("Enter number : "))
    contact_book.update({new_name:new_number})
    print(f"Updated contact {new_name} with {new_number} ")
    print("Now updated contact book is : ", contact_book)


def delete_contact():
    del_name = input("Enter contact name to delete : ")
    if del_name in contact_book:
        print(f"This contact number has been deleted : {contact_book.pop(del_name)}")
    else:
        print("Not found this contact name")

while True:
    print("\nContact Book Menu:")
    print("1. Display Contacts")
    print("2. Search a name")
    print("3. Change or add a contact")
    print("4. Delete a contact")
    print("5. Exit")

    choice = int(input("Enter your choice : "))
    if choice==1 : 
        contact_list()

    elif choice==2 :
        search_contact()

    elif choice==3 :
        update_contact()

    elif choice==4 :
        delete_contact()

    elif choice==5:
        print("Exit")
        break
    else:
        print("Invalid choice ")
