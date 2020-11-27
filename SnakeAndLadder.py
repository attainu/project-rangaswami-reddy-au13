from random import randint


class SnakeAndLadder:
    def __init__(self):
        pass

    def ladders(self, x):                   # snake's score
        if x == 2:
            return 25
        elif x == 7:
            return 31
        elif x == 20:
            return 44
        elif x == 33:
            return 76
        elif x == 41:
            return 96
        elif x == 53:
            return 89
        else:
            return x

    def snakes(self, x):                         # ladder's score
        if x == 40:
            return 5
        elif x == 46:
            return 11
        elif x == 99:
            return 23
        elif x == 70:
            return 27
        elif x == 83:
            return 57
        elif x == 92:
            return 92
        else:
            return x

    def turn(self, player, score):                  # Turn function
        print()
        print("Its", player, "turn.")
        self.roll2 = input("Press enter to Roll the DICE")
        print()

        if self.roll2 == "":
            self.a = randint(1, 6)
            print(player, "DICE Rolling....")                       # player dice rolling
            print(player, "got", self.a)
            score += self.a
            if score <= 100:
                lad = self.ladders(score)                  # checking for ladders for player
                if lad != score:
                    print("There's a ladder!", player, "climbed up.")
                    score = lad
                snk = self.snakes(score)

                if snk != score:                                     # checking for snakes for player
                    print(player, "snake bite !", player, "fall down!")
                    score = snk
                print(player, "is now on number", score)

            else:                                           # checks if player score is not greater than 100
                score -= a
                print(player, "can't move.")
                print(player, "is still on box", score)

            if score == 100:
                print()
                print("#" * 15, player, "won the game!", "#" * 15)
                print("#" * 20, "congratulations", player, "#" * 20)

            return score

    def start(self):
        print("\n")
        print("#" * 25, "WELCOME TO SNAKE AND LADDER", "#"*25)
        print("\n")
        print("#" * 30, "MAIN MENU", "#"*30)
        print("""
    Rules:
      >>> Initally both the players are at starting position i.e. 0 . 
          Take it in turns to roll the dice. 
          Move forward the number of spaces shown on the dice.
      >>> If you lands at the bottom of a ladder,
          you can move up to the top of the ladder.
      >>> If you lands on the head of a snake,
          you must slide down to the bottom of the snake.
      >>> The first player to get to the FINAL position is the winner.
      >>> Hit enter to roll the dice.
    """)
        print("-------------------------SNAKES N LADDERS-------------------------")           # game starts
        print()

        while True:
            self.play = input("PLEASE Press 'ENTER' to start the game: ")
            if self.play == "":
                print("Choose your mode (Single player/Multiplayer)")                        # mode selection
                self.mode = input("Enter \"S\" for sigle player and \"M\" for multiplayer: ")

                if self.mode == "S" or self.mode == "s":
                    player2 = "Computer"
                    num_players = 2
                else:
                    num_players = int(input("PLEASE Enter how many players are playing : "))
                player1 = input("Enter player 1 name: ")

                if (self.mode == "m" or self.mode == "m") and 5 > num_players > 1:
                    player2 = input("Enter player 2 name: ")
                if 5 > num_players > 2:
                    player3 = input("Enter player 3 name: ")
                if 5 > num_players > 3:
                    player4 = input("Enter player 4 name: ")
                    print()
                print("Good Luck!")
                print()
                while True:
                    self.play2 = input("PLEASE Press 'ENTER' to start THE GAME.")
                    if self.play2 == "":
                        self.player1_score = self.player2_score = self.player3_score = self.player4_score = 0
                        while True:
                            if 5 > num_players > 1:
                                player1_score = self.turn(player1, self.player1_score)
                                if player1_score == 100:
                                    break
                                player2_score = self.turn(player2, self.player2_score)
                                if player2_score == 100:
                                    break
                            if 5 > num_players > 2:
                                player3_score = self.turn(player3, self.player3_score)
                                if player3_score == 100:
                                    break
                            if 5 > num_players > 3:
                                player4_score = self.turn(player4, self.player4_score)
                                if player4_score == 100:
                                    break
                            print("____________________________________________________________")

                    break
            elif self.play == "exit" or self.play == "Exit":
                break
                quit


if __name__ == "__main__":
    snakegame = SnakeAndLadder()
    snakegame.start()
