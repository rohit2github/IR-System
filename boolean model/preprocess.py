import os
td_matrix={}
s=open('../StopWord.txt','r')
s=s.read()
stop_words=[]
for w in s.split():
	stop_words.append(w)
#	print(w)
for i in os.listdir('../tempfiles/'):
        f=open('../tempfiles/'+i)
        f1=f.readlines()
        for lines in f1:
            for word in lines.split():
                if word not in stop_words:
                        if word in td_matrix:
                                if i not in td_matrix[word]:
                                	td_matrix[word].append(i)
                        else:
                        	td_matrix[word]=[]
                        	td_matrix[word].append(i)
        f.close()
f=open('preprocessed_file','w')
f.write(str(td_matrix))
f.close
