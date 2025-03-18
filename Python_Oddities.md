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

## Arch Linux venv
Installing python packages is more involved on Arch Linux, so try to do these in this order

1. Install from official repo/AUR, these packages are installed system-wide
2. If not available via pacman or paru, then install into a custom venv

# --system-site-packages allows the venv to "inherit" global packages, and the venv packages
to "overwrite" them (tbh this is kind of the default behaviour I expected...)
virtualenv -p /usr/bin/python3 venv --system-site-packages
# add this line to your ~/.bashrc, or ~/.zshrc
source venv/bin/activate

pip install package

## Pytorch specific

Convolution layers surprisingly do not care about the input size of the image
This explains why they are so widely applicable IRL

## Tensorboard, and managing dependencies

Python 3.13 removed the imghdr library, which is required by tensorboard
A hotfix is to install standard-imghdr, or python-deadlib from the AUR

For some reason, the arch linux repo of tensorboard when installed is unable to 
see either of these
so the solution is to 
pip install tensorboard
instead of the Arch version

# accessing venv packages from Jupyter

Create a venv for Jupyter 
python3 -m ipykernel install --user --name=projectname

Edit VSCODE settings
Exntensions -> Python 
Python: venv folders
and add the relevant folder for venv

Restart VSCODE, then the venv will appear as an available kernel

# outputting directly
assigning something to _ specifically will directly output the result

# Numpy grievances
## slicing
These actually follow MATLAB, and require colons : in the empty dimensions

## simple mathematical operations
these require import math, then math.sqrt, etc
Python is also really anal about types
e.g. if rho is a numpy array, np.float_power(rho[1], 2) is required to square it

# Pandas vs Numpy
numpy is like base R's arrays, very basic, but also very fast
Pandas is like base R's dataframes, built on top of numpy, and better for real data analysis
However, there is more overhead

Both have far less features than their equivalents in R
e.g. numpy does not support named dimensions


