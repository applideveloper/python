# coding: UTF-8
# リスト <> 関数 map
# 無名関数 lambda
def double(x):
	return x * x
print map(double, [2, 5, 8]) # [4, 25, 64] 

print map(lambda x:x * x, [2, 5, 8]) # [4, 25, 64]
