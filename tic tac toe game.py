import tkinter as tk 
from tkinter import messagebox

def check_winner():
    for combo in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
        if button[combo[0]]["text"] == button[combo[1]]["text"] == button[combo[2]]["text"] !="":
                   button[combo[0]].config(bg="green")
                   button[combo[1]].config(bg="green")
                   button[combo[2]].config(bg="green")
                   messagebox.showinfo("tic-tac-toe", f"player {button[combo[0]]['text']} wins!")
                   root.quit()
                   
def button_click(index):
      if button[index]["text"] == "" and not winner:
            button[index]["text"] = current_player
            check_winner()
            toggle_player()

def toggle_player():
      global current_player
      current_player = "X" if current_player == "o" else "o"
      label.config(text=f"player {current_player}'s turn")

root = tk.Tk()
root.title("tic-tac-toe")

button = [tk.Button(root, text="",font=("normal", 25), width=6, height=2, command=lambda i=i: button_click(i)) for i in range(9)]

for i, button in enumerate(button):
      button.grid(row=i //3, column=i % 3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop() 