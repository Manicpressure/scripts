#Blackjack is a card game where players try to get the number 21, or as close as possible without going over.
#All royal cards count as 10, aces count as 1 or 11, and all other cards count their numeric value.
#There is a maximum of 6 players at a table. In this game we will have at least 1 human player.

#Blackjack!
#The players each take a turn, either hitting or staying. Once all the players have finished, the dealer
#takes all his turns in one go. If the player gets a blackjack, he gets a payout of 1.5 times the bet,
#unless the dealer gets a blackjack himself. In which case there is a draw.

#Dealer rules
#The dealer must hit until a total of at least 17 has been achieved.
#The players start with 2 cards face up, the dealer will have 1 card showing.

#Game
#Lose - Player's bet is taken by the dealer
#Win - The player wins what he bet
#Blackjack - 1.5 times his bet
#Push - Draw

#Deck
#The cards will be drawn from a card shoe of 1 - 8 card decks shuffled inside it.
#You can use this game to practice card counting.

#Future revisions
#Make design docstrings that explain the rules of Blackjack
#Line 124 - Is it necessary to initialize by setting variables to 0?
#Line 180 - Is the returning updated variables to originating function a necessary one?
#Line 249 - Using recursion in 'decision' function to loop back to the start of the function is not good. It creates a recursive
#situation where the user needs to input the same thing multiple times to escape the recursion depth.
#Line 267 - Add option to add money to whoever you want
#Line 330 - How to make game restart even if the player presses enter. Indexerror occurs
# When a player runs out of money, they don't get eliminated.






#Line 40
import random


class deck:
   cardDeck = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] #Template to build a card deck on

   def __init__(self,nDecks):
      self.deck = deck.cardDeck * nDecks * 4 #Build the shoe depending on the number of decks to mix
      self.royal = {"A": 11, "J" : 10, "Q" : 10, "K" : 10} #Dictionary to translate royal cards to their values

   def deckCount(self): #Shows what cards are left in the deck. This can be used to check your card counting
      print(self.deck)

   def shuffleDeck(self,nDecks): #For the function of being able to shuffle cards.
      random.shuffle(self.deck) #random.shuffle is used to shuffle the deck.
      print("Shuffling deck")

   def draw(self): #pop the last card in the deck and return it as a string value
      return self.deck.pop() #Needs to be used within the function hitMe().

   def resetDeck(self, nDecks): #This will set the deck into straight order
      self.deck = deck.cardDeck * nDecks * 4
      print("Card shoe filled with new cards")

   def refillDeck(self, nDecks): #This will refill and shuffle the deck.
      self.deck = deck.cardDeck * nDecks * 4
      random.shuffle(self.deck)
      print("Resetting and shuffling deck")


class Players: #Parent class for the players.
   def __init__(self, name, money): #only need money parameter to construct the generic player template
      self.hand = []
      self.score = 0
      self.money = money
      self.turn = False #turn is marker to indicate whether the player has finished playing on the round
      self.name = name #only necessary for the functions we create here

   def show(self): #presents hand and money
      print("{} is holding {} and has ${}".format(self.name, self.hand, self.money))

   def hit(self, card): #adds a card to the hand. Needs to be used within the function hitMe().
      self.hand.append(card)

   def reset(self): #resets to empty hand and score
      self.hand = []
      self.score = 0

   def setScore(self, Score): #forcibly set the score to a certain number
      self.score = Score

   def cash(self):
      print(self.name, "has", self.money)

   def addMoney(self, money): #add or subtract money to the account
      self.money = self.money + money

class dealer(Players): #dealer is different in that he has 'infinite' money and only shows 1 card
   def __init__(self):
      self.name = "Dealer"
      self.money = 25000
      self.score = 0
      self.hand = []
      self.human = False

   def dealerShow(self):
      print("The Dealer is showing", self.hand[0],"\n")


class player(Players):
   def __init__(self, name, money):
      self.name = name #Because human and computer players have a unique name, need to have name parameter
      self.human = True
      super().__init__(name, money) #inherit money from parent class


