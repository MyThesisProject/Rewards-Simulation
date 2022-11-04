'''
popularity index of athletes
secondary market based on popularity
secondary market based on log of popularity
'''

import csv
from random import sample, randrange, random

base_price = 0.001 #ETH
varPrice = 0.1 #ETH

k = 1

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
        rewards.append(0)
    for j in range(purchases):
        #price is fixed
        idx = randrange(0,athletes)
        rewards[idx] += base_price * athlete_reward_percent # number of purchases is random
    return rewards

def func_exchange_reward_betn_2athletes():
    ex_rewards = []
    for i in range(athletes):
        ex_rewards.append(0)
    for m in range(exchanges):
        i = randrange(0,athletes)
        j = randrange(0,athletes)
        while(j == i):
            j = randrange(0,athletes)
        sale_price1 = base_price + rand_float_range(0, varPrice * pow(popularity[i],k))
        sale_price2 = base_price + rand_float_range(0, varPrice * pow(popularity[j],k))
        exchange_price = abs(sale_price1 - sale_price2)   #the more difference in popularity, the more price to pay for higher popular celeb
        totalPopularity = popularity[i] + popularity[j]   #to find the fraction of exchange price that should go to each celeb
        ex_rewards[i] += exchange_price * popularity[i]/totalPopularity * athlete_reward_percent
        ex_rewards[j] += exchange_price * popularity[j]/totalPopularity * athlete_reward_percent   
    return ex_rewards

def func_exchange_reward_1athlete():
    ex_rewards = []
    for i in range(athletes):
        ex_rewards.append(0) 
    for j in range(exchanges):
        i = randrange(0,athletes)
        exchange_price = base_price + rand_float_range(0, varPrice * pow(popularity[i],k))
        ex_rewards[i] += exchange_price * athlete_reward_percent
    return ex_rewards


def func_auction():
    au_rewards = []
    for i in range(athletes):
        au_rewards.append(0)
    #when one auction its card, it could sell card of less popular athlete as well on a low price to get rid of it or a highly popular athlete with a higher price
    #hence, number of auctions for a given athlete may not be proportional to the popularity of the athlete
    for i in range(auctions):
        idx = randrange(athletes)
        winning_bid_price = base_price + rand_float_range(0, varPrice * pow(popularity[idx],k))
        au_rewards[idx] += winning_bid_price * athlete_reward_percent
    return au_rewards

with open('2.rewards_on_purchase.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(str(athletes) +' athletes, ' + str(purchases) + ' purchases')
    for i in range(100):
        p_rewards = func_purchase_reward()
        spamwriter.writerow(p_rewards)
    spamwriter.writerow('')

with open('2.rewards_on_exchange.csv', 'a') as csvfile:
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

with open('2.rewards_on_auction.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(str(athletes) +' athletes, ' + str(auctions))
    for i in range(100):
        au_rewards = func_auction()
        spamwriter.writerow(au_rewards)   
    spamwriter.writerow('')