# coding:UTF-8
a = 10
b = 1.234234
c = "taguchi"
d = {"fkoji":200, "dotinstall":500}
print "age: %d" % a # 10 # decimal 十進法
print "age: %10d" % a #         10 # decimal 十進法
print "age: %010d" % a # 0000000010# decimal 十進法
print "price: %f" % b # 1.234234# float 浮動小数点
print "price: %.2f" % b # 1.23 # float 浮動小数点
print "age: %s" % c # string 文字列
print "sales: %(fkoji)d" % d # 200 
print "%d and %f" % (a, b) # 10 and 1.234234