class computer(Players):
   def __init__(self, name, money):
      self.name = name
      self.human = False
      super().__init__(name, money)


def newgame(): #This function will be used to start a new game, set new parameters
   money = 0 #Initializing new variables by resetting to 0. Is this necessary?
   nDecks = 0
   nPlayers = 0
   hPlayers = 0
   money = eval(input("This is a $25 Blackjack table. How much money does everyone start with? "))
   nDecks = eval(input("How many card decks are in the shoe? [Two to Eight decks] "))
   nPlayers = eval(input("How many players are at the table including you? [One to Six players] "))
   hPlayers = eval(input("How many of them will be controlled by people? [One human player required] "))

   if nPlayers > 6 or nPlayers < 1: #number of players at table range from 1 to 6
      print("""There needs to be a minimum of one human player(you) and a maxmimum of five computer players,
            enter again\n""")
      newgame()
   elif hPlayers < 1 or hPlayers > nPlayers: #number of human players, at least one, less than total players.
      print("There needs to be a human player, enter again\n")
      newgame()
   elif nDecks > 8 or nDecks < 2: #number of decks in the shoe
      print("Number of maximum decks exceeded, or not enough decks, enter again\n")
      newgame()

   Participants = [] #List up participants in the game for efficient game process. Initialize list.
   print("\nDealer : Welcome to the Blackjack table!")
   cardShoe = deck(nDecks) #Initialize deck, parameter of nDecks.
   cardShoe.refillDeck(nDecks) #Reset and shuffle deck.
   for i in range(hPlayers): #iterate i over number of human players. append human players to participants list first
      HumPlayers = "Player{}".format(i + 1) #Make a variable to say "Player1".
      HumPlayer = player(HumPlayers, money) #INitialize the class object with the formatted string and money
      Participants.append(HumPlayer) #Add the class object to the list
      print(HumPlayer.name, "joins the table.")

   for i in range(nPlayers - hPlayers): #Repeat of the above, but with computers
      CompPlayers = "Computer{}".format(i + 1)
      CompPlayer = computer(CompPlayers, money)
      Participants.append(CompPlayer)
      print(CompPlayer.name, "joins the table.")

   Dealer = dealer() #Initialize dealer class. Does not need any parameters.
   Participants.append(Dealer) #Dealer is added last to make rounds easier to code.
   setTable(Participants, cardShoe) #Set everyones hand to 0, score to 0, draw 2 cards, and place bets
   return Participants, cardShoe, nDecks #These parameters will be used elsewhere

def setTable(Participants, cardShoe): #Reset hand, score. Draws two cards.
   for i in Participants:
      i.turn = False
      i.reset() #Reset self.hand and self.score to 0
      hitMe(i, cardShoe) #Function to pop from cardShoe, and append to self.hand
      i.addMoney(-25) #Players bet the table amount
   for i in Participants: #cards are given to everyone once, and then another on second round of draws
      hitMe(i,cardShoe)
   print("Starting new game, placing bets.") #Announce a new game
   return Participants, cardShoe #return the update variables back to the originating function

def hitMe(Players, cardShoe): #Players inserted as paramter. Card will be going to that player.
   card = cardShoe.draw() #Use the cardshoe.draw method to pop a card from the shoe and return it as 'card'
   Players.hit(card) #'card' variable will be parameter of the .hit method from player class. Appends a card
   #to the self.hand list
   return cardShoe #Do I need to return the updated cardshoe to the governing function?

def present(Participants): #This is equivalent of the player looking around the table to see what everyone
   #is holding.
   for i in Participants: #loop through the participants
      if i.name == "Dealer": #If it is the dealer, we only show one card. So Dealer needs to be picked up
         i.dealerShow() #on specifically
      else:
         i.show() #print(self.hand) - instance method
   return

