'''
popularity index of athletes
secondary market based on popularity
secondary market based on log of popularity
'''

import csv
from random import sample, randrange, random

purchase_price = 0.001  #ETH

#percentage of rewards
athlete_reward_percent = 0.1
owner_reward_percent = 0.05

#number of total counts
athletes = 500
purchases = 10000
exchanges = 10000
auctions = 10000

popularity = []

def rand_float_range(start, end):
    return random() * (end - start) + start

for i in range(athletes):
    popularity.append(rand_float_range(0,1))

def func_purchase_reward():
    '''create a list to store the reward each athlete receives'''
    rewards = []
    for i in range(athletes):
        reward = purchase_price * athlete_reward_percent * (popularity[i] * purchases)
        rewards.append(reward)  
    return rewards

def func_purchase_reward_vary_price():
    '''create a list to store the reward each athlete receives'''
    rewards = []
    for i in range(athletes):
        price = purchase_price + 0.001 * popularity[i]
        reward = price * athlete_reward_percent * (popularity[i] * purchases)
        rewards.append(reward)
    return rewards

def func_exchange_reward_betn_2athletes():
    ex_rewards = []
    for i in range(athletes):
        ex_rewards.append(0)
    for i in range(exchanges):
        idx = sample(range(athletes), 2)
        diffPopularity = abs(popularity[idx[0]] - popularity[idx[1]])   #the more difference in popularity, the more price to pay for higher popular celeb
        exchange_price = rand_float_range(0.001 * diffPopularity, 0.01 * diffPopularity) # more difference implies exchange price range is larger and shifts to right
        totalPopularity = popularity[idx[0]] + popularity[idx[1]]   #to find the fraction of exchange price that should go to each celeb
        ex_rewards[idx[0]] += exchange_price * popularity[idx[0]]/totalPopularity * athlete_reward_percent
        ex_rewards[idx[1]] += exchange_price * popularity[idx[1]]/totalPopularity * athlete_reward_percent   
    return ex_rewards

def func_exchange_reward_1athlete():
    ex_rewards = []
    for i in range(athletes):
        ex_rewards.append(0) 
    #when one exchanges its card, it could sell card of less popular athlete as well on a low price to get rid of it or a highly popular athlete with a higher price
    for i in range(exchanges):
        idx = randrange(athletes)
        exchange_price = 0.001 + rand_float_range(0.001 * popularity[idx], 0.1 * popularity[idx])
        ex_rewards[idx] += exchange_price * athlete_reward_percent
    return ex_rewards


def func_auction():
    au_rewards = []
    for i in range(athletes):
        au_rewards.append(0)
        # more popularity more auctions
        for j in range(int(auctions * popularity[i])):
            winning_bid_price = 0.001 + rand_float_range(0.001 * popularity[i], 0.1 * popularity[i])
            au_rewards[i] += winning_bid_price * athlete_reward_percent
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