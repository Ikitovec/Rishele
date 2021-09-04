from tkinter import *
from tkinter import scrolledtext
from tkinter.ttk import Combobox
from tkinter import messagebox

def clicked():

    txt_original = txt.get("1.0", 'end-1c')
    txt2.delete(1.0, END)
    txt_key = txt3.get("1.0", 'end-1c')
    ouput_text=['']*len(txt_original)
    key_alphabet='1234567890, '
    total_sovapad=0
    print(len(txt_original))
    if len(txt_original)<0:
        pass
        #messagebox.showinfo('Ошибка!','Ваш ключ длиннее (рас)шифруемоего текста!')
    else:
        key=txt_key.split()
        index=0
        for i in range (len(key)):
            b=key[i]
            k=b.split(',')
            temp_flag=0
            sovpad=0
            for j in range (1,len(k)+1):
                for m in range (0, len(k)):
                    if k[m]=='':
                        #messagebox.showinfo('Ошибка!','Вы ввели неправильный ключ (две запятые)!')
                        break

                    else:
                        temp_string=str(k[m]).split()
                        for i in temp_string:
                            if key_alphabet.find(i)==-1:
                                temp_flag=1
                                break
                        if temp_flag==0:
                            if j==int(k[m]):
                                k[m]=0
                                sovpad+=1
                                break

            if sovpad!=len(k):
                messagebox.showinfo('Ошибка!','Вы ввели неправильный ключ!')
                index=-1
            total_sovapad=total_sovapad+sovpad

        if total_sovapad>len(txt_original):
            messagebox.showinfo('Ошибка!','Ваш ключ длиннее (рас)шифруемоего текста!')
            index=-1
        if ((combo2.get() == 'Зашифровать') | (combo2.get() == 'Расшифровать')):
            if combo2.get() == 'Зашифровать':
                if index !=-1:
                    begin = 0
                    total_count = 0

                    for i in range(0, len(key)):
                        b=key[i].split(',')
                        for j in range (0, len(b)):
                            txt2.insert(INSERT, txt_original[begin + int(b[j]) - 1])
                            total_count += 1

                        begin = begin + int(len(b))

                    if total_count<len(txt_original):
                        txt2.insert(INSERT, txt_original[total_count:len(txt_original)])

            if combo2.get() == 'Расшифровать':
                if index != -1:
                    begin = 0
                    total_count = 0

                    for i in range(0, len(key)):
                        b = key[i].split(',')
                        for j in range(0, len(b)):
                            ouput_text[begin+int(b[j])-1]=txt_original[begin+j]
                            total_count += 1
                        begin=begin+len(b)

                    txt2.insert(INSERT, ''.join(ouput_text))
                    if total_count<len(txt_original):
                        txt2.insert(INSERT, txt_original[total_count:len(txt_original)])
        else:
            messagebox.showinfo('Ошибка!', f'Вы неверно ввели действие! (Зашифровать или Расшифровать)')
def swap():
    temp1=txt2.get("1.0", 'end-1c')
    txt.delete(1.0, END)
    txt.insert(INSERT, temp1)
    txt2.delete(1.0, END)

window = Tk()
window.title("Шифр Ришелье")
window.geometry('500x200')

lbl = Label(window, text="Исходный текст")
lbl.grid(column=0, row=0)


lbl = Label(window, text="ключ")
lbl.grid(column=0, row=3)

txt3 = scrolledtext.ScrolledText(window, width=40, height=1)
txt3.grid(column=2, row=3)


combo2 = Combobox(window)
combo2['values'] = ("Зашифровать", "Расшифровать")
combo2.current(0)
combo2.grid(column=0, row=4)



btn = Button(window, text="Получить ответ", command=clicked)
btn.grid(column=0, row=5)
lbl = Label(window)

btn = Button(window, text="преместить", command=swap)
btn.grid(column=2, row=4)
lbl = Label(window)


txt = scrolledtext.ScrolledText(window, width=40, height=1)
txt.grid(column=2, row=0)

txt2 = scrolledtext.ScrolledText(window, width=40, height=1)
txt2.grid(column=2, row=5)


window.mainloop()

