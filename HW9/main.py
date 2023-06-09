import user
import contact


def log_in():
    while True:
        choice1 = input("1)Sing up\n2)Log in\n3)modify\n4)Quit\nplease select:")
        if choice1 == "1":
            user.User.creating()
            print(user.User.read_users_file())
            break
        elif choice1 == "2":
            print(user.User.authenticating())
            break
        elif choice1 == "3":
            user.User.modifying()
            break
        elif choice1 == "4":
            break
        else:
            print("invalid input, try again")


def main():
    log_in()
    while True:
        choice = input("1) View all contacts\n2)Add a new contact\n3)Edit an existing contact\n4)Delete contact"
                       "\n5)Export CSV\n6)import CSV\n7)Search contact\n8)Quit\nselect option:")
        if choice == "1":
            print(contact.Contact.read_contact())
            break
        elif choice == "2":
            contact.Contact.add_contacts()
            break
        elif choice == "3":
            contact.Contact.edit_contacts()
            break
        elif choice == "4":
            contact.Contact.delete_contacts()
            break
        elif choice == "5":
            contact.Contact.export_csv()
            break
        elif choice == "6":
            contact.Contact.import_csv()
            break
        elif choice == "7":
            contact.Contact.search_contact()
            break
        else:
            print("invalid choice, please try again")



if __name__ == "__main__":
    main()
