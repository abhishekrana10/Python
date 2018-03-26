"""program to show the use of major list methods"""

mylist=[]
yourlist=[1,"tommy"]
nested_list=[34,["name",45,11],23]

print yourlist[1]    #print 2nd item of yourlist
print nested_list[2]
print nested_list[1]

print nested_list[-1]    #print first item of nested_list

mylist.append(19)    #19 will be append at the end of mylist
print mylist

mylist.extend(yourlist)    #yourlist's all elememts will be appended in mylist
print mylist

mylist.append("hut")
mylist.append(200)
mylist.append("orange")
mylist.append("potter")
print mylist

print(mylist[2:5])    #print 3rd to fifth element of mylist
print(mylist[:-3])    #print first to 4th last element

mylist.pop()    #pop out last element of mylist
print mylist

"""yourlist.clear() #delete all elements of yourlist(Won't work in python 2)
print yourlist"""

mylist[0]=2999    #change 1st item of mylist to 3000
print mylist


 
