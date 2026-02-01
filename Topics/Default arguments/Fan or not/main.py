def add_viewer(name, fan_list=None):
    if fan_list is not None:

        fan_list.append(name)
    else:
        fan_list = []
        fan_list.append(name)

    return fan_list


# print(add_viewer("all"))
# print(add_viewer("all", ["sss", "dddd"]))