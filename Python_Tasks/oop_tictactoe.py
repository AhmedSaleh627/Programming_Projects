import random
class Board:
    def __init__(self):
        self.board = ['-', '-', '-', '-',
                      '-', '-', '-', '-',
                      '-', '-', '-', '-',
                      '-', '-', '-', '-']

    def print_board(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2] + " | " + self.board[3])
        print("-" * 17)
        print(self.board[4] + " | " + self.board[5] + " | " + self.board[6] + " | " + self.board[7])
        print("-" * 17)
        print(self.board[8] + " | " + self.board[9] + " | " + self.board[10] + " | " + self.board[11])
        print("-" * 17)
        print(self.board[12] + " | " + self.board[13] + " | " + self.board[14] + " | " + self.board[15])


class TicTacToe(Board):
    def __init__(self, vs_computer):
        super().__init__()
        self.current_player = "X"
        self.vs_computer = vs_computer

        if(self.current_player == "X"):
            self.computer_player = "O"
        else:
            "X"

        

        self.winner = None
        
        self.game_running = True

    def player_input(self):
        if self.vs_computer and self.current_player == self.computer_player:
            self.computer_input()
        else:
            while True:
                if self.current_player == "X":
                    inp = int(input(f"Player (X) Enter a number 1-16  : "))
                else:
                    inp = int(input(f"Player (O) Enter a number 1-16  : "))
                if inp >= 1 and inp <= 16 and self.board[inp - 1] == "-":
                    self.board[inp - 1] = self.current_player
                    break
                else:
                    if self.current_player == "X":
                        print(f"Oops! Try again! Player (X) ! ")
                    else:
                        print(f"Oops! Try again! Player (O) ! ")
                    self.print_board()

    def computer_input(self):
        available_moves = [i for i, val in enumerate(self.board) if val == "-"]
        move = random.choice(available_moves)
        self.board[move] = self.current_player

    def check_horizontal(self):
        if (self.board[0] == self.board[1] == self.board[2] == self.board[3] != "-") or  (self.board[4] == self.board[5] == self.board[6] == self.board[7] != "-") or  (self.board[8] == self.board[9] == self.board[10] == self.board[11] != "-") or (self.board[12] == self.board[13] == self.board[14] == self.board[15] != "-"):
            self.winner = self.current_player
            return True
        return False

    def check_row(self):
        if (self.board[0] == self.board[4] == self.board[8] == self.board[12] != "-") or (self.board[1] == self.board[5] == self.board[9] == self.board[13] != "-") or (self.board[2] == self.board[6] == self.board[10] == self.board[14] != "-") or   (self.board[3] == self.board[7] == self.board[11] == self.board[15] != "-"):
            self.winner = self.current_player
            return True
        return False

    def check_diagonal(self):
        if (self.board[0] == self.board[5] == self.board[10] == self.board[15] != "-") or (self.board[3] == self.board[6] == self.board[9] == self.board[12] != "-"):
            self.winner = self.current_player
            return True
        return False

    def check_tie(self):
        if "-" not in self.board:
            self.print_board()
            print("It's a TIE!!")
            self.game_running = False

    def check_win(self):
        if self.check_diagonal() or self.check_horizontal() or self.check_row():
            print(f"The Winner is {self.winner}")

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def play_game(self):
        self.setup_game()
        while self.game_running:
            self.print_board()
            print("                             ")
            if self.winner is not None:
                break
            self.player_input()
            self.check_win()
            self.check_tie()
            self.switch_player()

    def setup_game(self):
        print("Welcome to Tic Tac Toe!")
        while True:
            choice = input("Do you want to play against the computer? (y/n): ")
            if choice.lower() == "y":
                self.vs_computer = True
                break
            elif choice.lower() == "n":
                self.vs_computer = False
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

        
        if(self.current_player == "X"):
            self.computer_player = "O"
        else:
            "X"

        print("Let's start the game!")
        
        

game = TicTacToe(vs_computer=False)
game.play_game()