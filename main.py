
def happy_number():
    current_number = input('Enter your number: ')
    seen_number = set()
    
    while current_number != 1 and current_number not in seen_number:
        seen_number.add(current_number)
        current_number = sum([int(digit)**2 for digit in str(current_number)])
        
    if current_number == 1:
        print('The number is a happy number')
    else:
        print('The number is not a happy number')

if __name__ == '__main__':
    happy_number()