def coffeeShop():
    input("Welcome to Starbucks!")
    answer = input("What is your name?")
    print(answer)
    question = input("What is your order?")
    print(question)
    print("Thank you for your order!")
    receipt = ( "order number:01" + ","+ question +","+ answer )
    return receipt

def palindrome(str):

    str = input("Type your word ")

    if (str[::-1]==str):
        print(True)
    else:
        print(False)

def main():
 var = coffeeShop()
 print(var)

 palindrome(str)

if __name__ == "__main__":
    main()
