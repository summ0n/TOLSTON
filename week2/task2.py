def strcompare(a,b):
    if not isinstance(a, str) or not isinstance(b, str):
        return 0
    elif a == b :
        return 1
    elif a != b and b == 'learn':
        return 3
    elif len(a) > len(b):
        return 2




print(strcompare(1, 100))
print(strcompare(1, 'привет'))
print(strcompare('мир', 'мир'))
print(strcompare('программист', 'привет'))
print(strcompare('learp', 'learn'))