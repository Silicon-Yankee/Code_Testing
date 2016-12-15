### This is the testing of Black Jack (21)

import random, itertools, time

### Call this function to calculate current hand value
###
## example of calling 'Calculate' function
##
## >>> hnd = Calculate(dl_hnd) # This creates an instance of hnd by passing a hand to the fucntion 'Calculate'
## >>> print (hnd.hnd_value()) # this takes the instance 'hnd' and calls function to pass back value

class Player_Logic:

    def __init__(self, DLR_HAND, PLY_HAND, LOSS_streak, WIN_streak, PUSH, LAST_bet, MINIMUM):
        self.dlr_hand = DLR_HAND
        self.ply_hand = PLY_HAND
        self.lss_strk = LOSS_streak
        self.win_strk = WIN_streak
        self.psh_cmbo = PUSH
        self.last_bet = LAST_bet
        self.minimum = MINIMUM

    def logic(self):
        ###
        ###
        ### Currently this does not take into consideration if the hand is: 'A' '2' '3' essentially equal to 'A' '5'
        ###
        ###
        dlr_hnd = self.dlr_hand
        ply_hnd = self.ply_hand
        #dlr_hnd_instance = Calculate(self.dlr_hand)
        #dlr_hnd_vlu = dlr_hnd_instance.hnd_value()
        dlr_hnd_vlu = dlr_hnd[0][0]
        ply_hnd_instance = Calculate(self.ply_hand)
        ply_hnd_vlu = ply_hnd_instance.hnd_value()
        # Creates a list of just the first values in each hand passed to Player Logic
        frst_crd = []
        for x in range(0,len(self.ply_hand)):
            frst_crd.append(self.ply_hand[x][0])
        ### First find if an Ace is in hand
        if len(ply_hnd) == 2:
            if (('A' in frst_crd) and ('8' in frst_crd)) or (('A' in frst_crd) and ('9' in frst_crd)) or (('A' in frst_crd) and ('10' in frst_crd)):
                return 'STAY'
            elif (('A' in frst_crd) and ('7' in frst_crd)):
                if dlr_hnd_vlu == '2' or dlr_hnd_vlu == '7' or dlr_hnd_vlu == '8':
                    return 'STAY'
                elif dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            elif (('A' in frst_crd) and ('6' in frst_crd)):
                if dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            elif (('A' in frst_crd) and ('5' in frst_crd)) or (('A' in frst_crd) and ('4' in frst_crd)):
                if dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            elif (('A' in frst_crd) and ('3' in frst_crd)) or (('A' in frst_crd) and ('2' in frst_crd)):
                if dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            ### Check if DOUBLES are in hand
            elif frst_crd.count('A') == 2 or frst_crd.count('8') == 2:
                return 'SPLIT'
            elif frst_crd.count('T') == 2 or frst_crd.count('J') == 2 or frst_crd.count('Q') == 2 or frst_crd.count('K') == 2:
                return 'STAY'
            elif frst_crd.count('9') == 2:
                if dlr_hnd_vlu == '7' or dlr_hnd_vlu == 'T' or dlr_hnd_vlu == 'J' or dlr_hnd_vlu == 'Q' or dlr_hnd_vlu == 'K' or dlr_hnd_vlu == 'A':
                    return 'STAY'
                else:
                    return 'SPLIT'
            elif frst_crd.count('7') == 2 or frst_crd.count('2') == 2 or frst_crd.count('3') == 2:
                if dlr_hnd_vlu == '8' or dlr_hnd_vlu == '9' or dlr_hnd_vlu == 'T' or dlr_hnd_vlu == 'A':
                    return 'HIT'
                else:
                    return 'SPLIT'
            elif frst_crd.count('6') == 2:
                if dlr_hnd_vlu == '2' or dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'SPLIT'
                else:
                    return 'HIT'
            elif frst_crd.count('5') == 2:
                if dlr_hnd_vlu == 'T' or dlr_hnd_vlu == 'A':
                    return 'HIT'
                
                else:
                    return 'DOUBLE'
            elif frst_crd.count('4') == 2:
                if dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'SPLIT'
                else:
                    return 'HIT'
            else:
                if ply_hnd_vlu == 17 or ply_hnd_vlu == 18 or ply_hnd_vlu == 19 or ply_hnd_vlu == 20 or ply_hnd_vlu == 21:
                    return 'STAY'
                elif ply_hnd_vlu == 13 or ply_hnd_vlu == 14 or ply_hnd_vlu == 15 or ply_hnd_vlu == 16:
                    if dlr_hnd_vlu == '2' or dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                        return 'STAY'
                    else:
                        return 'HIT'
                elif ply_hnd_vlu == 12:
                    if dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                        return 'STAY'
                    else:
                        return 'HIT'
                elif ply_hnd_vlu == 11:
                    if dlr_hnd_vlu == 'A':
                        return 'HIT'
                    else:
                        return 'DOUBLE'
                elif ply_hnd_vlu == 10:
                    if dlr_hnd_vlu == 'A' or dlr_hnd_vlu == 'T':
                        return 'HIT'
                    else:
                        return 'DOUBLE'
                elif ply_hnd_vlu == 9:
                    if dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                        return 'DOUBLE'
                    else:
                        return 'HIT'
                else:
                    return 'HIT'
        ### Check for all other hands
        else:
            if ply_hnd_vlu == 17 or ply_hnd_vlu == 18 or ply_hnd_vlu == 19 or ply_hnd_vlu == 20 or ply_hnd_vlu == 21:
                return 'STAY'
            elif ply_hnd_vlu == 13 or ply_hnd_vlu == 14 or ply_hnd_vlu == 15 or ply_hnd_vlu == 16:
                if dlr_hnd_vlu == '2' or dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'STAY'
                else:
                    return 'HIT'
            elif ply_hnd_vlu == 12:
                if dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'STAY'
                else:
                    return 'HIT'
            elif ply_hnd_vlu == 11:
                if dlr_hnd_vlu == 'A':
                    return 'HIT'
                else:
                    return 'DOUBLE'
            elif ply_hnd_vlu == 10:
                if dlr_hnd_vlu == 'A' or dlr_hnd_vlu == 'T' or dlr_hnd_vlu == 'J' or dlr_hnd_vlu == 'Q' or dlr_hnd_vlu == 'K':
                    return 'HIT'
                else:
                    return 'DOUBLE'
            elif ply_hnd_vlu == 9:
                if dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            else:
                return 'HIT'

    def Determine_Bet(self):#Eventually pass parameters that will help determine what the betting amount is

        #if self.win_strk >=5:
            #self.win_stre
        if self.lss_strk == 1 or self.lss_strk == 2:
            #play minimum bet
            bet = self.minimum
            return bet
        elif self.win_strk == 1 or self.win_strk == 5 or self.win_strk == 9:# or self.win_strk == 2 or self.win_strk == 3:
            #increase bet by 1/2 last bet value
            #bet = self.last_bet+(self.last_bet/2)
            bet = minimum*3
            return bet
        elif self.win_strk == 2 or self.win_strk == 6 or self.win_strk == 10:
            bet = minimum*2
            return minimum
        elif self.win_strk == 3 or self.win_strk == 7 or self.win_strk == 11:
            bet = minimum*6
            return minimum
        elif self.win_strk == 4 or self.win_strk == 8 or self.win_strk == 12:
            bet = minimum
            return minimum
        #elif self.win_strk >= 4 or self.psh_cmbo >= 3 :#or(self.win_strk == 2 and self.psh_cmbo >= 1) or (self.win_strk == 1 and self.psh_cmbo >= 2):
            #play minimum bet
            #bet = self.minimum
            #return bet
        elif self.lss_strk == 3 :#or self.lss_strk == 4:#or (self.lss_strk == 2 and self.psh_cmbo >= 1):
            #Triple minimum bet
            bet = self.minimum*3
            return bet
        else:
            #Play minimum bet
            bet = self.minimum
            return bet

