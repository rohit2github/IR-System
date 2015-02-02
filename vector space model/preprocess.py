import os
td_matrix={}
s=open('../StopWord.txt','r')
s=s.read()
stop_words=[]
for w in s.split():
	stop_words.append(w)
for i in os.listdir('../tempfiles/'):
        td_matrix[i]={}
        f=open('../tempfiles/'+i)
        f1=f.readlines()
        for lines in f1:
                for word in lines.split():
                        if word not in stop_words:
                                if word in td_matrix[i]:
                                        td_matrix[i][word]=td_matrix[i][word]+1
                                else:
                                        td_matrix[i][word]=1
        f.close()
f=open('preprocessed_file','w')
f.write(str(td_matrix))
f.close