def calculate(Participants, cardShoe): #Calculates the score by analyzing self.hand
   for i in Participants: #Loop through once per participant
      Score = 0 #initialize the score per participant
      for j in i.hand: #Loop through the hand of each participant
         try:
            Score = Score + j #If element in list is integer, use score = score + j
            i.setScore(Score) #Set the score after every calculation or the final score does not calculate
         except TypeError: #If there is a royal card, we will get a type error.
            Score = int(Score + cardShoe.royal.get(j)) #Use dictionary to translate royal card to number value
            i.setScore(Score) #Make sure to set score, or the score does not consider this card
         else: continue
      if i.score > 21: #In case we get a bust, we will replace the score as a numerical value with "bust"
         if "A" in i.hand: #If there is an Ace, we can subtract 10 points. A will default to 11.
            Score = Score - 10
         else: #If there is no ace, the score will be Bust!
            Score = "Bust!"
            i.turn = True
      i.setScore(Score) #At the end, set calculated score to class variable.
   return Participants, cardShoe

def roundtable(Participants, cardShoe, nDecks): #Function will go around the table once
   for i in Participants: #First loop to have everyone but dealer play a move
      if i.human is True and i.turn is False: #First people to play are humans who have not stayed
         TF = decision(i, cardShoe, nDecks, Participants) #TF True/False is a return from decisions function
         if TF is True: #If TF is true, we turn the self.turn variable into True, marking that the player
            i.turn = True #has stayed
         else: continue #if TF is false, just continue
      elif i.human is False and i.turn is False and type(i) is not dealer: #Next comes the computers
         TF = AIdecision(i, Participants, cardShoe) #return T/F from AIdecisions function
         if TF is True:  #As usual, if TF is true, turn the i.turn true to indicate the player is stayed
            i.turn = True
         else: continue #If not, continue

   for j in Participants: #After looping player/computers, we check the dealer once
      if j.turn is False and type(j) is not dealer and j.score != "Bust!": #if player/comp has not finished, roundtable again
         roundtable(Participants, cardShoe, nDecks) #IF there are non-stayed players, repeat the function
      elif type(j) is dealer and j.turn is False: #make sure that the player checked on is dealer
         TF = AIdecision(i, Participants, cardShoe)
         if TF is True:
            i.turn = True
         else: roundtable(Participants, cardShoe, nDecks)
      elif j.turn is True: #if everyone has stayed, calculate the score again and continue on to return True
         continue
   return True


def decision(Player, cardShoe, nDecks, Participants): #Function is the decision of the player
   uplay = input("{} is playing, type 'hit', 'stay', 'present', or\
'menu' to configure the game ".format(Player.name))
   if uplay == 'hit':
      hitMe(Player, cardShoe)
      print("{} is now holding ".format(Player.name), Player.hand) #hit adds a card to the current players hand
      return False
   elif uplay == 'stay': #returns True which will get interpreted by roundtable function to determine stay
      print("{} stays. ".format(Player.name))
      return True
   elif uplay == 'present': #Presents a decision, and reverts back to function
      present(Participants)
      decision(Player, cardShoe, nDecks, Participants) #Using recursive functions to loop back to start of function is not good
   elif uplay == 'menu': #Allows player to make executive decisions on the state of the table
      menu = input("""Type 'deck' to see remaining cards in the shoe
Type 'reset' to refill and then shuffle the card shoe
Type 'refill' to refill the deck, or 'shuffle' to shuffle
Type 'money' to add money to player accounts
Type 'start' to start a whole new game
Type 'continue' to go back to decision """)
      if menu == 'deck':
         cardShoe.deckCount()
      elif menu == 'reset':
         cardShoe.resetDeck(nDecks)
      elif menu == 'refill':
         cardShoe.refillDeck(nDecks)
      elif menu == 'shuffle':
         cardShoe.shuffleDeck()
      elif menu == 'money': #Should add a menu to add money to whoever you want
         money = input("How much money will you add? ")
         Player.addmoney(money)
      elif menu == 'start':
         newgame()
      elif menu == 'continue':
         decision(Player, cardShoe, nDecks, Participants) #recursion -
      else:
         print("Invalid input, please type the command in lower case with correct spelling ")
      decision(Player, cardShoe, nDecks, Participants) #recursion -
   else:
      print("Invalid input, please type the command in lower case with correct spelling ")
      decision(Player, cardShoe, nDecks, Participants) #recursion -
   if Player.score == "Bust!" or Player.score >= 21: #If no meaningful choices can be made, break
      return True
   return False, Participants, cardShoe

