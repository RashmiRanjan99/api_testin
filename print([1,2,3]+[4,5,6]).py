#  #print([1,2,3]+[4,5,6])

# # print(list(map(lambda x: x**2, [1,2,3])))

# print(type(1,))

def even_numbers():
    for num in range(1, 101, 2):
        yield num

# # Example of how to use the generator
for odd in even_numbers():
    print(odd)

