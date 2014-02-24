# coding:UTF-8
# 文字列
# 文字列 len
# 検索 find
# 切り出し [] [start:end]
s = "abcdefghi"
print len(s) # 9
print s.find("c") # 2
print s.find("x") # -1
print s[2] # c
print s[2:5] # cde
print s[:5] # abcde
print s[2:] # cdefghi
print s[2:-1] # cdefgh
