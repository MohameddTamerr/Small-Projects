class user():
    def __init__(self, name, age, gender, email):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.password= 123

    def show_details(self):
        print("The Personal Details: ")
        print("Your Name: ", self.name)
        print("Your Age: ", self.age)
        print("Your Gender: ", self.gender)
        print("Your Email: ", self.email)

class bank_process(user):
    def __init__(self, name, age, gender, email):
        super().__init__(name, age, gender ,email)
        self.balance = 20000
        self.password = 12345
        self.password_attempts = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("The Transaction Is Successfully, The Balance Has Been Updated")

    def withdraw(self, amount):
        if amount > self.balance - 5:
            print("Sorry, you don't have enough money.")
        else:
            self.balance -= 5
            self.balance -= amount
            print("Successfully your credit now is ",self.balance)

    def check_password(self, password_attempt):
        if password_attempt == self.password:
            self.password_attempts = 0
            return True
        else:
            self.password_attempts += 1
            print("Incorrect password. Try again.")
            if self.password_attempts == 3:
                print("Too many password attempts. Exiting program.")
                exit()

    def change_password(self):
        i = 0
        while i < 3:
            old_password = int(input("Enter your old password: "))
            if self.check_password(old_password):
                new_password = int(input("Enter your new password: "))
                self.password = new_password
                print("Password successfully changed.")
                break
            else:
                i += 1
        if i == 3:
            print("Too many attempts. Exiting program.")
            exit()



