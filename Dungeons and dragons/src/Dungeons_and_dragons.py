import time


def start():
    play = input("\n\n\tWhats up fam? \n\n\t Wanna play some dungeons and dragons babe? y/n")
    if play == "y":
        print("\n\nThanks babe, knew I could count on u, there is a lot of questions lmao <3 - Made by Sam")
        time.sleep(3)
        begin()
    if play == "n":
        print("\n\nWow i spend time making this awful game and you refuse to play it lmaooooooooooo fuk u :(")


def begin():
    print("\n\n\n\n\n\n\n\n\n\nYou approach a creepy old homeless guy on the street, you have 2 options: \n\n 1. Beat him up and take his cash. \n\n 2. Walk off like any sane person would?")
    homeless_guy = input("\n1 or 2?")
    if homeless_guy == "1":
        print("\n\n\n\n\n\n\n\n\n\n\nCongratulations you asshole! \n You just beat up a homeless man! \n You just happend to find 5 grand worth of cash on him.")
        time.sleep(10)
        begin2()
    if homeless_guy == "2":
        print("\n\n\n\n\n\n\n\n\n\n\t As you walk off the homeless guy starts going fucking ballistic, he gets his beer bottle and smashes it over your head, you die from blood loss because you just so happend to live in \n the middle of nowhere called BARRY SCOTT LAND BANG AND THE DIRT IS GONE ville and it would take 5 hours for an ambulance to come \n THE END")
        time.sleep(12)


def begin2():
    print("\n\n\n\n\n\n\n\n\n\n\n\nAs you walk across John Cena land, you see a cave and decide to enter it because the creator making this game said so.")
    print("Suddenly a the dark cave is filled with light, light of a lit bomb fire and a wild feminazi appears.")
    print('It shrieks out the words "HOW DARE YOU WHITE MALE ENTER THIS CAVE, I WILL SACRIFICE YOU TO BLACK LIVES MATTER".')
    print('Shit just hit the fucking fan man, what will you do now?')
    print("\n 1. Try to be logical and rational explaining that you were only entering the cave to view it. \n 2. Stand there awkwardly and do nothing. \n 3. Scream at the feminazi that there are only two genders and you are a neo-nazi")
    feminist = input("\n1, 2, or 3?")
    if feminist == "1":
        print("\nThe feminazi suddenly shrieks in anger as she teleports behind you with her 1337 femmy hacks, rips your head off and sells your organs and donates all the money made from your corpse to anita sarkesian \n THE END")
        time.sleep(10)
        begin2()
    if feminist == "2":
        print("\nThe feminazi pulls out her pistol made by black lives matter and pops a cap in yo ass, you die. \n THE END")
        time.sleep(10)
        begin2()
    if feminist == "3":
        print("\nYou have just triggered the feminazi so fucking hard that she gets a brain aneurysm and died on the spot, you pick up her glock and get the fuck of that cave.")
        time.sleep(10)
        begin3()


def begin3():
    print("\n\n\n\n\n\n\n\n\nYou decide today has been a really fucked up day after encountering a feral feminazi so you hit the bed.")
    print("Approaching your house you see that homeless guy you beat up and stole his money from, this is bad.")
    print("He turns around, the burning rage and hatred in his eyes")
    print("He sprints towards you with his shiv, what do you do?")
    print("\n 1. Give his money back \n 2. Run for your fucking life \n 3. Use the random item in your right pocket \n 4. Use the random item in your left pocket pocket")
    homeless_guy2 = input("1, 2, 3, or 4?")
    if homeless_guy2 == "1":
        print("\n\n\n\n\n\n\n after screaming at him telling him to stop saying you will give his cash back, you try negotiate giving him extra money. \n During this he suddenly pulls out his shiv and stabs you to death. \nTHE END")
        time.sleep(10)
        begin3()
    if homeless_guy2 == "2":
        print("The homeless guy you are running away from just so happend to used to be an olympic sprinter and still kept himself in shape.")
        print("Because of this the guy easily caught up with you and drove the shiv into your right leg rendering you unable to walk.")
        print("He stabs you multiple times leaving you for dead taking all your belongings, you die from blood loss. \n THE END")
        time.sleep(10)
        begin3()
    if homeless_guy2 == "3":
        print("When you were standing still checking your right pocket you found your trusty shiv, you stand firmly ready for him to charge at you.")
        print("The homeless guy jumped onto you and managed to kill you lol, \n THE END")
        time.sleep(10)
        begin3()
    if homeless_guy2 == "4":
        print("Luckily for you, you pull out your glock that you got from that feminazi, the homeless guy shits his pants and runs off never to be seen again. \n You shoot him to death anyways like the asshole you are.")
        time.sleep(10)
        begin4()


def begin4():
    print("\n\n\n\n\t   You finally reach your bed and begin your deep slumber, THE END.    \n\n\t  Thanks for playing ;)")


start()