import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """

    ratio = []
    for word in wordList:
        numVowels = 0.0
        for letter in word:
            if letter in ['a','e','i','o','u']:
                numVowels += 1
        ratio.append((len(word)-numVowels)/len(word))



    pylab.title('Proportion of vowels in words.txt')
    pylab.xlabel('Vowels')
    pylab.ylabel('Proportion ')

    pylab.hist(ratio,bins=15)
    pylab.show()


if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
