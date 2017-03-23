import physics

data = [[],[]]
switch = {0:'Position',
          1:'Velocity',
          2:'Mass',
          3:'Coefficient of Restitution'}

for i in range(2):
    for j in range(4):
        data[i].append(float(input('Please enter the %s for particle %d: '%(switch[j], i+1))))

s = physics.space(data)

for i, j in zip(s, range(100)):
    print(i)
