import matplotlib.pyplot as plt
import math
# This part I define the problem using functions then put parameter na x for the value na x na iinput sa naa sa Value_x na file
def prob1(x):
    return x ** 2 + 7 * x + 2

def prob2(x):
    return 3 * x + 2

def prob3(x):
    return x ** 2

def prob4(x):
    return x ** 3

def prob5(x):
    return x ** 5

def prob6(x):
    return x ** 3 + 2 * x ** 2 + x + 10

def prob7(x):
    return x ** 4 - 3 * x ** 3 - 2 * x ** 2 - x + 11

def prob8(x):
    return math.sin(x)

def prob9(x):
    return math.cos(x)

def prob10(x):
    return x ** 5 + 4 * x ** 4 + x ** 3 - 2 * x ** 2 + 100
# naghimo dayun kug dictionary nga ang values is nakatuple  ng functions tas with color na and label for later purpose sa graphing
# also this dictionary is easy nalang to call using its variable name when you graph
Problems = {
    '1': (prob1, 'r', "x^2 + 7^x + 2"),
    '2': (prob2, 'b', "3*x + 2"),
    '3': (prob3, 'g', "x^2"),
    '4': (prob4, 'c', "x^3"),
    '5': (prob5, 'm', "x^5"),
    '6': (prob6, 'y', "x^3 + 2*x^2 + x + 10"),
    '7': (prob7, 'k', "x^4 - 3*x^3 - 2*x^2 - x + 11"),
    '8': (prob8, 'tab:orange', "sin(x)"),
    '9': (prob9, 'tab:purple', "cos(x)"),
    '10': (prob10, 'tab:brown', "x^5 + 4*x^4 + x^3 - 2*x^2 + 100")
}
# then here na part is iread ang value sa akong x nga naa sa txt file
with open('values.txt', 'r') as file:
    Value_x = ([int(line.strip()) for line in file.readlines()])
#this one is my main function for the graphing sa value of x
def main():
    # this one will be shown on the terminal window
    print("Choose the expressions you want to plot (separate with commas), or type '11' to plot all expressions:")
    for key, value in Problems.items():
        # ang output for this is katong key nga naa sa akong problem na dictionary and ang naka index na 2 is tawagan lang niya tung expression na value
        print(f"{key}. {value[2]}")

    Users_choice = input("What you want to graph: ")
    # if condition ko siya sa choices na gipili ni user to graph 
    if Users_choice == '11':
        # so if the user has a choice and output result for y values will be written sa txt file also magraph sad siya
        with open('output.txt' , 'w') as output_file:
        # so nagdeclare ko ug variable sa for loop for the variable sa akong dictionary and calling its values nga nakatuples
            for func, color, label in Problems.values():
                # so paggraph ana ang value_x is ang value sa x axis while func(x) for x in Value_x kay ang value sa y axis
                plt.plot(Value_x, [func(x) for x in Value_x], color=color, label=label)
                #i declare a variable indication for my y values to pass sa akong txt file
                Problems_values = [func(x) for x in Value_x]
                output_file.write(f"{func.__name__}:\n")
                output_file.write(" ".join(str(value) for value in Problems_values) + "\n")
            plt.title('Problems Graph')
    else:
        # nagdeclare og condition for individual or depends on user choices
        choices = Users_choice.split(',')
        # so this  part mag loop siya sa kung unsa ang gipili ni user na choices
        for choice in choices:
            # .get() method ay ginagamit upang kunin ang value mula sa dictionary gamit ang key na gipili ni user
            func, color, label = Problems.get(choice.strip()) 
            if func:
                plt.plot(Value_x, [func(x) for x in Value_x], color=color, label=label)
                plt.title(f'Graph of Function {choice.strip()}')
                with open('output.txt' , 'w') as output_file:
                    Problems_values = [func(x) for x in Value_x]
                    output_file.write(f"Problem {choice.strip()}: \n")
                    output_file.write(", ".join(str(val) for val in Problems_values))
            else:
                print(f"Invalid Choice: {choice}")

    plt.legend(loc='upper left')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
if __name__ == "__main__":
    main()


