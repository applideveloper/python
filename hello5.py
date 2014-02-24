# encoding: UTF-8
# 文字列
# "hello" 'hello'
# 日本語 u"こんにちは!" 
# unicodeのuをつける 文字コードの長さを調べられない
# + 連結 * 繰り返し
# エスケープ \n \t \\ 
print "hello" + "world"
print u"無駄!" * 10
print 'hello\n wo\trld\\ it\'s a pen'

print """<html lang="ja">
<body>
</body>
</html>"""
