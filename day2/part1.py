with open('input', 'r') as f:
    lines = f.read().strip().split("\n")
    checksum = 0
    for line in lines:
        nums = list(map(int, line.split("\t")))
        min = nums[0]
        max = nums[0]
        for num in nums:
            if num > max:
                max = num
            elif num < min:
                min = num
        checksum += max - min
    print(checksum)
