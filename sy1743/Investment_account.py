from __future__ import division
import numpy as np
import random
# DS-GA 1007
# HW8
# Author: Sida Ye



class Investment_account(object):

    """
    Class Investment_account takes input purchase_value. It also has
    a method invest_sim to simulate the daily return based on position
    and number of trials.
    """

    def __init__(self, purchase_value):
        if purchase_value >= 0:
            self.purchase_value = purchase_value
        else:
            raise ValueError('Value must be greater than 0!')


    def invest_sim(self, position, num_trials):
        position_value = self.purchase_value / position 
        cumu_ret = []
        for trial in range(num_trials):
            gain = sum(np.random.uniform(0, 1, size=position) > 0.49)   # number of random variable which is greater than 0.49
            cumu_ret.append(position_value * gain * 2)

        daily_ret = [(ret/self.purchase_value)-1 for ret in cumu_ret] # calculate the daily return
        
        return daily_ret


