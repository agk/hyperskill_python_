def startswith_capital_counter(names):
    res = 0
    for name in names:
        uppers = [l for l in name if l.isupper()]
        if uppers:
            res += 1

    return res

# names = input()
# print(startswith_capital_counter(names))