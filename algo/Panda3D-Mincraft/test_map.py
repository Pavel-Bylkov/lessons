from random import shuffle
colors = {'R':(1.0, 0, 0, 0.9),
          'G':(0, 1.0, 0, 0.9),
          'B':(0, 0, 1.0, 0.9),
          'Y':(1.0, 1.0, 0, 0.9),
          'O':(1.0, 0.5, 0.0, 0.9),
          'g1':(0.25, 0.5, 0.5, 0.9),
          'gr':(0.75, 0.75, 0.75, 0.9),
          'W':(1.0, 1.0, 1.0, 0.9),
          '-':None}
l_colors = [x for x in colors if x != "-"]
blocks = []
def switch_color(simbol):
    if simbol == " ":
        return "-"
    shuffle(l_colors)
    return l_colors[0]
def flour():
    s_flour = []
    flag = 1
    for i in range(71):
        if flag == 1:
            flour_line = ['W' if j % 2 == 0 else 'gr' for j in range(69)]
            flag = 0
        else:
            flour_line = ['gr' if j % 2 == 0 else 'W' for j in range(69)]
            flag = 1
        s_flour.append(flour_line)
    return s_flour
blocks.append(flour())
for k in range(5):
    with open("map1.txt", "r") as map:
        s_level = []
        for line in map:
            s_line = list(line) # создаем список из строки
            s_line.pop() # удаляем \n
            color_line = [switch_color(simbol) for simbol in s_line]
            s_level.append(color_line)
        blocks.append(s_level)
print(*blocks[4], sep="\n")