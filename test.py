import pandas as pd 

game_board = [[ ' ' for _ in range(3)] for _ in range(3)]

def create_gameboard(game_board):
    df = pd.DataFrame(game_board,  columns=["1", "2", "3"], index=["1", "2", "3"])
    print(df)
    
          
def start_game():
    player = "X"
    
    while True:
        create_gameboard(game_board)
        print(f"Spieler {player} ist dran")
        zeile = int(input("Gib eine Zeile von 1 - 3 an: "))-1 
        spalte = int(input("Gib eine Spalte von 1 - 3 an: "))-1
        
        if zeile > 2 or zeile  < 0 or spalte > 2 or spalte < 0:
            print("Falsche Eingabe")
            continue
        
        if  game_board[zeile][spalte] == " ":
            game_board[zeile][spalte] = player
            
            if player ==  "X":
                player = "O"
            elif player == "O":
                player = "X"
            
            if game_won(game_board, player):
                create_gameboard(game_board)
                print(f"{player} hat gewonnen")
                break
        
        else:
            print("Feld bereits besetzt!")

        
        
        
def game_won(game_board, player):
    # Check rows
    for row in game_board:
        if all(cell == player for cell in row):
            return True
    
    # Check columns
    for col in range(3):
        if all(game_board[row][col] == player for row in range(3)):
            return True
    
    # Check diagonals
    if all(game_board[i][i] == player for i in range(3)) or \
       all(game_board[i][2-i] == player for i in range(3)):
        return True
    
    return False
    
    
    
start_game()
        
        
        
    
    