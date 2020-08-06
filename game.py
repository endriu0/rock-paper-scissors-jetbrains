from random import choice

# Write your code here
options = ["scissors", "rock", "paper"]
user = input("Enter your name: ")
print(f"Hello, {user}")
new_options = input()

# If user provided his own options then use them - otherwise default
if len(new_options) != 0:
    options = new_options.split(',')

print("Okay, let's start")

ratings_file = open('rating.txt', 'r+')

for line in ratings_file:
    if user in line:
        user, score = line.split()
        score = int(score)
        break
else:
    score = 0

ratings_file.close()
ratings_file = open('rating.txt', 'w+')


def results(result, comp_option):
    if result == "draw":
        print(f"There is a draw ({comp_option})")
    elif result == "loss":
        print(f"Sorry, but computer chose {comp_option}")
    else:
        print(f"Well done. Computer chose {comp_option} and failed")


def compare_options(usr_option, comp_option, options):
    global score
    if usr_option == comp_option:
        result = "draw"
        score += 50
    else:
        usr_position = options.index(usr_option)  # This is ok
        options_before = options[0:usr_position]  # Take all the options before our pick
        options_after = options[usr_position + 1:]  # Take all the options that follow after users pick
        options_after.extend(options_before)
        winning_options = options_after[int(len(options_after) / 2):]
        if comp_option in winning_options:
            result = "win"
            score += 100
        else:
            result = "loss"
    return results(result, comp_option)

while True:
    usr_option = input()
    if usr_option in options:
        comp_option = choice(options)
        compare_options(usr_option, comp_option, options)
    elif usr_option == "!exit":
        print(user, score, file=ratings_file)
        ratings_file.close()
        print("Bye!")
        break
    elif usr_option == "!rating":
        print(score)
    else:
        print("Invalid input")
