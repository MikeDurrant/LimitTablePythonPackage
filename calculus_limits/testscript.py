def add_one(x):
    return x + 1

output = add_one(4)
print(output)

from limits import LimitTable

a = LimitTable(5,0.1,3,add_one)

print(a.func_result(5))


x_list_left = a._generate_x_list_left()
print(x_list_left)

x_list_right = a._generate_x_list_right()
print(x_list_right)

array = a._generate_fx_array()
print(array)