n = int(input("enter your number:"))
triangle=[[1 for i in range(n)] for j in range(n) ] 

for i in range(0,n):
        
        for j in range(1,i):
               
               triangle[i][j]=triangle[i-1][j-1] + triangle[i-1][j]
               
print()               
                        
for i in range(n):        
        for j in range(i+1):
                print(triangle[i][j],end="   ")
                 
        print()       