str='hello'
print("index at 0",str*2)
list1=['yu',23,'lk',89]
list1[2]="op"
print(list1)
del list1[2]
print(list1)
tuple1=(8,9,"kl")
tup2=("hj","kl")
print(tuple1[::-1])
print(tuple1 + tup2)
dicty={}
dicty['one']='name'
dicty[2]=9
dictu={'kl':'hj','hg':'9'}
print(dicty['one'])
print(dictu.keys())
print(dictu.values())
print (dicty['one'])
var2=0
if var2:
    print('hi')
elif var2==0:
    print ("no")
c=0
while(c<9):
    if c==4:
     print("loop broke")
     break
    print("io")
    c=c+1
st='python'
for letter in st[::-1]:
    print("Current letter",letter)
    #print("At index",)

fruits=['op','ikl']
for fruits in fruits:
    print("fruits:",fruits)
for i in range(2,10,4):
    print(i)
for i in range(10,0,-2):
    print(i)
else:
    print("OPhg")
dict9={'k':9,'z':6}
for key,value in dict9.items():
    print(key,':',value)
for i in range(5):
    for j in range (3):
        if i==2:
            break
        print(f"i:{i} and j: {j}")
for i in range(5):   
    if i==3:
        break
    print(i)   
else:   
    print("Loop completed successfully!")
for index,letter in enumerate('python'):
    print(f"inndex={index},letter={letter}")

class Dog : 
# Class Attribute 
 species =  'mammal'
# Initializer / Instance Attributes 
 def __init__ ( self , name , age ): 
  self . name = name 
  self . age = age 
# instance method 
 def description ( self ): 
  return " {} is {} years old ". format ( self . name , self . age )
 def speak ( self , sound ): 
  return " {} says {} ". format ( self . name , sound )
class cat:
    species ='mammal'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def desc(self):
     return f"{self.name} and {self.age}"
    def spe(self,sound):
        return f"sound:{sound}"
mi=cat('mi',3)
print(mi.desc())
print(mi.spe("Meow mew"))


print('\nhi my name')
print("klhhg km")
    