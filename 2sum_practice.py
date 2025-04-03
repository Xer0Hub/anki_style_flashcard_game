nums = [2,7,11,15]
target = 9

compare_me = {}
return_list = []

for index, number in enumerate(nums):
    compare_me[index] = number

for value in compare_me.values():
    compliment = target - value
    number1 = value
    if compliment in compare_me:
        for key, val in compare_me.items():
            if val == compliment:
                return_list.append(key)
            if val == number1:
                return_list.append(key)
print(return_list)