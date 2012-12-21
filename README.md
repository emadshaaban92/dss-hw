

# DESCRIPTION
Simple script solves a simple DSS problem (making decision under uncertainty) .

# DEPENDENCIES

### Python2.7
Python is a programming language that lets you work more quickly and integrate your systems more effectively.
You can download and install Python easily from http://www.python.org/
Note : Don't use Python 3.x .. It won't work .

### NumPy
NumPy is the fundamental package for scientific computing with Python.

Besides its scientific uses, NumPy can also be used as an efficient multi-dimensional container of generic data. Arbitrary data-types can be defined. This allows NumPy to seamlessly and speedily integrate with a wide variety of databases.

Numpy is licensed under the BSD license, enabling reuse with few restrictions.

You can install NumPy with
    
    pip install numpy

### Pandas
pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.

Note : Pandas depends on NumPy so Please install NumPy first .

You can install it with
 
    pip install pandas 

or 

    easy_install pandas

# Files

### solver.py
This file contains everything :), it's more like a script not a program . 

### Examples
ex1.csv , ex2.csv and ex3.csv
These files contain some data to validate the script ... enjoy editing them ;) 

# USAGE
simply excute solver.py with one argument (filename which contains your data)

###### Example 
    python solver.py ex1.csv
    

The script is interactive, you will be asked to choose your prefered (Optimistic, Pessimistic or Minimax Regret)
and hopefully you will see the result :)

