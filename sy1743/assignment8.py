from Investment_account import Investment_account
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sys
# DS-GA 1007
# HW8
# Author: Sida Ye

try:
    """
    Main program runs my program with positions set to [1, 10, 100, 1000] and num_trials set to 10000.
    It will save four histogram plots and a results.txt file. 
    """
    while True:
        x = raw_input('Do simulation? Please enter Yes or No?\n')
        if x == 'Yes':           
            positions = [1, 10, 100, 1000]
            ntrials = 10000
            invest_amount = Investment_account(1000)                                # Create an instance with amount 1000
            results = pd.DataFrame(columns=['position', 'mean', 'std'])             # Store mean and std for differnet position
            i = 0
            for position in positions:
                print 'Generating histogram with position = {} ...'.format(position)
                daily_ret = invest_amount.invest_sim(position, ntrials)
                results.loc[i] = [position, np.mean(daily_ret), np.std(daily_ret)]
                i = i + 1

                p = plt.figure()
                plt.hist(daily_ret, 100, range=[-1,1], color='black')               # plot histogram
                plt.title('Histogram of Daily Return with position {}'.format(position))
                plt.xlabel('Daily return')
                p.savefig('histogram_{}_pos.pdf'.format(str(position).zfill(4)))


            print 'Saved results file and histogram plots under current dictory'
            results.to_csv('result.txt', sep=',')
        elif x == 'No':
            sys.exit()
        break
        
except KeyboardInterrupt, ValueError:
    print "\n Interrupted!"
except ArithmeticError, OverflowError:
    print "\n Math Error"
except ZeroDivisionError:
    print "\n Math Error"
except TypeError:
    print "\n Type Wrong!"
except EOFError:
    print "\n Interrupted!"

