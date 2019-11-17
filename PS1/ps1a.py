###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import re

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    with open(filename, 'r') as f:
        return dict(re.findall(r'([A-Z].*[a-z]),(\d+)', f.read()))

# Problem 2
def greedy_cow_transport(cows, limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    trip_list = []
    cds = dict(sorted(cows.items(), key=lambda x: x[1], reverse=True))
    while len(cds) > 0:
        new_trip = []
        limit_left = limit
        for cow in cds.copy():
            if int(cds[cow]) <= limit_left:
                limit_left -= int(cds[cow])
                new_trip.append(cow)
                cds.pop(cow)
        trip_list.append(new_trip)
    return trip_list

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)

    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    def sub_part_possible(spp_part):
        """
        checks if a list of cows fits in one spaceship
        
        input: list with cows from the cows dictionary
        
        output: true if weight of cows is <= 10
        
        """
        sum_weight = 0
        for cow in spp_part:
            if sum_weight + int(cows[cow]) <= 10:
                sum_weight += int(cows[cow])
            else:
                return False
        return True

    def part_possible(pp_part):
        for sub_part in pp_part:
            if not sub_part_possible(sub_part):
                return False
        return True

    c = []
    len_part = 1000
    cow_part = get_partitions(cows.keys())
    for part in cow_part:
        
        if len(c) > 0 and len(part) >= len(c):
            break
        else:
            if part_possible(part):
                if len(part) < len_part:
                    len_part = len(part)
                c = part
    return c


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.

    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    start_greedy = time.time()
    print(greedy_cow_transport(load_cows('ps1_cow_data.txt')))
    end_greedy = time.time()
    print('Greedy takes:', '{0:.10f}'.format(end_greedy - start_greedy))
    start_bf = time.time()
    print(brute_force_cow_transport(load_cows('ps1_cow_data.txt')))
    end_bf = time.time()
    print('Brute Force takes:', '{0:.10f}'.format(end_bf - start_bf))

if __name__ == '__main__':
    compare_cow_transport_algorithms()
