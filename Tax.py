# Takes 4 lines of input salary,age, gender, invested, amount 

amt=int(input("Enter the income you earn :"))
age=int(input("Ener your age :"))
gen=input("Enter your gender \n if Male M \n else F :")
if(gen=='m' or gen=='M' or gen=='f' or gen=='F'): 
   
    print("Correct entry")

else:

   
    print("The letter you entered is worong terminate the program and run it once again becaue you may get the answer wrong")

inv=eval(input("Invested amount : "))
tax=0

if(inv<100001):
    amt1=amt-inv

else:
    amt1=amt

if amt1<250001:
    print("No tax as your amount is less than 2,50,000")
    tax=0


if(amt1>250000 and amt1<500001):

    if(age<60 and (gen=='M' or gen=='m')):
        tax=((amt1-250000)*(5/100))

if(age>60 or (gen=='F' or gen=='f')):
    tax=((amt1-250000)*(3/100))

if(amt1>500000 and amt1<1000001):

    if(age<60 and(gen=='m' or gen=='M')):
        tax(((amt1-500000)*(1/5))+12500)

    if(age>60 or (gen=='F' or gen=='f')):
         tax=(((amt1-500000)*(1/5))+7500) 

if(amt1>1000001):

     if(age<60 and (gen=='m' or gen=='M')):
        tax=(((amt1-1000000)*(3/10))+125000) 

else:

    if(age>60 or (gen=='F' or gen=='f')):
        tax=(((amt1-1000000)*(1/5))+107500)   

EduHea=tax*(4/100)
print("The amount you earn is :")
print(amt)
print("Left out amount after investing : ")
print(amt1)
print(" Total Tax you pay is :")
print(EduHea+tax)
print("Education and health tax is :")
print(EduHea)
print("Left out money is :")
print(amt1-EduHea-tax)     






