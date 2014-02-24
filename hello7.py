# coding:UTF-8
# 数値 <> 文字列

# 文字列 -> 数値 int float
# 数値 -> 文字列 str

#print 5 + "5" # ERROR
print 5 + int("5") # 10 
print 5 + float("5") # 10.0
age = 20
#print "i am " + age + " years old" # ERROR
print "i am " + str(age) + " years old" # ERROR
