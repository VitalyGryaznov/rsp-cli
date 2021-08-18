import requests
print("Welcome  to the ROCK-SCISSORS-PAPER game!")
play = True;
resultTexts = {"WIN": "You WIN!", "LOSE": "You lose!", "TIE": "It's a tie"}
while play:
	print("Please input your choie. Possible options are: ROCK, SCISSORS, PAPER")
	choice = input()
	while(choice not in ["ROCK", "PAPER", "SCISSORS"]):
		print("Please enter valid value. Possible options are: ROCK, SCISSORS, PAPER")
		choice = input()
	response = requests.post('http://localhost:8080/play', json={"customerChoice": choice})
	print("Your choice is: {0}".format(choice))
	print("Computer's choice is: {0}".format(response.json()['computerChoice']))
	print(resultTexts[response.json()['result']])
	print("Play again? Y/N")
	choice = input()
	while(choice not in ["Y", "N"]):
		print("Please, enter Y or N")
		choice = input()
	if choice == "N":
		play = False
		print("Good bye!")