import tkinter as tk


def two_player():
    global player, current_sym, win_or_draw, frame, button, score_player_x_button, score_player_o_button, score_player_x_text, score_player_o_text

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
    player = 1
    current_sym = ""
    score_player_x_text = 0
    score_player_o_text = 0
    win_or_draw = False


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



    def new_game():
        global player, current_sym, win_or_draw, frame, button, score_player_x_button, score_player_o_button
        player = 1
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
        score_player_x_button.destroy()
        score_player_o_button.destroy()
        frame_game()
        button_for_loop()
        score()

    def enter_x():
        global player, current_sym
        player = 2


    def enter_o():
        global player, current_sym
        player = 1


    def win_or_draw_fun():
        global win_or_draw
        if win_or_draw:
            return


    def check_button():
        pass


    def win_x():
        global win_or_draw, score_player_x_text
        score_player_x_text += 1
        score()
        win_or_draw = True
        label_x_win = tk.Button(frame, text='PLAYER X IS WIN', bg='#772fd4', width=20, height=2)
        label_x_win.grid(row=2, column=1, padx=4, pady=4)
        button_play_again_x = tk.Button(frame, text='New Game', bg='#772fd4', width=15, height=2, command=new_game)
        button_play_again_x.grid(row=2, column=2, padx=4, pady=4)
        button_esc = tk.Button(frame, text='QUIT', bg='#772fd4', command=root.quit, width=10, height=2)
        button_esc.grid(row=2, column=3, padx=4, pady=4)
        

    def win_o():
        global win_or_draw, score_player_o_text
        score_player_o_text += 1
        score()
        win_or_draw = True
        label_o_win = tk.Button(frame, text='PLAYER O IS WIN', bg='#772fd4', width=20, height=2)
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


    def entry(button):
        global player, current_sym, win_or_draw, win_or_draw
        if win_or_draw:
            return    
        if list_buttons[button._name] != '':
            return
        if player == 1:
            current_sym = "X"
            enter_x()
        else:
            current_sym = "O"
            enter_o()
        button.config(text=current_sym)
        list_buttons[button._name] = current_sym
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
            win_x()

        elif (list_buttons['!button'] == 'O' and list_buttons['!button2'] == 'O' and list_buttons['!button3'] == 'O') \
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
            win_o()

        elif all(map(lambda x: x != '', list_buttons.values())):
            draw()
            


    def button_for_loop():
        global frame, button
        for i in range(1, 4):
            for j in range(1, 4):
            # buttonName = "btn-" + str(i) + "-" + str(j)
                button = tk.Button(frame, background=color, font="Helvetica 40", padx=1, pady=1, width=4, height=2, fg='#b21031')
                button.config(command=lambda button=button: entry(button))
                button.grid(row=i, column=j, padx=6, pady=6)


    def score():
        global score_player_x_button, score_player_o_button
        score_player_x_button = tk.Button(frame, text=f' PLAYER X : {score_player_x_text}', background='#772fd4', width=15, height=2)
        score_player_x_button.grid(row=0, column=1, padx=4, pady=4)
        score_player_o_button = tk.Button(frame, text=f' PLAYER O : {score_player_o_text}', background='#772fd4', width=15, height=2)
        score_player_o_button.grid(row=0, column=3, padx=4, pady=4)

    frame_game()
    button_for_loop()
    score()

    root.mainloop()
