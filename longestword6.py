# program to find longest word in sentence
def longestword(text):
    word = text.split() # used to split the word in Given sentence
    longest = max(word, key=len) # max is used to find Max len of word
    return longest # return longest word in string
if __name__ == "__main__":
    text = str(input("Enter your Text Here:")) # to take string as an input
    answer = longestword(text) # to pass text to function
    print(f"Longest word in Given sentence is :{answer}")