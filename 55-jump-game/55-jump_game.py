def jump_game(nums: list[int]) -> bool:
    last = len(nums) - 1
    i = 0
    jump = nums[0]
    if jump >= last:
        return True
    while jump <= last:
        if i > jump:
            break
        if jump + nums[jump] >= last:
            return True
        for j in range(i, jump + 1):
            if j + nums[j] >= last:
                return True
        i += 1
        jump = jump + nums[jump]
    return False


if __name__ == "__main__":
    a = [2,3,1,1,4]
    b = [3,2,1,0,4]
    print(jump_game(a))
    print(jump_game(b))
