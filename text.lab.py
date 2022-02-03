def main():


    
    f = open("polyanna.txt", "r")
    text = f.read()
    text = text.lower()
    text.replace("\n"," ")
    tree = text.split(" ")

    count = 0;  
    word = "";  
    maxCount = 0;  
    words = [];

    for line in tree:  

        line = line.replace(".","")
        line = line.replace(",","")
        line = line.replace("“","")
        line = line.replace("”","")
        line = line.replace(";","")
        line = line.replace(":","")
        line = line.replace("!","")
        line = line.replace("?","")

         
        words.append(line);
#average word length
        
    average = 0
    for i in range(0, len(words)):
        average = average+len(words[i]);

    print("The average word length is " + str(average/len(words)))
       
# most common word   
    for i in range(0, len(words)):  
        count = 1;  
        
        for j in range(i+1, len(words)):  
            if(words[i] == words[j]):
                   count = count + 1;  
                  
        
        if(count > maxCount):  
            maxCount = count;  
            word = words[i];  

    print("Most repeated word: " + word); 

if __name__ == "__main__":
    main()
