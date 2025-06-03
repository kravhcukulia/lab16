from tkinter import *
import winsound

def play():
    val = var.get()
    
    if val == 0:
        winsound.PlaySound("C:/Users/Asus/Desktop/лабораторна16/apple.wav.wav", winsound.SND_FILENAME)
    elif val == 1:
        winsound.PlaySound("C:/Users/Asus/Desktop/лабораторна16/banana.wav.wav", winsound.SND_FILENAME)
    elif val == 2:
        winsound.PlaySound("C:/Users/Asus/Desktop/лабораторна16/вишня.wav", winsound.SND_FILENAME)
    elif val == 3:
        winsound.PlaySound("C:/Users/Asus/Desktop/лабораторна16/персик.wav", winsound.SND_FILENAME)
    elif val == 4:
        winsound.PlaySound("C:/Users/Asus/Desktop/лабораторна16/ківі.wav", winsound.SND_FILENAME)
    elif val == 5:
        winsound.PlaySound("C:/Users/Asus/Desktop/лабораторна16/полуниця.wav", winsound.SND_FILENAME)

# Створення вікна
root = Tk()
root.minsize(width=1000, height=800)
root.title("Словник")
root['bg'] = 'white'

# Фрейм з радіокнопками
frame = LabelFrame(root, text="Виберіть слово", padx=50, bg="white", bd=3)
frame.pack()

var = IntVar()
var.set(0)

# Радіокнопки
Radiobutton(frame, bg="white", text="Яблуко", variable=var, value=0).pack(anchor=W)
Radiobutton(frame, bg="white", text="Банан", variable=var, value=1).pack(anchor=W)
Radiobutton(frame, bg="white", text="Вишня", variable=var, value=2).pack(anchor=W)
Radiobutton(frame, bg="white", text="Персик", variable=var, value=3).pack(anchor=W)
Radiobutton(frame, bg="white", text="Ківі", variable=var, value=4).pack(anchor=W)
Radiobutton(frame, bg="white", text="Полуниця", variable=var, value=5).pack(anchor=W)
# Кнопка для запуску звуку
Button(text="Відтворити", width=15, height=2, bg="yellow", command=play).pack(pady=10)

# Полотно зображення
canvas = Canvas(root, width=500, height=800, bg="white")
canvas.pack()

# Зображення (приклад: "image.png")
img = PhotoImage(file="C:/Users/Asus/Desktop/лабораторна16/яблуко_app-removebg-preview-removebg-preview.png")
canvas.create_image(10, 10, image=img, anchor=NW)
canvas.image = img  # зберігаємо посилання на зображення, щоб не зникло

root.mainloop()
