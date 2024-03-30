def product_except_self(nums):
    n = len(nums)
    prefix_product, suffix_product = [], []

    product = 1

    prefix_product.append(product)

    for i in range(1, n):
        product *= nums[i - 1]
        prefix_product.append(product)

    product = 1
    suffix_product.append(product)

    for j in range(n - 2, -1, -1):
        product *= nums[j + 1]
        suffix_product.append(product)

    for pos, (n1, n2) in enumerate(zip(prefix_product, suffix_product[::-1])):
        nums[pos] = n1 * n2

    return nums


nums = [0,0 ,0]

print(product_except_self(nums))
