'''
Created on Aug 12, 2019

@author: mac
'''

PERCENTAGES = [1, 2/3, 0.618, 0.5,0.382, 1/3, 0]
def CalcPercentages(low, high):
    
    for percentage in PERCENTAGES:
        data = 1.0*percentage*high + (1.0-percentage)*low
        print("位置:%04f         值:%04f"% (percentage, data))


if __name__ == '__main__':
    CalcPercentages(32.84, 42.08)