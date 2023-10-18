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
    pass

def calculate_force(body1, body2):
    """Returns the force exerted on body1 by body2, in 2 dimensions as a tuple"""
    pass

def calculate_net_force_on(body, system):
    """Returns the net force exerted on a body by all other bodies in the system, in 2 dimensions as a tuple"""
    pass

def calculate_acceleration(body, system):
    """Returns the acceleration of a body due to the net force exerted on it by all other bodies in the system, in 2 dimensions as a tuple"""
    pass

def update_velocity(system, dt):
    """Updates the velocities of all bodies in the system, given a time step dt"""
    pass
   

def update(system, dt):
    """Update the positions of all bodies in the system, given a time step dt"""
    pass

def simulate(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps"""
    pass

def simulate_with_visualization(system, dt, num_steps):
    """Simulates the motion of a system of bodies for a given number of time steps, and visualizes the motion"""
    pass

if __name__ == '__main__':
    pass





