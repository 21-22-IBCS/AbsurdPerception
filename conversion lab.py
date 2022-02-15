def main() :
    d = {
        "ukrainian hryvnia" : 27.98,
        "russian ruble" : 75.32,
        "euro" : 0.87,
        "chinese yuan" : 6.36,
        "pound sterling" : 0.74,
        "poland złoty" : 3.96
        }

    while True:
        
        response = input("Type an amount of usd dollars")
        response = int(response)
        print("ukrainian hryvnia","russian ruble", "euro", "chinese yuan", "pound sterling", "poland złoty")
        choice = input("choose one of the options")
        conversion = d.get(choice)*response
        print(conversion)
        question = input("do you want to continue?")
        if question == "no":
            break


if __name__ == "__main__":
    main() 

