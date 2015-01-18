import os
td_matrix={}
for i in os.listdir('files/'):
        f=open('files/'+i)
        f1=f.readlines()
        for lines in f1:
                for word in lines.split():
                        if td_matrix.has_key(word):
                                if i not in td_matrix[word]:
                                        td_matrix[word].append(i)
                        else:
                                td_matrix[word]=[]
                                td_matrix[word].append(i)
        f.close()
print "Enter query"
input=raw_input().split()
result=td_matrix[input[0]]
for word in input:
        result=list(set(result).intersection(set(td_matrix[word])))
print result