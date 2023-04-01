def ticket():
    age = (int(input("Please enter your age:")))
    if age<=13 or age>=50:
        print('$30')
    else:
        print('$60')