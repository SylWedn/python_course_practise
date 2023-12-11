types_list = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]

no_bool_list = list(filter(lambda x: not isinstance(x, bool), types_list))

print(no_bool_list)

# with filter method type
# int_list = filter(lambda x: type(x) is int or type(x) is float, types_list)
# int_list = filter(lambda x: type(x) in [int, float] types_list)

int_list = list(filter(lambda x: isinstance(x, int) or isinstance(x, float), no_bool_list))
print(int_list)
print(sum(int_list))

str_list = list(filter(lambda x: isinstance(x, str), types_list))

print(str_list)

true_list = len(list(filter(lambda x: x is True, types_list)))
print(true_list)
