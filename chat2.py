lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for _ in f:
        lines.append(_.strip())

for _ in lines:
    s = _.split(' ')
    time = s[0][:5]
    name = s[0][5:]
    print(time)
    print(name)
