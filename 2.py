stork_chat = ['skpkoiruyotrtwqS', 'savi', 'SklyhmanbwvclxZa', 'tgtrnewiqakasldfaght', 'itiuuytorebqwa', 'gjhngfidshaqtweertmyuoopS']


def birds_talking(*arg, great=False):
    count = 0
    for elem in stork_chat:
        elem = elem[::-len(*arg)].split()
        if great:
            elem = str(elem).upper()
        stork_chat[count] = elem
        count += 1


birds_talking('get', great=True)
print(stork_chat)