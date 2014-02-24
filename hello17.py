# coding: UTF-8
# for ループ
users = {"taguchi":200, "fkoji":300, "dotinstall":500}

for key, value in users.iteritems():
	print "key: %s value: %d" % (key, value)
else:
	print

for key in users.iterkeys():
	print key
else:
	print

for value in users.itervalues():
	print value
else:
	print
