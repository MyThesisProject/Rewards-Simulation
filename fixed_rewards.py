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
m = 10
athletes = 5 * m
purchases = 1000 * m
exchanges = 1000 * m
auctions = 1000 * m

popularity = []
rewards = []

def rand_float_range(start, end):
    return random() * (end - start) + start

for i in range(athletes):
    popularity.append(rand_float_range(0,1))

popularity.sort()

def func_purchase_reward():
    for i in range(athletes):
        rewards.append(0)
    for j in range(purchases):
        #price is fixed
        idx = randrange(0,athletes)
        rewards[idx] += base_price * athlete_reward_percent

def func_exchange_reward_betn_2athletes():
    for m in range(exchanges):
        i = randrange(0,athletes)
        j = randrange(0,athletes)
        while(j == i):
            j = randrange(0,athletes)
        sale_price1 = base_price + rand_float_range(0, varPrice * pow(popularity[i],k))
        sale_price2 = base_price + rand_float_range(0, varPrice * pow(popularity[j],k))
        exchange_price = abs(sale_price1 - sale_price2)   #the more difference in popularity, the more price to pay for higher popular celeb
        totalPopularity = popularity[i] + popularity[j]   #to find the fraction of exchange price that should go to each celeb
        rewards[i] += exchange_price * popularity[i]/totalPopularity * athlete_reward_percent
        rewards[j] += exchange_price * popularity[j]/totalPopularity * athlete_reward_percent   

def func_exchange_reward_1athlete():
    for j in range(exchanges):
        i = randrange(0,athletes)
        exchange_price = base_price + rand_float_range(0, varPrice * pow(popularity[i],k))
        rewards[i] += exchange_price * athlete_reward_percent


def func_auction():
    #when one auction its card, it could sell card of less popular athlete as well on a low price to get rid of it or a highly popular athlete with a higher price
    #hence, number of auctions for a given athlete may not be proportional to the popularity of the athlete
    for i in range(auctions):
        idx = randrange(athletes)
        winning_bid_price = base_price + rand_float_range(0, varPrice * pow(popularity[idx],k))
        rewards[idx] += winning_bid_price * athlete_reward_percent

with open('total_rewards.csv', 'a') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in range(100):
        rewards = []
        func_purchase_reward()
        func_exchange_reward_betn_2athletes()
        func_exchange_reward_1athlete()
        func_auction()
        spamwriter.writerow(rewards)
    spamwriter.writerow('')