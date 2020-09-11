import jieba
excludes = {"我们","我国"}
txt = open("C:\\Users\\70706\\Desktop\\python\\十九大习近平开幕报告.txt", "r", encoding='gbk').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:  #排除单个字符的分词结果
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True) 
for i in range(20):
    word, count = items[i]
    print ("{0:^10}{1:^10}".format(word, count))
