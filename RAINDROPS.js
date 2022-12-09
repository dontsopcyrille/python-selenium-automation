/ Define the number of raindrops to create
const numRaindrops = 100;

// Define the maximum speed of the raindrops
const maxSpeed = 5;

function setup() {
  // Create a canvas that covers the entire window
  createCanvas(windowWidth, windowHeight);
}

function draw() {
  // Set the background color to a light blue
  background(100, 100, 250);

  // Create an array to store the raindrop positions
  let raindrops = [];

  // Generate the raindrops
  for (let i = 0; i < numRaindrops; i++) {
    // Create a raindrop at a random position at the top of the screen
    let raindrop = createVector(random(width), random(-height, 0));

    // Set the raindrop's speed to a random value between 0 and maxSpeed
    let speed = random(maxSpeed);

    // Add the raindrop and its speed to the array
    raindrops.push({raindrop, speed});
  }

  // Draw the raindrops
  for (let i = 0; i < raindrops.length; i++) {
    let raindrop = raindrops[i].raindrop;
    let speed = raindrops[i].speed;

    // Update the raindrop's position
    raindrop.y += speed;

    // If the raindrop falls off the bottom of the screen,
    // move it back to the top of the screen
    if (raindrop.y > height) {
      raindrop.y = 0;
    }

    // Draw the raindrop as a small circle
    fill(255);
    ellipse(raindrop.x, raindrop.y, 2);
  }
}