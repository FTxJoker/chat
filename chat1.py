def read_file(_):
    chats = []
    with open(_, 'r', encoding='utf-8-sig') as f:
        for _ in f:
            chats.append(_.strip())
    return chats


def convert(_):
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_world_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for _ in _:
        s = _.split(' ')
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1
            else:
                for m in s[2:]:
                    viki_world_count += len(m)
    print('Allen說了 {0} 個字'.format(allen_word_count))
    print('Allen傳了 {0} 個貼圖'.format(allen_sticker_count))
    print('Allen傳了 {0} 張圖片'.format(allen_image_count))
    print('Viki說了 {0} 個字'.format(viki_world_count))
    print('Viki傳了 {0} 個貼圖'.format(viki_sticker_count))
    print('Viki傳了 {0} 張圖片'.format(viki_image_count))


def write_file(_, chats):
    with open(_, 'w', encoding='utf-8-sig') as f:
        for _ in chats:
            f.write(_ + '\n')


def main(_):
    chats = read_file(_)
    chats = convert(chats)
    #  write_file('output.txt', chats)


if __name__ == '__main__':
    main('LINE-Viki.txt')
