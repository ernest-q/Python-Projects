from random import randint


# Coin object that starts unflipped, when it is unflipped it is neither on
# heads nor tails. Once the coin is flipped it is randomly on heads on tails.s
class coin:

    def __init__(self,heads=False,tails=False):
        self.heads = heads
        self.tails = tails

    def flip(self):
        flip_result = randint(1,2)
        if flip_result == 1:
            self.heads = True
            self.tails = False
        else:
            self.tails = True
            self.heads = False

    def is_heads(self):
        if self.heads == False and self.tails == False:
            print("Coin hasn't been flipped yet")
        elif self.heads:
            return True
        else:
            return False

    def is_tails(self):
        if self.heads == False and self.tails == False:
            print("Coin hasn't been flipped yet")
        elif self.tails:
            return True
        else:
            return False

    def print_face(self):
        if self.heads == False and self.tails == False:
            return "hasn't flipped"
        elif self.heads:
            return "heads"
        elif self.tails:
            return "tails"

# Class that gets passed a coin, a number of flips and has methods to return
# the probabilities for heads and tails, and can print all the stats. 
class coin_flip_test:

    def __init__(self,coin,number_of_heads=0,number_of_tails=0):
        self.number_of_heads = number_of_heads
        self.number_of_tails = number_of_tails
        self.coin = coin

    def flip_comp(self,flips):
        self.flips = flips
        for i in range(self.flips):
            self.coin.flip()
            if self.coin.is_heads():
                self.number_of_heads += 1
            elif self.coin.is_tails():
                self.number_of_tails += 1

    def get_heads(self):
        return self.number_of_heads

    def get_tails(self):
        return self.number_of_tails

    def get_flips(self):
        return self.flips

    def head_probability(self):
        head_prob = (self.number_of_heads / self.flips)
        return head_prob

    def tail_probability(self):
        tail_prob = (self.number_of_tails / self.flips)
        return tail_prob

    def print_all_stats(self):
        print("Heads: {}".format(self.number_of_heads))
        print("Tails: {}".format(self.number_of_tails))
        print("Flips: {}".format(self.flips))
        print("Head Probability: {}".format(self.head_probability()))
        print("Tail Probability: {}".format(self.tail_probability()))
    

