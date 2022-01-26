
import tkinter as tk
from functools import partial
import random
from tkinter import messagebox
# import os
import sys
# import TkMessageBox


def user_num(user: str) -> bool:
    """
    check there are duplicate digits in the given number
    """
    for i in user:
        while user.count(i) > 1:
            return False
    return True


def randomly_generate():
    """
    Randomly generates a 4-digit number (with unique digits).
    hello
    """
    pc_random = random.randrange(1023, 9999)
    pc_random = set(str(pc_random))
    while len(pc_random) < 4:
        pc_random = random.randrange(1023, 9999)
        pc_random = set(str(pc_random))
    else:
        pc_random = "".join(pc_random)
        return pc_random






class GamesGam:

    def __init__(self):
        self.number_1 = None
        self.text = ""
        self.pc_random_number = randomly_generate()

    def number_insert(self, num):
        self.number_1 = str(num)
        print(self.number_1)
        # self.text += self.number_1
        if len(self.text) < 4:
            self.text += self.number_1
            label.configure(text=self.text, font=('helvetica', 22))
        else:
            label.configure(text=self.text, font=('helvetica', 22))
            print(self.text)

    def number_delet(self):
        if self.text != "":
            self.text = list(self.text)
            self.text.pop(-1)
            self.text = "".join(self.text)
            print(self.text)
            label.configure(text=self.text, font=('helvetica', 22))
        else:
            label.configure(text=self.text, font=('helvetica', 22))

    def number_delet_del(self):
        self.text = ""
        label.configure(text=self.text, font=('helvetica', 22))
        print(self.text)

    def helloCallBack(self):
        messagebox.askokcancel("HAppi", f"congratulations you guessed the number {self.text} guesses made by the user-")
        pc_random_number = randomly_generate()
        # self.cows_and_bulls(pc_random_number)
        print(pc_random_number)
        return pc_random_number
        # print(pc_random_number)
        # a = GamesGam()
        # os.execv()
        # os.system("shutdown /r /t 1")
        # os.close()
        # os.closerange()

    def exit_(self):
        sys.exit()

    def cows_and_bulls(self, pc_random_number):
        user = self.text
        pc_random_number =self.pc_random_number
        """
        For every digit that the user guessed correctly in the correct place,
        they have a “cow”.
        For every digit the user guessed correctly in the wrong place is a “bull.”
        Every time the user makes a guess,
        tell them how many “cows” and “bulls” they have.
        Once the user guesses the correct number, the game is over.
        """
        guesses = 0
        if user != pc_random_number and user_num(user) and len(user) == 4:
            print(pc_random_number)
            cow = 0
            bull = 0
            for i in user:
                if i in pc_random_number:
                    if user.index(i) == pc_random_number.index(i):
                        cow += 1
                    elif user.index(i) != pc_random_number.index(i):
                        bull += 1
                    else:
                        continue
                    guesses += 1
                else:
                    continue
            xs = (f"cow-{cow}--bull-{bull}")
            label_1.configure(text=xs, font=("Courier", 20))
            print(f"cow-{cow}--bull-{bull}----{user} guess a 4-digit number **** -")
        elif user_num(user) == False:
            pass

        else:
            # b = GamesGam()
            self.helloCallBack()
            # rend_num = randomly_generate()
            b = a.pc_random_number
            print("congratulations you guessed the number ", pc_random_number, "guesses made by the user-", guesses)

            return b


# b = a
a = GamesGam()
b = a.pc_random_number

root = tk.Tk()
# print(dir(root))
root.title("Games cow or bull")
root.config(bg='#5FB698')
frame_4 = tk.Frame(root, borderwidth=5, background="red")
frame_5 = tk.Frame(root, borderwidth=5, background="blue")
frame_6 = tk.Frame(root, borderwidth=5, background="black")
frame = tk.Frame(root, borderwidth=5, background="green")
frame_1 = tk.Frame(root, borderwidth=5, background="orange")
frame_2 = tk.Frame(root, borderwidth=5, background="violet")
frame_3 = tk.Frame(root, borderwidth=5, background="yellow")
frame_4.pack()
frame_5.pack()
frame_6.pack()
frame.pack()
frame_1.pack()
frame_2.pack()
frame_3.pack()
# a.cows_and_bulls()
k = "X X X X"
# root.geometry("250x170")
# l_1 = tk.Label(frame_4, text=krandomly_generate)
# l_1.config(font=("Courier", 24))
l_2 = tk.Label(frame_4, text=k)
l_2.config(font=('helvetica', 22))
label_1 = tk.Label(frame_6, text="guess a 4-digit number ****", font=('helvetica', 20))
label_1.grid(column=1, row=1)
label = tk.Label(frame_5, text="* * * *", font=('helvetica', 22))
label.grid(column=2, row=1)
slogan = tk.Button(frame, text="1", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 1))
slogan_1 = tk.Button(frame, text="2", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 2))
slogan_2 = tk.Button(frame, text="3", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 3))
button_bc = tk.Button(frame, text="BC", width=4, height=2, font=('helvetica', 22), command=partial(a.number_delet_del))
slogan_3 = tk.Button(frame_1, text="4", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 4))
slogan_4 = tk.Button(frame_1, text="5", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 5))
slogan_5 = tk.Button(frame_1, text="6", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 6))
slogan_6 = tk.Button(frame_2, text="7", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 7))
slogan_7 = tk.Button(frame_2, text="8", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 8))
slogan_8 = tk.Button(frame_2, text="9", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 9))
slogan_9 = tk.Button(frame_3, text="0", width=4, height=2, font=('helvetica', 22), command=partial(a.number_insert, 0))
button_exit = tk.Button(frame_3, text="exit", width=4, height=2, font=('helvetica', 22), command=partial(a.exit_))
slogan_10 = tk.Button(frame_1, text="<", width=4, height=2, font=('helvetica', 22), command=partial(a.number_delet))
button_ok = tk.Button(frame_2, text="OK", width=4, height=2, font=('helvetica', 22), command=partial(a.cows_and_bulls,b))


l_2.pack(side=tk.TOP)
slogan.pack(side=tk.LEFT)
slogan_1.pack(side=tk.LEFT)
slogan_2.pack(side=tk.LEFT)
slogan_3.pack(side=tk.LEFT)
button_bc.pack(side=tk.LEFT)
slogan_4.pack(side=tk.LEFT)
slogan_5.pack(side=tk.LEFT)
slogan_6.pack(side=tk.LEFT)
slogan_7.pack(side=tk.LEFT)
slogan_8.pack(side=tk.LEFT)
slogan_9.pack(side=tk.LEFT)
button_exit.pack(side=tk.LEFT)
slogan_10.pack(side=tk.LEFT)
button_ok.pack(side=tk.LEFT)

root.mainloop()


name = "Artash"

print("karen" %name)