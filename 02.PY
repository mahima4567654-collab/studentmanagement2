#math 
import math

print(dir(math))
#module_name.method
#ssqrt
print(math.sqrt(9))
print(math.sqrt(36))

#'factorial'
#6!=6*5*4*3*2*1
print(math.factorial(8))
print(math.factorial(5))

#pow(num,power)
print(math.pow(x: 3, y:2))
print(math.pow(x: 5,y:3))

#round up the value
#ceil()
print(math.ceil(4,1))
#floor()
print(math.floor(4.9))

#pi
print(math.pi)

# 4 digit opt:
def otp(num): 
    res=''
    for i in range(num):
        res+=str(random.randit(a:0,b:9))
        
