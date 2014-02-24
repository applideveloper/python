# coding: UTF-8
# リスト
sales = [50, 100, 80, 45]
print sales # [50, 100, 80, 45]
# sort / reverse

sales.reverse() # 単純に順番を逆にするだけ
print sales # [45, 80, 100, 50] 

sales.sort() # 降冪の順 
print sales # [45, 50, 80, 100]

sales.reverse() # 単純に順番を逆にするだけ
print sales # [100, 80, 50, 45]

# 文字列とリストを相互変換
d = "2013/12/15"
print d.split("/") # ['2013', '12', '15']

a = ['a', 'b', 'c']
print "-".join(a) # a-b-c
