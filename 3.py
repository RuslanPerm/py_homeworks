def impostor(*args, **kwargs):
    words = []
    for word in args:
        if 'to_reverse' in kwargs.keys():
            word = word[::-1]
        if 'swap' in kwargs.keys():
            lst = list(kwargs['swap'])
            if (len(word) > lst[1]) and (len(word) > lst[0]):
                new_word = list(word)
                new_word[lst[0]], new_word[lst[1]] = new_word[lst[1]], new_word[lst[0]]
                word = ''.join(new_word)
        if 'register' in kwargs.keys():
            if kwargs['register'] == 0:
                word = word.upper()
            elif kwargs['register'] == 1:
                word = word.lower()
            elif kwargs['register'] == 2:
                word = word.capitalize()
        words.append(word)
    return words


data = ['dtltear', 'Smurd', 'oewDlb', 'tupmert', 'gnas', 'Etulf']
conditions = {'to_reverse': True, 'swap': (2, 5), 'register': 2}
print(*impostor(*data, **conditions))

