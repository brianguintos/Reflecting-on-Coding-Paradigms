class Pod_Racer:
    def __init__(self, max_speed, condition, price, owner):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
        self.owner = owner

    def repair(self):
        self.condition = 'repaired'


class Anakin_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner = 'Anakin'):
        super().__init__(max_speed, condition, price, owner)        

    def boost(self):
        self.max_speed *= 2

class Sebulba_Pod(Pod_Racer):
    def __init__(self, max_speed, condition, price, owner = 'Sebula'):
        super().__init__(max_speed, condition, price, owner)

    def flame_jet(self, other_pod):
        print('flaming', other_pod.owner)
        other_pod.condition = 'trashed'

anakins_pod = Anakin_Pod(25, 'perfect', 1000)        

sebulba_pod = Sebulba_Pod(28, 'perfect', 1000000)

print('anakin condition:', anakins_pod.condition)
print('sebulba condition:', sebulba_pod.condition)

sebulba_pod.flame_jet(anakins_pod)

print('anakin condition:', anakins_pod.condition)
print('sebulba condition:', sebulba_pod.condition)

anakins_pod.repair()

print('anakin condition:', anakins_pod.condition)
print('sebulba condition:', sebulba_pod.condition)

print('anakin max_speed:', anakins_pod.max_speed)
print('sebulba max_speed:', sebulba_pod.max_speed)

anakins_pod.boost()

print('anakin max_speed:', anakins_pod.max_speed)
print('sebulba max_speed:', sebulba_pod.max_speed)


# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply):
# 1. Encapsulation is demonstrated in defining the idea of the flame_jet, boost and in repair.
# 2. Inheritance is demonstrated when we use the class of Pod_Racer as an argument in the classes of Anakin_Pod and Sebulba_Pod.

# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# 1. I want to say yes but I don't know why.

# How in particular did Object Oriented Programming assist in the solving of this problem?
# 1. By organizing code using encapsulation and inheritance