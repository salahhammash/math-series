def fibonacci(n):
    if n == 0:
        return 0 
    
    elif n == 1:
        return 1

    else :
        return fibonacci(n-1) + fibonacci(n-2)




def lucas (n):
   if n == 0:
        return 2 
   
   elif n == 1:
       return 1
   
   else:
        return lucas(n-1) + lucas(n-2)
    






def sum_series (a,b=0,c=1):
    if b == 0 and c == 1:
        return fibonacci(a)
    elif b==2 and c ==1 :
        return lucas(a)
    else:
        if a == 0 :
            return b 
        elif a== 1 :
            return c
        else : 
           return sum_series(a-1 ,b,c) + sum_series(a-2,b,c)



    
