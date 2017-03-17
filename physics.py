'''
Samuel Beardmore
Collisions Engine
9 Mar 2017

Description:
A 2D particle collision, physics engine designed to be used in a collisions and momentun learning tool.

The code is designed to create a 2D rectangluar 'Space' when called and simulate 2 particles.

Initial variables of position, velocity, mass and coefficient of restitution are required.
The 'Space' can then be iterated through, each iteration advancing the the simulation a step.

Collisions are checked for on each iteration and if one is found, the collision is resolved accordingly.
'''


#remove NumPy

class space(object):
    def __init__(self, x, y):
        self.limits = []
        self.limits.append(x - 60)
        self.limits.append(y - 60)

    def __iter__(self):
        self.p = [particle(), particle()]
        return self

    def __next__(self):
        #Update positions
        for i, j in zip(self.p, range(2)):
            i.pos[j] += i.vel[j]
            
            #Wall collision check
            if (i.pos[j] <= 0) or (i.pos[j] >= self.limits[j]):
                i.vel[j] = -(i.e * i.vel[j])

        a = self.p[0]
        b = self.p[1]
        #Check distance between particles (Pythagoras)
        if 900 > ((a.vel[0] + b.vel[0])^2 + (a.vel[1] + b.vel[1])^2):
            #If particles collided/overlapped, resolve collision
            relVel = []
            normal = []
            for i in range(2):
                relVel.append(b.vel[i] - a.vel[i])
                normal.append(b.pos[0] - a.pos[0])

            relVel = sum(p*q for p,q in zip(relVel, normal))

            if (relVel > 0):
                e = min(a.e, b.e)
                relImp = (-(1+e)*relVel)/((1/a.mass)+(1/b.mass))

                imp = relImp * normal
                for i in range(2):
                    a.vel[i] -= (1/a.mass)*imp
                    b.vel[i] += (1/a.mass)*imp

        return self

    def setLimits(self, x, y):
        '''Update the x and y limits, arguments x, y type int'''
        self.limits = []
        self.limits.append(x - 60)
        self.limits.append(y - 60)
        return self
        

    def setPos(self, particle, x, y):
        '''set pos for particle a/b, arguments 'a'/'b' type str and x and y values type int'''
        switch = {'a':0, 'b':1}
        i = switch[particle]
        self.p[i].pos[0] = x
        self.p[i].pos[1] = y
        return self


    def setVel(self, particle, x, y):
        '''set vel for particle a/b, arguments 'a'/'b' type str and x and y values type int'''
        switch = {'a':0, 'b':1}
        i = switch[particle]
        self.p[i].vel[0] = x
        self.p[i].vel[1] = y
        return self

        
    def setMass(self, particle, mass):
        '''set mass for particle a/b, arguments 'a'/'b' type str and mass value type int'''
        switch = {'a':0, 'b':1}
        i = switch[particle]
        self.p[i].mass = mass
        return self

    def setE(self, particle, e):
        '''set e for particle a/b, arguments 'a'/'b' type str and e value type int'''
        switch = {'a':0, 'b':1}
        i = switch[particle]
        self.p[i].e = e
        return self


class particle(object):
    pos =[0, 0]
    vel = [0, 0]
    mass = 0
    e = 0



    
