def recite(start_verse, end_verse):
     diccionario={1:["a Partridge in a Pear Tree.","first"],
                 2: ["two Turtle Doves, ","second"],
                 3: ["three French Hens, ","third"],
                 4: ["four Calling Birds, ","fourth"],
                 5: ["five Gold Rings, ","fifth"],
                 6: ["six Geese-a-Laying, ","sixth"],
                 7: ["seven Swans-a-Swimming, ","seventh"],
                 8: ["eight Maids-a-Milking, ","eighth"],
                 9: ["nine Ladies Dancing, ","ninth"],
                 10:["ten Lords-a-Leaping, ","tenth"],
                 11:["eleven Pipers Piping, ","eleventh"],
                 12:["twelve Drummers Drumming, ","twelfth"]
                 }
     
     oracion =[]
     list_verses=[]
     if start_verse==end_verse:
         oracion =["On the " + diccionario[start_verse][1] +  " day of Christmas my true love gave to me: "]
         for i in range(start_verse,0,-1):
             if i==1 and start_verse!=1:
                 oracion[0]=oracion[0] + "and " + diccionario[i][0]
             else:
                 oracion[0]=oracion[0] + diccionario[i][0]
         return oracion        
     else:
         for u in range(start_verse,end_verse+1):
             oracion =["On the " + diccionario[u][1] +  " day of Christmas my true love gave to me: "]
             for i in range(u,0,-1):
                 if i==1 and u!=1:
                     oracion[0]=oracion[0] + "and " + diccionario[i][0]
                 else:
                     oracion[0]=oracion[0] + diccionario[i][0]
             list_verses.extend(oracion)
             
         return list_verses        
     
        
        
     
            
            
            
            
            
            
            
            
            
            
            
            
        
