
# user_name = "arbaj07"
# password = 786786
# user_name = input("enter your user name:")
# password = int(input("enter your password:"))
# attempts = 3
# if user_name == "arbaj07" and password == 786786:
#     print("user name is correct", user_name)
# elif user_name != "arbaj07"  and password != 786786:
#     print(attempts -1, "attempts left")


# else:
#     print("user name and password are incorrect")


      

# Problem number 2
 
# otp = {
#     "otp": 483920
# }
# attempts = 3
# locked = set()
# while True:
#     user_otp = int(input("enter the otp:"))
#     if user_otp == otp["otp"]:
#         print("otp is correct")
#         break
#     elif user_otp != otp["otp"]:
#         attempts -= 1
#         print(attempts, "attempts left")
#         if attempts == 0:
#             print("your account is locked")
#             locked.add(user_otp)
#             break





#  Problem number 3

# wallet for widhtraw
#  1. Deposit
# 2. Withdraw
# 3. Mini statement
# 4. Exit


# class Wallet :
#     def __init__(self, balance= 0):
#         self.balance = balance

# class deposit(Wallet):
#     deposit_amount = int(input("enter the amout to deposite:"))
#     def __init__(self, balance):
#         self.balance= balance
#         return self.balance

# class withdraw(Wallet):
#     withdraw_amount = int(input("enter the amount to withdraw:"))
#     def __init__(self, balance):
#         self.balance = balance
#         return self.balance
# class mini_statement(Wallet):
#     def __init__(self, balance):
#         self.balance= balance


# deposit1= deposit(deposit.deposit_amount)
# print(deposit1.balance)
# withdraw1 = withdraw(withdraw.withdraw_amount)
# print(withdraw1.balance)


# problem number 4

# Making a string password checker program
# password = input("Enter you password:")
# if len(password) < 8:
#     print("Password must be at least 8 characters long.")
#     password = input("Enter your password:")
# if not any(char.isdigit() for char in password):
#             print("Password must contain at least one digit.")
#             password = input("Enter your password:")
# elif  any(char.isupper() for char in password):
#     print("Password must contain at least one uppercase letter.")
#     password = input("Enter your password:")
# else:
#     print("Password is valid.")


# coupan use for the shopping cart discouut after the total ammount is calculates


# cart = {
#     "item1": 10000,
#     "item2": 20000,
#     "item3": 74463636.

# }
# if cart:
#     total_amount = sum(cart.values())
#     print("Total amount:", total_amount)
#     coupan_code = input("Enter the coupan code:")
#     if coupan_code == "DISCOUNT10":
#         discount = total_amount * 0.1
#         total_amount -= discount
#         print("Discount applied. New total amount:", total_amount)
#     else:
#         print("Invalid coupan code. Total amount remains:", total_amount)


import random
class OtpEngine:
    def __init__(self, lenght=6, attempts= 3):
        self.lenght = lenght
        self.attempts = attempts
        self.otp = None
        self.attempts_left = 0
    def send(self):
        low = 10 **(self.lenght - 1)
        high = 10 ** self.lenght- 1
        self.otp = random.randint(low, high)
        self.attempts_left = self.attempts     
        print(f"otp is sent to you number: {self.otp}")
    def verify(self, user_otp):
        if self.otp   is None:
            print("Please send the otp first.")
            return False  
        if self.attempts_left <= 0:
            print("No attempts left. please request a new otp:")
            return "Expired"
        if user_otp == self.otp:
            self.otp = None
            return "ok"
        wrong_guess = self.attempts_left - 1
        if self.attempts_left <= 0:
            return  "Expired"
        else:
            return "wrong"


if __name__ == "__main__":
    engine = OtpEngine()
    real = engine.send()
    print("verify (wrong) otp:", engine.verify(0))
    print("verify{real} ", engine.verify(real))
    