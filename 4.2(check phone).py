def start_check(number):
    if (number[0] == '+' and number[1] == '7') or (number[0] == '8'):
        return brackets_check(number)
    else:
        return 'error'


def brackets_check(number):
    open_br = 0
    for i in number:
        if i == "(":
            open_br += 1
        elif (i == ")") and (open_br > 0):
            open_br -= 1
    if open_br != 0:
        return 'error'
    else:
        return hyphen_check(number)


def hyphen_check(number):
    if number[-1] == '-':
        return 'error'
    else:
        h_count = 0
        for j in range(len(number)):
            if number[j] == '-':
                h_count += 1
                if h_count > 1:
                    return 'error'
            else:
                h_count -= 1
        return corrector(number)


def corrector(number):
    if number[0] == '8':
        number[0] = '+7'
    for i in number:
        if i == ')':
            number.remove(')')
    for i in number:
        if i == '(':
            number.remove('(')
    for i in number:
        if i == '-':
            number.remove('-')
    return ''.join(number)


full_num, phone_number = input(), []
for k in range(len(full_num)):
    phone_number.append(full_num[k])

print(start_check(phone_number))
