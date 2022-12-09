#Initialize Pygame
pygame.init()

# Set  the screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Load the plane image
plane_image = pygame.image.load("plane.png")

# Set the initial position of the plane
plane_x = SCREEN_WIDTH / 2
plane_y = SCREEN_HEIGHT / 2

# Set the initial velocity of the plane
plane_vx = 0
plane_vy = 0

# Set the plane's acceleration
plane_ax = 0
plane_ay = 0

# Set the plane's mass
plane_mass = 1

# Set the plane's thrust
plane_thrust = 0.1

# Set the plane's drag coefficient
plane_drag = 0.01

# Set the frame rate
FRAME_RATE = 60
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update the plane's velocity
    plane_vx += plane_ax
    plane_vy += plane_ay

    # Update the plane's position
    plane_x += plane_vx
    plane_y += plane_vy

    # Apply drag to the plane's velocity
    plane_vx *= (1 - plane_drag)
    plane_vy *= (1 - plane_drag)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the plane
    screen.blit(plane_image, (plane_x, plane_y))

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(FRAME_RATE)