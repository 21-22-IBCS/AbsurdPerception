def main() :

    response = input("Type an amount of usd dollars")
    response = int(response)
    #for response in range(0,5):
        #if response == exit
            #print(exit)
            #exit()
    d = {
        "ukrainian hryvnia" : 27.98,
        "russian ruble" : 75.32,
        "euro" : 0.87,
        "chinese yuan" : 6.36,
        "pound sterling" : 0.74,
        "poland złoty" : 3.96
        }
    print("ukrainian hryvnia","russian ruble", "euro", "chinese yuan", "pound sterling", "poland złoty")
    choice = input("choose one of the options")
    conversion = d.get(choice)*response
    print(conversion)


if __name__ == "__main__":
    main() 

