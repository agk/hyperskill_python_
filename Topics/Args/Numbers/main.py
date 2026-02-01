# put your python code here
def multiply(a, *nums):
    if len(nums) == 0:
        return a * 1

    total = a * a
    for n in nums:
        total *= n

    return total

print(multiply(*[1, 2, 3]))