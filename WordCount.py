#WordCount.py
#Name:
#Date:
#Assignment:

with open("gettysberg.txt", 'r') as textFile:
    lineCount = 0
    wordCount = 0
    letterCount = 0

    # Read through each line in the file
    for line in textFile:
        lineCount += 1  # Count lines
        words = line.split()  # Split line into words
        wordCount += len(words)  # Count words
        letterCount += sum(len(word) for word in words)  # Count letters (excluding spaces)

# Print the results
print(f"Lines: {lineCount}")
print(f"Words: {wordCount}")
print(f"Characters (excluding spaces): {letterCount}")