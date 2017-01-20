print([n for n in range(0,10)])
print([((n*n+n)/2) for n in range(0,10)])
print([x for x in range(1,20) if x%2==0 ])
print([x for x in 'MATHEMATICS' if x in ['A','E','I','O','U']])

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)