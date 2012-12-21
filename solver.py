import numpy as np
import pandas as pd
import sys

infile = sys.argv[1]
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

func = min if m == 2 else max

if m == 3:
    for c in data.columns :
        data[c] = data[c].max() - data[c]

data['choosen'] = pd.Series([func(o) for o in data.values],data.index)
print data

i = data['choosen'].argmin() if m == 3 else data['choosen'].argmax()

print "\n\nBest Decision is " ,data.index[i] , " with value = " , data['choosen'][i] ,"\n\n"
raw_input("Press any key to exit")

