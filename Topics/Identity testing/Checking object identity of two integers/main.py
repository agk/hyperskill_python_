a = int(input())
b = int(input())

def are_same_object(object_a, object_b):
    return True if object_a == object_b else False

print(are_same_object(a, b))