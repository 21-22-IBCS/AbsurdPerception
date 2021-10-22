def selection_sort(aList):
    for i in range(len(aList)):
        min_index = i
        for j in range(i+1, len(aList)):
            if aList[j] < aList[min_index]:
                min_index = j

        aList[i], aList[min_index] = aList[min_index], aList[i]

def main():
    aList = [3,5,45,67,90,34,56,789,39,68,25]
    print(aList)
    
    selection_sort(aList)
    print(aList)
    

if __name__ == "__main__":
    main()

