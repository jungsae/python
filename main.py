sentence = input("sentence: ")
emptyArr = []
count = 0

while count < len(sentence):
    emptyArr.append(sentence[count])
    if (count + 1 == len(sentence)) or (sentence[count] == " "):
        print(emptyArr[0])
        emptyArr.clear()
    count += 1