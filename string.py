"""
BankManager = 'Kartik Bharadwaj'
print(BankManager)
print(BankManager[0:6])
print(len(BankManager))
"""

nm = "harry"
# print(nm[-4:-2])
# print(len(nm))

# String methods tut 13 harry bhai

myJob = 'Frontend Dev'
# print(myJob.upper())
# print(myJob.lower())

# remove trailing character
# my_state = 'Utter Pradesh!!!!!!!!!!'
# print(my_state.rstrip("!"))



my_state1 = 'Utter Pradesh'
# print(my_state1.rstrip("sh"))




# replace character or word from string
your_distt = "my district Is Vellore"
result = your_distt.replace('vellore' , 'Kollam')
result1 = your_distt.split(" ")
result2 = your_distt.capitalize()
result3 = your_distt.center(50)
result4 = your_distt.count('d')
result4_a = your_distt.count('e')
result5 = your_distt.endswith('l')
result5_a = your_distt.endswith('e')
result5_b = your_distt.endswith('s',3,14)
result6 = your_distt.find('ict')
# result7 = your_distt.index('icst')
result7_a = your_distt.index('is')
result8 = your_distt.swapcase()
result8_a = your_distt.swapcase()
# print(your_distt)

'''
print(result)
print(result1)
print(result2)
print(len(your_distt))
print(result3)  
print(len(result3))
print(result4)
print(result4_a)
print(result5)
print(result5_a)
print(result5_b)
print(result6)
 print(result7)
print(result7_a)
print(result8)
print(result8_a)
'''


you_name = input("Enter your name: ")
print("Hi, your name contains " , len(you_name), "Letters")

for name in you_name:
    print(name)