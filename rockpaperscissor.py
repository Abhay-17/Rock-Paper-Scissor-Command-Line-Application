import random

"""
User at start will have 3 lifes
Everytime user loses a game life get removed
If life becomes zero then game will be over

Print score of user and comp after every play
Then print final score on gameover
and decide if user or comp is winner

"""



# 1 = rock , 2 = scissor , 3 = paper

def main():
	lives = 3
	countuser =0
	countcomp =0

	while(lives > 0) :
		x = random.randint(1,3)

		u = int(input("Enter Your input :\n 1 for rock \n 2 for scissor \n 3 for paper \n"))

		if(u==1 or u==2 or u==3) : 
			if(u == x ): print("It is a draw")
			elif(u==1 and x == 3) : 
				print("Computer wins")
				lives -= 1
				countcomp +=1						
			elif(u==2 and x == 1) :
				print("Computer wins")
				lives -= 1
				countcomp +=1	
			elif(u==3 and x == 2) :
				print("Computer wins")
				lives -= 1
				countcomp +=1	
			elif(u==3 and x == 1) :  
				print("You win")
				countuser +=1	
			elif(u==1 and x == 2) :
				print("You win")
				countuser +=1	
			elif(u==2 and x == 3) :
				print("You win")
				countuser +=1	
		else : print("invalid input")
		print("Comp : " , countcomp)
		print("User : " , countuser)
 

	if(countcomp > countuser) : 
		print("Computer wins with a score of " , countcomp ,"/" , countuser)
	elif(countcomp < countuser) :
		print("User wins with a score of " , countuser ,"/" , countcomp)
	else :
		print("It is a draw with a score of " , countuser , "/" , countcomp) 


	again = input("Do you want to Play again? \n If Yes : y \n If No : n \n")
	
	while(again != "y" or again != "n") :
		if(again == "y") : main()
		elif(again == "n") : 
			print("Thank You for playing")
			break	
		else : 
			print("Invalid Input , Try Again")
			again = input("Do you want to Play again? \n If Yes : y \n If No : n \n")


if __name__ == '__main__':
	main()