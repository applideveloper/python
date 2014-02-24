# coding: UTF-8
# セット(集合型) - 重複を許さない

a = set([1, 2, 3, 4, 3, 2]) # set([1, 2, 3, 4])
print a

b = set([3, 4, 5])
print b # set([3, 4, 5])

# - 差集合
print a - b # set([1, 2])
print b - a # set([5])

# | 和集合
print a | b # set([1, 2, 3, 4, 5])

# & 積集合
print a & b # set([3, 4])

# ^ 排他的論理和
print a ^ b # set([1, 2, 5])