def AIdecision(Player, Participants, cardShoe): #AI decision is for computer/dealer
   calculate(Participants, cardShoe) #First calculate score to get rid of any strings
   if Player.score == "Bust!": #Stop playing upon bust
      return True
   elif Player.score >= 17 and Player.score <= 21: #If player reaches 17-21, stop hitting
      return True
   elif Player.score < 17: #If palyer score is below 17, hit and calculate score
      hitMe(Player, cardShoe)
      calculate(Participants, cardShoe) #Update score before return, for any functions that need updated scores
   return Participants, cardShoe #Return updated list

def scoring(Participants, cardShoe): #Finishing function. Will conclude the game by scoring everyone and distributing money.
   calculate(Participants, cardShoe) #First calculate score to get rid of any residual strings
   for i in Participants:
      if type(i) is not dealer and i.score == "Bust!": #When player goes bust, continue
         print(i.name, "goes Bust!")
         continue
      if type(i) is not dealer and i.score == 21 and len(i.hand) == 2: #if player get blackjack
         print(i.name, "Blackjack!")
         if len(Participants[-1].hand) == 2 and Participants[-1].score == 21: #If dealer gets blackjack, push
            print("Push. Dealer also got Blackjack. Everyone keeps their bet ")
            i.addMoney(25)
         else:
            i.addMoney(65) #otherwise, player gets 1.5times payout
      elif i.name == "Dealer" and i.score == 21 and len(i.hand) == 2: #When dealer gets blackjack,
         print("Dealer gets Blackjack!")
         break #Break function, if this conditional triggers, it means no one got a blackjack. Everyone loses their $25 bet
      elif i.name == "Dealer" and i.score == "Bust!": #if dealer busts, everyone who didnt bust wins.
         for l in Participants:
            if l.score != "Bust!" and l.name != "Dealer":
               l.addMoney(50)
               break
      elif i.score != "Bust!" and type(i) is not dealer and Participants[-1].score != "Bust!": #compare scores with dealer
         if i.score > Participants[-1].score: #need to block dealers bust situation from seeping into condition
            i.addMoney(50)
            print(i.name, "won against dealer with a score of", i.score, "against ", Participants[-1].score)
         elif i.score < Participants[-1].score:
            print(i.name, "lost against dealer with a score of", i.score, "against", Participants[-1].score)
            continue
         elif i.score == Participants[-1].score:
            i.addMoney(25)
            print(i.name, "got a push against dealer with a score of", i.score)
   for k in Participants: #present final scoreboard for clarity
      print(k.name, "is holding", k.hand, "and has $", k.money)
   return Participants, cardShoe

def playagain(Participants, cardShoe, nDecks): #asks player for input, input triggers another round or quitting
   play = input("Play another round?  y/n ")
   if play[0] == 'y' or play[0] == 'Y' or play == "": #I wanted this condition to trigger if player pressed enter, but doesnt work
      newround(Participants, cardShoe, nDecks) #only necessary parameters are carried into a new round
   else: #The cardshoe does not get refreshed
      print("Thanks for playing")

def newround(Participants, cardShoe, nDecks): #Same as main, but without newgame.
   setTable(Participants, cardShoe)
   present(Participants)
   Finish = roundtable(Participants, cardShoe, nDecks)
   if Finish is True:
      scoring(Participants, cardShoe)
   playagain(Participants, cardShoe, nDecks)
   return True

def main():
   Participants, cardShoe, nDecks = newgame()
   present(Participants)
   Finish = roundtable(Participants, cardShoe, nDecks)
   if Finish is True:
      scoring(Participants, cardShoe)
   playagain(Participants, cardShoe, nDecks)

main()
