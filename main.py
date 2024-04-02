import tkinter as tk
import random
from game import TicTacToe 


class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="PLACEHOLDER", color='#c2c2c2', *args, **kwargs):
        
        super().__init__(master, **kwargs)

        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']

        self.bind("<FocusIn>", self.foc_in)
        self.bind("<FocusOut>", self.foc_out)

        self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def foc_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def foc_out(self, *args):
        if not self.get():
            self.put_placeholder()

class MainWindow(tk.Tk):
    def __init__(self,*args, **kwargs) -> None:
        tk.Tk.__init__(self,*args, **kwargs)
        
        self.developers = ['Kaleev Anton', 'Surkaeva Polina', 'Tandalov Kirill']
        
        # self.attributes('-fullscreen', True)
        self["bg"] = "black"
        self.geometry("500x500")
        self.resizable(False, False)
        self.columnconfigure(index=[0, 1], weight=1)
        self.rowconfigure(index=[0, 1], weight=1)
        self.label = tk.Label(self, text="", foreground='white', font=('Courier', 25))
        
        self.after(500, lambda: self.TextAnimation(
            text='Welcome to'+'\n'+' TicTacToe Project!'+"\n"+"♩✧♪●♩○♬☆"+"\n"+"Developed by"+"\n"+"Kaleev Anton"+"\n"+"Surkaeva Polina"+"\n"+"Tandalov Kirill"+"\n"+"(っ'-')╮=💌",
            label=self.label)
        )
        
        self.label["bg"] = "black"
        self.label.grid(column=0, row=0, columnspan=2)
        self.mainloop()
    
    def TextAnimation(self, text, label, is_underscore=1, is_text_typing_finished=0, i=0):  # i - индекс выводимого символа
        if i < len(text):
            label['text'] = label['text'][:-1]
            label['text'] += (text[i]+"_")
            time_wait = round(random.random()*300)
            if len(text) - 1 == i:
                time_wait = 1500
            self.after(time_wait, lambda: self.TextAnimation(text, i=i+1, is_underscore=1, is_text_typing_finished=1, label=self.label))
        else:
            if is_text_typing_finished:
                self.label1 = tk.Label(self, foreground='white', background="black", text="Player 1", font=('Courier', 10))
                self.label1.grid(column=0, row=2)
                self.label2 = tk.Label(self, foreground='white', background="black", text="Player 2", font=('Courier', 10))
                self.label2.grid(column=0, row=3)
                self.first_player_name = EntryWithPlaceholder(self, placeholder="Player 1", foreground='white', background="black", text="First player", font=('Courier', 10))
                self.second_player_name = EntryWithPlaceholder(self, placeholder="Player 2", foreground='white', background="black", text="Second Player", font=('Courier', 10))
                self.first_player_name.grid(row=2, column=1)
                self.second_player_name.grid(row=3, column=1, pady=10)
                button = tk.Button(self, text="Играть!", foreground='white', background="black", font=('Courier', 20), command = self.start_game)
                button.grid(row=4, column=0, columnspan=2, pady=50)
                label['text'] = "TicTacToe Project_"
            if is_underscore:
                is_underscore = 0
                label['text'] = self.label['text'][:-1]
                label['text'] += (" ")
            else:
                is_underscore = 1
                label['text'] = self.label['text'][:-1]
                label['text'] += ("_")
            self.after(180, lambda: self.TextAnimation(text, i=i+1, is_underscore=is_underscore, is_text_typing_finished=0, label=self.label))

    def start_game(self):
        TicTacToe(self, self.first_player_name.get(), self.second_player_name.get())
        self.label1.grid_remove()
        self.label.grid_remove()
        self.first_player_name.grid_remove()

if __name__ == '__main__':
    MainWindow()