import pickle #Pickle is imported from the default python library. It is used to store the members and teams in .pkl files.

#The lists to contain each member as team, members and teams will be objects

class member: #How members are recorded
    def __init__(self, name, score, event):
        self.name = name#Name of member
        self.score = score#Total score for each event
        self.event = event#Events the person is enrolled into


class team: #How teams are recorded
    def __init__(self, teamname, totalscore, members, team_event):
        self.teamname = teamname #Name of the team
        self.totalscore = totalscore #Score which is all of the contestants added together
        self.members = members#Members stored inside a list
        self.team_event = team_event#Events the team is attending


#This is the function to setup a new event, containing both the team and individuals
def setup():

    print("\nInputting individuals:")

    for x in range(20): # Change this in order to change individual members
        
        attending = []

        name_ind = input("\nPlease input a name\n")
 
        #IMPORTANT: INDIVIDUALS CAN ONLY DO ACHEDEMIC EVENTS WHILE TEAMS CAN DO EITHER
        while True:
            ans_attending = input("\nIs the individual participating in the art competition? Y/N\n")

            if ans_attending == "y" or ans_attending == "Y":
                attending.append("ART")
                break
            elif ans_attending == "n" or ans_attending == "N":
                break
            else:
                print("\nPlease input Y or N\n")

        while True:
            ans_attending = input("\nIs the individual participating in trivia? Y/N\n")

            if ans_attending == "y" or ans_attending == "Y":
                attending.append("TRIVIA")
                break
            elif ans_attending == "n" or ans_attending == "N":
                break
            else:
                print("\nPlease input Y or N\n")

        while True:
            ans_attending = input("\nIs the individual participating in writing? Y/N\n")

            if ans_attending == "y" or ans_attending == "Y":
                attending.append("WRITING")
                break
            elif ans_attending == "n" or ans_attending == "N":
                break
            else:
                print("\nPlease input Y or N\n")
    
        individual = member(name_ind, 0, attending)

        individual_members.append(individual)
    
        print(individual_members[x].event)


    print("\nInputting teams:")

    for x in range(4): # The start of the loop to input teams, the number controlls the amount of teams

        attending = []
        teamnames = []

        name_team = input("\nPlease input a team name\n")



        for x in range(5):#Input each member,the number controlls the amount of teams
            name_ind = input("\nPlease input a name:\n")
            teamnames.append(name_ind)
            #input each name

    #IMPORTANT: INDIVIDUALS CAN ONLY DO ACHEDEMIC EVENTS WHILE TEAMS CAN DO EITHER
        while True:
            ans_attending = input("\nIs the team participating in the group trivia competition? Y/N\n")

            if ans_attending == "y" or ans_attending == "Y":
                attending.append("TRIVIA")
                break
            elif ans_attending == "n" or ans_attending == "N":
                break
            else:
                print("\nPlease input Y or N\n")

        while True:
            ans_attending = input("\nIs the team participating in the football competition? Y/N\n")

            if ans_attending == "y" or ans_attending == "Y":
                attending.append("FOOTBALL")
                break
            elif ans_attending == "n" or ans_attending == "N":
                break
            else:
                print("\nPlease input Y or N\n")

        while True:
            ans_attending = input("\nIs the team participating in the group running competition? Y/N\n")

            if ans_attending == "y" or ans_attending == "Y":
                attending.append("RUNNING")
                break
            elif ans_attending == "n" or ans_attending == "N":
                break
            else:
                print("\nPlease input Y or N\n")
        
        teamentry = team(name_team, 0, teamnames, attending)

        teams.append(teamentry)

    with open('members.pkl', 'wb') as f:  # open a text file
        pickle.dump(individual_members, f) # serialize the list

    with open('teams.pkl', 'wb') as f:  # open a text file
        pickle.dump(teams, f) # serialize the list


