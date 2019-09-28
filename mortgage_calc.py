'''
Mortgage Calculator -
Figure out your mortgage term based on what you can afford

'''


# Establish starting mortgage
# Init interest rate
# Init Term
# Monthly principal paydown
# calc N (months)


mortgage = int(input('What is your starting mortgage? '))
rate_input = float(input('What is your annual interest rate? '))
monthly_pay = int(input('What is the maximum you can pay each month?: '))
monthly_int_rate = rate_input/100/12
principal_pay = 0
int_pay = 0
month_count = 0
not_enough = False

while mortgage > 0:
    int_pay = mortgage * monthly_int_rate
    while not_enough == False:
        print('Make sure you can cover your interest')
        monthly_pay = int(input('What is the maximum you can pay each month?: '))
        if monthly_pay < int_pay:
            continue
        else:
            not_enough = True
            break
    if monthly_pay - int_pay > mortgage:
        principal_pay = mortgage
        print(f'last mortgage payment! {principal_pay:.2f}')
        break
    else:
        not_enough = True
        principal_pay = monthly_pay - int_pay
        mortgage -= principal_pay
        month_count = month_count + 1
    print(f'Monthly pay: ${monthly_pay}, '
          f'Interest pay: {int_pay:.2f}, '
          f'Principal pay ${principal_pay:.2f}, '
          f'Remaining mortgage: ${mortgage:.0f}')

year = (month_count+1)/12
print(f'It will take {year:.1f} years to pay off')






