file1=open(r'C:\Users\Navya\Desktop\goodies\input.txt','r') 
lines=file1.readlines() #reads file 
goodies=[]  
number_of_employees=int(lines[0][-2]) 
for i in range(4,len(lines)):
    l=lines[i].split(":")
    goodies.append([l[0],int(l[1])]) 
goodies=sorted(goodies,key=lambda x:x[1]) #sorted the list
min_diff=float('inf') 
for i in range(0,len(goodies)-number_of_employees+1): 
    diff=goodies[i+number_of_employees-1][1]-goodies[i][1]
    if diff<min_diff:
        min_index=i
        min_diff=diff
file1.close() 
file2=open(r'C:\Users\Navya\Desktop\goodies\output.txt','w')
file2.write("\n")
for i in range(min_index,min_index+number_of_employees):
    file2.write(goodies[i][0]+":"+str(goodies[i][1])+"\n")
file2.write("\n")
file2.write("And the difference between the chosen goodie with highest price and the lowest price is "+ str(min_diff))
file2.close() #closing output file
