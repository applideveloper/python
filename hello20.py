# coding: UTF-8
# 変数のスコープ
# 関数内で宣言された変数は関数ないでしか有効でない
name = "taguchi"

def hello():
	name = "fkoji"
print name # taguchi

# pass インターフェースみたいなもの
def hello2():
	pass


