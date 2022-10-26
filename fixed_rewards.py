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
purchases = 1000
exchanges = 100
auctions = 1000

popularity = []

def rand_float_range(start, end):
    return random() * (end - start) + start

for i in range(athletes):
    popularity.append(rand_float_range(0,1))

def func_purchase_reward():
    '''create a list to store the reward each athlete receives'''
    rewards = []
    for i in range(athletes):
        rewards.append(0)  #initialize rewards to 0
    '''
    randomly generate an index from 0 to number of athletes for purchase
    increment the reward by 0.1 * purchase price for the index
    '''
    for i in range(purchases):
        idx = randrange(athletes)
        rewards[idx] += purchase_price * athlete_reward_percent
    return rewards

def func_purchase_reward_vary_price():
    '''create a list to store the reward each athlete receives'''
    rewards = []
    purchase_price = []
    for i in range(athletes):
        rewards.append(0)  #initialize rewards to 0
        purchase_price.append(rand_float_range(0.00001, 0.1)) # each athlete has a different purchase price
    for i in range(purchases):
        idx = randrange(athletes)
        rewards[idx] += purchase_price[idx] * athlete_reward_percent
    return rewards

def func_exchange_reward_betn_2athletes():
    ex_rewards = []
    for i in range(athletes):
        ex_rewards.append(0)   
    #when both exchange their cards
    for i in range(exchanges):
        exchange_price = rand_float_range(0.00001, 0.1) # if 0, then no price and no rewards
        idx = sample(range(athletes), 2)
        ex_rewards[idx[0]] += exchange_price * athlete_reward_percent/2
        ex_rewards[idx[1]] += exchange_price * athlete_reward_percent/2   
    return ex_rewards

def func_exchange_reward_1athlete():
    ex_rewards = []
    for i in range(athletes):
        ex_rewards.append(0) 
    #when both exchange their cards
    for i in range(exchanges):
        exchange_price = rand_float_range(0.00001, 0.1) # if 0, then no price and no rewards
        idx = randrange(athletes)
        ex_rewards[idx] += exchange_price * athlete_reward_percent
    return ex_rewards

def func_auction():
    au_rewards = []
    for i in range(athletes):
        au_rewards.append(0)
    for i in range(auctions):
        winning_bid_price = rand_float_range(0.00001, 0.1)
        idx = randrange(athletes)
        au_rewards[idx] += winning_bid_price * athlete_reward_percent
    return au_rewards

with open('rewards_on_purchase.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(str(athletes) +' athletes, ' + str(purchases) + ' purchases')
    for i in range(100):
        p_rewards = func_purchase_reward()
        spamwriter.writerow(p_rewards)
    spamwriter.writerow('')

    spamwriter.writerow(str(athletes) +' athletes, ' + str(purchases) + ' purchases varying purchase price')
    for i in range(100):
        vp_rewards = func_purchase_reward_vary_price()
        spamwriter.writerow(vp_rewards)
    spamwriter.writerow('')

with open('rewards_on_exchange.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(str(athletes) +' athletes, ' + str(exchanges) + ' exchanges both athletes')
    for i in range(100):
        ex_rewards2 = func_exchange_reward_betn_2athletes()
        spamwriter.writerow(ex_rewards2)    
    spamwriter.writerow('')

    spamwriter.writerow(str(athletes) +' athletes, ' + str(exchanges) + ' exchanges one athlete')
    for i in range(100):
        ex_rewards1 = func_exchange_reward_1athlete()
        spamwriter.writerow(ex_rewards1)    
    spamwriter.writerow('')

with open('rewards_on_auction.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(str(athletes) +' athletes, ' + str(auctions))
    for i in range(100):
        au_rewards = func_auction()
        spamwriter.writerow(au_rewards)   
    spamwriter.writerow('')