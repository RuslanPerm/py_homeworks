def num_check():
    check = 0
    for i in password:
        if i is int():
            check = 1
    return check


def len_check():
    if len(password) <= 8:
        return 0
    else:
        return 1


def low_up_check():
    alphabet_up = [j.upper() for j in alphabet_low]
    counter_low, counter_up = 0, 0
    for i in lst_password:
        if i in alphabet_low:
            counter_low += 1
        elif i in alphabet_up:
            counter_up += 1
    return int(counter_up * counter_low)


def combo_check():
    combo = []
    for i in range(len(alphabet_low) - 2):
        array = []
        array.append(alphabet_low[i])
        array.append(alphabet_low[i + 1])
        array.append(alphabet_low[i + 2])
        combo.append(array)

    password_combo = []
    for i in range(len(lst_password) - 2):
        array = []
        array.append(lst_password[i])
        array.append(lst_password[i + 1])
        array.append(lst_password[i + 2])
        password_combo.append(array)

    counter = 0
    combo = [''.join(j) for j in combo]
    password_combo = [''.join(j) for j in password_combo]
    map(lambda x: x.lower(), password_combo)
    for j in combo:
        if ''.join(j) in ''.join(password_combo):
            return int(counter)
        else:
            counter += 1
    return int(counter)


def test_password():
    try:
        a = 1 / (combo_check() * low_up_check() * num_check() * len_check())
        print('ok')
        print(combo_check())
        print(num_check())
        print(len_check())
        print(low_up_check())
    except ZeroDivisionError:
        print('error')


alphabet_low = ['ё', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', '', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'kl', '', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
password = input('enter ur password: ')
lst_password = [_ for _ in password]
test_password()