#Scoring menu for the program for the user to add points for every user in an event
def scoring():
    while True:
        #switch statement to check for answer and to redirect to relevent function
        answer = input("\nInput which event you want to prepare the scoring for:\n\n[1] - Art\n\n[2] - Solo trivia\n\n[3] - Writing\n\n[4] - Group Trivia\n\n[5] - Football\n\n[6] - Running\n\n[Q] - Quit to selection\n\n")

        match answer:
            case "1":
                for member in individual_members:
                    if "ART" in member.event:
                        while True:
                            score = int(input(f"\nPlease input the score of {member.name} in art:\n\n"))
                            if score < 0:
                                member.score += score
                            else:
                                print("\nScore must not be negative")
        
                    with open('members.pkl', 'wb') as f:  # open a text file
                        pickle.dump(individual_members, f) # serialize the list

            case "2":
                for member in individual_members:
                    if "TRIVIA" in member.event:
                        while True:
                            score = int(input(f"\nPlease input the score of {member.name} in trivia:\n\n"))
                            if score < 0:
                                member.score += score
                            else:
                                print("\nScore must not be negative")
    
                with open('members.pkl', 'wb') as f:  # open a text file
                    pickle.dump(individual_members, f) # serialize the list

            case "3":
                for member in individual_members:
                    if "WRITING" in member.event:
                        while True:
                            score = int(input(f"\nPlease input the score of {member.name} in writing:\n\n"))
                            if score < 0:
                                member.score += score
                            else:
                                print("\nScore must not be negative")

                    with open('members.pkl', 'wb') as f:  # open a text file
                        pickle.dump(individual_members, f) # serialize the list

            case "4":
                for team in teams:
                    while True:
                        if "TRIVIA" in team.team_event:
                            score = int(input(f"\nPlease input the score of {team.teamname} in group trivia:\n\n"))
                            if score < 0:
                                member.score += score
                            else:
                                print("\nScore must not be negative")

                with open('teams.pkl', 'wb') as f:  # open a text file
                    pickle.dump(teams, f) # serialize the list

            case "5":
                for team in teams:
                    while True:
                        if "FOOTBALL" in team.team_event:
                            score = int(input(f"\nPlease input the score of {team.teamname} in football:\n\n"))
                            if score < 0:
                                member.score += score
                            else:
                                print("\nScore must not be negative")

                        with open('teams.pkl', 'wb') as f:  # open a text file
                            pickle.dump(teams, f) # serialize the list

            case "6":
                for team in teams:
                    while True:
                        if "RUNNING" in team.team_event:
                            score = int(input(f"\nPlease input the score of {team.teamname} in running:\n\n"))
                            if score < 0:
                                member.score += score
                            else:
                                print("\nScore must not be negative")

                with open('teams.pkl', 'wb') as f:  # open a text file
                    pickle.dump(teams, f) # serialize the list

            case "Q" | "q": #takes the user back to the main selection page
                selection()

            case _:
                print("\nPlease input one of the available choices")
    

#Prints every member and team, including their points
def tally():
    for member in individual_members:
        print(f"{member.name} has a total score of {member.score}")

    for team in teams:
        print(f"{team.teamname} has a score of {team.totalscore}, the members of this team are {team.members}")


#reset password function
def password_reset():
    while True:
        while True:
            password = input("\nPlease enter a new password\n")
            password_check = input("\nPlease re-enter the password\n")
            if password == password_check:
                print("\nPassword saved successfully!")
                with open("password.txt" , "w") as f:
                    f.write(password)
                    f.close
            else:
                print("Passwords do not match, please try again")


#Shuts down the program
def quit():
    exit()


#The menu which allows the user to select which function of the program they wish to execute
def selection():
    while True:
        answer = input("\nInput the number corresponding to the process:\n\n[1] - Create new event\n\n[2] - Assign scores\n\n[3] - Show current tally\n\n[4] - Reset password\n\n[Q] - Quit\n\n")


        #switch statement to check for answer and to redirect to relevent function
        match answer:
            case "1":
                setup() #Sets up a new event
            case "2":
                if individual_members == [] or teams == []: # checks to see if a new event has been made
                    print("\nThere are no teams or members set, please create a new event first")
                else:
                    scoring()#scoring menu
            case "3":
                if individual_members == [] or teams == []: # checks to see if a new event has been made
                    print("\nThere are no teams or members set, please create a new event first")
                else:
                    tally()#Displays names and points
            case "4":
                password_reset()#resets the password
            case "Q" | "q": 
                quit()#Ends the program
            case _:
                print("\nPlease input one of the available choices")


#The progam tries to load things here, if it fails it assigns lists for functions to use later
try:
    with open('members.pkl', 'rb') as f:

        individual_members = pickle.load(f) # deserialize using load()
except:
    individual_members = []

try:
    with open('teams.pkl', 'rb') as f:

        teams = pickle.load(f) # deserialize using load()
except:
    teams = []
                

#Password query/setting
try:#Tries to open file
    with open("password.txt", "r") as f:
        saved_password = f.read()
except:#If it fails to open the file it asks the user to set a password
    while True:
        password = input("\nPlease enter a new password\n\n")
        password_check = input("\nPlease re-enter the password\n\n")

        if password == password_check:
            with open("password.txt" , "w") as f: #Makes a file to store the password
                f.write(password)
                f.close
            print("\nPassword saved successfully!")
            break
        else: 
            print("Passwords do not match, please try again")
else:
    while True: #Password check
        password = input("\nInput your password\n\n")

        if password == saved_password:
            break
        else:
            print("Password is incorrect")   

selection() #executes the rest of the program