def row_division(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] % nums[j] == 0:
                return int(nums[i] / nums[j])

with open('input', 'r') as f:
    lines = f.read().strip().split("\n")
    checksum = 0
    for line in lines:
        nums = list(map(int, line.split("\t")))
        checksum += row_division(nums)
    print(checksum)
