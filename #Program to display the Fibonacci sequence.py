#Program to display the Fibonacci sequence up to n-th term
nterms = int(input("How many terms? "))
# first two terms
n1,n2 =0,1
count =0
# check if the number of term is valid
if nterms <=0:
    print("please enter a positive integer")
#if there is only one term,return n1
elif nterms ==1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
#generate fibonacci sequence
else:
    print("fibonacci sequence:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        #update values
        n1=n2
        n2=nth
        count+=1