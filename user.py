class User:
    def __init__(self,username,email_address,other_user):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        self.other_user = other_user

    def make_deposit(self,amount):
        self.account_balance += amount

    def make_withdrawal(self,amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print("User: ",self.name,"Balance: $",self.account_balance)

    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount

hakeem = User("prince hakeem", "onlyjuicesandberries@yahoo.com", "king")
semmi = User("semmi", "iamtherealprince@gmail.com", "none")
king = User("king jaffe joffer", "rullerofzamunda@comcast.net", "hakeem")

hakeem.make_deposit(330)
hakeem.make_deposit(50)
hakeem.make_deposit(80)
hakeem.make_withdrawal(150)

hakeem.display_user_balance()

semmi.make_deposit(25)
semmi.make_deposit(35)
semmi.make_withdrawal(30)
semmi.make_withdrawal(40)

semmi.display_user_balance()

king.make_deposit(25000)
king.make_withdrawal(500)
king.make_withdrawal(1500)
king.make_withdrawal(3500)

king.display_user_balance()

hakeem.transfer_money(king,200)
hakeem.display_user_balance()
king.display_user_balance()