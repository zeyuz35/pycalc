# Python Oddities

Collection of various oddities I've found unique to Python

## = Conventions

Python uses = for both variable assignment, and keyword arguments

So, PEP8 dictates that spaces should be used around = for variable assignment
But no spaces for keyword arguments

x = 1

some_func(
    1, 2, kw1=kw1
)

This is actually somewhat of a bad convention - the no spaces places a significant cognitive load for humans to process reading the code

However, it does make editing code using tools significantly easier

## Multiple assignment

Python allows for multiple assignment like MATLAB

x, y = 1, 2

## Implicit Assignments

## Lack of clarity wrt Functions and Methods

Not sure if this is just due to shitty documentation, but there is a surprising lack of clarity between functions and methods

Most documentation seems to erroneously call methods which are unique to classes "functions"

## Dictionaries vs Lists
Difference seems to boil down to low-level implementation

Dictionaries are key-value pairs (similar to a factor variable in R)
Lists are generic

## Zero Based Indexing

## Jupyter
Jupyter's REPL is whack, though its variable watch is really nice for ML/DS workflows

it implicitly prints only the LAST thing you output
so in reality, you still need to call print on everything

## 

