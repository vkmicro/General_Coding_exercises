'''
    Author: Vasiliy Ulin
    Date: 3/31/2019
    Disclaimer: all code is done by me, Vasiliy Ulin
        all questions are provided by https://www.dailycodingproblem.com
        I do not own any of the questions, only the code solution
            UNLESS specified otherwise
'''


def main():
    print("main")
    q1()
    q2()
    q4()


def q1():
    print()
    print("--------------")
    print()
    '''
    Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    '''
    arr = [10, 15, 3, 7]
    k = 17
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            print(str(arr[i]) + " + " + str(arr[j]))
            if arr[i] + arr[j] == k:
                print("yes")
                print(str(arr[i]) + " + " + str(arr[j]) + " = " + str(k))
                return True
            else:
                print("not")
                continue


def q2():
    print()
    print("--------------")
    print()
    print("Q2 after i registered, queston by uber: given arr, return new arr ")
    '''
    This problem was asked by Uber.
    Given an array of integers, return a new array such that each element at index i of the new array is the product of 
    all the numbers in the original array except the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?'''
    # What division? why would u use division?

    # the following solution was made by a friend of mine
    input_arr = [1, 2, 3, 4, 5]
    i = 0
    temp_arr = []
    res_arr = []
    for i in range(0, len(input_arr)):  # in python i in range(startValue , endValue)
        temp = 1
        for j in range(0, len(input_arr)):
            if i != j:
                temp *= input_arr[j]
        res_arr.append(temp)
    print(res_arr)


def q3():
    '''
    Good morning! Here's your coding interview problem for today.

    This problem was asked by Google.

    Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

    For example, given the following Node class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    :return:
    '''


def q4():
    print("---------------------")
    print("Q4, find lowest integer which doesn't exist in array")
    '''
    Good morning! Here's your coding interview problem for today.

    This problem was asked by Stripe.

    Given an array of integers, find the first missing positive integer in linear time and constant space.
    In other words, find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

    You can modify the input array in-place.
    '''
    # temp = [3,4,-1,1]   # find lowest possible integer which doesn't exist in the array
    temp = [1, 2, 0]   # find lowest possible integer which doesn't exist in the array
    temp_highest = temp[0]
    for i in range (len(temp)):  # expected = 2
        if temp_highest < temp[i]:
            temp_highest = temp[i]
            print("highest int in array: " + str(temp_highest))
    temp_highest += 1
    temp.append(temp_highest)




    print(temp)

if __name__ == "__main__":
    main()
