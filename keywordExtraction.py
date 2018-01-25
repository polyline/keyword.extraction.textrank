from summa import keywords
from getComments import getComments


lis = getComments()

kw_list = []
for com in lis:
	kws = keywords.keywords(com.encode('utf-8'), ratio=0.5)
	kws = kws.split('\n')
	for kw in kws:	
		kw_list.append(kw)
print kw_list

# count keywords 

dic = dict()
for keyword in kw_list:
	if keyword not in dic:
		dic[keyword] = 1
	else:
		dic[keyword] = dic[keyword] + 1

# print keywords list
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

for t in dic:
	print t
 