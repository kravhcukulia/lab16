from tkinter import *

root = Tk()
canvas = Canvas(root, width=800, height=400, bg="black")
canvas.pack()

# Трава (зелений прямокутник внизу)
canvas.create_rectangle(0, 350, 800, 400, fill='forest green', outline='')

# Дерево — стовбур
canvas.create_rectangle(100, 220, 130, 350, fill='saddlebrown', outline='black')

# Дерево — крона
canvas.create_oval(60, 160, 170, 270, fill='forest green', outline='black')
canvas.create_oval(40, 190, 120, 290, fill='forest green', outline='black')
canvas.create_oval(110, 190, 190, 290, fill='forest green', outline='black')

# Будинок — стіни
canvas.create_rectangle(350, 200, 450, 350, fill='darkorange', outline='black')

# Будинок — дах
canvas.create_polygon(340, 200, 400, 120, 460, 200, fill='peru', outline='black')

# Вікно
canvas.create_rectangle(360, 210, 400, 240, fill='skyblue', outline='black')

# Двері
canvas.create_rectangle(380, 250, 420, 330, fill='peru', outline='black')

# Зірки — великі та маленькі (зірка як багатокутник)
def draw_star(x, y, size):
    points = [
        x, y - size,
        x + size * 0.3, y - size * 0.3,
        x + size, y - size * 0.2,
        x + size * 0.4, y + size * 0.1,
        x + size * 0.6, y + size,
        x, y + size * 0.5,
        x - size * 0.6, y + size,
        x - size * 0.4, y + size * 0.1,
        x - size, y - size * 0.2,
        x - size * 0.3, y - size * 0.3
    ]
    canvas.create_polygon(points, fill="yellow", outline='')

# Малюємо кілька зірок
stars = [
    (600, 100, 20), (700, 130, 10), (750, 90, 15),
    (720, 200, 25), (670, 170, 10), (740, 160, 8),
    (680, 80, 5), (760, 210, 12)
]
for x, y, s in stars:
    draw_star(x, y, s)

root.mainloop()
