# Author: Vasiliy Ulin
# Learning and exploring
# this project just contains random stuff i did on my own for extra practice

"""
Find the most frequent word in a Wikipedia Article (try to use Wikipedia API to fetch the text)

create dict wordFreq: {word,frequency}
- for word in listOfWords(full text)
   if word in wordFreq
     wordFreq = wordFreq.frequency +1 or something like that
   else add word to wordFreq

"""


import wikipedia
import numpy as np

articleName = "Library (computing)"
# articleName = "Application programming interface"
# print(wikipedia.summary(articleName, sentences = 1))
# print(wikipedia.summary(articleName))
textArr = wikipedia.summary(articleName).replace('\n',' ').split(' ')  # splits by empty spaces so it's separating everything into words
textDict = {}   # item: value pairs

print(textArr)

for words in textArr:
    textDict.update({words: 0})


def main():
    price_algo_test()
    print(textDict)
    print("---------------------")
    print("now look for the frequency of words")
    print("--------------------")

    #for word, frequency in textDict.items():  # iterate over all words in the item's
    for word in textArr:  # iterate over all words in the item's
            # HAVE TO ITIRATE NOT OVER ITSELF (the dict) BUT SOMETHING ELSE!
                # SO EITHER ITIRATE OVER DICT, ADD TO NEW DICT AND COUNT UP IN THE NEW DICT
                # OR ITIRATE OVER THE ARRAY!
        textDict[word] += 1  # textDict[key] = value (it returns the VALUE of the key

    #print(textDict)

    tempDict = {}

    #print(len(textDict.items()))


    for word, frequency in textDict.items():
        if(frequency>15):
            print (word + " " + str(frequency))


#############################
    print()
    print("---------------------")
    print("now look for the frequency of groups of 3 words")
    print("--------------------")

    #i = 0
    #while i < len(textArr):
    #    i +=1
        #print (i)


    tempArr = []

    tempArr.append(textArr[0])
    tempArr.append(textArr[1])
    tempArr.append(textArr[2])

    #tempArr = []
    #tempArrr = []
    resArr = []
    tempArrOfRepetitions = []
    i = 0
    counter = 0
    j = 0


    '''
    arrA = ["a","b","c"]
    print(arrA)
    temp = ''.join(arrA)
    print(temp)
    arrB = []
    arrB.append(temp)
    arrB.append("aaa")
    print(arrB)
    '''

    while (j < len(textArr)-5):
        #stempArr[0] = textArr[j+1]
        #tempArr[1] = textArr[j+2]
        #tempArr[2] = textArr[j+3]
        tempArr[0] = textArr[j]
        tempArr[1] = textArr[j+1]
        tempArr[2] = textArr[j+2]
        #print(str(tempArr[0]) + "  " + str(tempArr[1]) + "  " + str(tempArr[2]))
        i = 0
        counter = 0
        while (i < len(textArr)-5):
            #counter = 0
            #print(" COMPARING: '" +  str(tempArr[0]) + " " + str(tempArr[1]) + " " + str(tempArr[2]) + "' AND '"
            #      +  str(textArr[i + 3]) + " " + str(textArr[i + 4]) + " " + str(textArr[i + 5]) +"'")

            if(tempArr[0] == textArr[i+3] and tempArr[1] == textArr[i+4] and tempArr[2] == textArr[i+5]):
             #   print()
             #   print(" *** REPETITION FOUND ***" )
             #   print(" SAME 3 WORDS: " + str(tempArr[0]) + " " + str(tempArr[1]) + " " + str(tempArr[2]) + " AND "
             #         + str(textArr[i + 3]) + " " + str(textArr[i + 4]) + " " + str(textArr[i + 5]))
             #   print(" *** REPETITION FOUND ***" )
             #   print()
                counter += 1
                #tempArrOfRepetitions.append((counter))

                #using this kind of mechanic to make sure it doesn't keep appending over and over
                # if item not in (item for item in medication_types):
                for item in tempArr:
                    tempStr = ' '.join(tempArr)
                    #print(tempStr)
                    if tempStr not in (item for item in resArr):
                        resArr.append(tempStr)
        #        resArr.append(' '.join(tempArr))
                i += 1
            #end if
            i += 1
        if(counter >= 1):
            tempArrOfRepetitions.append((counter))
        #end inner while
        j += 1
    #end outer while

    i = 0
    for i in range (len(resArr)):
        #print("group of these 3 words: " + str(resArr[i]) + " repeats: " + str(tempArrOfRepetitions[i]) + " times")
        if(tempArrOfRepetitions[i] >= 3): #set repetition threshold
            print("group of these 3 words: " + str(resArr[i]) + " repeats: " + str(tempArrOfRepetitions[i]) + " times")



    #print(repeating_three_words)
    print()
    print()
    print()


def price_algo_test():
    print()
    # TODO implement the price algorithm i thought of for my game here

    '''
    price formula 
    default ceil(price + (defaultPrice * supply/demand)/2)
    invert supply/demand to demand / supply?
    ---
    default price is 10
    supply 30
    demand 70
    dPrice = 10 + (10 * (70/30)) = 33
    dPrice = 10 + (10 * (70/30))/2 = 21
    ----------------
    supply 2
    demand 90
    dPrice = 10 + (10*(90/2)) / 2 = 235
    -----------------
    over supply 
    supply = 70
    demand = 10
    dPrice = 10 + (10 * (10/70))/2 - ceil(10/70) = 10 or 9 
    ------------------
    supply = 90
    demand = 2
    dPrice = 10 + (10 * (2/90))/2) - ceil(2/90) = 
    -------------------------
    bell curve stuff:
    
    z is the number of standard deviations your data point is from the mean.
    
    to calculate it you take x (test score) minus it from mew (mean) and then divide by sigma (standard deviation. 
    it will tell you how many sd away that point is from the mean and depending on that will depend on if it falls into 
        the rejection area on a bell curve or not

    '''






if __name__ == "__main__":
    main()
