def integer_to_roman(num):
    symbols = [
        (1000,'M'),
        (900,'CM'),
        (500,'D'),
        (100,'C'),
        (90,'XC'),
        (50,'L'),
        (40,'XL'),
        (10,'X'),
        (9,'IX'),
        (5,'V'),
        (4,'IV'),
        (1,'I')
    ]
    # initialization of empty string
    roman = ""
    for value, symbol in symbols:
        # while num (for ex: 14 )  14 >=10 True  (1,,5,9,10) , so num - value (14 - 10)= 4, 4 >= value(4 >= 4 then roman =roman + symbol) IV , then remaining 10 >= 10 true = XIV
        while num >= value:
            roman = roman + symbol
            num = num - value
    return roman
num = int(input("Enter a number you want change it to roman number : "))
# to take input as number from user
answer = integer_to_roman(num)
# pass num to function
print(f"Value of integer {num} in roman is {answer}")
# print output roman number
