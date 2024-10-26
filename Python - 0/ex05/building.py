import sys

def countPunctiations(text):
    """function to count the punctiations"""
    punctuationMarks = ['.', ',', '?', '!', ':', ';', "'", '"', '(', ')', '-', '—', '…'];
    counter = 0
    for count in text:
        for punc in punctuationMarks:
            if punc == count:
                counter += 1
    return counter


def main(argv):
    """main program"""
    upperLetters = 0
    lowerLetters = 0
    punctuationMarks = 0
    spaces = 0
    digits = 0
    globalCounter = 0
    if (len(sys.argv) == 1 or argv[1] == "None"):
        print("What is the text to count?")
        store = sys.stdin.read()
        for count in store:
            if count.isupper() : upperLetters += 1
            if count.islower() : lowerLetters += 1
            if count.isdigit() : digits += 1
            if count.isspace() : spaces += 1
        punctuationMarks = countPunctiations(store)
        globalCounter = len(store)
    elif (len(sys.argv) == 2):
        for count in argv[1]:
            if count.isupper() : upperLetters += 1
            if count.islower() : lowerLetters += 1
            if count.isdigit() : digits += 1
            if count.isspace() : spaces += 1
        punctuationMarks = countPunctiations(argv[1])
        globalCounter = len(argv[1])
    elif (len(sys.argv) == 1):
        print("1")
    else:
        print("error")
    print(f"The text contains {globalCounter} characters:\n{upperLetters} upper letters\n{lowerLetters} lower letters\n{punctuationMarks} punctuation marks\n{spaces} spaces\n{digits} digits");

if __name__ == "__main__":
    main(sys.argv)
