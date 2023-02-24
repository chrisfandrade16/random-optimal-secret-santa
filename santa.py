from math import floor, ceil
from random import randint

# Using a random number of directed cyclic graphs
# (NodeFrom == Giver, NodeTo == Receiver)
# with a random number of distributed players in each graph
# where each graph must contain a minimum of two nodes (players)

def santa(players_original):
    players = players_original[:]
    matchings = []

    minimum_number_of_cycles = 1
    maximum_number_of_cycles = floor(len(players) / 2)
    using_number_of_cycles = randint(minimum_number_of_cycles, maximum_number_of_cycles)

    for cycle_counter in range(using_number_of_cycles):
        maximum_number_of_cycles = floor(len(players) / 2)

        number_of_cycles_left = using_number_of_cycles - cycle_counter

        if(number_of_cycles_left == 1):
            minimum_number_of_players = len(players)
            maximum_number_of_players = len(players)
        else:
            minimum_number_of_players = 2
            maximum_number_of_players = ceil(len(players) / maximum_number_of_cycles) + (2 * (maximum_number_of_cycles - number_of_cycles_left))

        using_number_of_players = randint(minimum_number_of_players, maximum_number_of_players)

        for player_counter in range(using_number_of_players):
            receiver_index = randint(0, len(players) - 1)
            receiver = players.pop(receiver_index)

            if player_counter == 0:
                first_giver = receiver
            else:
                matchings.append([giver, receiver])

            giver = receiver

        # closing the cycle
        matchings.append([giver, first_giver])

    return matchings

# Test cases

all_players = []

minimum_number_of_players = 2
maximum_nunber_of_players = 12

for number_of_players in range(minimum_number_of_players, maximum_nunber_of_players + 1):
    players = []
    for player_counter in range(number_of_players):
       players.append(chr(ord('A') + player_counter))
    all_players.append(players)

for players in all_players:
    print('For ', len(players), ' number of players:')
    matchings = santa(players)
    print(matchings)

# Possible distributions of players in different graph sizes:

# 2 players:
# 1 graph -> 2 (MIN: 2, MAX: 2)

# 3 players:
# 1 graph -> 3 (MIN: 3, MAX: 3)

# 4 players:
# 2 graphs -> 2 2 (MIN: 2, MAX: 2)
# 1 graph -> 4 (MIN: 4, MAX: 4)

# 5 players:
# 2 graphs -> 3 2 (MIN: 2, MAX: 3)
# 1 graph -> 5 (MIN: 5, MAX: 5)

# 6 players:
# 3 graphs -> 2 2 2 (MIN: 2, MAX: 2)
# 2 graphs ->  3 3 or 4 2 (MIN: 2, MAX: 4)
# 1 graph -> 6 (MIN: 6, MAX: 6)

# 7 players:
# 3 graphs -> 3 2 2 (MIN: 2, MAX: 3)
# 2 graphs -> 4 3 or 5 2 (MIN: 2, MAX: 5)
# 1 graph -> 7 (MIN: 7, MAX: 7)

# 8 players:
# 4 graphs: 2 2 2 2 (MIN: 2, MAX: 2)
# 3 graphs: 3 3 2 or 2 2 4 (MIN: 2, MAX: 4)
# 2 graphs: 4 4 or 5 3 or 6 2 (MIN: 2, MAX: 6)
# 1 graph: 8 (MIN: 8, MAX: 8)

# 9 players:
# 4 graphs: 3 2 2 2 (MIN: 2, MAX: 3)
# 3 graphs: 3 3 3 or 2 3 4 or 2 2 5 (MIN: 2, MAX: 5)
# 2 graphs: 4 5 or 3 6 or 2 7 (MIN: 2, MAX: 7)
# 1 graph: 9 (MIN: 9, MAX: 9)

# 10 players:
# 5 graphs: 2 2 2 2 2 (MIN: 2, MAX: 2)
# 4 graphs: 4 2 2 2 or 3 3 2 2 (MIN: 2, MAX: 4)
# 3 graphs: 3 3 4 or 2 3 5 or 2 2 6 (MIN: 2, MAX: 6)
# 2 graphs: 4 6 or 3 7 or 2 8 (MIN: 2, MAX: 8)
# 1 graph: 10 (MIN: 10, MAX: 10)

# 11 players:
# 5 graphs: 3 2 2 2 2 (MIN: 2, MAX: 3)
# 4 graphs: 4 3 2 2 or 5 2 2 2 (MIN: 2, MAX: 5)
# 3 graphs: 3 4 4 or 3 3 5 or 2 4 5 or 2 3 6 or 7 2 2 (MIN: 2, MAX: 7)
# 2 graphs: 5 6 or 4 7 or 3 8 or 9 2 (MIN: 2, MAX: 9)
# 1 graph: 11 (MIN: 11, MAX: 11)