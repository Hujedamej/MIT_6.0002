###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, t_weight):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    # by starting with the biggest egg ensures that the first solution in memo is the fastest
    sorted_egg_weights = egg_weights[::-1]

    def make_weight(sew, target_weight, memo={}):
        if target_weight in memo:
            return memo[target_weight]

        if target_weight in sew:
            memo[target_weight] = 1
            return 1        

        for egg in sew:
            if target_weight - egg > 0:
                memo[target_weight - egg] = make_weight(sew, target_weight - egg, memo)
                if memo[target_weight - egg] is not None:
                    return memo[target_weight - egg] + 1

    return make_weight(sorted_egg_weights, t_weight)

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
    egg_weight = (15, 20)
    n = 30
    print("Egg weights = (15, 20)")
    print("n = 30")
    print("Expected ouput: 2 (2 * 15)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()