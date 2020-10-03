"""
Given an integer value `n`, write a function that will return a list of the string representation of numbers from 1 to `n`.

However, there are a few additional rules to follow:

- For multiples of three, it should output "Lambda" instead of the number.
- For multiples of five, it should output "School" instead of the number.
- For numbers which are multiples of three and five, it should output "LambdaSchool" instead of the number.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Lambda",
    "4",
    "School",
    "Lambda",
    "7",
    "8",
    "Lambda",
    "School",
    "11",
    "Lambda",
    "13",
    "14",
    "LambdaSchool"
]
"""


def lambda_school(n):
    arr = []
    # Your code here
    # Create a list that takes in an integer from index + 1 upto n
    for i in range(1, n + 1):
        arr.append(i)
    # It should RETURN an ARRAY of strings up to that integer - starting from 1
    # return arr
    # If the number at specific index is a multiple of 3 - it should output Lambda
    for i, item in enumerate(arr):
        print("ARR", arr)
        if (item % 3 == 0 and item % 5 == 0):
            arr[i] = "LambdaSchool"
        elif (item % 5 == 0):
            arr[i] = "School"
        elif (item % 3 == 0):
            arr[i] = "Lambda"
        print(arr)
    # for i in range(1, len(arr)):
    #     print("I", i)
    #     if i % 3 == 0:
    #         arr[i] = "School"

result = lambda_school(15)
    # If the number at specific index is a multiple of 5 - it should output Lambda
    # if the number at specific index is a multiple of 3 AND 5 - it should output LambdaSchool
    