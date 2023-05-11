#*args, **kwargs
def f(*args, **kwargs):
    print("Positional:", args) #tupple

f(100, 50, 25)

#----------

def f(*args, **kwargs):
    print("Named:", kwargs) #dictionary

f(galleons=100, sickles=50, knuts=25)