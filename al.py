from tkinter import *
import os.path

b, c, a = True, True, True


def change(ws, button):
    global b, c, a
    if ws == 'b':
        if b == True:
            button['bg'] = "#e15656"
            b = False
        else:
            button['bg'] = "#56e171"
            b = True
    if ws == 'c':
        if c == True:
            button['bg'] = "#e15656"
            c = False
        else:
            button['bg'] = "#56e171"
            c = True
    if ws == 'a':
        if a == True:
            button['bg'] = "#e15656"
            a = False
        else:
            button['bg'] = "#56e171"
            a = True
    update()

root = Tk()
root.title('Алгебра логики')
if os.path.exists("al.ico"):
    root.iconbitmap("al.ico")
t = Canvas(root, width=555, height=340, bg="#e7e7e7")
# кнопка B
frameB = Frame(root, width=56, height=56)
frameB.pack_propagate(0)
frameB.place(x=20, y=20)
buttonB = Button(frameB, text="B", bg="#56e171", activebackground='#2f2d2d', fg='#fff', activeforeground='#fff', bd=0, cursor="hand2")
buttonB.config(command=lambda: change('b', buttonB))
buttonB.pack(fill=BOTH, expand=1)
# кнопка C
frameC = Frame(root, width=56, height=56)
frameC.pack_propagate(0)
frameC.place(x=20, y=109)
buttonC = Button(frameC, text="C", bg="#56e171", activebackground='#2f2d2d', fg='#fff', activeforeground='#fff', bd=0, cursor="hand2")
buttonC.config(command=lambda: change('c', buttonC))
buttonC.pack(fill=BOTH, expand=1)
# кнопка A
frameA = Frame(root, width=56, height=56)
frameA.pack_propagate(0)
frameA.place(x=20, y=198)
buttonA = Button(frameA, text="A", bg="#56e171", activebackground='#2f2d2d', fg='#fff', activeforeground='#fff', bd=0, cursor="hand2")
buttonA.config(command=lambda: change('a', buttonA))
buttonA.pack(fill=BOTH, expand=1)
#
def update():
    if b:
        t.create_line(75, 48, 136, 48, fill="#56e171")
        t.create_line(135, 48, 135, 65, fill="#56e171", arrow=LAST)
    else:
        t.create_line(75, 48, 136, 48, fill="#e15656")
        t.create_line(135, 48, 135, 65, fill="#e15656", arrow=LAST)
    if c:
        t.create_line(75, 136, 308, 136, fill="#56e171")
        t.create_line(135, 136, 135, 118, fill="#56e171", arrow=LAST)
        t.create_line(222, 136, 222, 119, fill="#56e171", arrow=LAST)
        t.create_line(307, 136, 307, 154, fill="#56e171", arrow=LAST)
    else:
        t.create_line(75, 136, 308, 136, fill="#e15656")
        t.create_line(135, 136, 135, 118, fill="#e15656", arrow=LAST)
        t.create_line(222, 136, 222, 119, fill="#e15656", arrow=LAST)
        t.create_line(307, 136, 307, 154, fill="#e15656", arrow=LAST)
    if a:
        t.create_line(75, 225, 446, 225, fill="#56e171")
        t.create_line(176, 225, 176, 182, fill="#56e171")
        t.create_line(176, 182, 195, 182, fill="#56e171", arrow=LAST)
        t.create_line(446, 225, 446, 119, fill="#56e171", arrow=LAST)
    else:
        t.create_line(75, 225, 446, 225, fill="#e15656")
        t.create_line(176, 225, 176, 182, fill="#e15656")
        t.create_line(176, 182, 195, 182, fill="#e15656", arrow=LAST)
        t.create_line(446, 225, 446, 119, fill="#e15656", arrow=LAST)
    #Out1. Штрих Шеффера
    if b and c and b == c:
        out1 = False
    else:
        out1 = True
    if out1:
        t.create_rectangle(109, 65, 162, 118, fill="#56e171")
        t.create_line(163, 91, 195, 91, fill="#56e171", arrow=LAST)
    else:
        t.create_rectangle(109, 65, 162, 118, fill="#e15656")
        t.create_line(163, 91, 195, 91, fill="#e15656", arrow=LAST)
    t.create_text(135, 92, text="l", fill="#fff", font=("Myriad Pro", 26))
    #Out2. Сложение
    if not out1 and not c:
        out2 = False
    else:
        out2 = True
    if out2:
        t.create_rectangle(195, 65, 248, 118, fill="#56e171")
        t.create_line(249, 91, 335, 91, fill="#56e171", arrow=LAST)
    else:
        t.create_rectangle(195, 65, 248, 118, fill="#e15656")
        t.create_line(249, 91, 335, 91, fill="#e15656", arrow=LAST)
    t.create_text(221, 93, text="∨", fill="#fff", font=("Myriad Pro", 26))
    #Out3. Обратное C
    out3 = not c
    if out3:
        t.create_rectangle(281, 155, 334, 208, fill="#56e171")
        t.create_line(280, 182, 248, 182, fill="#56e171", arrow=LAST)
    else:
        t.create_rectangle(281, 155, 334, 208, fill="#e15656")
        t.create_line(280, 182, 248, 182, fill="#e15656", arrow=LAST)
    t.create_text(308, 182, text="¬", fill="#fff", font=("Myriad Pro", 26))
    #Out4. Умножение
    if out3 and a:
        out4 = True
    else:
        out4 = False
    if out4:
        t.create_rectangle(195, 155, 248, 208, fill="#56e171")
        t.create_line(222, 209, 222, 216, fill="#56e171")
        t.create_line(222, 216, 361, 216, fill="#56e171")
        t.create_line(361, 216, 361, 117, fill="#56e171", arrow=LAST)
    else:
        t.create_rectangle(195, 155, 248, 208, fill="#e15656")
        t.create_line(222, 209, 222, 216, fill="#e15656")
        t.create_line(222, 216, 361, 216, fill="#e15656")
        t.create_line(361, 216, 361, 117, fill="#e15656", arrow=LAST)
    t.create_text(221, 181, text="∧", fill="#fff", font=("Myriad Pro", 26))
    #Out5. Стрелка Пирса
    if not out2 and not out4:
        out5 = True
    else:
        out5 = False
    if out5:
        t.create_rectangle(335, 65, 388, 118, fill="#56e171")
        t.create_line(389, 91, 420, 91, fill="#56e171", arrow=LAST)
    else:
        t.create_rectangle(335, 65, 388, 118, fill="#e15656")
        t.create_line(389, 91, 420, 91, fill="#e15656", arrow=LAST)
    t.create_text(362, 87, text="↓", fill="#fff", font=("Myriad Pro", 26))
    #Out6. Импликация
    if out5 and not a:
        out6 = False
    else:
        out6 = True
    t.create_text(525, 90, text="F", fill="#2f2d2d", font=("Myriad Pro", 30))
    t.create_text(525, 91, text="F", fill="#2f2d2d", font=("Myriad Pro", 30))
    t.create_text(527, 91, text="F", fill="#2f2d2d", font=("Myriad Pro", 30))
    t.create_text(526, 89, text="F", fill="#2f2d2d", font=("Myriad Pro", 30))
    if out6:
        t.create_rectangle(421, 65, 474, 118, fill="#56e171")
        t.create_line(475, 91, 507, 91, fill="#56e171", arrow=LAST)
        t.create_text(526, 90, text="F", fill="#56e171", font=("Myriad Pro", 30))
    else:
        t.create_rectangle(421, 65, 474, 118, fill="#e15656")
        t.create_line(475, 91, 507, 91, fill="#e15656", arrow=LAST)
        t.create_text(526, 90, text="F", fill="#e15656", font=("Myriad Pro", 30))
    t.create_text(447, 89, text="→", fill="#fff", font=("Myriad Pro", 26))

t.create_text(285, 300, text="F=(CvB|C)↓(А^(¬C))→A     (B-11)", fill="#2f2d2d", font=("Source Sans Variable", 18))


update()

t.pack()
root.mainloop()
