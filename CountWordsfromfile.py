def countWordsfromfile():
    fileName=input("Enter the  file name: ")
    numberOfwords=0

    file=open(fileName)

    for line in file:
        words=line.split()
        numberOfwords=numberOfwords+len(words)
    print("Number of words: ")
    print(numberOfwords)

countWordsfromfile()        