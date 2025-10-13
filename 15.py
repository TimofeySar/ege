
for amax in range(201):
    sh = 0
    for x in range(200):
        if not( ((x<5 or x>54) and (x>50 and x<= 93)) <= (x>amax)):
            sh +=1
    if sh == 20:
        print(amax)
        break