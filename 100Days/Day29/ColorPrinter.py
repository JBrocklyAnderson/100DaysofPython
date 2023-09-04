def print_color(word, color):
    # Dictionary to map color names to their respective ANSI codes
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "purple": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m"
    }
    
    # ANSI reset code
    reset = "\033[0m"

    # If the color exists in our dictionary, print the word in that color.
    # If not, print the word in the default color.
    if color in colors:
        print(colors[color], word, reset, sep="", end="")
    else:
        print(word, end="")

# Test the subroutine
print("I've made a great subroutine")
print("with my ", end="")
print_color("amazing", "blue")
print_color(" colorful", "purple")
print_color(" ", "reset")
print_color("code!", "yellow")