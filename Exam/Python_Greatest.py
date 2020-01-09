a = int(input('Enter value for A: '))
b = int(input('Enter value for B: '))
c = int(input('Enter value for C: '))
lst = [a, b, c]
lst.sort()
if a == b == c:
  print('The numbers are equal')
else:
  print('The greatest number is', lst[-1])

''' Kakvo az bih napisal:

lst = []
print('Press "Enter" to see the result.')
while True:
  try:
    lst.append(int(input('Enter value to compare: ')))
  except:
    break
lst.sort()  
st = set(lst)
if len(st) == 1:
  print('The numbers are equal')
else:
  print(f'The greatest number is {lst[-1]}')

'''