# Глобальные переменные (настройки)
win_width = 800 
win_height = 600
left_bound = win_width / 40             # границы, за которые персонаж не выходит (начинает ехать фон)
right_bound = win_width - 8 * left_bound
shift = 0

x_start, y_start = 20, 10

img_file_back = 'cave.png'
img_file_hero = 'm1.png'
img_file_enemy = 'enemy.png' 
img_file_bomb = 'bomb.png'
img_file_princess = 'princess.png'
FPS = 60

# цвета:
C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)