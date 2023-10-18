import math
from render import InitRender, Render

G = 6.67408e-11

# Define the bodies
central_body = (1e12, (400.0, 400.0), (0.0, 0.0))  # Central body with large mass, positioned at the origin, stationary
planet1 = (1e4, (360.0, 400.1), (0.0001, 1.5))   # Planet 1 starting at (1000, 0) with a velocity vector giving it a circular orbit
planet2 = (1e3, (400.1, 280.0), (-0.5, 0.0001))  # Planet 2 starting at (0, -500) with a velocity vector giving it a circular orbit

# Define the system
system = [central_body, planet1, planet2]

def calculate_distance(body1, body2):
    """Returns the distance between two bodies"""
    return math.sqrt((body1[1][0] - body2[1][0])**2 + (body1[1][1] - body2[1][1])**2)

def calculate_force(body1, body2):
    """Returns the force exerted on body1 by body2, in 2 dimensions as a tuple"""
    r = calculate_distance(body1, body2)
    rx = body2[1][0] - body1[1][0]
    ry = body2[1][1] - body1[1][1]

    f = G * body1[0] * body2[0] / r**2
    fx = f * rx / r
    fy = f * ry / r

    return (fx, fy)

def calculate_net_force_on(body, system):
    """Returns the net force exerted on a body by all other bodies in the system, in 2 dimensions as a tuple"""
    fx = 0.0
    fy = 0.0
    
    for other in system:
        if other != body:
            force = calculate_force(body, other)
            fx += force[0]
            fy += force[1]

    return (fx, fy)

def calculate_acceleration(body, system):
    """Returns the acceleration of a body due to the net force exerted on it by all other bodies in the system, in 2 dimensions as a tuple"""
    fx, fy = calculate_net_force_on(body, system)
    ax = fx / body[0]
    ay = fy / body[0]
    return (ax, ay)

def update_velocity(system, dt):
    """Updates the velocities of all bodies in the system, given a time step dt"""
    for i in range(len(system)):
        mass, (x, y), (vx, vy) = system[i]
        ax, ay = calculate_acceleration(system[i], system)
        new_vx = vx + ax * dt
        new_vy = vy + ay * dt
        system[i] = (mass, (x, y), (new_vx, new_vy))

    return system
   

def update(system, dt):
    """Update the positions of all bodies in the system, given a time step dt"""
    system = update_velocity(system, dt)

    for i in range(len(system)):
        mass, (x, y), (vx, vy) = system[i]
        new_x = x + vx * dt
        new_y = y + vy * dt
        system[i] = (mass, (new_x, new_y), (vx, vy))

    return system

def simulate(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps"""
    for _ in range(num_steps):
        system = update(system, dt)

    return system

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""
    InitRender()
    for _ in range(num_steps):
        system = update(system, dt)
        Render(system)
        dump_system(system)


    return system

def dump_system(system):
    """Prints the system state"""
    for body in system:
        print(f'{body[0]}kg @ ({body[1][0]:.2f}, {body[1][1]:.2f})m, v = ({body[2][0]:.8f}, {body[2][1]:.8f})m/s')

if __name__ == '__main__':
    simulate_with_visualization(system, 0.1, 100000)





