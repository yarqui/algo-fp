import turtle


def draw_fractal_tree(
    t: turtle.Turtle, branch_length: float, angle: float, level: int
) -> None:
    """
    Recursively draws a line-based fractal (binary) tree.

    Args:
        t (turtle.Turtle): The turtle object for drawing.
        branch_length (float): Length of the current branch.
        angle (float): Angle between parent and child branches.
        level (int): Current depth of recursion.
    """
    if level == 0:
        return

    # Draw the current branch
    t.forward(branch_length)

    # Left subtree
    t.left(angle)
    draw_fractal_tree(t, branch_length * 0.7, angle, level - 1)

    # Right subtree
    t.right(angle * 2)
    draw_fractal_tree(t, branch_length * 0.7, angle, level - 1)

    # Restore original position and heading
    t.left(angle)
    t.backward(branch_length)


def setup_turtle() -> turtle.Turtle:
    """
    Configures the turtle graphics environment and returns the turtle.
    """
    t = turtle.Turtle()
    t.speed(0)
    t.color("brown")
    t.pensize(1)
    t.penup()
    t.goto(0, -300)
    t.setheading(90)  # Point upwards
    t.pendown()
    return t


def main():
    """
    Main function to prompt user input and draw the fractal tree.
    """
    while True:
        resp = input("Enter recursion depth (e.g. 8), or 'q' to quit: ")
        if resp.lower() == "q":
            print("Exiting.")
            return
        try:
            depth = int(resp)
            screen = turtle.Screen()
            screen.bgcolor("white")
            t = setup_turtle()
            draw_fractal_tree(t, branch_length=100, angle=30, level=depth)
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    turtle.done()


if __name__ == "__main__":
    main()
