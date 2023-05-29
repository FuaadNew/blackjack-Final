############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return(card)

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(cards):
 #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game. 
  if 11 in cards and 10 in cards and len(cards)==2:
    return 0
  elif 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  else:
    return sum(cards)

def compare(user_score,computer_score):
  
  if user_score == computer_score:
    return ("Draw")
  elif computer_score == 0:
    return ("You lose.")
  
  elif user_score == 0:
    return ("You Win!")
    
  elif user_score > 21:
    return ("You Lose.")
    
  elif computer_score >21:
    return ("You Win!")
  elif user_score > computer_score:
    return ("You Win!")
  else:
    return ("You lose.")
def play_game():
    
  print(logo)
  user_cards = []
  computer_cards = []
  Endgame = False
  for i in range (2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    while Endgame == False:
      user_score= calculate_score(user_cards)
      computer_score = calculate_score(computer_cards)
      print(f" Your Cards: {user_cards}, current score: {user_score}")
      print(f" Computer's first Card: {computer_cards[0]}")
      #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
      if user_score == 0 or computer_score == 0 or user_score >21:
        Endgame = True
      else:
        User_Deal = input("Type 'y' to get another another card, type 'n' to pass:")
        if User_Deal == 'y':
          user_cards.append(deal_card())
        else:
          Endgame = True
     
    while computer_score !=0  and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)                    
    print(f"Your final hand is :{user_cards},final score: {user_score}")
    print(f"Computer's final hand is :{computer_cards},final score: {computer_score}")
    
    print(compare(user_score,computer_score))   
  
while  input("Do you want to play again?: TYPE 'y' Or 'n'") == 'y':
  clear()
  play_game()
  

  
