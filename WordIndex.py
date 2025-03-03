#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
   
    with open("fish.txt", 'r') as textFile:
        words = {}  
        lineNum = 0

        for line in textFile:
            lineNum += 1  
            wordList = line.split()  

            for w in wordList:
                w = w.lower()  
                w = w.replace(",", "").replace(".", "").replace("!", "")  

                if w in words:
                    if lineNum not in words[w]:  
                        words[w].append(lineNum)  
                else:
                    words[w] = [lineNum] 


    for word in words:
        print(word, words[word])

  
    print("fish" in words)  
    words["fish"] = [2]  
    print("fish" in words)
    words["fish"].append(5)  
    print(words)

\
if __name__ == '__main__':
    main()
