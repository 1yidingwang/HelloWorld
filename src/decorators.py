class myclass:

    def __init__(self, prop):
        
        self._prop = prop

    @property
    def adder(self):
        return self._prop 
    
    @prop.setter
    def setter(self, new_prop):
        if new_prop != nan:
            self._prop = new_prop
        else:
            print("you are crazy")

    @prop.deleter
    def prop_del(self):

        del  self._prop

def print_again( func ):

    def inner():

        # discard all new modification

        func()
    
    return inner

@print_again
def ord():

    print("hello world")

ord()