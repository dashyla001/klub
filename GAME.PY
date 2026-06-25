import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root 
        self.root.title("🗿 Камень ✂️ Ножницы 📄 Бумага")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.root.configure(bg='#1a1a2e')
        
        
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        
       
        self.player_choice = tk.StringVar(value="❓")
        self.computer_choice = tk.StringVar(value="❓")
        self.result_text = tk.StringVar(value="🎮 Начни игру! Выбери свой ход")
        
        
        self.create_interface()
        
    def create_interface(self):
        
        title_frame = tk.Frame(self.root, bg='#1a1a2e')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="🗿 КАМЕНЬ ✂️ НОЖНИЦЫ 📄 БУМАГА",
            font=('Arial', 22, 'bold'),
            bg='#1a1a2e',
            fg='#e94560'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Игра до 5 побед!",
            font=('Arial', 12),
            bg='#1a1a2e',
            fg='#aaaaaa'
        )
        subtitle_label.pack()
        
        
        score_frame = tk.Frame(self.root, bg='#16213e', relief='ridge', bd=3)
        score_frame.pack(pady=15, padx=20, fill='x')
        
        self.score_label = tk.Label(
            score_frame,
            text=f"🏆 Игрок: {self.player_score}  |  🤝 Ничьи: {self.ties}  |  💻 Компьютер: {self.computer_score}",
            font=('Arial', 16, 'bold'),
            bg='#16213e',
            fg='#ffffff',
            pady=10
        )
        self.score_label.pack()
        
        
        choices_frame = tk.Frame(self.root, bg='#1a1a2e')
        choices_frame.pack(pady=20)
        
        
        player_frame = tk.LabelFrame(
            choices_frame,
            text="🤔 Твой выбор",
            font=('Arial', 14, 'bold'),
            bg='#16213e',
            fg='#4ecdc4',
            padx=40,
            pady=15,
            relief='solid',
            bd=2
        )
        player_frame.pack(side=tk.LEFT, padx=20)
        
        self.player_label = tk.Label(
            player_frame,
            textvariable=self.player_choice,
            font=('Arial', 64),
            bg='#16213e',
            fg='#ffffff',
            width=2
        )
        self.player_label.pack()
        
        
        computer_frame = tk.LabelFrame(
            choices_frame,
            text="🤖 Выбор компьютера",
            font=('Arial', 14, 'bold'),
            bg='#16213e',
            fg='#ff6b6b',
            padx=40,
            pady=15,
            relief='solid',
            bd=2
        )
        computer_frame.pack(side=tk.RIGHT, padx=20)
        
        self.computer_label = tk.Label(
            computer_frame,
            textvariable=self.computer_choice,
            font=('Arial', 64),
            bg='#16213e',
            fg='#ffffff',
            width=2
        )
        self.computer_label.pack()
        
        
        buttons_frame = tk.Frame(self.root, bg='#1a1a2e')
        buttons_frame.pack(pady=20)
        
        # Камень
        rock_btn = tk.Button(
            buttons_frame,
            text="🗿 Камень",
            font=('Arial', 16, 'bold'),
            bg='#e94560',
            fg='white',
            padx=25,
            pady=15,
            relief='raised',
            bd=3,
            cursor='hand2',
            command=lambda: self.play_round(0)
        )
        rock_btn.pack(side=tk.LEFT, padx=10)
        
       
        scissors_btn = tk.Button(
            buttons_frame,
            text="✂️ Ножницы",
            font=('Arial', 16, 'bold'),
            bg='#0f3460',
            fg='white',
            padx=25,
            pady=15,
            relief='raised',
            bd=3,
            cursor='hand2',
            command=lambda: self.play_round(1)
        )
        scissors_btn.pack(side=tk.LEFT, padx=10)
        
        
        paper_btn = tk.Button(
            buttons_frame,
            text="📄 Бумага",
            font=('Arial', 16, 'bold'),
            bg='#1b9aaa',
            fg='white',
            padx=25,
            pady=15,
            relief='raised',
            bd=3,
            cursor='hand2',
            command=lambda: self.play_round(2)
        )
        paper_btn.pack(side=tk.LEFT, padx=10)
        
        
        result_frame = tk.Frame(self.root, bg='#16213e', relief='ridge', bd=3)
        result_frame.pack(pady=15, padx=20, fill='x')
        
        self.result_label = tk.Label(
            result_frame,
            textvariable=self.result_text,
            font=('Arial', 18, 'bold'),
            bg='#16213e',
            fg='#f9ca24',
            pady=15,
            wraplength=500
        )
        self.result_label.pack()
        
        
        control_frame = tk.Frame(self.root, bg='#1a1a2e')
        control_frame.pack(pady=10)
        
        reset_btn = tk.Button(
            control_frame,
            text="🔄 Новая игра",
            font=('Arial', 14, 'bold'),
            bg='#6c5ce7',
            fg='white',
            padx=25,
            pady=10,
            relief='raised',
            bd=3,
            cursor='hand2',
            command=self.reset_game
        )
        reset_btn.pack(side=tk.LEFT, padx=10)
        
        exit_btn = tk.Button(
            control_frame,
            text="❌ Выйти",
            font=('Arial', 14, 'bold'),
            bg='#d63031',
            fg='white',
            padx=25,
            pady=10,
            relief='raised',
            bd=3,
            cursor='hand2',
            command=self.root.quit
        )
        exit_btn.pack(side=tk.LEFT, padx=10)
    
    def play_round(self, player_choice):
        
        emojis = ['🗿', '✂️', '📄']
        names = ['Камень', 'Ножницы', 'Бумага']
        
        
        self.player_choice.set(emojis[player_choice])
        
        
        computer_choice = random.randint(0, 2)
        self.computer_choice.set(emojis[computer_choice])
        
        
        if player_choice == computer_choice:
            result = "🤝 Ничья!"
            self.ties += 1
            color = '#f9ca24'
        elif (player_choice == 0 and computer_choice == 1) or \
             (player_choice == 1 and computer_choice == 2) or \
             (player_choice == 2 and computer_choice == 0):
            result = "🎉 Ты победил!"
            self.player_score += 1
            color = '#2ecc71'
        else:
            result = "😢 Компьютер победил!"
            self.computer_score += 1
            color = '#e74c3c'
        
        
        self.result_text.set(f"{result}\n\nТы: {names[player_choice]}  |  Компьютер: {names[computer_choice]}")
        self.result_label.config(fg=color)
        
        
        self.update_score()
        
        
        if self.player_score >= 5:
            messagebox.showinfo(
                "🏆 ПОБЕДА!",
                f"Ты выиграл игру со счётом {self.player_score}:{self.computer_score}!\n\nОтличная игра! 🎉"
            )
            self.reset_game()
        elif self.computer_score >= 5:
            messagebox.showinfo(
                "😔 ПОРАЖЕНИЕ",
                f"Компьютер выиграл со счётом {self.player_score}:{self.computer_score}!\n\nВ следующий раз повезёт! 💪"
            )
            self.reset_game()
    
    def update_score(self):
        self.score_label.config(
            text=f"🏆 Игрок: {self.player_score}  |  🤝 Ничьи: {self.ties}  |  💻 Компьютер: {self.computer_score}"
        )
    
    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.ties = 0
        self.player_choice.set("❓")
        self.computer_choice.set("❓")
        self.result_text.set("🎮 Новая игра! Выбери свой ход!")
        self.result_label.config(fg='#f9ca24')
        self.update_score()


if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()