text = open('Input/Day7.txt').read().splitlines()
##text = open('Solutions/test.txt').read().splitlines()
def check_valid(equation, index, current, target):
    if current == target and index == len(equation):
        return True
    elif current > target or index == len(equation):
        return False
    else:
        new_operator = str(current) + str(equation[index])
        new_operator = int(new_operator)
        return check_valid(equation, index + 1, current + int(equation[index]), target) or check_valid(equation, index + 1, current * int(equation[index]), target) or check_valid(equation, index + 1, new_operator, target)

result = 0

for line in text:
    target, nums = line.split(': ')
    nums = nums.split()
    if check_valid(nums, 1, int(nums[0]), int(target)):
        result += int(target)

print(result)