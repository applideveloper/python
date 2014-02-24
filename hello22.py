# coding: UTF-8
# オブジェクト(変数と関数をまとめたもの)
# クラス: オブジェクトの設計図
# インスタンス: クラスを実体化したもの
class User(object):
	def __init__(self, name):
		self.name = name
	def greet(self):
		print "My name is %s!" % self.name
	
bob = User("Bob")
tom = User("Tom")

print bob.name # Bob
bob.greet() # My name is Bob! 
tom.greet() # My name is Tom! 
