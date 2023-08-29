################
#
# DAY 12 N-Body Problem
#
################

# INPUT:
#<x=-16, y=15, z=-9>
#<x=-14, y=5, z=4>
#<x=2, y=0, z=6>
#<x=-3, y=18, z=9>


class moon:
    def __init__(self,xin,yin,zin):
        self.x = xin
        self.y = yin
        self.z = zin
        self.vx = 0
        self.vy = 0
        self.vz = 0
        self.pos_history = []
        self.pos_history.append([self.x,self.y,self.z])
        self.vel_history = []
        self.vel_history.append([self.vx,self.vy,self.vz])
        
    def cur_position(self):
        return [self.x, self.y, self.z]
        
    def cur_velocity(self):
        return [self.vx, self.vy, self.vz]
        
    def update_velocity(self,vect):
        self.vx += vect[0]
        self.vy += vect[1]
        self.vz += vect[2]
#        print('['+str(self.vx)+','+str(self.vy)+','+str(self.vz)+']')
        
    def update_position(self):
        # happens at end-of-step
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz
        self.pos_history.append([self.x,self.y,self.z])
        self.vel_history.append([self.vx,self.vy,self.vz])
        

########
#
# Example 1
#m = {}
#m[1] = moon(-1,0,2)
#m[2] = moon(2, -10, -7)
#m[3] = moon(4, -8, 8)
#m[4] = moon(3, 5, -1)
#
#########
########
#
# Example 2
m = {}
m[1] = moon(-8,-10,0)
m[2] = moon(5, 5, 10)
m[3] = moon(2, -7,3)
m[4] = moon(9, -8, -3)
#
#########
########
#
# PUZZLE INPUT
#m = {}
#m[1] = moon(-16,15,-9)
#m[2] = moon(-14, 5, 4)
#m[3] = moon(2, 0,6)
#m[4] = moon(-3, 18,  9)
#
#########

def process(moon1, moon2):
    x1,y1,z1 = moon1.cur_position()
    x2,y2,z2 = moon2.cur_position()
    update1 = 0
    update2 = 0
    update3 = 0
    if x1 > x2:
        update1 = 1
    elif x1 < x2:
        update1 = -1

    if y1 > y2:
        update2 = 1
    elif y1 < y2:
        update2 = -1
        
    if z1 > z2:
        update3 = 1
    elif z1 < z2:
        update3 = -1
    update = [update1, update2, update3]
    moon2.update_velocity(update)
    moon1.update_velocity([i*-1 for i in update])
    
def process_step():
    process(m[1], m[2])
    process(m[1], m[3])
    process(m[1], m[4])
    process(m[2], m[3])
    process(m[2], m[4])
    process(m[3], m[4])
    
    m[1].update_position()
    m[2].update_position()
    m[3].update_position()
    m[4].update_position()

    


max_step = 10

for step in range(max_step):
    process_step()
    
m[1].cur_position()
m[1].cur_velocity()

m[2].cur_position()
m[2].cur_velocity()

m[3].cur_position()
m[3].cur_velocity()

m[4].cur_position()
m[4].cur_velocity()

##
# Total energy  Calculation
##
def total_energy():
    pot = []
    kin = []
    energy = []
    for moon in m:
        position = m[moon].cur_position()
        velocity = m[moon].cur_velocity()
        pot.append(sum([abs(i) for i in position]))
        kin.append(sum([abs(i) for i in velocity]))
        energy.append(pot[-1] * kin[-1])
    return sum(energy)
    
total_energy()

def check_if_previous(mn):
    p = mn.cur_position()
    v = mn.cur_velocity()
    p1_idx = 0
    v1_idx = 0
    if p in mn.pos_history[0:-1]:
        p1_idx = mn.pos_history.index(p)
    if v in mn.vel_history[0:-1]:
        v1_idx = mn.vel_history.index(v)
        
    if p1_idx == v1_idx:
        return p1_idx
    else:
        return 0
        
#    p1 = m[1].cur_position()
#    v1 = m[1].cur_velocity()
#    
#    p2 = m[2].cur_position()
#    v2 = m[2].cur_velocity()
#    
#    p3 = [3].cur_position()
#    v3 = [3].cur_velocity()
#    
#    p4 = m[4].cur_position()
#    v4 = m[4].cur_velocity()
#    
#    if p1 in m[1].pos_history:
#        p1_idx = m[1].pos_history.index(p1)
#    if v1 in m[1].pos_history:
#        v1_idx = m[1].pos_history.index(v1)
#    
    

#####
# Part B
#####

step = 0
process_step()
while True:
    step += 1
    if step % 1000 == 0:
        print("Step: "+str(step))
    process_step()
    i1 = check_if_previous(m[1])
    if i1 == 0:
        continue
    i2 = check_if_previous(m[2])
    if i2 == 0:
        continue
    i3 = check_if_previous(m[3])
    if i2 == 0:
        continue
    i4 = check_if_previous(m[3])
    if i2 == 0:
        continue
    if i1 == i2 == i3 == i4:
        if i1 > 0:
            break
