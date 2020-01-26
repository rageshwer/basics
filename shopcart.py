print("**************")
print("**************")
print("**************")
print("**************")
print("**************")
print("Welcome to the Shopmore!!!!")
print("We have following options to choose from :-")
print("**************")
print("**************")
print("**************")
print("**************")
items={"Cap":100,"Jeans":1000,"Shirt":1500,"T-shirt":500}
for i in items:
    print(i,end="         ")
print()
for y,t in items.items():
    print(t,end="          ")
print()
pfl={"Item":[],"Price":[],"Number":[],"Total":[]}

def buy():
    j=1
    while j==1:
        entry=input("What do you want to buy :- ")
        if entry=='Cap'or entry=='cap':
            b=int(input("Enter Number of Items :- "))
            pfl.setdefault('Item',[]).append(entry)
            pfl.setdefault('Number',[]).append(b)
            pfl.setdefault('Price',[]).append(100)
            pfl.setdefault('Total',[]).append(b*100)
            break
        elif entry=='Jeans' or entry=='jeans':
            b=int(input("Enter Number of Items :- "))
            pfl.setdefault('Item',[]).append(entry)
            pfl.setdefault('Number',[]).append(b)
            pfl.setdefault('Price',[]).append(1000)
            pfl.setdefault('Total',[]).append(b*1000)
            break
        elif entry=='Shirt' or entry=='shirt':
            b=int(input("Enter Number of Items :- "))
            pfl.setdefault('Item',[]).append(entry)
            pfl.setdefault('Number',[]).append(b)
            pfl.setdefault('Price',[]).append(1500)
            pfl.setdefault('Total',[]).append(b*1500)
            break
        elif entry=='T-shirt'or entry=='t-shirt'or entry=='tshirt':
            b=int(input("Enter Number of Items :- "))
            pfl.setdefault('Item',[]).append(entry)
            pfl.setdefault('Number',[]).append(b)
            pfl.setdefault('Price',[]).append(500)
            pfl.setdefault('Total',[]).append(b*500)
            break
        else :
            print("Please choose within options ")
            
    print("*****")
    print("*****")
    print("You are buying.....")
    print("*****")
    print("*****")
    length=len(pfl['Item'])
    for q in pfl:
        print(q,end="         ")
    print()
    for qw in range(0,length):    
        for w,e in pfl.items():
            print(e[qw],end="           ")
        print()
l=2
while l==2:
    z=input("Enter YES if you wish to buy or NO to proceed :- ")
    if z=='YES' or z=='yes':
        buy()
    elif z=='NO'or z=='no':
        break
        l=1
    else:
        print("Please choose valid option")
print()
print()

print("Sub Total  :",sum(pfl["Total"]))
print()
print("***********")
print("***********")
print("THANK YOU FOR SHOPPING WITH US")     
print("***********")
print("***********")

















