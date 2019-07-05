class User:
    def __init__(self,username,email_address,other_user):
        self.name = username
        self.email = email_address
        self.account_balance = 0
        self.other_user = other_user
        
    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self,amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print("user: ",self.name,"balance: $",self.account_balance)
        return self
    def transfer_money(self,other_user,amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self
        

hakeem = User("prince hakeem", "onlyjuicesandberries@yahoo.com", "king")
semmi = User("semmi", "iamtherealprince@gmail.com", "none")
king = User("king jaffe joffer", "rullerofzamunda@comcast.net", "hakeem")

hakeem.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()


semmi.make_deposit(25).make_deposit(35).make_withdrawal(30).make_withdrawal(40).display_user_balance()

king.make_deposit(25000).make_withdrawal(500).make_withdrawal(1500).make_withdrawal(3500).display_user_balance()

hakeem.transfer_money(king,200).display_user_balance()
king.display_user_balance()