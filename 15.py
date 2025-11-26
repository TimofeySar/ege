#
# for amax in range(201):
#     sh = 0
#     for x in range(200):
#         if not( ((x<5 or x>54) and (x>50 and x<= 93)) <= (x>amax)):
#             sh +=1
#     if sh == 20:
#         print(amax)
#         break


for a in range(1,1000):
    f = True
    for x in range(1,1000):
        for y in range(1,1000):
           if ((y > a) or (152 != 2 * y + 3 * x) or (a < x)) == 0:
                 f = False
    if f == True:
        print(a)
