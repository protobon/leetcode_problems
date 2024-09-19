def numJewelsInStones(jewels, stones):
    jewels = set(jewels)
    count = 0
    for stone in stones:
        if stone in jewels:
            count += 1
    return count


if __name__ == "__main__":
    print(numJewelsInStones("aA", "aAAbbbb"))
    print(numJewelsInStones("z", "ZZ"))
