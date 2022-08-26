# Object-Oriented Programming Intro: Creating a Class


def joe(y: int)->int:
    """
    Returns 5*y as tested in the following doctest
    >>> joe(5)
    25
    """
    return 5*y


# test joe()
# should print 4*5=20
print(joe(4))


# creating a class Fish with a field x representing the position of the fish along the x-axis
class Fish:
    # create a custom fish (ie. a constructor)
    def __init__(self, z):
        # automatically creates a field x for new object of class Fish and sets value to z
        self.x = z

    # defining a method swim() for class Fish
    def swim(self, y):
        # adds y to field x of the object (ie. x=x+y)
        self.x += y


# sets fish1.x to 2
fish1 = Fish(2)

# sets fish1.x to 2+3=5 (calling swim() with class Fish)
Fish.swim(fish1, 3)

# sets fish1.x to 5+2=7 (calling swim() with object fish1)
fish1.swim(2)

# should print 7 since fish1.x=7
print(fish1.x)

# deleting the field x from fish1
del fish1.x

# field still exists in class Fish
fish2 = Fish(3)
print(fish2.x)  # should print 3

# deleting objects fish1 and fish2
del fish1
del fish2

if __name__ == "__main__":
    # just to do the doctest for joe()
    # no output if all tests pass
    import doctest
    doctest.testmod()
