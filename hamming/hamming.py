def distance(strand_a, strand_b):
    if len(strand_a)==len(strand_b):
        print("")
        cont=0
        for i in range(0,len(strand_b)):
            if strand_a[i]!=strand_b[i]:
                cont=cont+1
        return cont   
    else:
        raise ValueError("Value Error")
                
    
            
