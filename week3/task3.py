def read_file():
    file_name = input("Введите имя файла(по умолчанию referat.txt): ") or "referat.txt"
    with open(file_name, 'r', encoding='utf-8') as var:
        content = var.read()
        return content


with open('referat.txt', 'r', encoding='utf-8') as var01:
    result = var01.read()
    print('Длинна строки: {}'.format(len(result)))
    print('Количество слов: {}'.format(len(result.split())))
    print('Длинна строки: {}'.format(len(result)))
    var01.close()



with open('referat2.txt', 'w', encoding='utf-8') as var02:
    content = read_file()
    result = content.replace('.','!')
    var02.write(result)
    var02.close()

