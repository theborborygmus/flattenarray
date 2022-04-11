entry = input("---------\nEnter 'quit' to quit.\nEnter array of INTEGERS (Ex: [[1,2,[3]],4]):\n")

while entry != "quit":
    #split the entry by commas
    parse = entry.split(',')
    output = []
    for i in range(len(parse)):
        new = ''
        for j in range(len(parse[i])):
            if parse[i][j] == '.':
                print("\nWARNING: non-integers will be rounded.") #accounting for floats/decimals
                break
            elif parse[i][j].isdigit(): #testing for digits and formatting them into elements
                new = new + parse[i][j]
            elif len(new) == 0 and parse[i][j] == '-': #accounting for negative integers
                new = new + parse[i][j]
        output.append(int(new)) #add new elements into a new list
    #print output
    print("Flattened Array:\n", output, "\n")
    entry = input("---------\nEnter 'quit' to quit.\nEnter array of INTEGERS (Ex: [[1,2,[3]],4]):\n")
