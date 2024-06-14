import tkinter as tk
import random
import time

def one_player():
    global win_or_draw, player, current_sym, frame, button, list_buttons, choice_button, score_player_user_text, \
        arr_buttons, score_player_computer_text

    root = tk.Tk()

    def frame_game():
        global frame
        frame = tk.Frame(root, bg='#b4b8ea')
        frame.grid(padx=450, pady=70)

    root.geometry("1390x850")
    root.title('TIK TAK TOE')
    root['bg'] = '#b4b8ea'
    #root.iconbitmap('X.ico')
    color = "#4752e6"
    player = 'user'
    current_sym = ""
    score_player_user_text = 0
    score_player_computer_text = 0
    win_or_draw = False
    arr_buttons = []


    list_buttons = {
        '!button': '',
        '!button2': '',
        '!button3': '',
        '!button4': '',
        '!button5': '',
        '!button6': '',
        '!button7': '',
        '!button8': '',
        '!button9': '',
    }

    def enter_user():
        global player, current_sym
        player = 'computer'


    def enter_computer():
        global player, current_sym
        player = 'user'
        choice_computer()
        

    def choice_computer():
        global choice_button
        new_list_buttons = {}
        for i in list_buttons.keys():
            values_list = list_buttons[i]
            if values_list == '':
                new_list_buttons[i] = values_list
        choice_button = random.choice(list(new_list_buttons.keys()))
        

    def get_button_computer():
        for i in arr_buttons:
            if i._name == choice_button:
                time.sleep(2)
                i.config(text=current_sym)
                list_buttons[i._name] = current_sym


    def win_user():
        global win_or_draw, score_player_user_text
        score_player_user_text += 1
        score()
        win_or_draw = True
        label_x_win = tk.Button(frame, text='PLAYER IS WIN', bg='#772fd4', width=20, height=2)
        label_x_win.grid(row=2, column=1, padx=4, pady=4)
        button_play_again_x = tk.Button(frame, text='New Game', bg='#772fd4', width=15, height=2, command=new_game)
        button_play_again_x.grid(row=2, column=2, padx=4, pady=4)
        button_esc = tk.Button(frame, text='QUIT', bg='#772fd4', command=root.quit, width=10, height=2)
        button_esc.grid(row=2, column=3, padx=4, pady=4)


    def win_computer():
        global win_or_draw, score_player_computer_text
        score_player_computer_text += 1
        score()
        win_or_draw = True
        label_o_win = tk.Button(frame, text='COMPUTER IS WIN', bg='#772fd4', width=20, height=2)
        label_o_win.grid(row=2, column=1, padx=4, pady=4)
        button_play_again_o = tk.Button(frame, text='New Game', bg='#772fd4', width=10, height=2, command=new_game)
        button_play_again_o.grid(row=2, column=2, padx=4, pady=4)
        button_esc = tk.Button(frame, text='QUIT', bg='#772fd4', command=root.quit, width=5, height=2)
        button_esc.grid(row=2, column=3, padx=4, pady=4)


    def draw():
        label_draw = tk.Button(frame, text='DRAW', bg='#772fd4', width=20, height=2)
        label_draw.grid(row=2, column=1, padx=4, pady=4)
        button_play_again_draw = tk.Button(frame, text='New Game', bg='#772fd4', width=10, height=2, command=new_game)
        button_play_again_draw.grid(row=2, column=2, padx=4, pady=4)
        win_or_draw = True
        button_esc = tk.Button(frame, text='QUIT', bg='#772fd4', command=root.quit, width=5, height=2)
        button_esc.grid(row=2, column=3, padx=4, pady=4)


    def new_game():
        global player, current_sym, win_or_draw, frame, button, score_player_user_button, score_player_computer_button
        player = 'user'
        current_sym = ""
        win_or_draw = False
        list_buttons['!button'] = ''
        list_buttons['!button2'] = ''
        list_buttons['!button3'] = ''
        list_buttons['!button4'] = ''
        list_buttons['!button5'] = ''
        list_buttons['!button6'] = ''
        list_buttons['!button7'] = ''
        list_buttons['!button8'] = ''
        list_buttons['!button9'] = ''
        frame.destroy()
        button.destroy()
        score_player_user_button.destroy()
        score_player_computer_button.destroy()
        arr_buttons.clear()
        frame_game()
        button_for_loop()
        score()


    def check_win_user():
        if (list_buttons['!button'] == 'X' and list_buttons['!button2'] == 'X' and list_buttons['!button3'] == 'X') \
            or \
            (list_buttons['!button4'] == 'X' and list_buttons['!button5'] == 'X' and list_buttons['!button6'] == 'X') \
            or \
            (list_buttons['!button7'] == 'X' and list_buttons['!button8'] == 'X' and list_buttons['!button9'] == 'X') \
            or \
            (list_buttons['!button'] == 'X' and list_buttons['!button4'] == 'X' and list_buttons['!button7'] == 'X') \
            or \
            (list_buttons['!button2'] == 'X' and list_buttons['!button5'] == 'X' and list_buttons['!button8'] == 'X') \
            or \
            (list_buttons['!button3'] == 'X' and list_buttons['!button6'] == 'X' and list_buttons['!button9'] == 'X') \
            or \
            (list_buttons['!button'] == 'X' and list_buttons['!button5'] == 'X' and list_buttons['!button9'] == 'X') \
            or \
            (list_buttons['!button3'] == 'X' and list_buttons['!button5'] == 'X' and list_buttons['!button7'] == 'X'):
            win_user()
            return 1


    def check_win_computer():
        if (list_buttons['!button'] == 'O' and list_buttons['!button2'] == 'O' and list_buttons['!button3'] == 'O') \
            or \
            (list_buttons['!button4'] == 'O' and list_buttons['!button5'] == 'O' and list_buttons['!button6'] == 'O') \
            or \
            (list_buttons['!button7'] == 'O' and list_buttons['!button8'] == 'O' and list_buttons['!button9'] == 'O') \
            or \
            (list_buttons['!button'] == 'O' and list_buttons['!button4'] == 'O' and list_buttons['!button7'] == 'O') \
            or \
            (list_buttons['!button2'] == 'O' and list_buttons['!button5'] == 'O' and list_buttons['!button8'] == 'O') \
            or \
            (list_buttons['!button3'] == 'O' and list_buttons['!button6'] == 'O' and list_buttons['!button9'] == 'O') \
            or \
            (list_buttons['!button'] == 'O' and list_buttons['!button5'] == 'O' and list_buttons['!button9'] == 'O') \
            or \
            (list_buttons['!button3'] == 'O' and list_buttons['!button5'] == 'O' and list_buttons['!button7'] == 'O'):
            win_computer()
            return 1


    def check_draw():
        if all(map(lambda x: x != '', list_buttons.values())):
            draw()
            return 1


    def entry(button):
        global player, current_sym, win_or_draw
        if win_or_draw:
            return    
        if list_buttons[button._name] != '':
            return
        if player == 'user':
            current_sym = "X"
            enter_user()
            button.config(text=current_sym)
            list_buttons[button._name] = current_sym
            if not check_win_user() and not check_draw():
                current_sym = "O"
                enter_computer()
                get_button_computer()
                check_win_computer()
                check_draw()
            

    def button_for_loop():
        global frame, button
        for i in range(1, 4):
            for j in range(1, 4):
            # buttonName = "btn-" + str(i) + "-" + str(j)
                button = tk.Button(frame, background=color, font="Helvetica 40", padx=1, pady=1, width=4, height=2, fg='#b21031')
                button.config(command=lambda button=button: entry(button))
                button.grid(row=i, column=j, padx=6, pady=6)
                arr_buttons.append(button)

    def score():
        global score_player_user_button, score_player_computer_button
        score_player_user_button = tk.Button(frame, text=f' USER : {score_player_user_text}', background='#772fd4', width=15, height=2)
        score_player_user_button.grid(row=0, column=1, padx=4, pady=4)
        score_player_computer_button = tk.Button(frame, text=f' COMPUTER : {score_player_computer_text}', background='#772fd4', width=15, height=2)
        score_player_computer_button.grid(row=0, column=3, padx=4, pady=4)

    frame_game()
    button_for_loop()
    score()
    root.mainloop()