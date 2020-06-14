def convert(number):
    num7=number%7
    num5=number%5
    num3=number%3
    resul=""
    
    # if num7==0&num5==0&num3==0:
    #     return "PlingPlangPlong"
    # if num5==0&num7==0:
    #     return "PlingPlang"
    
    if num3==0:
        resul="Pling"
    if num5==0:
        resul=resul+"Plang"
    if num7==0:
        resul=resul+"Plong"
    if num3!=0 and num5!=0 and num7!=0:
        resul=str(number)
    
    print(resul)    
    return resul    
    
