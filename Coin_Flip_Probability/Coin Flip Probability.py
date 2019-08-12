# Author:   Ernest J. Quant
# Classes:  coin, coin_flip
# Imports:  scipy, matplotlib
# Purpose:  Create a class for a coin object that is initialized as an 
#           unflipped coin that can then be flipped and will have a True
#           boolean value for either heads or tails. 
#           Create a class that gets passed a coin object and can flip a coin
#           however many times the user would like the coin to flip. It is 
#           initialized by default with zero head or tail values but can be
#           initialized with a specified amount of either. After the desired
#           flips take place, when the specified amount is passed to the function,
#           the number of each result is recorded and the probabilities for
#           the coin to land on heads or tails can be found using this class.


from scipy.stats.distributions import t as tdist
from matplotlib import pyplot as plt
from random import randint
from numpy import sqrt


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



# Class that gets passed a coin, a number of flips and has methods to return
# the probabilities for heads and tails, and can print all the stats. 
class coin_flip:

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
    


# This class gets passed p_hat which is the number of successes over trials,
# an int for the desired confidence interval and the number of trials performed.
class probability_interval:

    def __init__(self,p_hat,confidence_interval,trials):
        self.trials = trials
        self.p_hat = p_hat
        self.confidence_interval = confidence_interval

    def get_interval(self):
        self.degrees_of_freedom = self.trials - 1
        half_alpha = (1 - (self.confidence_interval * 10 **(-2))) / 2
        t_val = tdist.ppf(1-half_alpha,self.degrees_of_freedom)
        error_val = (sqrt((self.p_hat * (1 - self.p_hat)) / self.trials))

        interval = (self.p_hat-(t_val*error_val),self.p_hat+(t_val*error_val))
        return interval

    def get_confidence_interval(self):
        return self.confidence_interval

    def get_degrees_freedom(self):
        return self.degrees_of_freedom

    def print_interval(self):
        print(self.get_interval())







penny = coin()

test1 = coin_flip(penny)
test1.flip_comp(50)
test1.print_all_stats()

prob_test = probability_interval(test1.head_probability(),99,test1.get_flips())
prob_test.print_interval()




# Matplotlib Graph
x1 = test1.get_heads()
x2 = test1.get_tails()
y = test1.get_flips()

x_categories = [x1,x2]
x_labels = ["Heads","Tails"]

plt.subplot(1,2,1)
plt.pie(x_categories,
        labels=x_labels,
        startangle=90,
        autopct="%1.1f%%",
        shadow=True,
        explode=(.05,.05))
plt.title("Results of {} Coin Flips\nHeads or Tails".format(test1.get_flips()))


x3 = 2
y3 = 5
plt.subplot(1,2,2)


dy=.8
plt.errorbar(x3,y3,yerr=dy)
plt.ylabel('y')
plt.xlabel('x')


plt.tight_layout()
plt.show()
