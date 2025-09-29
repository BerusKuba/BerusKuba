name = input('Greetings! What is your name? ')
print(f'Hello, {name}! It is good to see you!')

number = int(input('Enter a number: '))
print(f'The square of {number} is {number * number}.')

runs = int(input('How many runs scored? '))
overs = int(input('How many overs used? '))
print(f'Run rate: {runs / overs:.2f} runs per over.')

runs = int(input('How many runs scored? '))
batted = int(input('How many times batted? '))
notout = int(input('How many times not out? '))
print(f'Average score: {runs * batted * notout / 3}')