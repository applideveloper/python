# coding: UTF-8
# 辞書 key value
# [2505, 523, 500] これが誰の売り上げがわかった方がいいので辞書型が生まれた
sales = {"taguchi":200, "fkoji":300, "dotinstall":500} 
print sales # 必ずしも順番に表示されるわけではない
print sales["taguchi"]
sales["fkoji"] = 800
print sales

# in  keyの存在チェック return True or False
print "taguchi" in sales # True

# keys, value, items の一覧表示
print sales.keys() # ['dotinstall', 'taguchi', 'fkoji'] 
print sales.values() # [500, 200, 800] 
print sales.items() # [('dotinstall', 500), ('taguchi', 200), ('fkoji', 800)] 
