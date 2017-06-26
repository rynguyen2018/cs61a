"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################
def roll_dice(num_rolls, dice=six_sided):

    total=0
    pigout= False 
    for i in range(num_rolls):
        outcome= dice()
        #print("Outcome ", str(i), ":", str(outcome))
        if outcome ==1:
            pigout=True 
            total=1
        elif pigout==False:
            total+=outcome 
        #
        print("Outcome ", str(i), ":", str(outcome))    
    return total

def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    "*** REPLACE THIS LINE ***"
    if opponent_score< 10 : 
        score = opponent_score+1
    else: 
        one_digit= opponent_score//10
        tens_digit= opponent_score%10 
        score= max(one_digit,tens_digit) +1 
    return score 


# Write your prime functions here!

def isPrime(score):
    n=2 
    if score ==1: 
        return False
    while n*n<= score: 
        if score%n ==0: 
            return False 
        n+=1      
    return True 



def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime rule.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    "*** REPLACE THIS LINE ***"
    score=0

    if num_rolls !=0 : 
        score =roll_dice(num_rolls,dice)
        if isPrime(score)==True: 
            score +=1 
            while isPrime(score) ==False: 
                score+=1 
    else: 
        score= free_bacon(opponent_score)

        if isPrime(score)==True: 
            score +=1 
            while(isPrime(score)==False): 
                    score+=1 
    return score  



def select_dice(dice_swapped):

    """Return a six-sided dice unless four-sided dice have been swapped in due
    to Perfect Piggy. DICE_SWAPPED is True if and only if four-sided dice are in
    play.
    """
    # BEGIN PROBLEM 3
    "*** REPLACE THIS LINE ***"
    #dice_swapped= is_perfect_piggy(turn_score)
    if dice_swapped:
        return four_sided
    else: 
        return six_sided  
    # END PROBLEM 3


# Write additional helper functions here!


def is_perfect_piggy(turn_score):
    """Returns whether the Perfect Piggy dice-swapping rule should occur."""
    # BEGIN PROBLEM 4
    if ((turn_score**(1/2)== int(turn_score**(1/2)) or turn_score**(1/3)== int(turn_score**(1/3))) and turn_score!=1 ):
        return True
    else:
        return False 



def is_swap(score0, score1):
    """Returns whether one of the scores is double the other."""
    # BEGIN PROBLEM 5
    "*** REPLACE THIS LINE ***"
    if (score0 ==0 or score1==0):
        return False
    if (score0/score1== 0.5) or (score1/score0==0.5): 
        return True 
    else:
        return False 


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0:     The starting score for Player 0
    score1:     The starting score for Player 1
    """
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False # Whether 4-sided dice have been swapped for 6-sided
    current_dice= six_sided
    # BEGIN PROBLEM 6
    "*** REPLACE THIS LINE ***"
    count=1
    hasBeenSwapped= False
    taketurncount=0
    while score0<goal or score1<goal:
        addition0= take_turn(strategy0(score0,score1), score1,dice=current_dice)
        taketurncount+=1
        score0+=addition0
        print("Turn: " + str(count))
        print("We added ", str(addition0), "to score 0")
        
        print("score0: ", str(score0))
        print("score1: ", str(score1))
        
        if is_swap(score0,score1) and hasBeenSwapped==False:
            score0,score1= score1, score0 
            if score0>=goal or score1>=goal:
                return score0, score1 
            print("hasBeenSwapped state after score 0 swap : ", hasBeenSwapped)
        else: 
            hasBeenSwapped=False 

        if score0>=goal: 
            return score0, score1        
        if is_perfect_piggy(addition0):
            print("dice swap occured because of score 0")
            dice_swapped= not dice_swapped
            current_dice= select_dice(dice_swapped)
        addition1= take_turn(strategy1(score1,score0), score0, dice= current_dice)
        score1+=addition1
        print("We added ", str(addition1), "to score 1")
        print("score0: ", str(score0))
        print("score1: ", str(score1))
        if is_swap(score0,score1) and hasBeenSwapped==False:
            score0,score1= score1, score0
            hasBeenSwapped=True
            if score0>=goal or score1>=goal:
                return score0, score1 
            print("hasBeenSwapped state after score 1 swap: ", hasBeenSwapped)
        else:  
            hasBeenSwapped=False 
        if score1>=goal:
            return score0,score1
        if is_perfect_piggy(addition1):
            print("dice swap occured because of score 1")
            dice_swapped=True 
            current_dice= select_dice(dice_swapped)
        input("press Enter to continue")
        taketurncount+=1
        count+=1
        print("Take Turn count= 2: ",str(taketurncount==2))
        taketurncount=0
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments (the
    current player's score, and the opponent's score), and returns a number of
    dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert 0 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the strategy
    returns a valid input. Use `check_strategy_roll` to raise an error with a
    helpful message if the strategy returns an invalid output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 7
    "*** REPLACE THIS LINE ***"
    # END PROBLEM 7


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.0
    """
    # BEGIN PROBLEM 8
    "*** REPLACE THIS LINE ***"
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** REPLACE THIS LINE ***"
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points, and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 10
    "*** REPLACE THIS LINE ***"
    return 4  # Replace this statement
    # END PROBLEM 10
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 11
    "*** REPLACE THIS LINE ***"
    return 4  # Replace this statement
    # END PROBLEM 11
check_strategy(swap_strategy)



def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 11
    "*** REPLACE THIS LINE ***"
    return 4  # Replace this statement
    # END PROBLEM 11
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()