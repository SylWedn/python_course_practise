

def f_get_century(str_nin: str) -> int:
    century_map = {
        "1": 1800,
        "2": 1800,
        "3": 1900,
        "4": 1900,
        "5": 2000,
        "6": 2000,
    }
    return century_map.get(str_nin[0])
def f_is_date_valid(str_nin: str) -> bool:
    century = 1

sample_nin = "3-720416-10"

def f_calculate_control_nr (nin: str) -> int:

    int_sum=0
    nin_numbers = list(map(int,list(nin)))
    factors_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    factors_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    for index in range(10):
        int_sum += nin_numbers [index] * factors_1[index]

    if int_sum % 11 != 10:
        return int_sum % 11

    int_sum = 0
    for index in range (10):
        int_sum += nin_numbers[index] * factors_2[index]

    if int_sum % 11 != 10:
        return int_sum % 11


    return 0

def f_validate_nin