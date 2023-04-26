def fibonacci(n):
    '''
    this function return the sum of the 2 previous numbers 
   The first few terms of the Lucas sequence are: 0,1

    we start with a brief description of what the function does: it computes the nth Fibonacci number.

Next, we list the parameters that the function takes in. In this case, there is only one parameter, n, which is the index of the Fibonacci number to compute. We also specify that n must be non-negative.

After that, we describe what the function returns: the nth Fibonacci number, which is an integer.

Finally, we specify that the function will raise a ValueError if n is negative.
    '''
    if n == 0:
        return 0 
    
    elif n == 1:
        return 1

    else :
        return fibonacci(n-1) + fibonacci(n-2)




def lucas (n):
   '''As with the Fibonacci sequence, the Lucas sequence can also be implemented recursively or iteratively in a computer program
   its do the same thing as fibonacci but 
   The first few terms of the Lucas sequence are: 2,1
   '''
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



    
