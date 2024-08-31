
'''
mylist = [1,4,5,'pratap',True,33]
print(mylist)
print(mylist[:])
print(type(mylist))
print(len(mylist))
print(mylist[1:2])
print(mylist[1:-1])
print(mylist[5-2])
print(mylist[1:len(mylist)-3])

if 'pratap' in mylist:
    print('yes')
else:
    print('no')


if 'tap' in mylist:
    print('yes')
else:
    print('no')



if 'tap' in mylist[3]:
    print('yes')
else:
    print('no')
'''


'''
nlist = [i for i in range(10) ]
print(nlist)

nlist = [i+2 for i in range(10) ]
print(nlist)

nlist = [i*2 for i in range(10) ]
print(nlist)


nlist = [i for i in range(50) if i%5==0]
print(nlist)
'''


# Mathods of list
of = [1,25,2,3,5,385,174,5,8,5,6]
# print(of)
# of.append(3) add 3 in last
# of.clear()  remove all items from list
# of.copy()  copy of list
'''
count3 =  of.count(3)
count3 =  of.count(5)
print(count3)
'''


'''
name = ['Py','js','css','ts','jsx','html']
of.extend(name)
print(of)
'''

'''
name = ['Py','js','css','ts','jsx','html']
# name.index(5)
print(name.index('ts'))
print(name.index('js'))
'''


'''
name = ['Py','js','css','ts','jsx','html']
print(name)
name.insert(2,'React.js')
print(name)
name.pop()
print(name)
name.remove('jsx')
# name.remove('jsx','ts') will get type error
print(name)




name = ['Py','js','css','ts','jsx','html']
name.reverse()
print(name)
'''


'''
of = [1,25,2,3,5,385,174,5,8,5,6]
of.sort()
minnum_of = min(of)
print(minnum_of)
maxnum_of =max(of)
print(maxnum_of)

'''

