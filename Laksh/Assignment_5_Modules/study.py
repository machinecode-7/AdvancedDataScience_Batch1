def ticket_price():
    age= int(input("please enter your age:"))
    if age <= 13 or age>=50:
        print('30')
    else:
        print('60')