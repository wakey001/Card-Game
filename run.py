
class Card:
    def __init__(self, model, power, weight, top_speed, zero_to_sixty):
        self.model = model
        self.power = power
        self.weight = weight
        self.top_speed = top_speed
        self.zero_to_sixty = zero_to_sixty 
    
    

    def show(self):
        print("Your card is a {} ".format(self.model))
        print("{}hp {}kg {}mph {}0-60".format(self.power, self.weight, self.top_speed, self.))
    

class Deck():
    def __init__(self):
A = Card("Honda civic type R", 320, 1380, 167, 5.6)
B = Card('Toyota yaris GR', 260, 1280, 142, 5.3)
C = Card('Renault megane RS', 300, 1440, 165, 5.3)
D = Card('Ford focus st', 280, 1510, 155, 5.8)
E = Card('Hyundai i30 N', 270, 1430, 155, 5.8)
F = Card('Mercedes a45 AMG', 360, 1370, 155, 4.1)
G = Card('Volkswagon golf R', 300, 1500, 155, 4.7)
H = Card('BMW 135i M', 306, 1600, 155, 4.5)
I = Card('Volkswagon golf GTI', 241, 1430, 155, 5.6)
J = Card('Mini clubman JCW', 302, 1550, 155, 4.6)       
    
    def get_user_card(self):
        try:
            player_hand = input("Enter a number to be given random card: ")
            while player_hand not in '12345678910':
                print("Error please enter a number between 1-10")
                player_hand = input("Enter a number to be given random card: ")
            return int(player_hand), Card.get_letters_to_numbers()


 
    
A.show()