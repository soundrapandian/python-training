world = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

def print_world():
    for row in world:
        print ("|", end="")
        for cell in row:
            if cell:
                print ('X', end="")
            else:
                print (' ', end="")
        print ("|")

def count_neighbours(x, y):
    def get_neighbour(x, y):
        try:
            if x >= 0 and y >= 0:
                return world[x][y]
            else:
                return 0
        except IndexError:
            return 0
    
    neighbours = [(x_index, y_index) for x_index in (x-1, x, x+1) if x_index >= 0 \
                                     for y_index in (y-1, y, y+1) if y_index >= 0]
    
    return get_neighbour(x-1, y-1) +\
        get_neighbour(x-1, y) +\
        get_neighbour(x-1, y+1) +\
        get_neighbour(x, y-1) +\
        get_neighbour(x, y+1) +\
        get_neighbour(x+1, y-1) +\
        get_neighbour(x+1, y) +\
        get_neighbour(x+1, y+1)
        
def move_world():
    global world
    new_world = [[life_condidtion(world[x][y], count_neighbours(x, y)) for y in range(len(world[0]))] for x in range(len(world))]
    world = new_world

def life_condidtion(current_state, neighbour_count):
    if (current_state and neighbour_count in (2, 3)) or \
    (not current_state and neighbour_count == 3):
        return 1
    return 0 
    
while True:
    """world = """
    move_world()
    print_world()
    if input("Next?").lower() not in ('y', 'yes'):
        print ("Done!")
        break