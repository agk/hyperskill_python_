def list_sum(some_list):
    #print(some_list)
    if some_list == []:
        return 0
    # base case
    elif len(some_list) == 1:
        return some_list[0]
    # recursive case
    else:
        return sum(some_list)

# int_list = list(map(int, input().split(" ")))
# print(list_sum(int_list))