class Split_Hand_Hit:
    
    def __init__(self, DLR_HAND, PLY_HAND):
        
        self.dlr_hand = DLR_HAND
        self.ply_hand = PLY_HAND

    def split_logic(self):
        ###
        ###
        ### Currently this does not take into consideration if the hand is: 'A' '2' '3' essentially equal to 'A' '5'
        ###
        ###
        dlr_hnd = self.dlr_hand
        ply_hnd = self.ply_hand
        #dlr_hnd_instance = Calculate(self.dlr_hand)
        #dlr_hnd_vlu = dlr_hnd_instance.hnd_value()
        dlr_hnd_vlu = dlr_hnd[0][0]
        ply_hnd_instance = Calculate(self.ply_hand)
        ply_hnd_vlu = ply_hnd_instance.hnd_value()
        # Creates a list of just the first values in each hand passed to Player Logic
        frst_crd = []
        for x in range(0,len(self.ply_hand)):
            frst_crd.append(self.ply_hand[x][0])
        ### First find if an Ace is in hand
        if len(ply_hnd) == 2:
            if (('A' in frst_crd) and ('8' in frst_crd)) or (('A' in frst_crd) and ('9' in frst_crd)) or (('A' in frst_crd) and ('10' in frst_crd)):
                return 'STAY'
            elif (('A' in frst_crd) and ('7' in frst_crd)):
                if dlr_hnd_vlu == '2' or dlr_hnd_vlu == '7' or dlr_hnd_vlu == '8':
                    return 'STAY'
                elif dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            elif (('A' in frst_crd) and ('6' in frst_crd)):
                if dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            elif (('A' in frst_crd) and ('5' in frst_crd)) or (('A' in frst_crd) and ('4' in frst_crd)):
                if dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            elif (('A' in frst_crd) and ('3' in frst_crd)) or (('A' in frst_crd) and ('2' in frst_crd)):
                if dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            ### Removed doubles for split hit as doubles sometimes choose to split, and a second split is not possible
            else :
                if ply_hnd_vlu == 17 or ply_hnd_vlu == 18 or ply_hnd_vlu == 19 or ply_hnd_vlu == 20 or ply_hnd_vlu == 21:
                    return 'STAY'
                elif ply_hnd_vlu == 13 or ply_hnd_vlu == 14 or ply_hnd_vlu == 15 or ply_hnd_vlu == 16:
                    if dlr_hnd_vlu == '2' or dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                        return 'STAY'
                    else:
                        return 'HIT'
                elif ply_hnd_vlu == 12:
                    if dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                        return 'STAY'
                    else:
                        return 'HIT'
                elif ply_hnd_vlu == 11:
                    if dlr_hnd_vlu == 'A':
                        return 'HIT'
                    else:
                        return 'DOUBLE'
                elif ply_hnd_vlu == 10:
                    if dlr_hnd_vlu == 'A' or dlr_hnd_vlu == 'T':
                        return 'HIT'
                    else:
                        return 'DOUBLE'
                elif ply_hnd_vlu == 9:
                    if dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                        return 'DOUBLE'
                    else:
                        return 'HIT'
                else:
                    return 'HIT'
        ### Check for all other hands
        else:
            if ply_hnd_vlu == 17 or ply_hnd_vlu == 18 or ply_hnd_vlu == 19 or ply_hnd_vlu == 20 or ply_hnd_vlu == 21:
                return 'STAY'
            elif ply_hnd_vlu == 13 or ply_hnd_vlu == 14 or ply_hnd_vlu == 15 or ply_hnd_vlu == 16:
                if dlr_hnd_vlu == '2' or dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'STAY'
                else:
                    return 'HIT'
            elif ply_hnd_vlu == 12:
                if dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'STAY'
                else:
                    return 'HIT'
            elif ply_hnd_vlu == 11:
                if dlr_hnd_vlu == 'A':
                    return 'HIT'
                else:
                    return 'DOUBLE'
            elif ply_hnd_vlu == 10:
                if dlr_hnd_vlu == 'A' or dlr_hnd_vlu == 'T' or dlr_hnd_vlu == 'J' or dlr_hnd_vlu == 'Q' or dlr_hnd_vlu == 'K':
                    return 'HIT'
                else:
                    return 'DOUBLE'
            elif ply_hnd_vlu == 9:
                if dlr_hnd_vlu == '3' or dlr_hnd_vlu == '4' or dlr_hnd_vlu == '5' or dlr_hnd_vlu == '6':
                    return 'DOUBLE'
                else:
                    return 'HIT'
            else:
                return 'HIT'

