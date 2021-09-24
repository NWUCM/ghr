h = 0.01
yn = 1
tn = 0
def f(tn, yn):
    return (4*tn*yn**0.5)
for i in range(10):
    yn1 = yn + h * f(tn, yn)
    tn = tn + h
    print(yn1)
    

