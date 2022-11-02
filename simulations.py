import random
import time


def SIMULATION_01(lb, ub):
    """
    Takes a uniformly random amount of time to complete between :param lb: and :param ub:
    """
    t = random.randint(lb, ub)
    time.sleep(t)
    return 0


def SIMULATION_02(lb, ub, alpha=2, beta=5):
    """
    Takes the Beta [betavariate()] distribution of :param alpha: and :param beta:.
    Then takes the proportion between :param lb: and :param ub: to complete the simualtion
    """
    p = random.betavariate(alpha, beta)
    t = round(lb + ((ub - lb) * p))
    time.sleep(t)
    return 0
