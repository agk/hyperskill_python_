import math
#  You can experiment here, it won’t be checked
print(float('nan') * 0.0)

inf = math.inf
nan = math.nan

print(100 * inf + nan)
print(inf / 2 - inf)
print(-inf * inf)
print(0.0 / inf)
print(inf - 10 ** 300)

print('' in 'universe')                            # 1

pet = "myguineapignamedSparks"
print(pet.startswith("pig", 3))                    # 2

longest_word = "Antidisestablishmentarianism"
print(longest_word.endswith("establishment", 20))  # 3

person = "lover"
print(person.endswith("over"))