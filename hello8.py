# coding: UTF-8
# リスト
sales = [255, 100, 353, 400, 'aba']

# len + 連結 * 繰り返し [] 切り出し
print len(sales) #4
print sales[2] # 353
sales[2] = 100
print sales[2] # 100

# in 存在チェック return True or False
print 100 in sales # True 

# range
print range(10) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print range(3, 10) # [3, 4, 5, 6, 7, 8, 9] 
print range(3, 10, 2) # [3, 5, 7, 9] 