class Calculate:

    def __init__(self, hand):
        self.hand = hand

    def hnd_value(self):
        tot = 0
        temp_keep = []
        temp_remv = self.hand[:]
        for x in range(0,len(self.hand)):
            if self.hand[x][0] == 'A':
                temp_keep.append(self.hand[x])
                temp_remv.remove(self.hand[x])
            else: #do nothing
                temp_keep = temp_keep
        if len(temp_keep) == 0:
            for x in range(0,len(self.hand)):
                if self.hand[x][0] == 'T' or self.hand[x][0] == 'J' or self.hand[x][0] == 'Q' or self.hand[x][0] == 'K':
                    tot+=10
                elif self.hand[x][0] == 'A':
                    tot+=11
                    if tot > 21:
                        tot-= 10
                    else:
                        tot = tot
                else :
                    tot+=int(self.hand[x][0])
        else:
            hand = temp_remv + temp_keep
            tot = 0
            for x in range(0,len(hand)):
                if hand[x][0] == 'T' or hand[x][0] == 'J' or hand[x][0] == 'Q' or hand[x][0] == 'K':
                    tot+=10
                elif hand[x][0] == 'A':
                    tot+=11
                    if tot > 21:
                        tot-= 10
                    else:
                        tot = tot
                else :
                    tot+=int(hand[x][0])
        #print tot
        return tot


### This class is used to double down
class Double:

    def __init__(self, hand):
        self.hand = hand

    def hnd_value(self):
        
        return

### This class is used to hit
class Hit:

    def __init__(self, old_hnd):
        self.old_hnd = old_hnd

    def hit_value(self):
        hit = random.sample(DECK,1)
        # insert function to remove card right here <<<
        # function below appends
        rmv = RMV(hit)
        rmv.rmv_card()
        new_hnd= self.old_hnd + hit
        return new_hnd

#Example of calling split function
#test = ['3s', 'AH']
#split_cllr = Split(test)
#spl_hnd_1, spl_hnd_2 = split_cllr.split_hands()
### This class is used to split
class Split:

    def __init__(self, hand):
        self.hand = hand

    def split_hands(self):
        temp_1 = list()
        hnd_1 = Hit(temp_1)
        hnd_1 = hnd_1.hit_value()
        hnd_1.append(self.hand[0])

        temp_2 = list()
        hnd_2 = Hit(temp_2)
        hnd_2 = hnd_2.hit_value()
        hnd_2.append(self.hand[1])
        
        return hnd_1, hnd_2
        
### this class is used to stay
class Stay:

    def __init__(self, hand):
        self.hand = hand

    def hnd_value(self):
        return

### this class is used to Remove used cards from the DECK
class RMV:

    def __init__(self, hand):
        self.hand = hand

    def rmv_card(self):
        for x in range(0,len(self.hand)): #removes card from DECK
            DECK.remove(self.hand[x])
        return





### 
### Getting starting amount and betting amount

### Globals
total_decks = 2
SUITS = 'CDHS'
RANKS = '23456789TJQKA'
DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
DECK = DECK*total_decks #creates 2 DECK of cards, but could also use : DECK = DECK + DECK + etc.....

Dealer_Wins = 0
Player_Wins = 0
Push_Wins = 0

minimum = 0
last_bet = 0
win_streak = 0
loss_streak = 0
push_combo = 0

hands_played = 0 #Dealer_Wins, Player_Wins, Push_Wins
want_to_play = 60

plot_bank = []
win_plot = []
lss_plot = []
psh_plot = []

    
print('\n')
print ("Welcome to the one and only BlackJack!!! \n")
while True:
    try:
        bank = int(input("Amount of money you are starting with! : "))
        break
    except NameError:
        print("Oops! That was not a valid number. Try again...")
    except ValueError:
        print("Oops, ValueError. Please type a number!")
    except TypeError:
        print("Oops, TypeError. Please type a number!")
    except SyntaxError:
        print("Oops, SyntaxError. Please type a number!")
    except:
        print("Not sure what the error is.")

print ('\n')
print ('\n')
bank_amt = 'This is your current bank amount: ' + str(bank)
print (bank_amt)


###
### Main function takes place here, everything before this is defining or initializing parameters
###


