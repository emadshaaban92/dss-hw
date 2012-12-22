import numpy as np
import pandas as pd
import sys

infile = sys.argv[1]
payoff = sys.argv[2]
if payoff not in ("profit","cost") :
    print payoff,"isn't a vaild payoff option, please use profit or cost only"
    sys.exit()
df = pd.read_csv(infile)
if "Alternative" not in df.columns :
    print "Can't find Alternative Column in ", infile, ", Please use a valid input file."
    sys.exit()
data = df.set_index("Alternative")
print data

print "\n\nChoose method : "
print "Optimistic     : write 1"
print "Pessimistic    : write 2"
print "Minimax Regret : write 3"
m = int(raw_input())
while m not in range(1,4) :
    print m , " is not valid,please choose a valid option"
    m = int(raw_input())
if payoff == "profit" :
    func = min if m == 2 else max
else :
    func = min if m == 1 else max

if m == 3:
    if payoff == "profit" :
        for c in data.columns :
            data[c] = data[c].max() - data[c]
    else :
        for c in data.columns :
            data[c] -= data[c].min() 

data['choosen'] = pd.Series([func(o) for o in data.values],data.index)
print data

i = data['choosen'].argmin() if m == 3 or payoff == "cost" else data['choosen'].argmax()

print "\n\nBest Decision is " ,data.index[i] , " with value = " , data['choosen'][i] ,"\n\n"
raw_input("Press any key to exit")

