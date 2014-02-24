# coding: UTF-8
# while ループ
n = 0
while n < 10:
	print n
	#n = n + 1;
	n += 1
else:
	print

n = 0
while n < 10:
	if n == 3:
		n += 1
		continue
	print n
	n += 1
else: 
	print

n = 0
while n < 10:
  if n == 3:
   	break
  print n
  n += 1
else:
  print "end"
