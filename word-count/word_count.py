def count_words(sentence):
    sentence=sentence.replace("\t"," ")
    sentence=sentence.replace(","," ")
    sentence=sentence.replace("_"," ")
    sentence=sentence.replace("\n"," ")
    resul={}
    palabra=""
    list_ascii=[]
     
    st=sentence.split()
    
    for t in range(0,len(st)):
        print(st[t])
        aux=False
        st[t]=st[t].lower()
        palabra=""
        if st[t] == "can't" :
            palabra="can't"
            aux=True
        elif st[t] == "don't":
            palabra="don't"
            aux=True
        else:
            for i in range(0,len(st[t])):
                if (ord(st[t][i])>=65 and ord(st[t][i])<=90) or (ord(st[t][i])>=97 and ord(st[t][i])<=122) or (ord(st[t][i])>=48 and ord(st[t][i])<=57):
                    print(st[t][i])
                    palabra=palabra+st[t][i]
                    aux=True
        if aux:
            print("------->"+palabra)
            list_ascii.append(palabra)
        
    for i in range (0,len(list_ascii)):
        cont=0
        for n in range(0,len(list_ascii)):
            if list_ascii[i]==list_ascii[n]:
                cont=cont+1
                resul[list_ascii[i]]=cont

    return resul              
                
                
