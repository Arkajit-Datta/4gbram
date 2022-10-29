def overspeed(speeds):
    f = 0
    for speed in speeds:
        if(speed < 80):
            f = 1
    if f:
        return 0
    else:
        return 1
    
def idle(values):
    return all([x == 15 for x in values])

def tricking(a):
    i = 0
    j = -1
    k = -1
    p = 0
    d = 0
    n = 0
     
   
    if (len(a) < 3):
        return 0
         
    for i in range(len(a) - 1):
        if (a[i + 1] > a[i]):
             
            
            if (k != -1):
                k = -1
                j = -1
             
            
            if (j == -1):
                j = i
        else:
             
            
            if (a[i + 1] < a[i]):
                 
                
                if (j != -1):
                    k = i + 1
                     
                
                if (k != -1 and j != -1):
                     
                    
                    if (d < k - j + 1):
                        d = k - j + 1
             
            
            else:
                k = -1
                j = -1
     
    
    if (k != -1 and j != -1):
        if (d < k - j + 1):
            d = k - j + 1
             
    if d < len(a)//4:
        return True
    return False