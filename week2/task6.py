def get_sum(a,b):
    try:
        result = int(a) + int(b)
        return result
    except ValueError:
        return 'Исапользуй только числа.'

print(get_sum(123,321))
print(get_sum('test',123))