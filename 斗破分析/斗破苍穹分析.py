import jieba
excludes = {}#建立一个字典,去除不要的词
txt = open("C:\\Users\\70706\\Desktop\\23333\\python\\斗破苍穹.txt", "r", encoding='gbk').read()
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
for i in range(15):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))