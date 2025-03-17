'''
Created on Nov 23, 2020

@author: DingYang
'''

#descending sort to list
def descSort(l):
        n=len(l)
        for i in range(n):
            k=i
            j=i+1
            while j<n:
                if len(l[k])<len(l[j]):
                    k=j
                j=j+1
            if i!=k:
                temp=l[k]
                l[k]=l[i]
                l[i]=temp
        return l
#pName represent pattern name;
#fileName1 is old sequence,fileName2 is sequence of sort  
def sortAndSave(fileName1,fileName2,pName):
        #reading data and sort then save
        sequence=[]#sequence represent requirement sequence or service sequence
        try:
            with open(fileName1,'r') as f:
                data=f.readline()
                elePlace=0
                while data:
                    reqEle=[]
                    temp=data.strip().split(',')
                    for i in range(len (temp)):
                        reqEle.append(temp[i]) 
                    sequence.append(reqEle)
                    print(sequence[elePlace])
                    data=f.readline()
                    elePlace=elePlace+1
            sequence=descSort(sequence)#sort
            file=open(fileName2,'w')
            pName2=0
            for x in sequence:
                pName2+=1
                eleNum=0
                for ele in x:
                    eleNum=eleNum+1
                    if eleNum<len(x):
                        file.write(ele+',')
                    else:
                        file.write(ele+':'+pName+'%d'%pName2+'\n')
        except IOError as ioerr:
            print("File error:" + str(ioerr))
            return(None)