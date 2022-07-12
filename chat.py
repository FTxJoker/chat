def read_file(_):
    chats = []
    with open(_, 'r', encoding='utf-8-sig') as f:
        for _ in f:
            chats.append(_.strip())
    return chats


def convert(_):
    new = []
    person = None
    for _ in _:
        if _ == 'Allen':
            person = 'Allen'
            continue
        elif _ == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + _)
    return new


def write_file(_, chats):
    with open(_, 'w', encoding='utf-8-sig') as f:
        for _ in chats:
            f.write(_ + '\n')


def main(_):
    chats = read_file(_)
    chats = convert(chats)
    write_file('output.txt', chats)


if __name__ == '__main__':
    main('input.txt')
