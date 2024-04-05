class space_prop():
    def __init__(self, space_properties = [[0,0],[0,0],[0,0]], mass = 1):
        self.position = space_properties[0]
        self.speed = space_properties[1]
        self.accel = space_properties[2]
        self.mass = mass

    def apply_force(self,force):
        if force == None:
            return
        self.accel[0] = force[0]/self.mass
        self.accel[1] = force[1]/self.mass

    def apply_friction(self,friction):
        self.speed -= friction

    def update_speed(self, delta_t):
        # s = s0 + a
        self.speed[0] += self.accel[0]*delta_t
        self.speed[1] += self.accel[1]*delta_t
    
    def update_position(self,delta_t):
        # p = at²/2 + s0*t + p0
        self.position[0] += self.speed[0]*delta_t + (self.accel[0]*delta_t*delta_t)/2
        self.position[1] += self.speed[1]*delta_t + (self.accel[1]*delta_t*delta_t)/2

    def change_accel(self,accel):
        if accel == None:
            return
        self.accel = accel

    def change_speed(self,speed):
        if speed == None:
            return
        self.speed = speed
    
    def change_position(self,position):
        if position == None:
            return
        self.position = position

    def update(self, delta_t = 1, force=None ):
        self.update_position(delta_t)
        self.update_speed(delta_t)

    def change(self,speed=None, position=None, accel=None, mass=None):
        self.change_speed(speed)
        self.change_position(position)
        self.change_accel(accel)
        self.change_mass(mass)

class Entity():
    def __init__(self):
        self.phy_prop = space_prop()
        
    def update(self):
        pass
        self.phy_prop.update()  

    def get_position(self):
        return self.phy_prop.position 

    def print_position(self):
        print(self.position)