while len(DECK) > 21 :
    p_hnd_spl_1_BJ = 'NO'
    p_hnd_spl_2_BJ = 'NO'
    d_hnd_BJ = 'NO'
    p_hnd_BJ = 'NO'

    ### New round of betting starts here every time
    #amt_plyrs = input("How many players are sitting at the table? : ")
    amt_plyrs = 1
    #time.sleep(.75)
    ROUND = 'Play'
    while ROUND == 'Play':
        if amt_plyrs == 1 :
            # insert function to call bank() with values of previous
            if last_bet == 0:
                while True:
                    try:
                            bet_amt = int(input("This is your first bet, and your minimum bet value? : "))
                            last_bet = bet_amt
                            minimum = bet_amt
                            break
                    except NameError:
                            print("Oops! That was not a valid number. Try again...")
                    except ValueError:
                            print("Oops, ValueError. Please type a number!")
                    except TypeError:
                            print("Oops, TypeError. Please type a number!")
                    except SyntaxError:
                            print("Oops, SyntaxError. Please type a number!")
                    except:
                            print("Not sure what the error is.")
            else:
                last_bet = Player_Logic(dl_hnd,ply_hnd,loss_streak,win_streak,push_combo,last_bet,minimum).Determine_Bet()
                #last_bet = next_bet
                bet_amt = last_bet
            bank-= bet_amt # updates current bank value
            print ('This is your new bank amount ' + str(bank))
            print ('\n')


            #print('\n This is the length of the current DECK.')
            #print(len(DECK))


            # Present both dealer and player hands
            dl_hnd = random.sample(DECK,2)
            call_1 = RMV(dl_hnd)
            call_1.rmv_card()
            #d_hand = Calculate(dl_hnd[0])
            ply_hnd = random.sample(DECK,2)
            call_2 = RMV(ply_hnd)
            call_2.rmv_card()
            print ('\n'+ 'Dealer has: ' + dl_hnd[0] + ' __')        
            print ('\n'+ 'Player has: ' + ply_hnd[0] + ' ' + ply_hnd[1])
            p_hnd = Calculate(ply_hnd)
            print(p_hnd.hnd_value())
            #time.sleep(.5)
            #print (ply_hnd)

            ### remove Cards from DECK could turn this into a function right here
            '''for x in range(0,len(dl_hnd)): #removes card from DECK
                DECK.remove(dl_hnd[x])
                DECK.remove(ply_hnd[x])'''
            ### created RMV function and is being invoked below


            p_hnd = Calculate(ply_hnd)
            d_hnd = Calculate(dl_hnd)
            if p_hnd.hnd_value() == 21 and d_hnd.hnd_value() == 21:
                p_hnd_BJ = 'BJ'
                d_hnd_BJ = 'BJ'
                Round = 1
                dealer = "Both Player and Dealer got a BJ"
                did_split = 0
            elif d_hnd.hnd_value() == 21 and p_hnd.hnd_value() != 21:
                d_hnd_BJ = 'BJ'
                p_hnd = p_hnd.hnd_value()
                Round = 1
                dealer = "Dealer got a BJ"
                did_split = 0
            elif p_hnd.hnd_value() == 21 and d_hnd.hnd_value() != 21:
                d_hnd = d_hnd.hnd_value()
                p_hnd_BJ = 'BJ'
                Round = 1
                dealer = "Player got a BJ"
                did_split = 0
            else:
                Round = 0
                dealer = "Not Ready"
            #next_move = raw_input("What is your next move: STAY, HIT, DOUBLE, SPLIT, or SURRENDER?").lower()
            player = 0 # Zero means not ready, 1 means ready for dealer to hit
            while Round == 0:
                did_split = 0
                p_hnd_spl_1 = 0
                p_hnd_spl_2 = 0
                print('\n')
                #next_move = Player_Logic()
                #next_move = input("What is your next move: STAY, HIT, DOUBLE, SPLIT, or SURRENDER? : ").lower()
                while True:
                    try:
                            #next_move = Player_Logic(dl_hnd,ply_hnd).logic()
                            next_move = Player_Logic(dl_hnd,ply_hnd,loss_streak,win_streak,push_combo,last_bet,minimum).logic()
                            next_move = next_move.lower()
                            #next_move = raw_input("What is your next move: STAY, HIT, DOUBLE, SPLIT, or SURRENDER? : ").lower()
                            break
                    except NameError:
                            print("Oops! That was not a valid number. Try again...")
                    except ValueError:
                            print("Oops, ValueError. Please type a number!")
                    except TypeError:
                            print("Oops, TypeError. Please type a number!")
                    except SyntaxError:
                            print("Oops, SyntaxError. Please type a number!")
                    except:
                            print("Not sure what the error is.")
                print('\n')
                if next_move == 'stay':
                    print ("You decided to stay, dealer will now flip his hidden card. ")
                    print('\n')
                    Round = 1 # One means "Ready" and therefore exits loop
                elif next_move == 'hit':
                    print("\nYou decided to hit. Your new hand is :")
                    #Calling the Hit function for a new card
                    next_card = Hit(ply_hnd)
                    ply_hnd = next_card.hit_value()
                    #Calling the calculate function
                    p_hnd = Calculate(ply_hnd)
                    p_hnd = p_hnd.hnd_value()
                    if p_hnd > 21:
                        print(ply_hnd)
                        print('You busted! ')
                        print(p_hnd)
                        print ('\n')
                        #time.sleep(1.25)
                        Round = 1 # One means "Ready" and therefore exits loop
                    else:
                        print ('\n')
                        print(ply_hnd)
                        print('New value of : ' + str(p_hnd))
                elif next_move == 'double':
                    bank-=bet_amt # updating bank with double down
                    print("\nDoubling down, and therefor you are doubling your bet of : " + str(bet_amt))
                    bet_amt = bet_amt *2 #updating stored bet amount
                    print("Your new betting value is : " + str(bet_amt)+ "\n")
                    print("\nYour new hand is now :")
                    #time.sleep(.75)
                    
                    next_card = Hit(ply_hnd)
                    ply_hnd = next_card.hit_value() #Hitting and taking new card
                    
                    p_hnd = Calculate(ply_hnd) #Calculating value of new hand
                    p_hnd = p_hnd.hnd_value()
                    if p_hnd > 21:
                        print ('\n')
                        print(ply_hnd)
                        print('New value of : ' + str(p_hnd)+ "\n")
                        print('You busted! ')
                        print ('\n')
                        #time.sleep(1.25)
                        Round = 1 # One means "Ready" and therefore exits loop
                    else:
                        print ('\n')
                        print(ply_hnd)
                        print('New value of : ' + str(p_hnd)+ "\n")
                        #time.sleep(1.25)
                        Round = 1 # One means "Ready" and therefore will exit the loop
                elif next_move == 'split':
                    did_split = 1
                    spl_1_amt = bet_amt
                    spl_2_amt = bet_amt
                    bank-= spl_1_amt #Updating Bank for split amount
                    p_hnd = 0
                    print("Updating bank amount for split. Reducing by : " + str(spl_1_amt))
                    print(" New bank value of : " + str(bank) + "\n")
                    #time.sleep(1.25)
                    #spl_2_bank = bet_amt
                    #example of calling the split function
                    #test = ['3s', 'AH']
                    #split_cllr = Split(test)
                    #spl_hnd_1, spl_hnd_2 = split_cllr.split_hands()
                    ### New hands saved into spl_hnd_1 and spl_hnd_2
                    split_cllr = Split(ply_hnd)
                    spl_hnd_1, spl_hnd_2 = split_cllr.split_hands()

                    split_ready = 0 # Zero means'Not Ready'
                    split_ready_1 = 0
                    split_ready_2 = 0
                    print("\nYou decided to Split. Your first split hand is : ")
                    while split_ready == 0 : # Zero means 'Not Ready'
                        #print(spl_hnd_1)
                        ### This section of code is a repeat of all previous sections of code:
                        # Zero means not ready, 1 means ready for dealer to hit
                        if split_ready_1 == 0:
                            double_split_1 = 0
                            while split_ready_1 == 0:
                                print('\n')
                                print ('\n'+ 'Dealer has: ' + dl_hnd[0] + ' __')
                                print ('\n'+ 'Player has: ' + spl_hnd_1[0] + ' ' + spl_hnd_1[1]+ "\n")
                                p_hnd_spl_1 = Calculate(spl_hnd_1)
                                print(str(p_hnd_spl_1.hnd_value())+"\n")

                                ### Checking if BJ after split, if so then exiting first split hand 
                                if p_hnd_spl_1.hnd_value() == 21 and len(spl_hnd_1) == 2:
                                    p_hnd_spl_1_BJ = 'BJ'
                                    d_hnd_spl_1 = d_hnd.hnd_value()
                                    p_hnd_spl_1 = Calculate(spl_hnd_1)
                                    p_hnd_spl_1 = p_hnd_spl_1.hnd_value()
                                    #Round = 1
                                    #dealer = "Split hand one got a BJ"
                                    split_ready_1 = 1
                                    break
                                else:
                                    #Round = 0
                                    split_ready_1 = 0

                                #Eventually will call "Player_Hit" Function
                                #next_move = Player_Logic(dl_hnd,ply_hnd).logic()
                                if double_split_1 == 0:
                                    next_move = Player_Logic(dl_hnd,ply_hnd,loss_streak,win_streak,push_combo,last_bet,minimum).logic()
                                    next_move = next_move.lower()
                                else:
                                    print("Double Split Protocol implemented. For Split one!")
                                    #time.sleep(2)
                                #next_move = input("#### Split hand 'ONE': #### \nWhat is your next move: STAY, HIT, DOUBLE, SPLIT, or SURRENDER? : ").lower()
                                print('\n')
                                if next_move == 'stay':
                                    print ("You decided to stay, now moving onto second split hand. ")
                                    print('\n')
                                    p_hnd_spl_1 = Calculate(spl_hnd_1)
                                    p_hnd_spl_1 = p_hnd_spl_1.hnd_value()
                                    split_ready_1 = 1 # One means "Ready" and therefore exits loop
                                elif next_move == 'hit':
                                    print("\nYou decided to hit. Your new split hand one is :")
                                    #Calling the Hit function for a new card
                                    next_card = Hit(spl_hnd_1)
                                    spl_hnd_1 = next_card.hit_value()
                                    print(str(spl_hnd_1)+"\n")
                                    #Calling the calculate function
                                    p_hnd_spl_1 = Calculate(spl_hnd_1)
                                    p_hnd_spl_1 = p_hnd_spl_1.hnd_value() ### Saves value of 'Player Split Hand 1'
                                    if p_hnd_spl_1 > 21:
                                        print(p_hnd_spl_1) ### Saves value of 'Player Split Hand 1'
                                        print('You busted! ')
                                        print ('\n')
                                        #time.sleep(1.25)
                                        split_ready_1 = 1 # One means "Ready" and therefore exits loop
                                    else:
                                        #print ('\n')
                                        #print(spl_hnd_1)
                                        print('\n')
                                        print ('Dealer has      : ' + dl_hnd[0] + ' __')
                                        print ('New Player Hand : ' + str(spl_hnd_1)) ### Saves value of 'Player Split Hand 1'
                                elif next_move == 'double':
                                    #spl_1_amt = bet_amt
                                    bank-= spl_1_amt #Update Bank for doubling
                                    spl_1_amt = spl_1_amt*2 # Updating split value for double after splitting hand 1
                                    print("\nDoubling down, and therefor you are doubling your split bet of : " + str(spl_1_amt)+"\n")
                                    print("Your new bank value is : " + str(bank)+ "\n")
                                    #time.sleep(2)
                                    print("\nYour new hand is now :")
                                    
                                    next_card = Hit(spl_hnd_1)
                                    spl_hnd_1 = next_card.hit_value() #Hitting and taking new card
                                    
                                    p_hnd_spl_1 = Calculate(spl_hnd_1) #Calculating value of new hand
                                    p_hnd_spl_1 = p_hnd_spl_1.hnd_value()
                                    if p_hnd_spl_1 > 21:
                                        print ('\n')
                                        print(spl_hnd_1)
                                        print('New value of : ' + str(p_hnd_spl_1)+ "\n")
                                        print('You busted! ')
                                        print ('\n')
                                        #time.sleep(1.25)
                                        split_ready_1 = 1 # One means "Ready" and therefore exits loop
                                    else:
                                        print ('\n')
                                        print(spl_hnd_1)
                                        print('New value of : ' + str(p_hnd_spl_1)+ "\n")
                                        #time.sleep(1.25)
                                        split_ready_1 = 1 # One means "Ready" and therefore will exit the loop
                                elif next_move == 'split':
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    p_hnd_spl_1 = Calculate(spl_hnd_1) #Calculating value of new hand
                                    p_hnd_spl_1 = p_hnd_spl_1.hnd_value()
                                    #split_ready_1 = 1
                                    #next_move = 'STAY'
                                    next_move = Split_Hand_Hit(dl_hnd,spl_hnd_1).split_logic()
                                    next_move = next_move.lower()
                                    #time.sleep(2.5)
                                    split_ready_1 = 0 # One means "Ready"
                                    double_split_1 = 1
                                elif next_move == 'surrender':
                                    print("Currently surrender does not work \n")
                                    split_ready_1 = 0 # One means "Ready"
                                else :
                                    print ('\n')
                                    print("Incorrect word or spelling, choose again! :")
                        elif split_ready_2 == 0:
                            # Zero means not ready, 1 means ready for next step, most likely meaning dealer to hit
                            double_split_2 = 0
                            while split_ready_2 == 0:
                                print ('\n'+ 'Dealer has: ' + dl_hnd[0] + ' __')
                                print ('\n'+ 'Player has: ' + spl_hnd_2[0] + ' ' + spl_hnd_2[1]+ "\n")
                                p_hnd_spl_2 = Calculate(spl_hnd_2)
                                print(str(p_hnd_spl_2.hnd_value())+"\n")
                                
                                ### Checking if BJ after split, if so then exiting first split hand 
                                if p_hnd_spl_2.hnd_value() == 21 and len(spl_hnd_2) == 2:
                                    p_hnd_spl_2_BJ = 'BJ'
                                    d_hnd_spl_2 = d_hnd.hnd_value()
                                    p_hnd_spl_2 = Calculate(spl_hnd_2)
                                    p_hnd_spl_2 = p_hnd_spl_2.hnd_value()
                                    #Round = 1
                                    #dealer = "Split hand one got a BJ"
                                    split_ready_2 = 1
                                    split_ready = 1
                                    break
                                else:
                                    #Round = 0
                                    split_ready_2 = 0                                    
                                
                                print('\n')
                                if double_split_2 == 0:
                                    #next_move = Player_Logic(dl_hnd,ply_hnd).logic()
                                    next_move = Player_Logic(dl_hnd,ply_hnd,loss_streak,win_streak,push_combo,last_bet,minimum).logic()
                                    next_move = next_move.lower()
                                    #next_move = input("#### Split hand 'TWO': #### \nWhat is your next move: STAY, HIT, DOUBLE, SPLIT, or SURRENDER? : ").lower()
                                else:
                                    print("Implementing Double Split Protocol! ")
                                    #time.sleep(2)
                                print('\n')
                                if next_move == 'stay':
                                    print ("You decided to stay, now moving onto dealers hand. ")
                                    print('\n')
                                    split_ready_2 = 1 # One means "Ready" and therefore exits loop
                                    split_ready = 1
                                    p_hnd_spl_2 = Calculate(spl_hnd_2)
                                    p_hnd_spl_2 = p_hnd_spl_2.hnd_value()
                                elif next_move == 'hit':
                                    print("\nYou decided to hit. Your new split hand one is :")
                                    #Calling the Hit function for a new card
                                    next_card = Hit(spl_hnd_2)
                                    spl_hnd_2 = next_card.hit_value()
                                    print(str(spl_hnd_2)+"\n")
                                    #Calling the calculate function
                                    p_hnd_spl_2 = Calculate(spl_hnd_2)
                                    p_hnd_spl_2 = p_hnd_spl_2.hnd_value() ### Saves value of 'Player Split Hand 2'
                                    if p_hnd_spl_2 > 21:
                                        print(p_hnd_spl_2) ### Saves value of 'Player Split Hand 2'
                                        print('You busted! ')
                                        print ('\n')
                                        #time.sleep(1.25)
                                        split_ready_2 = 1 # One means "Ready" and therefore exits loop
                                        split_ready = 1
                                    else:
                                        #print ('\n')
                                        #print(spl_hnd_2)
                                        print('\n')
                                        print ('Dealer has      : ' + dl_hnd[0] + ' __')
                                        print ('New Player Hand : ' + str(spl_hnd_2)) ### Saves value of 'Player Split Hand 1'
                                        print(p_hnd_spl_2)
                                elif next_move == 'double':
                                    #spl_2_amt = bet_amt
                                    bank-= spl_2_amt #Update Bank for doubling
                                    spl_2_amt = spl_2_amt*2 # Updating split value for double after splitting hand 2
                                    print("\nDoubling down, and therefor you are doubling your split bet of : " + str(spl_2_amt)+"\n")
                                    print("Your new bank value is : " + str(bank)+ "\n")
                                    #time.sleep(2)
                                    print("\nYour new hand is now :")
                                    
                                    next_card = Hit(spl_hnd_2)
                                    spl_hnd_2 = next_card.hit_value() #Hitting and taking new card
                                    
                                    p_hnd_spl_2 = Calculate(spl_hnd_2) #Calculating value of new hand
                                    p_hnd_spl_2 = p_hnd_spl_2.hnd_value()
                                    if p_hnd_spl_2 > 21:
                                        print ('\n')
                                        print(spl_hnd_2)
                                        print('New value of : ' + str(p_hnd_spl_2)+ "\n")
                                        print('You busted! ')
                                        print ('\n')
                                        #time.sleep(1.25)
                                        split_ready_2 = 1 # One means "Ready" and therefore exits loop
                                        split_ready = 1
                                    else:
                                        print ('\n')
                                        print(spl_hnd_2)
                                        print('New value of : ' + str(p_hnd_spl_2)+ "\n")
                                        #time.sleep(1.25)
                                        split_ready_2 = 1 # One means "Ready" and therefore will exit the loop
                                        split_ready = 1
                                elif next_move == 'split':
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    print("Not allowed to split a second time")
                                    p_hnd_spl_2 = Calculate(spl_hnd_2) #Calculating value of new hand
                                    p_hnd_spl_2 = p_hnd_spl_2.hnd_value()
                                    #split_ready_2 = 1 # One means "Ready" and therefore exits loop
                                    #split_ready = 1
                                    next_move = Split_Hand_Hit(dl_hnd,spl_hnd_2).split_logic()
                                    next_move = next_move.lower()
                                    #time.sleep(2)
                                    double_split_2 = 1
                                    #split_ready_2 = 0 # One means "Ready"
                                elif next_move == 'surrender':
                                    print("Currently surrender does not work \n")
                                    split_ready_2 = 0 # One means "Ready"
                                else :
                                    print ('\n')
                                    print("Incorrect word or spelling, choose again! :")
                                #split_ready = 1
                        else:
                            print ("Error Occured, your money might have gotten stolen by the dealer!")
                            split_ready = 1
                            split_ready_1 = 1
                            split_ready_2 = 1
                    Round = 1 # One means "Ready"
                elif next_move == 'surrender':
                    print("Currently surrender does not work \n")
                    Round = 0 # One means "Ready"
                else :
                    print ('\n')
                    print("Incorrect word or spelling, choose again! :")
                    
            '''if p_hnd < 22:
                dealer = 'Not Ready'
            else:
                dealer = "Ready"'''
            while dealer == 'Not Ready':#Being used to create dealers hand
                p_hnd = Calculate(ply_hnd)
                d_hnd = Calculate(dl_hnd)
                p_hnd = p_hnd.hnd_value()
                d_hnd = d_hnd.hnd_value()
                '''p_hnd_spl_1 = Calculate(spl_hnd_1) #Calculating value of new hand
                p_hnd_spl_1 = p_hnd_spl_1.hnd_value()
                p_hnd_spl_2 = Calculate(spl_hnd_2) #Calculating value of new hand
                p_hnd_spl_2 = p_hnd_spl_2.hnd_value()'''
                if p_hnd_spl_1 > 21 and p_hnd_spl_2 > 21 :
                    #Do nothing, don't hit for the dealer, just present the dealers cards
                    print("Dealer is not drawing, as all players busted! ")
                    dealer = 'Ready'
                elif p_hnd > 21 :
                    #Do nothing, don't hit for the dealer, just present the dealers cards
                    print("Dealer is not drawing, as all players busted! ")
                    dealer = 'Ready'
                else:
                    d_hnd = Calculate(dl_hnd)
                    print("Dealers current hand: " + str(dl_hnd))
                    print("Dealers current Value: " +str(d_hnd.hnd_value()))
                    d_hnd = d_hnd.hnd_value()
                    if d_hnd == 21 or d_hnd == 20 or d_hnd == 19 or d_hnd == 18 or d_hnd == 17:
                        dealer = 'Ready'
                        print('Dealer is ready to determine winners')
                    else :
                        if d_hnd < 17:
                            next_card = Hit(dl_hnd)
                            dl_hnd = next_card.hit_value()
                            print('Dealer took a hit. New Card is : ' + str(dl_hnd[len(dl_hnd)-1]))
                            #print(dl_hnd[len(dl_hnd)-1])
                            print ('\n')
                            #time.sleep(.75)
                        else:
                            dealer = 'Ready'
            
            ### Calculate hands could turn into function
            
            #print ('\n'+ 'Dealer has: ' + str(dl_hnd[0]) + ' ' + dl_hnd[1])
            #print ('\n'+ 'Player has: ' + str(ply_hnd[0]) + ' ' + ply_hnd[1])

            if did_split == 1: #Implement bank updates for split
                d_hnd = Calculate(dl_hnd)
                #p_hnd = Calculate(ply_hnd)
                #spl_1_amt = bet_amt
                #spl_2_amt = bet_amt
                #p_hnd_spl_1 = Calculate(spl_hnd_1)
                #p_hnd_spl_1 = p_hnd_spl_1.hnd_value()
                ###
                ###
                # Now calculating first split bank amounts
                if p_hnd_spl_1_BJ == 'BJ':
                    print("BlackJack!!!! Pays 3 to 2 \n")
                    print ('The Dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                    print ('The Player has : 21 BlackJack ' + str(ply_hnd))
                    print ('\n')
                    bank = bank + (2*bet_amt) + (bet_amt/2)
                    bank_amt = 'This is your current bank amount: ' + str(bank)
                    print (bank_amt)
                    Player_Wins += 1 #Update Victories
                    ROUND = 'End of round'
                    if loss_streak >= 1:
                        push_combo = 0
                    else:
                        push_combo = push_combo
                    win_streak+=1
                    loss_streak = 0
                else:
                    p_hnd_spl_1 = Calculate(spl_hnd_1)
                    if d_hnd.hnd_value() > 21 and p_hnd_spl_1.hnd_value() < 22:
                        print("You beat the dealer for Split 1! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd_spl_1.hnd_value()) + ' ' + str(spl_hnd_1))
                        bank+= spl_1_amt*2
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Player_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if loss_streak >= 1:
                            push_combo = 0
                        else:
                            push_combo = push_combo
                        win_streak +=1
                        loss_streak = 0
                    elif p_hnd_spl_1.hnd_value() > d_hnd.hnd_value() and p_hnd_spl_1.hnd_value() < 22:
                        print("You beat the dealer! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd_spl_1.hnd_value()) + ' ' + str(spl_hnd_1))
                        bank+= spl_1_amt*2
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Player_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if loss_streak >= 1:
                            push_combo = 0
                        else:
                            push_combo = push_combo
                        win_streak+=1
                        loss_streak = 0
                    elif p_hnd_spl_1.hnd_value() == d_hnd.hnd_value():
                        print("Tied, therefor it is a PUSH on Split 1! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd_spl_1.hnd_value()) + ' ' + str(spl_hnd_1))
                        print ('\n')
                        bank+= spl_1_amt
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Push_Wins +=1
                        ROUND = 'End of round'
                        push_combo += 1
                    else:
                        print("The dealer beat you for Split 1! Try again. \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd_spl_1.hnd_value()) + ' ' + str(spl_hnd_1))
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Dealer_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if win_streak >= 1:
                            win_streak = 0
                            loss_streak +=1
                            push_combo == 0
                        else:
                            win_streak = 0
                            loss_streak += 1
                #time.sleep(1.5)
                ### Now calculating Second Split Bank amounts
                if p_hnd_spl_2_BJ == 'BJ':
                    print ("BlackJack!!!! Pays 3 to 2 \n")
                    print ('The Dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                    print ('The Player has : 21 BlackJack ' + str(ply_hnd))
                    print ('\n')
                    bank = bank + (2*bet_amt) + (bet_amt/2)
                    bank_amt = 'This is your current bank amount: ' + str(bank)
                    print (bank_amt)
                    Player_Wins += 1 #Update Victories
                    ROUND = 'End of round'
                    if loss_streak >= 1:
                        win_streak += 1
                        loss_streak = 0
                        push_combo = 0
                    else:
                        loss_streak = 0
                        win_streak += 1
                else:
                    p_hnd_spl_2 = Calculate(spl_hnd_2)
                    if d_hnd.hnd_value() > 21 and p_hnd_spl_2.hnd_value() < 22:
                        print("You beat the dealer for Split 2! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd_spl_2.hnd_value()) + ' ' + str(spl_hnd_2))
                        bank+= spl_2_amt*2
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Player_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if loss_streak >= 1:
                            win_streak += 1
                            loss_streak = 0
                            push_combo = 0
                        else:
                            loss_streak = 0
                            win_streak += 1
                    elif p_hnd_spl_2.hnd_value() > d_hnd.hnd_value() and p_hnd_spl_2.hnd_value() < 22:
                        print("You beat the dealer! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd_spl_2.hnd_value()) + ' ' + str(spl_hnd_2))
                        bank+= spl_2_amt*2
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Player_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if loss_streak >= 1:
                            win_streak += 1
                            loss_streak = 0
                            push_combo = 0
                        else:
                            loss_streak = 0
                            win_streak += 1
                    elif p_hnd_spl_2.hnd_value() == d_hnd.hnd_value():
                        print("Tied, therefor it is a PUSH on Split 2! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd_spl_2.hnd_value()) + ' ' + str(spl_hnd_2))
                        print ('\n')
                        bank+= spl_2_amt
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Push_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        push_combo += 1
                    else:
                        print("The dealer beat you for Split 2! Try again. \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd_spl_2.hnd_value()) + ' ' + str(spl_hnd_2))
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Dealer_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if win_streak >= 1:
                            win_streak = 0
                            loss_streak += 1
                            push_combo = 0
                        else:
                            loss_streak +=1
                            win_streak = 0
                #time.sleep(.5) 
                
            else: #Implements bank update if player chose not to split
                if p_hnd_BJ == 'BJ' or d_hnd_BJ == 'BJ':
                    d_hnd = Calculate(dl_hnd)
                    p_hnd = Calculate(ply_hnd)
                    if p_hnd_BJ == 'BJ' and d_hnd_BJ == 'BJ':
                        print("Tied with both Player and Dealer having BJ, therefor it is a PUSH! \n")
                        print ('The Dealer has : 21 BlackJack ' + str(dl_hnd))
                        print ('The Player has : 21 BlackJack ' + str(ply_hnd))
                        print ('\n')
                        bank+= bet_amt
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Push_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        push_combo += 1
                    elif d_hnd_BJ == 'BJ' and p_hnd_BJ != 'BJ':
                        print("The dealer beat you! Try again. \n")
                        print ('The Dealer has : 21 BlackJack ' + str(dl_hnd))
                        p_hnd = Calculate(ply_hnd)
                        print ('The player has : ' +  str(p_hnd.hnd_value()) + ' ' + str(ply_hnd))
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Dealer_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if win_streak >= 1:
                            win_streak = 0
                            loss_streak += 1
                            push_combo = 0
                        else:
                            loss_streak +=1
                            win_streak = 0
                    else :#p_hnd_BJ == 'BJ' and d_hnd_BJ != 'BJ':
                        print("BlackJack!!!! Pays 3 to 2 \n")
                        print ('The Dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The Player has : 21 BlackJack ' + str(ply_hnd))
                        print ('\n')
                        bank = bank+(2*bet_amt)+(bet_amt/2)
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Player_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if loss_streak >= 1:
                            win_streak += 1
                            loss_streak = 0
                            push_combo = 0
                        else:
                            loss_streak = 0
                            win_streak += 1
                else:
                    d_hnd = Calculate(dl_hnd)
                    p_hnd = Calculate(ply_hnd)
                    if d_hnd.hnd_value() > 21 and p_hnd.hnd_value() < 22:
                        print("You beat the dealer! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd.hnd_value()) + ' ' + str(ply_hnd))
                        bank+= bet_amt*2
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Player_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if loss_streak >= 1:
                            win_streak += 1
                            loss_streak = 0
                            push_combo = 0
                        else:
                            loss_streak = 0
                            win_streak += 1
                    elif p_hnd.hnd_value() > d_hnd.hnd_value() and p_hnd.hnd_value() < 22:
                        print("You beat the dealer! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd.hnd_value()) + ' ' + str(ply_hnd))
                        bank+= bet_amt*2
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Player_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if loss_streak >= 1:
                            win_streak += 1
                            loss_streak = 0
                            push_combo = 0
                        else:
                            loss_streak = 0
                            win_streak += 1
                    elif p_hnd.hnd_value() == d_hnd.hnd_value():
                        print("Tied, therefor it is a PUSH! \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd.hnd_value()) + ' ' + str(ply_hnd))
                        print ('\n')
                        bank+= bet_amt
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Push_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        push_combo += 1
                    else:
                        print("The dealer beat you! Try again. \n")
                        print ('The dealer has : ' + str(d_hnd.hnd_value()) + ' ' + str(dl_hnd))
                        print ('The player has : ' +  str(p_hnd.hnd_value()) + ' ' + str(ply_hnd))
                        print ('\n')
                        bank_amt = 'This is your current bank amount: ' + str(bank)
                        print (bank_amt)
                        Dealer_Wins += 1 #Update Victories
                        ROUND = 'End of round'
                        if win_streak >= 1:
                            win_streak = 0
                            loss_streak += 1
                            push_combo = 0
                        else:
                            loss_streak +=1
                            win_streak = 0
                    #time.sleep(.5) 
        else:
            print ('\n')
            print ('\n')
            print ('Game not designed yet for more then two players! Try again with one player. ')
    plot_bank.append(bank)
    win_plot.append(win_streak*10)
    lss_plot.append(loss_streak*10-50)
    psh_plot.append(push_combo*10)
    hands_played += 1
    #used to shuffle
    if hands_played < want_to_play:
        DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))
        DECK = DECK*total_decks #creates 2 DECK of cards, but could also use : DECK = DECK + DECK + etc.....
    else:
        print("Total of " + str(hands_played) + "hands played. ")
    
    
    
    
hands_played = Dealer_Wins + Player_Wins + Push_Wins
print("Dealer Wins, Player Wins, Push's. \n")
print(Dealer_Wins,Player_Wins,Push_Wins)
print("Total Hands Played : " + str(hands_played) + "\n \n")
print("Dealer win % = :" + str(round(float(Dealer_Wins)/hands_played,2)) + "\n")
print("Player win % = :" + str(round(float(Player_Wins)/hands_played,2)) + "\n")
print("Push game % = :" + str(round(float(Push_Wins)/hands_played,2)) + "\n")
dl_win = round(float(Dealer_Wins)/hands_played,2)*100
pl_win = round(float(Player_Wins)/hands_played,2)*100
ps_win = round(float(Push_Wins)/hands_played,2)*100

import plotly
from plotly.graph_objs import Scatter, Layout
x_range = range(0,len(plot_bank))
### This works to plot just the winnings
#plotly.offline.plot({"data": [Scatter(x=x_range, y=plot_bank)], "layout": Layout(title="Bank Plot over time!")})

import plotly.plotly as py
import plotly.graph_objs as go
#Trying to make several plots on one line
trace0 = go.Scatter(x = x_range, y = win_plot, mode = 'lines', name = 'Win Streak')
trace3 = go.Scatter(x = x_range,y = lss_plot, mode = 'lines', name = 'Loss Streak')
trace1 = go.Scatter(x = x_range, y = psh_plot, mode = 'markers', name = 'Push')
trace2 = go.Scatter(x = x_range, y = plot_bank, mode = 'lines+markers', name = 'Bank ')
data = [trace0, trace1, trace2, trace3]
# Plot and embed in ipython notebook!
#plotly.offline.init_notebook_mode()
#py.plot(data, filename='line-mode')
plotly.offline.plot(data, filename='line-mode.html')

# Pie Chart for Win vs Loss vs Push
fig = {'data': [{'labels': ['Dealer', 'Player', 'Push'],'values': [dl_win, pl_win, ps_win],'type': 'pie'}],'layout': {'title': 'Dealer vs Player vs Push'}}
plotly.offline.plot(fig)
#py.iplot(fig)


### Example of calculating a sum
'''
tot = 0
for x in range(0,len(hand))
    tot+=int(hand[x])
print sum

'''

### How to take one more card and append:
'''
hit = random.sample(DECK,1)
# insert function to remove card right here <<<
# function below appends
hand+=hit
'''
