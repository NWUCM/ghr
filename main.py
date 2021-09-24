h = 0.1
yn = 1
tn = 0
def f(tn, yn):
    return 4*tn*yn**0.5
def y(tn):
    return (1 + tn**2)**2   
for i in range(10):
    yn1 = yn + h * f(tn, yn)
    exc_y = y(tn)
    tn = tn + h
    error = yn1 - yn
    print(error)


    


