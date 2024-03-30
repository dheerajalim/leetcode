def single_number(nums):
    ans = 0
    # we will consider the complete length of the integer
    # i.e. 32 bits
    for bit in range(32):
        count = 0
        # we will check the bit for each number in the
        # nums from right to left
        for num in nums:
            # if the bit is 1, then increment the count
            if num & (1 << bit):
                count += 1

        # if all the bits at same position in all the num in nums
        # is divisible by 3, then this is repeating number, else
        # this number appears only once
        if count % 3 == 1:
            # we create the ans by using OR operator and left shifted 1
            # at the position where we count % 3 == 1
            ans = ans | (1 << bit)

    # if this is a negative number, by checking if the 32nd bit is set to 1
    # if yes then this if condition will return 1
    if ans & (1 << 31):
        # now this is tricky, since Python represents integers using arbitrary precision, meaning it doesn't have
        # fixed-width representations like 32-bit integers. Python's integers can
        # grow or shrink in size as needed to accommodate the value being represented.

        # Hence what we do is , we see that the 32nd bit in ans is 1, which makes it negative number
        # Subtracting (1 << 32) effectively sets the 33rd bit to 1, turning ans into a negative number.
        # This operation simulates the process of sign-extension, which is commonly used when
        # representing signed integers in binary. By setting the 33rd bit to 1, ans becomes a negative number
        # that correctly represents the result.
        ans -= (1 << 32)

        # example : ans = 4294967292
        # then 1 << 32 = 4294967296 ; there difference is -4

    return ans


nums = [0, 1, 0, 1, 0, 1, 99]
nums = [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
print(single_number(nums))
