import pickle
import getpass
filename = "users_file.pickle"


class User:
    def __init__(self, username: str = None, password: str = None):
        self.username = username
        self.password = password

    @staticmethod
    def creating():
        user_pass = []
        data = User.read_users_file()
        while True:
            user_name = input("Enter  Username : ")
            pass_word = input("Enter  Password : ")
            choice = input("are you sure ?yes or no ")
            if choice == "yes":
                user_pass.append(user_name)
                user_pass.append(pass_word)
                if user_pass in data:
                    print("username or password was exist, enter another value")
                    continue
                else:
                    break
            elif choice == "no":
                continue
            else:
                print("invalid choice, please try again")
        with open(filename, "+ab") as userpass_file:
            pickle.dump(user_pass, userpass_file)
        return user_pass

    @staticmethod
    def read_users_file():
        data = []
        with open(filename, "rb") as file:
            while True:
                try:
                    data.append(pickle.load(file))
                except EOFError:
                    break
        return data

    @staticmethod
    def authenticating():
        data = User.read_users_file()
        username = input("enter your username:").lower()
        password = input("enter your password:").lower()
        my_account = [username, password]
        if my_account in data:
            print("valid user")
            return my_account
        else:
            return "invalid user, please check username and password and try again later"

    @staticmethod
    def modifying():
        update_user = []
        data = User.read_users_file()
        # print(data)
        while True:
            c = User.authenticating()
            print(c)
            if c:
                while True:
                    choice = input("Do you want modify username or password? yes/no?")
                    if choice == "yes":
                        change_option = input("Which one do you want to change?\n1)username\n2)password\n3)both"
                                              "\nenter 1 or 2 or 3:")
                        if change_option == "1":
                            new_username = input("enter new username:")
                            update_user.append(new_username)
                            update_user.append(c[1])
                            print(update_user)
                            continue
                        elif change_option == "2":
                            new_password = input("enter new password:")
                            update_user.append(c[0])
                            update_user.append(new_password)
                            print(update_user)
                        elif change_option == "3":
                            new_username = input("enter new username:")
                            new_password = input("enter new password:")
                            update_user.append(new_username)
                            update_user.append(new_password)
                            print(update_user)
                        else:
                            print("invalid input, try again")
                            continue

                    elif choice == "no":
                        break
                    else:
                        print("invalid input,try again")
                        continue
                break
            else:
                print("The user is not valid")
                break
        return update_user
    #
    # @staticmethod
    # def replace_userpass():
    #    old_data = User.read_users_file()
        u





# while True:
#     choice = input("")
# u1 = User()
# u1.creating()
# print(u1.read_users_file())
# u1.authenticating()
# u1.modifying()
# name_file = open("username_password", "rb")
# ex = pickle.load(name_file)
# print(ex)
# u1.replace_userpass()

