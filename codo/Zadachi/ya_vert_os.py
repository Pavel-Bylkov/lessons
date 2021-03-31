"""
[(x1, y1), (x2, y2), ...]

Существует ли на плоскости вертикальная ось симметрии для этого множества точек?
"""

def has_vert_os(points):
    Y = {}
    for point in points:
        if point[1] in Y:
            Y[point[1]].append(point[0])
        else:
            Y[point[1]] = [point[0]]
    x_os = set()
    for y in Y:
        Y[y].sort()
        while len(Y[y]) > 1:
            x1 = Y[y].pop(0)
            x2 = Y[y].pop()
            x_os.add(abs(x1 - x2) // 2 + x1)
        if len(Y[y]):
            x_os.add(Y[y][0])
        if len(x_os) > 1:
            return False
    return True


points = [(3, 0), (4, -2), (6, -2), (5, -4), (4, 0), (6, 0), (7, 0)]
if has_vert_os(points):
    print("Да")
else:
    print("Нет")