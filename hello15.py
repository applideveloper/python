# coding: UTF-8
# 条件分岐 if
score = 70
print "score = %d" %score
if score > 60:
	print "score > 60"
else:
	print "score <= 60"

score = 40
print "score = %d" %score

if score > 60:
	print "score > 60"
elif score < 40:
	print "score < 40"
else:
	print "40 <= score <= 60" 

print "score > 60" if score > 60 else "score <= 60"
