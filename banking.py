# PROBLEM-1: banking
balance = 155
banking_type = input('Banking Type (deposit, withdraw): ')
user_amount = int(input('Amount: '))

def deposit (amount):
    global balance
    if amount > 0:
        balance = balance + amount
        print('Deposit Successful. Current Balance:', balance)
    else:
        print('Invalid Amount!')

def withdraw (amount):
    global balance
    if balance > 0 and amount > 0 and amount < balance:
        balance = balance - amount
        print('Withdraw Successful. Remaining Balance:', balance)
    else: 
        print('Insufficient Balance.')

if banking_type == 'deposit':
    deposit(user_amount)
elif banking_type == 'withdraw':
    withdraw(user_amount)
else:
    print('Please try again.')