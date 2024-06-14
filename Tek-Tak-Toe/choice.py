import tkinter as tk
from tik_tak_toe import two_player
from tik_tak_toe_computer import one_player


root_coice = tk.Tk()

root_coice.geometry("1390x850")
root_coice.title('TIK TAK TOE')
root_coice['bg'] = '#b4b8ea'
#root_coice.iconbitmap('X.ico')
color = "#4752e6"

frame_choice = tk.Frame(root_coice, bg='#b4b8ea')
frame_choice.grid(padx=500, pady=240)

button_one_player = tk.Button(frame_choice, text='One Player', bg='#772fd4', width=50, height=2, command=one_player)
button_one_player.grid(padx=10, pady=10)
button_Two_player = tk.Button(frame_choice, text='Tow Player', bg='#772fd4', width=50, height=2, command=two_player)
button_Two_player.grid(padx=10, pady=10)


root_coice.mainloop()