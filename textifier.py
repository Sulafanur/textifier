lenght = 0
x= 0 
k= 0
number = []
numbertext =[]

x = int(input("""What number do you want to textify? 
      : 
      """))
y = str(x)
lenght =len(y)
for i in range(lenght+1):
    (s) = (lenght) 
    (k) =  x // 10**(s-i)
    x = x-k*(10**(s-i))
    number.append(k)
number.pop(0)


print(number)

### 1 2 , 4 5 6 ###
numberlist = {0: "zero",1: "one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",}

for i in range (lenght+1):

    (k) = numberlist[number[i-1]]
    numbertext.append(k)
numbertext.pop(0)    

print(numbertext)

### one three six seven one eight ### 136718 one hundered thirty six thousand

quantifier ={1:"",2:"ten",3:"hundred",6:"thousand",12:"million",18:"billion",24:"trillion",30:"quadrillion"}
if lenght%(3) == 0:
    c=1
    for i in range (3):
        (k) = quantifier[3-i]
        
        numbertext.insert(c,k)
        c = c+2
    
    for n in range (7,(lenght*2)+1,6):
        
        for m in range (3):
            (k) = quantifier[3-m]
            
            numbertext.insert(n,k)
            n = n+2
    c=6
    for h in range (6,(lenght*2+1),6):
        (k) = quantifier.get(lenght*2-h)
        
        numbertext.insert(c,k)
        c = c+7

if lenght%(3) == 2:
    c=1
    for i in range (2):
        (k) = quantifier[2-i]
        
        numbertext.insert(c,k)
        c = c+2
    for n in range (5,(lenght*2)+1,6):
        
        for m in range (3):
            (k) = quantifier[3-m]
            
            numbertext.insert(n,k)
            n = n+2
    c = 4
    for h in range (6,(lenght*2+1),6):
        (k) = quantifier.get(lenght*2+2-h)
        
        numbertext.insert(c,k)
        c = c+7


if lenght%(3) == 1:
    c=1
    for i in range (1):
        (k) = quantifier[1-i]
        
        numbertext.insert(c,k)
        c = c+2
    for n in range (3,(lenght*2)+1,6):
        
        for m in range (3):
            (k) = quantifier[3-m]
            
            numbertext.insert(n,k)
            n = n+2    

    c = 2
    for h in range (6,(lenght*2+1),6):
        (k) = quantifier.get(lenght*2+4-h)
        
        numbertext.insert(c,k)
        c = c+7
### 3 hundered 4 ten 2 _ three two two one four six
finalform = " "
finalform = " ".join(numbertext)
finalform = finalform.replace("one ten two", "twelve ") 
finalform =finalform.replace("one ten one", "eleven ")
finalform =finalform.replace("  ", " ")
finalform =finalform.replace("three ten ", "thirty ")
finalform =finalform.replace("two ten ", "twenty ")
finalform =finalform.replace("one zero zero ", "one ")
finalform =finalform.replace("one zero ", "one ")
finalform =finalform.replace("zero ", "")
finalform =finalform.replace("one ten ", "ten ")
finalform =finalform.replace("four ten ", "fourty ")
finalform =finalform.replace("five ten ", "fifty ")
finalform =finalform.replace("one ten four", "fourteen ")
finalform =finalform.replace("six ten ", "sixty ")
finalform =finalform.replace("seven ten ", "seventy ")
finalform =finalform.replace("eight ten ", "eighty ")
finalform =finalform.replace("nine ten ", "ninety ")
finalform =finalform.replace("one ten three ", "thirteen ")
finalform =finalform.replace("one ten five" ,"fifteen " )
finalform =finalform.replace("one ten six" ,"sixteen ")
finalform =finalform.replace("one ten seven" ,"seventeen " )
finalform =finalform.replace("one ten eight" ,"eighteen " )
finalform =finalform.replace("one ten nine" ,"nineteen " )
finalform =finalform.replace("" ,"")
finalform =finalform.replace("" ,"" )
finalform =finalform.replace("" ,"" )
print(finalform)