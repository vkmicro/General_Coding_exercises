'''
Author: Vasiliy Ulin
This is a file with test code and explanatory comments which I use to teach my friends basics of programming



'''

import random
"""
block
comment


"""

'''
interchangable 
neat eh

'''

'''
var1 = 5
var2 = 2
res = 5/2
print( " res : " + str(res) + "\n hi")

i = 0
for i in range(10):
  print(i)
  i= i+1

# print("statement")

var1 = 2
var2 = 12

Res = var1 + var2
Res2 = var1 - var2
Res3 = var2 / var1

print('Res is: ' + str(Res) + '\nRes2 is: ' + str(Res2) + '\nRes3 is: ' + str(Res3))

#if Res > Res2:
#  print(Res3)

# create for loop which iterates 10 times and increments i every iteration, print i

i = 0
for i in range(10):
  print(i)
  i = i + 1

# casting int to string##
#temp1 = 1  ##5
#temp1Str = str(temp1)  # = "15" stri###ng
# (accessing loop)

# v1
# for loops
# for item in list:
# pr

# animals = ['lion', 'tiger', 'elephant', 'mouse']
# v1 loop would print:
# lion
# tiger
# elephant
# mouse
# e.g. if item == "lion"
# you can't print any other animal...

########################## int(i (indexing loop)tem)

# v2
# i = 0
# for i in range(len(list)):
# print(list

# prints the same but through indexing[# indexing allows you to access other indexies based on current index
# e.g
# if list[i] == "lion"
# print (list[i-1])i])
# i +=1


#k = random.randint

'''


def main():
    hwrk1()


def hwrk1():
    # given a string, turn string into an array of single characters
    # on same string, count up amount of occurences of letter "a"
    resArr = []
    #resArr2 = []
    countA = 0
    tempStr = "this is a temporary string aaaaaaaaaaa hah ho he ha"
    for char in tempStr:
        resArr.append(char)
        if char == "a":
            countA += 1
#            print(char)
    print(resArr)
    print(countA)




if __name__ == "__main__":
    main()