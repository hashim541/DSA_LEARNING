num1 = 11
num2 = num1

print(num1,' -> ',id(num1))
print(num2,' -> ',id(num2))

# num2=22

# print(num2,' -> ',id(num2))

dict1={'value':11}
dict2=dict1
print(dict1,' -> ',id(dict1))
print(dict2,' -> ',id(dict2))
dict2['value'] = 22
print(dict1,' -> ',id(dict1))
print(dict2,' -> ',id(dict2))
