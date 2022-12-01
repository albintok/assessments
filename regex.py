# import  re
#
# str="The giant panda is perhaps the most powerful symbol in the world when it comes to species conservation.\
# Adored around the world.the distinctive black and white animal is a national treasure in China and has been the symbol of WWF since its formation in 1961.\
# While its numbers are slowly increasing, the giant panda remains one of the rarest and most endangered bears in the world."
#
# x = re.search(r"panda", str)
# if x:
#     print(True)
# else:
#     print(False)




import re


print(re.search(r"[SC][1-9][a-z][^a-z][6,12]","S4aB8"))

