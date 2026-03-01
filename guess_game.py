import tkinter as tk
from tkinter import messagebox
import random

class GuessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Python 猜数字挑战")
        self.target_number = random.randint(1, 100)
        
        # 1. 创建界面元素
        self.label = tk.Label(root, text="我已经想好了一个 1-100 的数字，你猜是多少？", font=("Arial", 12))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=5)

        self.btn = tk.Button(root, text="我猜！", command=self.check_guess, bg="#4CAF50", fg="white")
        self.btn.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess < self.target_number:
                messagebox.showinfo("结果", "太小了！再试试看？")
            elif guess > self.target_number:
                messagebox.showinfo("结果", "太大了！再试试看？")
            else:
                messagebox.showinfo("恭喜", f"猜对了！就是 {self.target_number}！")
                self.target_number = random.randint(1, 100) # 重置游戏
        except ValueError:
            messagebox.showerror("错误", "请输入有效的整数！")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    game = GuessGame(root)
    root.mainloop()