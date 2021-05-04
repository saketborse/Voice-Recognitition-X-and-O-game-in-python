from IPython.display import clear_output
import pyttsx3
e = pyttsx3.init()
import speech_recognition as sr
r = sr.Recognizer()

import tkinter as tk


numbers = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'one': 1,'on':1, 'too':2,'Tu':2,'sex':6, 'to':2, 'two': 2, 'three': 3,'tree':3, 'four':4,'for':4, 'fore':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
board = [' '] * 10 
game_state = True
announce = ''
i=2

def reset():
    global board, game_state
    board = [' '] * 10
    game_state = True


def hash1():
    clear_output()
    print('\t'+board[7]+'\t'+'|'+'\t'+board[8]+'\t'+'|'+'\t'+board[9]) 
    print('-------------------------')
    print('\t'+board[4]+'\t'+'|'+'\t'+board[5]+'\t'+'|'+'\t'+board[6]) 
    print('-------------------------')
    print('\t'+board[1]+'\t'+'|'+'\t'+board[2]+'\t'+'|'+'\t'+board[3]) 
    print('\n')
    

def check(board, symbol):
    if(board[1] == board[2] == board[3] == symbol) or \
      (board[4] == board[5] == board[6] == symbol) or \
      (board[7] == board[8] == board[9] == symbol) or \
      (board[1] == board[4] == board[7] == symbol) or \
      (board[2] == board[5] == board[8] == symbol) or \
      (board[3] == board[6] == board[9] == symbol) or \
      (board[1] == board[5] == board[9] == symbol) or \
      (board[3] == board[5] == board[7] == symbol):
        return True
    else:
        return False

def empty(board):
    if " " in board[1:10]: 
        return False
    else:  
        return True

def position(symbol):
    global board
    
    x = 'position 1-9 on where to place your ' + symbol + '  --->  '
    while True:
        
        
        print('what is your move? (1-9)')
        e.setProperty('rate',170)
        e.say('enter number ')
        e.setProperty('rate',170)
        
        e.runAndWait() 
        
        try:
            try:
                
                with sr.Microphone() as source:
                    user_input = r.listen(source)
                    text = r.recognize_google(user_input)
                    print(text)
                if text in '1 2 3 4 5 6 7 8 9 one on two too Tu sex to three tree four for fore five six seven eight nine'.split():
                    pick = int(numbers[text])
                    while 10<pick or user_input=='':
                        print("Please input a number between 1-9")
                        e.say("Please input a number between 1-9")
                        e.runAndWait()
                        user_input = r.listen(source)
                        text = r.recognize_google(user_input)
                        print(text)
                elif 0 < int(text) < 10:
                    pick = int(text)
                else:
                    raise ValueError
            except:
                print('Sorry but we couldn\'t hear you. Please try via keyboard')
                e.say('Sorry but we couldn\'t hear you. Please try via keyboard')
                e.runAndWait()
                pick = int(input(x))
                while 10<pick:
                    print("Please input a number between 1-9")
                    e.say("Please input a number between 1-9")
                    e.runAndWait()
                    pick=int(input())
        except ValueError:
            print("Please input a number between 1-9")
            e.say("Please input a number between 1-9")
            e.runAndWait()
            continue
        
        if board[pick] == " ":
            board[pick] = symbol
            break
        else:
            print ('enter another postion')
            e.say('enter another postion')
            e.runAndWait()
            continue


def choice(symbol):
    global board, game_state, announce
    announce = ''
    symbol = str(symbol)
    position(symbol)
    
    
    clear_output()
    hash1()
    if check(board,symbol):
        clear_output() 
        announce = symbol + " win"
        
        e.say(symbol+'win')
        e.runAndWait()
        game_state = False
    if empty(board) and game_state != False:
        announce = "draw"
        
        e.say('The game is Tie!')
        e.runAndWait()
        game_state = False
    return game_state, announce



def play():
    
    reset()
    global announce,i
    print('welcome let start the game')
    e.say('welcome let start the game')


    X = 'X'
    O = 'O'
    hash1()
    while True:
        clear_output()
        if i%2==0:
            print('x turn')
            e.say('x turn')
            game_state, announce = choice(X)
            print (announce)
            if game_state == False:
                break
            
            print('O turn')
            e.say('O turn')
            game_state, announce = choice(O)
            print (announce)
            
            if game_state == False:
                break
        i=i+1
        
            
            
    
    e.say('Would you like to play again? y or n')
    e.runAndWait()
    ans = input('Would you like to play again? y or n')
    if ans == 'y':
        play()
    else:
        print ("EXIT")

play()
window = tk.Tk()

window.geometry("500x400")
window.mainloop()