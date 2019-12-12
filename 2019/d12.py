import math
class Moon:
    def __init__(self, x, y, z, name):
        self.x_pos = int(x)
        self.y_pos = int(y)
        self.z_pos = int(z)
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0
        self.name = "Moon " + str(name)
        self.state = ""

    def set_state(self):
        self.state = f"{self.x_pos}{self.y_pos}{self.z_pos}{self.x_vel}{self.y_vel}{self.z_vel}"

    def get_state(self):
        return self.state

    def add_x_pos(self, val):
        self.x_pos += int(val)

    def add_y_pos(self, val):
        self.y_pos += int(val)

    def add_z_pos(self, val):
        self.z_pos += int(val)

    def add_x_vel(self, val):
        self.x_vel += int(val)

    def add_y_vel(self, val):
        self.y_vel += int(val)

    def add_z_vel(self, val):
        self.z_vel += int(val)

    def get_x_pos(self):
        return int(self.x_pos)

    def get_y_pos(self):
        return int(self.y_pos)

    def get_z_pos(self):
        return int(self.z_pos)

    def get_x_vel(self):
        return int(self.x_vel)

    def get_y_vel(self):
        return int(self.y_vel)

    def get_z_vel(self):
        return int(self.z_vel)

    def get_name(self):
        return self.name



def create_moons(moon_list):
    moons = []
    for i in range(len(moon_list)):
        x = moon_list[i][0].split('=')[1]
        y = moon_list[i][1].split('=')[1]
        z = moon_list[i][2].split('=')[1]
        moon = Moon(x, y, z, i+1)
        moons.append(moon)
    return moons


def check_velocity(x, y):
    if x == y:
        vel = 0
    elif x < y:
        vel = 1
    elif x > y:
        vel = -1
    return vel


def calculate_velocity(moon, moons):
    m1x, m1y, m1z = get_positons(moon)
    for i in moons:
        m2x, m2y, m2z = get_positons(i)
        moon.add_x_vel(check_velocity(m1x, m2x))
        moon.add_y_vel(check_velocity(m1y, m2y))
        moon.add_z_vel(check_velocity(m1z, m2z))


def move_moons(moons):
    for moon in moons:
        calculate_velocity(moon, moons)
    for moon in moons:
        moon.add_x_pos(moon.get_x_vel())
        moon.add_y_pos(moon.get_y_vel())
        moon.add_z_pos(moon.get_z_vel())


def get_positons(moon):
    x = moon.get_x_pos()
    y = moon.get_y_pos()
    z = moon.get_z_pos()
    return x, y, z


def get_velocities(moon):
    x = moon.get_x_vel()
    y = moon.get_y_vel()
    z = moon.get_z_vel()
    return x, y, z


def calc_energy(moon):
    x, y, z = get_positons(moon)
    xv, yv, zv = get_velocities(moon)
    potential = math.fabs(x) + math.fabs(y) + math.fabs(z)
    kinetic = math.fabs(xv) + math.fabs(yv) + math.fabs(zv)
    return potential * kinetic


def add_states(moons):
    for moon in moons:
        moon.set_state()


def get_states(moons):
    full_state = ""
    for moon in moons:
        full_state += moon.get_state()
    return full_state


def part1(moons_list):
    for i in range(1000):
        move_moons(moons_list)
    total = 0
    for moon in moons_list:
        total += calc_energy(moon)
    return total

# def part2(moons):
#     found = False
#     steps =0
#
#         add_states(moons)
#         move_moons(moons)
#
#         steps += 1
#     return steps - 1

def main():
    input_file = "Inputs/d12Input.txt"
    test_file = "Inputs/d12test.txt"
    moon_list = [list(str(x).strip().replace("<", "").replace(">", "").split(",")) for x in
                 open(test_file).readlines()]
    moons_list = create_moons(moon_list)

    #print(part1(moons_list))
    print(part2(moons_list))

main()
