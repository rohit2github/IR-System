import os
import math
import operator
def dot_product(d,q):
        r=0
        mod_d=0
        mod_q=0
        for k in q.keys():
                if k in d:
                        r=r+(q[k]*d[k])
                mod_q=mod_q+(q[k]*q[k])
        for k in d.keys():
                mod_d=mod_d+(d[k]*d[k])
        return (r/(math.sqrt(mod_d)*math.sqrt(mod_q)))
td_matrix={}
s=open('../StopWord.txt','r')
s=s.read()
stop_words=[]
for w in s.split():
	stop_words.append(w)
f=open('preprocessed_file','r')
td_matrix=eval(f.read())
print ("Enter query")
input=input().split()
query={}
for word in input:
	if word not in stop_words:
                if word in query:
                        query[word]=query[word]+1
                else:
                        query[word]=1
result={}
for d in td_matrix.keys():
        result[d]=dot_product(td_matrix[d],query)
result=sorted(result.items(),key=operator.itemgetter(1),reverse=True)
print("\n Result:\n")
print (result)
