squares=[]

for x in range(1,11):
    squares.append(x**3)

print squares

squares=[x*2 for x in range(2,11)]
print squares

triple=lambda x: x*3
print triple(8)
