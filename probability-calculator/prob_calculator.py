import copy
import random

class Hat:

    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.contents.append(key)

    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        balls = []
        for _ in range(number):
            choice = random.randrange(len(self.contents))
            balls.append(self.contents.pop(choice))
        return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successes = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        balls = new_hat.draw(num_balls_drawn)

        # Check if the drawn balls match the expected distribution
        success = True
        for color, expected_count in expected_balls.items():
            if balls.count(color) < expected_count:
                success = False
                break

        if success:
            successes += 1

    return successes / num_experiments

# Example usage:
hat = Hat(red=5, blue=2)
probability = experiment(hat, {'red': 2, 'blue': 1}, 4, 1000)
print("Probability:", probability)
