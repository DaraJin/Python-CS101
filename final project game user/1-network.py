# network={'connection':{'John':['a','b','c']},'game':{'John':['A','B','C']}}
# print(network['connection']['John'][2])   #data structure


def create_data_structure(string_input):
    network={'connection':{},'game':{}}

    while string_input:
        dot = -1
        space = string_input.find(" ")
        name=string_input[dot+1:space]

        connect_place=string_input.find("connected to ")+len("connected to ") #此处有是否要+1的问题
        dot1=string_input.find('.')
        namelist=string_input[connect_place:dot1]
        network['connection'][name] = namelist.split(', ')

        dot2=string_input.find('.',dot1+1)
        game_place = string_input.find("play ",dot1+1) + len("play ")  # 此处有是否要+1的问题
        gamelist = string_input[game_place:dot2]
        network['game'][name] = gamelist.split(', ')

        string_input=string_input[dot2+1:]
        space=string_input.find(' ',dot2+1)

    return network

example_input = "John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."


def get_connections(network, user):
    if user not in network['connection']:
        return None
    return network['connection'][user]

def get_games_liked(network, user):
    if user not in network['game']:
        return None
    return network['game'][user]

def add_connection(network, user_A, user_B):
    if user_A not in network['connection']:
        return False
    if user_B not in network['connection']:
        return False
    if user_A not in network['connection'][user_B]:
        network['connection'][user_B].append(user_A)
    return network

def add_new_user(network, user, games):
    if user not in network['connection']:
        network['connection'][user]=[]
    if user not in network['game']:
        network['game'][user]=games
    return network

def get_secondary_connections(network, user):
    if user not in network['connection']:
        return None
    rst=[]
    list=network['connection'][user]
    if not list:
        return rst
    for i in list:
        if i in network['connection']:
            for e in network['connection'][i]:
                if e not in rst:
                    rst.append(e)
    return rst

def count_common_connections(network, user_A, user_B):
    a=network["connection"][user_A]
    b=network["connection"][user_B]
    count=0
    for i in a:
        for e in b:
            if i==e:
                count=count+1
    return count

def find_path_to_friend(network, user_A, user_B,visited=None):
    if visited is None:
        visited = []
    if user_A in network['connection'] and user_B in network['connection']:
        visited.append(user_A)
        if user_B in network['connection'][user_A]:
            return [user_A]+[user_B]
        for node in network['connection'][user_A]:
            if node not in visited:
                next= find_path_to_friend(network, node, user_B,visited)
                if next:
                    return [user_A]+ next
    # your RECURSIVE solution here!
    return None

def friend_play_game(network,game):
    for i in network['connection']:
        for e in network["connection"][i]:
            if i in network["connection"][e]:
                if network['game'][i]==game and network['game'][e]:
                    return i,e

# -----------------------------------------------------------------------------
# compute_user_popularity(network):
#   Roughly computes popularity of each user in gamer network based on two main
#   factors:
#       1)  The number of users that are connected to him/her is positively
#           correlated to his/her popularity.
#       2)  The popularity of the users who are connected to him/her is positively
#           correlated to his/her popularity.
#
# Arguments:
#   network: the gamer network data structure.
#
# Return:
#   A dictionary showing popularity of each user in the gamer network.


def compute_user_popularity(network):
    #no damping factor needed
    nloops = 10
    ranks = {}
    nusers = len(network['connection'])
    for user in network:
            ranks[user] = 1.0 / nusers

    for i in range(0, nloops):
        newpopularities = {}
        for user in network['connection']:
            newpopularity = 1/ nusers
            for friend in network['connection']:
                if friend in network['connection'][user]:
                    newpopularity = newpopularity + (ranks[friend] / len(network['connection'][friend]))
            newpopularities[user] = newpopularity
        ranks = newpopularities
    return ranks

    # for i in range(0, nloops):
    #     new_popularity = {}
    #     for user in network['connection']:
    #         popu = 0
    #         for user2 in network['connection']:
    #             if user in network['connection'][user2]:
    #                 popu = popu + popularity['connection'][user2] / len(network['connection'][user2])
    #         new_popularity[user] = popu
    #     popularity = new_popularity
    # return popularity



net = create_data_structure(example_input)
print (net['connection'])
print (compute_user_popularity(net))
