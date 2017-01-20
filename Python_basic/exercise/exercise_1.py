list1=[]
for i in range(10):
   list=(i, i*10)
   list1.append(list)
print(list1)
#=+++++++++++++++++++++++++++++++++++++++++++++

aList = [123, 'xyz', 'zara', 'abc', 123];
print(aList)
print("Count for 123 : ", aList.count(123))
print("Count for zara : ", aList.count('zara'))

#++++++++++++++++++++++++++++++++++++++++++++++

engineers = set(['John', 'Jane', 'Jack', 'Janice'])
programmers = set(['Jack', 'Sam', 'Susan', 'Janice'])
managers = set(['Jane', 'Jack', 'Susan', 'Zack'])
employees = engineers | programmers | managers           # union
engineering_management = engineers & managers            # intersection
fulltime_management = managers - engineers - programmers # difference
engineers.add('Marvin')                                  # add element
print(engineers)

employees.issuperset(engineers)     # superset test
employees.update(engineers)         # update from another set
employees.issuperset(engineers)

for group in [engineers, programmers, managers, employees]:
    group.discard('Susan')          # unconditionally remove element
    print(group)

#+++++++++++++++++++++++++++++++++++++++++++++++
# for num in range(10,20):  #to iterate between 10 to 20
#    for i in range(2,num): #to iterate on the factors of the number
#       if num%i == 0:      #to determine the first factor
#          j=num/i          #to calculate the second factor
#          print('%d equals %d * %d' % (num,i,j))
#          break #to move to the next number, the #first FOR
#    else:                  # else part of the loop
#       print(num, 'is a prime number')

for i in range(0,11):
    print("Square of" ,i, "is", i*i, "and square root of ",i,"is ",pow(i,0.5))
M = int(input("Enter a first number: "))
N = int(input("Enter a last number: "))
for i in range(M,N):
    sum = 0
    temp = i

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if i == sum:
        print(i, "is an Armstrong number")