my_list = list(range(1, 20))
my_list.append(20)
my_list.extend([21, 22, 23, 24, 25, 2, 2, 2, 2, 2])

my_list.pop()
del (my_list[20])
my_list.remove(2)

my_set = set(my_list)

print(my_list)
print(my_set)
print(my_list[5])
print(f'Last element: {my_list[-1]}')
print(len(my_set))
print(my_list.count(2))

if 2 in my_set:
    print('There is a two into my set')

print(my_list.index(2))

my_list.sort(reverse=True)
print(my_list)
print(my_list[5::])

my_list.clear()
