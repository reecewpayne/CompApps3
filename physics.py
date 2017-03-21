'''
Samuel Beardmore
Collision in one dimension
9 Mar 2017
'''


#remove NumPy

class space(object):
    def __init__(self, p):
        '''Initiate particles and save initial conditions'''
        self.p = [particle(), particle()]
        for i in range(2):
            #Extract pos for each particle
            self.p[i].pos = p[i][0]
            #Extract vel for each particle
            self.p[i].vel = p[i][1]
            #set mass
            self.p[i].mass = p[i][2]
            #set e
            self.p[i].e = p[i][3]

    def __iter__(self):
        return self

    def __next__(self):
        '''return:system: total momentum, ball 1&2: pos, vel, momentum.'''
        #Update positions
        for i in self.p:
            i.pos += i.vel    
            #Wall colision check
            if (i.pos <= 0) or (i.pos >= 530):
                i.vel = -(i.e * i.vel)

            a = self.p[0]
            b = self.p[1]
            #Check distance between particles
            if b.pos - a.pos <= 60:
            #If particles collided/overlapped, determine if moving towards eachother
                relVel = a.vel - b.vel
                if (relVel > 0):
                    e = min(a.e, b.e)
                    impulse = (-(1+e)*relVel)/((1/a.mass)+(1/b.mass))
                    a.vel -= (1/a.mass)*impulse
                    b.vel += (1/a.mass)*impulse

        return self



class particle(object):
    pos =[0, 0]
    vel = [0, 0]
    mass = 0
    e = 0
