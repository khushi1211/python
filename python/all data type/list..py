ls = [10,20,30,40,50]  #print list
print(ls)

print(type(ls))  #find type

i=0
while i < 5:   #print list using while loop
    print(ls[i],end=" ")
    i+=1


ls.insert(2,100)  #insert new number
print(ls)

ls[2]=45  #edit value
print(ls)

for x in ls:  #print list using for loop
    print(x,end=" ")

# functions


ls.count(10)
print(ls)


ls.append(60)
print(ls)

ls.copy()
print(ls)


ls.index(10)
print(ls)

ls.pop()
print(ls)

ls.remove(20)
print(ls)

ls.reverse()
print(ls)

ls.extend("khushi")
print(ls)

l1 =[12,13,14,15,16]
print(l1)



# built in function

print(len(l1))
print(max(l1))
print(min(l1))
print(sum(l1))

#find type for last comma list
l1 =[10,20,30,]
print(type(l1))