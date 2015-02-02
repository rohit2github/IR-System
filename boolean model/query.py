f=open('preprocessed_file','r')
td_matrix=eval(f.read())
s=open('../StopWord.txt','r')
s=s.read()
stop_words=[]
for w in s.split():
	stop_words.append(w)
flag=1
while flag==1:
	print ("Enter query")
	i=input().split()
	result=[]
	if i[0] in td_matrix:
		result=td_matrix[i[0]]
	for word in i:
 #               print (word)
                if word not in stop_words:
                	if word in td_matrix:
                		result=list(set(result).intersection(set(td_matrix[word])))
                	else:
                                result=[]
	print("\n Result:")
	print (result)
	print("\nFor further query press 1:")
	flag=int(input())
#	print (flag)
