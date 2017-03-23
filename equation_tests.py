def moving_collision(m,m2,vel1,vel2):
    
    v1= (((m-(m2))/(m+(m2)))*vel1) + (((2*m2)/(m+(m2)))*vel2)
            
    v2= (((2*m)/(m+(m2)))*vel1) - (((m-(m2))/(m+(m2)))*vel2)

    mo1= m*vel1

    mo2= m2*vel2

    mtot1= mo1+mo2

    mo3= m*v1

    mo4= m*v2

    mtot2= mo3+mo4

    print
    print('''After the collision of the two particles the velocity of
    particle 1 is now ''') + str(v1)+' m/s'
    print
    print('''After the collision of the two particles the velocity of
    particle 2 is now ''') + str(v2)+' m/s'
    print
    print('''Before the collision the momentum of particle 1
    is ''') + str(mo1)+' (kg m/s)'
    print
    print('''Before the collision the momentum of particle 2
    is ''') + str(mo2)+' (kg m/s)'
    print
    print('''Before the collision the total momentum of both particles
    is ''') + str(mtot1)+' (kg m/s)'
    print
    print('''After the collision the momentum of particle 1
    is ''') + str(mo3)+' (kg m/s)'
    print
    print('''After the collision the momentum of particle 2
