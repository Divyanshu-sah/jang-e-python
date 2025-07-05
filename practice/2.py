import pandas as pd

def bank_loan1():
    salary = int(input('salary :'))
    time = int(input('time :'))
    if 20000 <= salary <= 25000 and time <= 5:
        print('provide personl lone : 25lacks')
    else:
        print('not provide personl lone')

def bank_loan2():
    salary = int(input('salary :'))
    time = int(input('time :'))
    if 25000 <= salary <= 30000 and time <= 30:
        print('provide Home loan : 20lacks')
    else:
        print('not provide home loan lone')

def bank_loan3():
    salary = int(input('salary :'))
    time = int(input('time'))
    if  15000 <= salary <= 20000 and time <= 7:
        print('provide vihicle loan : 10lacks')
    else:
        print('not provide vihicle loan')

bank_loan3()

def bank_loan4():
    salary = int(input('salary :'))
    time = int(input('time :'))
    if 25000 <= salary <= 35000 and time <= 8:
        print('provide gold loan : 10lacks')
    else:
        print('not provide gold loan')

def bank_loan5():
    salary = int(input('salary :'))
    time = int(input('time :'))
    if 150000 <= salary <= 200000 and time <= 8:
        print('provide Business/startup loan : 50k-1cr')
    else:
        print('not provide Business/startup loan')

bank_loan1()
bank_loan2()
bank_loan3()
bank_loan4()
bank_loan5()

df = pd.DataFrame({
    'Salary': [salary],
    'Time': [time],
    'Loan_Status': [result]
})

# Show result
print(df)

