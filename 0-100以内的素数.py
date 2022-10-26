num = 2                
while(num < 100):   
    b = 2              
    while(b <= (num/b)):       
        if (num % b == 0):
            break
        b = b + 1              
    if (b > num/b):             
        print(num,"是素数")     
    num = num +1              

print("0-100所有的素数")

