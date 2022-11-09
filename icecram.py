# machine = (["vanilla", "chocolate"], ["chocolate sauce",'Orange sprinkles', 'Oreos'])
#
# a=machine[0]
# b=machine[1]
# c=[]
# for i in a:
#     for j in b:
#          c.append(i+" "+j)
# print(c)

c=[]

class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        for i in self.ingredients:
            for j in self.toppings:
                c.append(i+" "+j)
        return c



machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce", 'Orange sprinkles', 'Oreos'])
print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]