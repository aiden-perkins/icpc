count = int(input())

for i in range(count):
    nums = [str(int(a))[::-1] for a in input().split()]
    print(int(str(int(''.join(nums[0])) + int(''.join(nums[1])))[::-1]))
