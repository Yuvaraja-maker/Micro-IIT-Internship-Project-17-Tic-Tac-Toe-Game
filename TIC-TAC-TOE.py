import time

def print_board(sign_dictionary):
    board = f"""
     |     |     
  {sign_dictionary[0]}  |  {sign_dictionary[1]}  |  {sign_dictionary[2]}  
_____|_____|_____
     |     |     
  {sign_dictionary[3]}  |  {sign_dictionary[4]}  |  {sign_dictionary[5]}  
_____|_____|_____
     |     |     
  {sign_dictionary[6]}  |  {sign_dictionary[7]}  |  {sign_dictionary[8]}  
     |     |     
    """
    print(board)

def take_input(player_name, sign_dictionary, index_list):
    while True:
        try:
            X = int(input(f"{player_name}, enter a position (1-9): ")) - 1
            if 0 <= X < 9:
                if X in index_list:
                    print("This spot is already taken. Choose another one.")
                    continue
                index_list.append(X)
                return X
            else:
                print("Invalid input! Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculate_result(sign_dictionary, player_one, player_two):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    
    for a, b, c in winning_combinations:
        if sign_dictionary[a] == sign_dictionary[b] == sign_dictionary[c] and sign_dictionary[a] != ' ':
            winner = player_one if sign_dictionary[a] == 'X' else player_two
            print(f"Congratulations {winner}! You won the match. 🎉")
            return True
    return False

def main():
    print("\tWelcome to the TIC-TAC-TOE GAME 🎮")
    
    player_one = input("\nEnter Player 1 name: ")
    player_two = input("Enter Player 2 name: ")
    
    while True:
        sign_dictionary = [' '] * 9
        index_list = []
        
        print(f"\nHello  {player_one}  and  {player_two}!  Let's start the game. 🚀")
        print(f"\n{player_one} your sign is 'X' and {player_two} sign will be 'O'.\n")
        input("Press Enter to start the game...\n")
        
        print_board(sign_dictionary)
        
        for i in range(9):
            player = player_one if i % 2 == 0 else player_two
            sign = 'X' if i % 2 == 0 else 'O'
            index = take_input(player, sign_dictionary, index_list)
            sign_dictionary[index] = sign
            print_board(sign_dictionary)
            
            if calculate_result(sign_dictionary, player_one, player_two):
                break
        else:
            print("It's a tie game! 🤝 Nobody won. Play again.")
        
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'no']:
                break
            print("Invalid input! Please enter 'yes' or 'no'.")
        
        if play_again != 'yes':
            print("Thanks for playing! Goodbye! 👋")
            break
        print("\nStarting a new game... 🎲\n")
        time.sleep(1)

main()
