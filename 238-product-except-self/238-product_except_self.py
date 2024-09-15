def product_except_self(nums: list[int]) -> list[int]:
    l_mul = 1
    r_mul = 1
    n = len(nums)
    left = [0] * n
    right = [0] * n
    for i in range(n):
        j = -i - 1
        left[i] = l_mul
        right[j] = r_mul
        l_mul *= nums[i]
        r_mul *= nums[j]

    return [l * r for l, r in zip(left, right)]


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    print(product_except_self(a))
    b = [-1, 1, 0, -3, 3]
    print(product_except_self(b))
