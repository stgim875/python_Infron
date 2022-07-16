print(1 != 3) # True
print(not(1 != 3)) # False 풀이: 1과 3은 같지는 않는 것은 True는 맞지만 앞에 not이 붙어 있어서 False가 됨

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5)) # True
print((3 > 0) | (3 > 5)) # True
print((3 < 0) or (3 > 5)) # False


# print(5 > 4 > 3) # True
# print(5 > 4 > 7) # False
