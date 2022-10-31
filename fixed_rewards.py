'''
popularity index of athletes
secondary market based on popularity
secondary market based on log of popularity
'''

import csv
from random import sample, randrange, random

base_price = 0.001 #ETH
k = 3

#percentage of rewards
athlete_reward_percent = 0.1
owner_reward_percent = 0.05

#number of total counts
m = 100
athletes = 5 * m
purchases = 100 * m
exchanges = 100 * m
auctions = 100 * m

popularity = []

def rand_float_range(start, end):
    return random() * (end - start) + start

for i in range(athletes):
    popularity.append(rand_float_range(0,1))

def func_purchase_reward():
    rewards = []
    for i in range(athletes):
        #price is fixed
        reward = base_price * athlete_reward_percent * (popularity[i] * purchases) # number of purchases is proportional to popularity
        rewards.append(reward)  
    return rewards

def func_purchase_reward_vary_price():
    '''create a list to store the reward each athlete receives'''
    rewards = []
    for i in range(athletes):
        price = base_price + base_price * pow(popularity[i],k)  #price is proportional to popularity
        reward = price * athlete_reward_percent * (popularity[i] * purchases)   #number of purchase is proportional to popularity
        rewards.append(reward)
    return rewards

def func_exchange_reward_betn_2athletes():
    ex_rewards = []
    for i in range(athletes):
        ex_rewards.append(0)
    for i in range(athletes):
        for k in range(int(exchanges * popularity[i])):
            j = randrange(0,athletes)
            while(j == i):
                j = randrange(0,athletes)
            diffPopularity = abs(popularity[i] - popularity[j])   #the more difference in popularity, the more price to pay for higher popular celeb
            exchange_price = rand_float_range(0.001 * pow(diffPopularity,k), 0.01 * pow(diffPopularity,k)) # more difference implies exchange price range is larger and shifts to right
            totalPopularity = popularity[i] + popularity[j]   #to find the fraction of exchange price that should go to each celeb
            ex_rewards[i] += exchange_price * popularity[i]/totalPopularity * athlete_reward_percent
            ex_rewards[j] += exchange_price * popularity[j]/totalPopularity * athlete_reward_percent   
    return ex_rewards

def func_auction():
    ex_rewards = []
    for i in range(athletes):
        ex_rewards.append(0) 
        #more popularity, more exchanges
        for j in range(int(exchanges * popularity[i])):
            exchange_price = 0.001 + rand_float_range(0.001 * pow(popularity[i],k), 0.1 * pow(popularity[i],k))
            ex_rewards[i] += exchange_price * athlete_reward_percent

    return ex_rewards


def func_exchange_reward_1athlete():
    au_rewards = []
    for i in range(athletes):
        au_rewards.append(0)
    #when one auction its card, it could sell card of less popular athlete as well on a low price to get rid of it or a highly popular athlete with a higher price
    #hence, number of auctions for a given athlete may not be proportional to the popularity of the athlete
    for i in range(auctions):
        idx = randrange(athletes)
        winning_bid_price = 0.001 + rand_float_range(0.001 * pow(popularity[idx],k), 0.1 * pow(popularity[idx],k))
        au_rewards[idx] += winning_bid_price * athlete_reward_percent
    return au_rewards

with open('2.rewards_on_purchase.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(str(athletes) +' athletes, ' + str(purchases) + ' purchases')
    # for i in range(100):
    p_rewards = func_purchase_reward()
    spamwriter.writerow(p_rewards)
    spamwriter.writerow('')

    spamwriter.writerow(str(athletes) +' athletes, ' + str(purchases) + ' purchases varying purchase price')
    # for i in range(100):
    vp_rewards = func_purchase_reward_vary_price()
    spamwriter.writerow(vp_rewards)
    spamwriter.writerow('')

with open('2.rewards_on_exchange.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(str(athletes) +' athletes, ' + str(exchanges) + ' exchanges both athletes')
    # for i in range(100):
    ex_rewards2 = func_exchange_reward_betn_2athletes()
    spamwriter.writerow(ex_rewards2)    
    spamwriter.writerow('')

    spamwriter.writerow(str(athletes) +' athletes, ' + str(exchanges) + ' exchanges one athlete')
    # for i in range(100):
    ex_rewards1 = func_exchange_reward_1athlete()
    spamwriter.writerow(ex_rewards1)    
    spamwriter.writerow('')

with open('2.rewards_on_auction.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(str(athletes) +' athletes, ' + str(auctions))
    # for i in range(100):
    au_rewards = func_auction()
    spamwriter.writerow(au_rewards)   
    spamwriter.writerow('')