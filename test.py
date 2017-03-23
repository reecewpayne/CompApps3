import physics, sys


def test_f(data):    
    try:
        s = physics.space(data)
        for i, j in zip(s, range(100)):
            print(i)
    except:
        e = sys.exc_info()[0]
        print( "<p>Error: %s</p>" % e)


print('Test 1')
test_f('asdf') #Inavlid input test
input('\n\n\n')
print('Test 2')
test_f([[40, 5, 20, 0.9],[140, -2, 30, 0.8]]) #Valid inputs test
input('\n\n\n')
print('Test 3')
test_f([[0, 5, 20, 0.9],[1000, -2, 30, 0.8]]) #out of boundary test
input('\n\n\n')
print('Test 4')
test_f([[40, 0, 20, 0.9],[140, 0, 30, 0.8]]) #0 Velocity test
input('\n\n\n')
print('Test 5')
test_f([[40, 5, 0, 0.9],[140, -2, 30, 0.8]]) #0 mass test
input('\n\n\n')
print('Test 6')
test_f([[40, 5, 20, 0],[140, -2, 30, 0.8]]) #Inelastic test
input('\n\n\n')
print('Test 7')
test_f([[40, 5, 20, 1],[140, -2, 30, 1]]) #Fully Elastic
input('\n\n\n')
print('Test 8')
test_f([[40, 5, 20, 2],[140, -2, 30, 2]]) #Super Elastic


#User manual tests.
data = [[],[]]
switch = {0:'Position',
          1:'Velocity',
          2:'Mass',
          3:'Coefficient of Restitution'}

for i in range(2):
    for j in range(4):
        data[i].append(float(input('Please enter the %s for particle %d: '%(switch[j], i+1))))

test_f(data)
