'''
Samuel Beardmore
Collision in one dimension
9 Mar 2017
'''

class space(object):
    def __init__(self, p):
        '''Initiate particles with passed conditions:[[pos, vel, mass, e], ...]'''
        #Exclude/include defaults as required
        p[0][0] = 40
        #p[0][0]
        #p[0][0]
        p[0][0] = 0.8
        p[1][0] = 140
        #p[1][0]
        #p[1][0]
        p[1][0] = 0.8
        self.p = [particle(), particle()]
        for i in range(2):
            #Extract pos, vel, mass and e for each particle
            self.p[i].pos = float(p[i][0])
            self.p[i].vel = float(p[i][1])
            self.p[i].mass = float(p[i][2])
            self.p[i].e = float(p[i][3])

        self.mt = self.p[0].mass + self.p[1].mass
        self.dm = self.p[0].mass - self.p[1].mass
    def __iter__(self):
        return self

    def __next__(self):
        '''returns a list with [a pos, b pos, a momentum, b momentum, total momentum].'''
        
        a = self.p[0]
        b = self.p[1]
        mt = self.mt
        dm = self.dm

        #Check distance between particles
        if abs(b.pos - a.pos) <= 60:
            #If particles collided/overlapped, determine if moving towards eachother
            relVel = a.vel - b.vel
            if (relVel > 0):
                print('collision')
                e = min(a.e, b.e)
                a.vel = e*(((a.vel*dm)+(2*b.vel*b.mass))/mt)
                b.vel = e*(((b.vel*dm)-(2*a.vel*a.mass))/mt)
        a.momentum = abs(a.mass*a.vel)
        b.momentum = abs(b.mass*b.vel)

        for i in self.p:   
            #Wall colision check
            if ((i.pos <= 30) and (i.vel < 0)) or ((i.pos >= 560) and (i.vel > 0)):
                print('Wall')
                i.vel = -(i.e * i.vel)
            #Update Positions
            i.pos += i.vel 

        return [a.pos, b.pos, a.momentum, b.momentum, a.momentum + b.momentum]



class particle(object):
    pos = 0
    vel = 0
    mass = 0
    e = 0
