print("""~~~~~~~~~~Game of cricket~~~~~~~~~~
instructions:
1. You have select any random number from 1 to 6.
2. The computer will also select a number.
3. While batting,if the number selected by you and computer is different,then
your number will add to your runs.if the number selected by you and
computer is same ,then you will lose your wickets.
4. While bowling,if the number selected by you and computer is different,then
the computer's number will add to its runs.if the number selected by you and
computer is same ,then the computer will lose its wickets.
5. Each player will get 2 wickets and 2 overs (12 balls)for batting and
bowling.
6. The innings will end after either the three wickets fell or the overs end.
7. The player with maximum runs wins.""")
print("\n----------Start game----------")
import random
#Toss
print("\nhere comes the toss")
toss=input("choose heads and tails:").lower()
random_toss=random.randint(1,2)
random_opt=random.randint(1,2)
u_opt=0
c_opt=0
if random_toss==2 and toss=="heads":
    print("\nyou won the toss")
    u_opt=input("choose bat and ball:").lower()
elif random_toss==2 and toss=='tails':
    print("\nyou won the toss")
    u_opt=input("choose bat or ball:").lower()
else:
    print("\nyou lost the toss")
    if random_opt==1:
        c_opt="ball"
        print("computer choose to",c_opt)
        

#first innings
print("\n----------first innings begins----------")
runs_1=0
wickets_1=0
balls_1=0
while wickets_1!=2 and balls_1!=12:
    u_choice=int(input("\nchoose any number from 1 to 6:"))
    c_choice=random.randint(1,6)
    if u_choice<1 or u_choice>6:
        print("\nplease choose a value from 1 to 6.")
    else:
        print("your choice:",u_choice,"\ncomputer's choice:",c_choice)
        if u_choice==c_choice:
            wickets_1+=1
        else:
            if u_opt=="bat" or c_opt=="ball":
                bat_first="you"
                ball_first="computer"
                runs_1+=u_choice
            elif u_opt=="ball"or c_opt=="bat":
                bat_first="computer"
                ball_first="you"
                runs_1+=c_choice
        print("\nscore=",runs_1,"/",wickets_1)
        balls_1+=1
        if balls_1==6:
            print("end of over 1")
        elif balls_1==12:
            print("end of over 2")
        print("balls remaining:",12-balls_1)

print("\n----------End of innings----------")

print("\nfinal score:")
print("runs=",runs_1)
print("wickets=",wickets_1)

print("\n",ball_first,"needs",runs_1+1,"runs to win.")

#second innings
print("\n----------Second innings begins----------")

runs_2=0
wickets_2=0
balls_2=0

while wickets_2!=2 and balls_2!=12 and runs_2<=runs_1:
    u_choice=int(input("\nchoose any number from 1 to 6:"))
    c_choice=random.randint(1,6)

    if u_choice<1 or u_choice>6:
        print("\nplease choose a value from 1 to 6.")

    else:
        print("your choice:",u_choice,"\ncomputer's choice:",c_choice)

        if u_choice==c_choice:
            wickets_2+=1
        else:
            if bat_first =="computer":
                runs_2+=c_choice
                bat_second="you"

            elif bat_first=="you":
                runs_2+=c_choice
                bat_second="computer"

        print("\nscore=",runs_2,"/",wickets_2)

        balls_2+=1

        if balls_2==6:
            print("end of over 1")
        elif balls_2==12:
            print("end of over 2")

        if runs_2<=runs_1 and balls_2<=11 and wickets_2!=2:
            print("to win:",runs_1-runs_2+1,"runs needed from",12-balls_2,"balls.")


print("\n----------End of innings----------")

print("\nfinal score:")
print("runs=",runs_2)
print("wickets=",wickets_2)

#Result of match

print("\n~~~~~~~~~~Result~~~~~~~~~~")

if runs_1>runs_2:
      if bat_first=="you":
          print("\ncongratulations! you won the match by",runs_1- runs_2,"runs.")
      else:
          print("\nbetter luck next time!the computer won the match by",runs_-runs_2,"runs.")

elif runs_2>runs_1:

    if bat_second=="you":
        print("\ncongratulations! you won the match by",2-wickets_2,"wickets.")
    else:
        print("\nbetter luck next time! the computer won the match by",2-wickets_2,"wickets.")
elif runs_2>runs_1:
    if bat_second=="you":
        print("\nbetter luck next time! the computer won the match by",2-wickets_2,"wickets,")

else:
    print("the match is a tie.","\nNo on wins.")
        
