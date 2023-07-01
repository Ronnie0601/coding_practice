def greetings():
    return 'Namaste'
response = greetings()
print(response)

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissors:)")
    computer_choice = 'paper'
    choices ={"player" : player_choice, "computer" : computer_choice}
    return choices
response = get_choices()
print(response)