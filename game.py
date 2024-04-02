import tkinter as tk
import random
from tkinter.messagebox import showinfo
# from main import MainWindow

class TicTacToe():
    def __init__(self, master, first_player_name, second_player_name):
        self.draw_amount = 0
        self.master = master  # Определение корневого окна
        self.game_number = 1
        
        for c in range(3): self.master.columnconfigure(index=c, weight=1)
        for r in range(3): self.master.rowconfigure(index=r, weight=1)
        
        self.master.title("TicTacToe")  # Установка заголовка окна
        self.first_player_name = "Player1" if first_player_name == "" else first_player_name
        self.second_player_name = "Player2" if second_player_name == "" else second_player_name
        self.first_player = ['X', self.first_player_name, 0] # Установка начального игрока
        self.second_player = ['O', self.second_player_name, 0]
        self.current_player = random.choice([self.first_player, self.second_player])[0]
        self.board = [" " for _ in range(9)]  # Создание пустого игрового поля
        self.buttons = []  # Создание списка для хранения кнопок игрового поля
        
        self.player_turn_label = tk.Label(self.master, text='Game '+str(self.game_number)+'\n'+self.first_player_name+" move", foreground='white', background="black", font=('Courier', 20))
        self.player_turn_label.grid(row=0, column=0, columnspan=3)
        
        for i in range(1, 4):
            row = []  # Создание списка для хранения кнопок в строке
            for j in range(3):
                # Создание кнопки и привязка метода on_button_click к событию нажатия
                button = tk.Button(self.master, text=" ",  foreground='white', background="black", font=('Courier', 20),
                                   width=80, height=1, command=lambda i=i, j=j: self.on_button_click(i-1, j))
                button.grid(row=i, column=j, sticky="nsew")  # Размещение кнопки на сетке
                row.append(button)  # Добавление кнопки в строку
            self.buttons.append(row)  # Добавление строки кнопок в общий список

        self.reset_button = tk.Button(self.master, text="New Game", foreground='white', background="black", font=('Courier', 20), command=self.reset_game_with_scores)  # Создание кнопки для сброса игры
        self.reset_button.grid(row=4, column=0, columnspan=3, sticky="nsew")  # Размещение кнопки на сетке
        self.stats_label = tk.Label(self.master, text=self.first_player_name+' '+str(self.first_player[2])+':'+str(self.second_player[2])+' '+self.second_player_name, foreground='white', background="black", font=('Courier', 20))
        self.stats_label.grid(column=0, row=5, columnspan=3, sticky="nsew")
        
    def on_button_click(self, i, j):
        if self.board[i * 3 + j] == " ":  # Проверка, что клетка пуста
            # Установка символа текущего игрока в клетку
            self.board[i * 3 + j] = self.current_player
            # Обновление текста на кнопке
            self.buttons[i][j].config(text=self.current_player)  
            
            if self.current_player == "X":
                self.player_turn_label.config(text='Game '+str(self.game_number)+'\n'+self.first_player[1]+' move')
            elif self.current_player == "O":
                self.player_turn_label.config(text='Game '+str(self.game_number)+'\n'+self.second_player[1]+' move')
                
            if self.check_winner(i, j):  # Проверка на победу
                if self.current_player == "X":
                    self.first_player[2] += 1
                    showinfo("Победа",
                                        f"Игрок {self.first_player[1]} выиграл!☆")  # Отображение сообщения о победе
                elif self.current_player == "O":
                    self.second_player[2] += 1
                    showinfo("Победа",
                                        f"Игрок {self.second_player[1]} выиграл!☆")  # Отображение сообщения о победе
                self.reset_game()  # Сброс игры
            elif " " not in self.board:  # Проверка на ничью
                showinfo("Ничья", "Ничья!☆")  # Отображение сообщения о ничьей
                self.first_player[2] += 0.5
                self.second_player[2] += 0.5
                self.reset_game()  # Сброс игры
            else:
                self.current_player = "O" if self.current_player == "X" else "X"  # Смена игрока
                
            

    def check_winner(self, i, j):
        row = all(self.board[i*3 + col] == self.current_player for col in range(3))  # Проверка по горизонтали
        col = all(self.board[row*3 + j] == self.current_player for row in range(3))  # Проверка по вертикали
        diag1 = all(self.board[i*3 + i] == self.current_player for i in range(3))  # Проверка по диагонали
        diag2 = all(self.board[i*3 + 2-i] == self.current_player for i in range(3))  # Проверка по диагонали
        return any([row, col, diag1, diag2])  # Возвращает True, если есть победа

    def reset_game_with_scores(self):
        self.first_player[2] = 0
        self.second_player[2] = 0
        self.game_number = 0
        self.reset_game()

    def reset_game(self):
        if self.current_player == "X":
            self.current_player = "O"
        elif self.current_player == "O":
            self.current_player = "X"
        
        self.game_number += 1
        if self.current_player == "X":
            self.player_turn_label.config(text='Game '+str(self.game_number)+'\n'+self.first_player[1]+' move')
        elif self.current_player == "O":
            self.player_turn_label.config(text='Game '+str(self.game_number)+'\n'+self.second_player[1]+' move')
        
        self.board = [" " for _ in range(9)]
        self.stats_label = tk.Label(
            self.master,
            text=self.first_player_name+' '+str(self.first_player[2])+':'+str(self.second_player[2])+' '+self.second_player_name,
            foreground='white', 
            background="black", 
            font=('Courier', 20)
        )
        self.stats_label.grid(column=0, row=5, columnspan=4, sticky="nsew")
        # Очистка игрового поля
        for i in range(3):
            for j in range(0, 3):
                self.buttons[i][j].config(text=" ")  # Очистка текста на кнопках

