import pickle
import csv
import re

filename = "contacts_file.pickle"


class Contact:
    def __init__(self, name: str = None, email: str = None, phone: str = None):
        self.name = name
        self.email = email
        self.phone = phone
        self.contact = [name, email, phone]

    @staticmethod
    def check(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if re.search(regex, email):
            print("Valid Email")
        else:
            print("Invalid Email")

    @classmethod
    def check_phone(phone):
        regex_phone = '^(\+98|0)?9\d{9}$'
        if re.search(regex_phone, phone):
            print("valid password")
        else:
            print("invalid phone")

    @staticmethod
    def write_contact(contact):
        # name = input("name:")
        # email = input("email:")
        # phone = input("phone:")
        # contact = [name,email,phone]
        with open(filename, "+ab") as contacts_file:
            pickle.dump(contact, contacts_file)

    @staticmethod
    def read_contact():
        data = []
        with open(filename, "rb") as file:
            while True:
                try:
                    data.append(pickle.load(file))
                except EOFError:
                    break
        return data

    @staticmethod
    def add_contacts():
        name = input("enter new name:")
        email = input("enter new email")
        phone = input("enter new phone")
        contact = [name, email, phone]
        Contact.check(email)
        Contact.write_contact(contact)

    @staticmethod
    def edit_contacts():
        update_contact = []
        data = Contact.read_contact()
        while True:
            choice = input("Do you want edit contact? yes/no")
            if choice == "yes":
                desired_contact = input("which contact do you want to chang? enter name or phone or email:")
                if desired_contact not in data:
                    print("The contact doesn't exist")
                    break
                else:
                    change_option = input("1)name\n2)phone\n3)email:")
                    if change_option == "1":
                        new_name = input("enter new name:")
                        update_contact.append(new_name)
                        self.name = new_name
                    elif change_option == "2":
                        new_phone = input("enter new phone:")
                        update_contact.append(new_phone)
                        self.phone = new_phone
                    elif change_option == "3":
                        new_email = input("enter new email:")
                        update_contact.append(new_email)

                        self.email = new_email
                    else:
                        print("invalid input, try again")
                        continue
            elif choice == "no":
                break
            else:
                print("invalid input,try again")
                continue
        print(update_contact)

    @staticmethod
    def delete_contacts():
        print("Are you sure you want to delete?yes or no")
        ch = input("select yes or no:")
        if ch == "yes":
            remove_name = input("Enter the desired user: ")
            data = Contact.read_contact()
            for word in data:
                if remove_name in word[0]:
                    new_data = data.remove(word)
                    print(new_data)
                # else:
                #     print("This contact doesn't exist")
        elif ch == "no":
            print("that's OK")
        else:
            print("invalid input, try again")

    @staticmethod
    def export_csv():
        data = Contact.read_contact()
        with open("csvfile.csv", "w") as my_contact:
            writer = csv.writer(my_contact)
            writer.writerow(["contact_name", " contact_phone", "contact_mail"])
            writer.writerows(data)

    @staticmethod
    def import_csv():
        with open("csvfile.csv") as my_contact:
            my_data = csv.reader(my_contact)
            for line in my_data:
                print(line)

    @staticmethod
    def search_contact():
        data = Contact.read_contact()
        print(data)
        while True:
            ch = input("Which item do you want to search?\n1)name\n2)phone\n3)e-mail\n enter your choice: ")
            if ch == "1":
                name = input("enter contact_name:")
                for word in data:
                    if name in word[0]:
                        print(f"{word} is exist")
                    else:
                        print(f"{word[0]} is not exist")
                        break
            elif ch == "2":
                email = input("enter contact_phone:")
                for word in data:
                    if email in word[1]:
                        print(f"{word} is exist")
                    else:
                        print(f"{word[1]} is not exist")
                        break
            elif ch == "3":
                phone = input("enter contact_email:")
                for word in data:
                    if phone in word[2]:
                        print(f"{word} is exist")
                    else:
                        print(f"{word[2]} is not exist")
                        break
            else:
                print("invalid input, try again")
                continue


# c = Contact("shahrzad", "kjdas@.cde", "093128")
# c2 = Contact("mahshid", "jkhasd@jdfdsfb", "23891273126412")
# c3 = Contact()
# c3.add_contacts()
# # c.write_contact()
# c2.write_contact()
# c3.write_contact()
# c.delete_contacts()
# print(c3.read_contact())
# c3.export_csv()
# c.import_csv()
# c.search_contact()
