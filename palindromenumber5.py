# program to check number is palindrome or not (palindrome number = 12321 if it reverse and that number = entered number (12321))
def check_palindrome(num):
    temp = num
    reverse = 0
    while temp != 0:
        # to take last digit of number(remainder) num % 10
        # to reverse 
        reverse = (reverse * 10) + temp % 10
        # (12321 // 10 = 12321)
        temp = temp // 10
    return reverse == num

if __name__ == "__main__":
    num = int(input("Enter a Number"))
    answer = check_palindrome(num)
    # check number is palindrome or not
    if check_palindrome(num):
        print(f"Number is Palindrome")
    else:
        print(f"Number is not a palindrome")