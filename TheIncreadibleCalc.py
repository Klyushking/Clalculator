from tkinter import *


# Функция для кнопок
def add_digit(digit):
    new_digit = enter.get() + str(digit)
    enter.delete(0, END)
    enter.insert(0, new_digit)


def add_operation(operation):
    if operation in "+-÷×.":
        new_operation = enter.get() + str(operation)
        enter.delete(0, END)
        enter.insert(0, new_operation)
    else:
        if operation == 'C':
            enter.delete(0, END)
        else:
            if operation == '←':
                new_enter = str(enter.get())[0:-1]
                print(new_enter)
                enter.delete(0, END)
                enter.insert(0, new_enter)
            else:
                if operation == '=':
                    enter_new = enter.get().replace("÷", "/")
                    enter_new = enter_new.replace("×", "*")
                    enter_new = eval(enter_new)

                    if '.' in str(enter_new):
                        count_symbol = 0
                        dot = str(enter_new).find('.')
                        for symbol in str(enter_new)[dot + 1 : len(str(enter_new)) + 1]:
                            if symbol != '0':
                                count_symbol += 1
                                break

                        if count_symbol == 0:
                            enter_new = str(enter_new)[0:dot]

                    enter.delete(0, END)
                    enter.insert(0, enter_new)


root = Tk()  # Создаем приложение

# Задаем параметры приложение
root['bg'] = '#121111'
root.title("Calculator")
root.wm_attributes('-alpha', 0.97)
root.geometry('400x700')

# Чо-то
canvas = Canvas(root, height=400, width=700)
canvas.pack()

# Создаем фрэйм для создания гарфических объектов
frame = Frame(root, bg='#747474')
frame.place(relwidth=1, relheight=1)

# Создаем поле ввода
enter = Entry(frame, bg='#747474', font="Inter 55", fg='#F0F0F0', bd=0, justify=RIGHT)
enter.place(x=29, y=79, width=342, height=95)

# Первая строка кнопок
btn_dot = Button(frame, text='.', font="Bold 30", fg="#3E3D3D", bg='#979797', bd=0, command=lambda: add_operation('.'))
btn_dot.place(x=29, y=241, width=75, height=74)

btn_c = Button(frame, text='C', font="50", fg="#3E3D3D", bg='#979797', bd=0, command=lambda: add_operation('C'))
btn_c.place(x=118, y=241, width=75, height=74)

btn_back = Button(frame, text='←', font="50", fg="#3E3D3D", bg='#979797', bd=0, command=lambda: add_operation('←'))
btn_back.place(x=207, y=241, width=75, height=74)

btn_del = Button(frame, text='÷', font="50", fg="#3E3D3D", bg='#979797', bd=0, command=lambda: add_operation('÷'))
btn_del.place(x=296, y=241, width=75, height=74)

# Вторая строка кнопок
btn_1 = Button(frame, text='1', font="50", fg='#C2C2C2', bg='#656565', bd=0, command=lambda: add_digit(1))
btn_1.place(x=29, y=328, width=75, height=74)

btn_2 = Button(frame, text='2', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(2))
btn_2.place(x=118, y=328, width=75, height=74)

btn_3 = Button(frame, text='3', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(3))
btn_3.place(x=207, y=328, width=75, height=74)

btn_umn = Button(frame, text='×', font="50", fg="#3E3D3D", bg='#979797', bd=0, command=lambda: add_operation('×'))
btn_umn.place(x=296, y=328, width=75, height=74)

# Третья строка кнопок
btn_4 = Button(frame, text='4', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(4))
btn_4.place(x=29, y=415, width=75, height=74)

btn_5 = Button(frame, text='5', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(5))
btn_5.place(x=118, y=415, width=75, height=74)

btn_6 = Button(frame, text='6', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(6))
btn_6.place(x=207, y=415, width=75, height=74)

btn_min = Button(frame, text='-', font="50", fg="#3E3D3D", bg='#979797', bd=0, command=lambda: add_operation('-'))
btn_min.place(x=296, y=415, width=75, height=74)

# Четвертая строка кнопок
btn_7 = Button(frame, text='7', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(7))
btn_7.place(x=29, y=502, width=75, height=74)

btn_8 = Button(frame, text='8', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(8))
btn_8.place(x=118, y=502, width=75, height=74)

btn_9 = Button(frame, text='9', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(9))
btn_9.place(x=207, y=502, width=75, height=74)

btn_plus = Button(frame, text='+', font="50", fg="#3E3D3D", bg='#979797', bd=0, command=lambda: add_operation('+'))
btn_plus.place(x=296, y=502, width=75, height=74)

# Пятая строка кнопок
btn_0 = Button(frame, text='0', font="50", fg="#C2C2C2", bg='#656565', bd=0, command=lambda: add_digit(0))
btn_0.place(x=29, y=589, width=75, height=74)

btn_eq = Button(frame, text='=', font="50", fg="#3E3D3D", bg='#979797', bd=0, command=lambda: add_operation('='))
btn_eq.place(x=118, y=589, width=253, height=74)

root.mainloop()