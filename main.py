import random
from pyfiglet import Figlet #for ASCII art (Source:https://pypi.org/project/pyfiglet/)
from time import sleep #To induce delay in the code for game related features (Source:https://docs.python.org/3/library/time.html)
from zchar import winning_monster2,monster2,winning_hero4,winning_monster_dead,winning_hero_deto,glenwald_kingdom, monster4, monster5, monster9_, monsterv1,wsage,winning_monster_dead2,winning_monster_scrum3,monster15,monster9,monster11,monster10_8,winning_hero_scrum,monster14
from zhero import hero0, hero_su_c,hero_stance, hero_su, herot0
from rich.console import Console # To get coloured statements in the terminal window #cite the origins of this (Source:https://rich.readthedocs.io/en/stable/console.html)
from rich.panel import Panel #For panels in the game title (Source:https://rich.readthedocs.io/en/stable/console.html)
from rich import box
from zscrabble import scramble # A function that convert normal words into scrabbled words in a random order
from inputimeout import inputimeout, TimeoutOccurred # To have time dependent gameplay. (Source:https://pypi.org/project/inputimeout/)
from zanimation2 import sword_attack, sword_attack2,deto_att,deto_att2,deto_win, sceptre_ani
from zanimation1 import battle3,thunder, meteor, hero_att, hail_att,unicorn,pegasus,poison_att,fire_att,win,boss2
from zboss import veldrek_win


figlet= Figlet(width=80)
figlet.setFont(font= "standard")
c = Console(width=80)
p = Panel


def ability(num): #Allows the player to activate abilities
    if num == 3:
        return "monh" #Monster health decreased
    elif num == 2:
        return "wara" #Warrior Attack increased
    elif num == 5:
        return "warh" #Warrior health increased
    else:
        return "af"


def generate_integer(level):
    if level == 1:
        num = random.randint(100,999)
        return num
    elif level == 2:
        num = random.randint(1000,9999)
        return num
    elif level == 3:
        num = random.randint(10,999)
        return num


def calc(x,y):
    while True:
        c.print("\nTime starts now....⌛", style= "red")
        #sleep(1)
        try:
            user_inp= int(inputimeout(prompt= (f"\nType the Neutralization code for {x} + {y}:  "),timeout=20)) #Give the sourse of this technique
        except (TimeoutOccurred, ValueError):
            user_inp = -1
        if user_inp == -1:
            c.print("\nTime's up⌛", style="red")
        return [user_inp, x+y]


def start():
    for _ in range(2):
        print(" ")
    print("------------------------------------------------------------------")
    sleep(0.5)
    c.print(p.fit("WELCOME TO THE GAME: ⚔️  MONSTERS OF GLENWALD🛡️ ", style="green", box=box.ROUNDED)) #CITE its source
    sleep(3)
    while True:
        start = input("\nPress '$' to start the story / press 'S' to skip story: ").lower()
        if start == "$":
            c.print("Starting story...", style="blue")
            sleep(3)
            c.print("\n\nOnce upon a time there was the ancient Kingdom of Glenwald. It was known for its prosperity, heartwarming people and friendly culture.", style="blue")
    #Introduce the kingdom
            sleep(7)
            print(glenwald_kingdom)
            sleep(7)
            c.print("\nUnder King Glenwald people lived very fullfilling lives.",style="blue")
    #Introduce the king
            sleep(4)
            print(hero0)
            c.print("King Glenwald - the Brave", style="green")
            sleep(4)
            c.print("\n\nBut one day, the monster King VELDREK attacked on the kingdom with his monster army...", style="blue")
            sleep(4)
    #introduce the monsters
            print(monster4)
            c.print("VELDREK - the vampire king! \n\nHe is the leader of the monsters, who is known for his ruthlessness and powerful cannon blasts!",style = "red")
            print("------------------------------------------------------------------")
            sleep(6)
            print(monster5)
            c.print("DETONARCH - the destroyer! \n\nRight hand of King VELDREK. Known for his destructive bombs that he carries in his chest!", style="red")
            print("------------------------------------------------------------------")
            sleep(5)
            print(monster9_)
            c.print("SCRUM - alien insectoid from beyond the stars! \n\nGeneral of King VELDREK's army. He is the most intelligent and only wits and fast thinking can defeat him. ", style="red")
            print("------------------------------------------------------------------")
            sleep(5)
            print(monsterv1)
            c.print("GRINWRECK - the laughing ghoul that feeds on fear! \n\nCommander in the army of VELDREK. ", style="red")
            print("------------------------------------------------------------------")
            sleep(5)
            c.print("\nNow, with his wits, strength and the help of some unexpected allies, King Glenwald must defeat the monsters for once and all.", style="blue")
            sleep(6)
            break
        elif start == "s":
            break
        else:
            c.print("Invalid input. Try again...", style="red")


def action(life,wh=150,wa=40,mh=300,ma=20):
    hero_poses= [herot0,hero_su,hero_stance]
    num1=["1","2","3","4","5","6","7","8","9","10"]
    count=True
    while True:
        inp = input("Choose a number between 1 to 10 to move King Glenwald: ")
        if inp in num1:
            player_action = int(inp)
            print("------------------------------------------------------------------")
            monster_action= random.randint(1,10)
            if (monster_action+ player_action)%2 ==0:
                mh -= wa
                c.print("\nGreat Job...⚔️ 🛡️  Your attack on the monster was successful!!", style ="green")
                if mh<=0:
                    print("\n",winning_hero4)
                    print("------------------------------------------------------------------")
                    c.print("Congratulations! You have defeated GRINWRECK..🎉", style="green")
                    return life
                elif mh>0:
                    hero_order= random.randint(0,2)
                    print(hero_poses[hero_order])
                    c.print(f"\nMonster health decreased... by {wa} points 🗡️", style="green")
                    print("\nMonster health 💀          :",mh)
                    print("King health 🧔             :",wh)
                    print("Monster attack strength 🔪 :", ma)
                    print("King attack strength ⚔️     :", wa)
                    print(f"King life 👑               : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")

            else:
                wh-= ma
                c.print("\nOh no...💀 The monster sneaked up and attacked you!", style="red")
                if wh<=0 and life > 0:
                    life-=1
                    if life >=1:
                        print("\n",winning_monster2)
                        print("------------------------------------------------------------------")
                        c.print("GRINWRECK defeated you..😢", style ="red")
                        sleep(2)
                    if life == 0 and wh<=0:
                        print("\n",winning_monster_dead)
                        print("------------------------------------------------------------------")
                        c.print("So sorry, you have lost the Game..😢💀", style ="red")
                        return life #returning life here so that the fure programm can undeerstand that life is over and not execute
                    elif life > 0:
                        print(f"King lives remaining:{life*'❤️ '}\n")
                        sleep(2)
                        while life>0:
                            renew_life = input("\nPress '0' to use another life: ")
                            if renew_life == "0":
                                sleep(3)
                                c.print("\nBattle with GRINWRECK restarted....Good Luck!\n", style="blue")
                                sleep(2)
                                life = action(life,wh=150,wa=40,mh=300,ma=20)
                                return life #returns life so that this life value can be used further in the program
                            else:
                                c.print("Invalid input. Try again..", style ="red")
                elif wh>0:
                    print(monster2)
                    c.print(f"\nKing health decreased... by {ma} points 💥", style= "red")
                    print("\nMonster health 💀          :",mh)
                    print("King health 🧔             :",wh)
                    print("Monster attack strength 🔪 :", ma)
                    print("King attack strength ⚔️     :", wa)
                    print(f"King life 👑               : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")

                if wh<=50 and count== True:
                    c.print("King health low. Time for the ability to kick in...!!",style="yellow")
                    count = False
                    num = random.randint(1,5)
                    ability_key = ability(num)
                    sleep(1)
                    if ability_key == "monh":
                        mh-=80
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You used the mysterious spell.... 🪄", style="magenta")
                        sleep(3)
                        c.print(f"Monster health decreased by... 80 points ✨", style = "green")
                        print("------------------------------------------------------------------","\n")
                        sleep(1.5)
                        if mh <=0:
                            print("\n",winning_hero4)
                            print("------------------------------------------------------------------")
                            c.print("Congratulations! You have defeated GRINWRECK..🎉", style="green")
                            return life

                    elif ability_key == "wara":
                        wa+=30
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You received the battle axe.... 🪓 ", style="magenta")
                        sleep(3)
                        c.print(f"King damage boosted by... 30 points ✨", style = "green")
                        c.print("King attack increased to:",wa,style= "green")
                        print("------------------------------------------------------------------","\n")
                        sleep(1.5)
                    elif ability_key == "warh":
                        wh+=60
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You used health orb.... 🔮 ", style= "magenta")
                        sleep(3)
                        c.print(f"King health boosted by... 60 points ✨", style = "green")
                        print("------------------------------------------------------------------","\n")
                        if mh<=0:
                            print("\n",winning_hero4)
                            print("------------------------------------------------------------------")
                            c.print("Congratulations! You have defeated GRINWRECK..🎉", style="green")
                            return life
                        sleep(1.5)
                    elif ability_key == "af":
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("Bad luck! Ability activation failed 😞", style="magenta")
                        print("------------------------------------------------------------------","\n")
                        sleep(1)
                    print("\nMonster health 💀          :",mh)
                    print("King health 🧔             :",wh)
                    print("Monster attack strength 🔪 :", ma)
                    print("King attack strength ⚔️     :", wa)
                    print(f"King life 👑               : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")
        else:
            c.print("Invalid input. Try again...\n",style="red")


def action2(life,wh=160,wa=50,mh=250,ma=40):
    hero_poses= [herot0,hero_su,hero_stance]
    mon_poses = [monster15,monster10_8,monster9,monster11,monster14]
    count=True
    while True:
        c.print("\nOH NO, SCRUM IS COMING TO ATTACK US!!", style="red")
        sleep(1)
        player_action = input("\nHurry! press 'H' for HINT🕯️ : ").lower()
        if player_action == "h":
            c.print("\nThe Gods listened! Get ready to decipher the magic word from their HINT!",style="blue")
            sleep(2)
            word = scramble()
            c.print("\nGuess and type the magic word in '20 seconds'!", style ="blue")
            sleep(2)
            c.print("HINT: ", word[1],style="magenta")
            sleep(2.5)
            player_answer={"answer":None}
            def user_inp():
                c.print("\nTime starts now....⌛", style= "red")
                #sleep(1)
                try:
                    answer = inputimeout(prompt= ("\nType the magic word: "), timeout=20).upper().strip() #Give citation and reference to this technique
                    player_answer["answer"]= answer
                except TimeoutOccurred: #cite sourse of this
                    player_answer["answer"]= "def00"
                if player_answer["answer"] == "def00": #If the user is not able to answer on time. Give user input the dummy value of def00. Why "def00", cause its very unlikely to be one of the answers to the input question.
                    c.print("\nTime's up⌛", style="red")
                return player_answer["answer"]
            user_word= user_inp()
            sleep(1)
            if user_word != word[0] or user_word=="def00":
                c.print(f"\nYou couldn't guess the magic word '{word[0]}' in time!", style ="red")
                print("------------------------------------------------------------------")
                sleep(3)
                wh-= ma
                c.print("\nOh no...👾 The monster sneaked up and attacked you!", style="red")
                if wh<=0:
                    life-=1
                    if life > 0:
                        print("\n",winning_monster_scrum3)
                        print("------------------------------------------------------------------")
                        c.print("SCRUM defeated you..😢", style ="red")
                        sleep(1)
                        print(f"King lives remaining:{life*'❤️ '}\n")
                        while life >0:
                            sleep(1)
                            renew_life = input("\nPress '0' to use another life: ")
                            if renew_life == "0":
                                sleep(2)
                                c.print("\nBattle with SCRUM restarted....Good Luck!\n", style="blue")
                                sleep(1)
                                life = action2(life,wh=160,wa=50,mh=250,ma=40)
                                return life
                            else:
                                c.print("Invalid input. Try again..", style="red")
                    elif life == 0:
                        print("\n",winning_monster_dead2)
                        print("------------------------------------------------------------------")
                        sleep(1)
                        c.print("So sorry, you lost the Game..😢☠️", style ="red")
                        break
                elif wh>0:
                    mon_order= random.randint(0,4)
                    print(mon_poses[mon_order])
                    sleep(1)
                    c.print(f"\nKing health decreased... by {ma} points 💥", style= "red")
                    print("\nMonster health 👾       :",mh)
                    print("King health 🧔          :",wh)
                    print("Monster attack damage ꥟ :", ma)
                    print("King attack strength ⚔️  :", wa)
                    print(f"King life 👑            : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")
                    sleep(2)

                if wh<=50 and count== True:
                    c.print("King health low. Time for the ability to kick in...!!",style="yellow")
                    count = False
                    num = random.randint(1,5)
                    ability_key = ability(num)
                    sleep(1)
                    if ability_key == "monh":
                        mh-=80
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You used the mysterious spell.... 🪄", style="magenta")
                        sleep(3)
                        c.print(f"Monster health decreased by... 80 points ✨", style = "green")
                        print("------------------------------------------------------------------","\n")
                        sleep(1.5)
                        if mh <=0:
                            print("\n",winning_hero_scrum)
                            print("------------------------------------------------------------------")
                            sleep(1)
                            c.print("Congratulations! You have defeated SCRUM..🎉", style="green")
                            return life
                    elif ability_key == "wara":
                        wa+=40
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You received the battle axe.... 🪓 ", style="magenta")
                        sleep(3)
                        c.print(f"King damage boosted by... 40 points ✨", style = "green")
                        c.print("King attack increased to:",wa,style= "green")
                        print("------------------------------------------------------------------","\n")
                        sleep(1.5)
                    elif ability_key == "warh":
                        wh+=60
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You used health orb.... 🔮 ", style= "magenta")
                        sleep(3)
                        c.print(f"King health boosted by... 60 points ✨", style = "green")
                        print("------------------------------------------------------------------","\n")
                        if mh<=0:
                            print("\n",winning_hero_scrum)
                            print("------------------------------------------------------------------")
                            c.print("Congratulations! You have defeated SCRUM..🎉", style="green")
                            break
                        sleep(1.5)
                    elif ability_key == "af":
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("Bad luck! Ability activation failed 😞", style="magenta")
                        print("------------------------------------------------------------------","\n")
                        sleep(1)

                    print("\nMonster health 👾       :",mh)
                    print("King health 🧔          :",wh)
                    print("Monster attack damage ꥟ :", ma)
                    print("King attack strength ⚔️  :", wa)
                    print(f"King life 👑            : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")
                    sleep(2)

            elif user_word== word[0]:
                sleep(2)
                c.print("\nYou guessed the magic word!", style ="green")
                print("------------------------------------------------------------------")
                mh -= wa
                sleep(1)
                c.print("\nGreat Job...⚔️ 🛡️  Your attack on the monster was successful!!", style ="green")
                if mh<=0:
                    print("\n",winning_hero_scrum)
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("Congratulations! You have defeated SCRUM..🎉", style="green")
                    return life
                elif mh>0:
                    hero_order= random.randint(0,2)
                    print(hero_poses[hero_order])
                    sleep(2)
                    c.print(f"\nMonster health decreased... by {wa} points 🗡️", style="green")
                    print("\nMonster health 👾       :",mh)
                    print("King health 🧔          :",wh)
                    print("Monster attack damage ꥟ :", ma)
                    print("King attack strength ⚔️  :", wa)
                    print(f"King life 👑            : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")
                    sleep(2)
        else:
            c.print("Invalid input. Try again..",style ="red")


def action3(life,wh=200,wa=90,mh=290,ma=80):
    count=True
    while True:
        c.print("\nWATCH OUT! DETONARCH THREW A BOMB AT YOU!!", style="red")
        sleep(1)
        player_action = input("\nFast! press 'N' to neutralize the bomb💣 : ").lower()
        if player_action == "n":
            level1 = random.randint(1,3)
            level2 = random.randint(1,3)
            x= generate_integer(level1)
            y= generate_integer(level2)
            c.print("\nHurry! Calculate the neutralizing code from the equation in '20 seconds'",style="blue")
            sleep(2)
            user= calc(x,y)
            user_answer=user[0]
            answer= user[1]
            sleep(1)
            if user_answer !=answer or user_answer== -1:
                c.print(f"\nYou couldn't get the neutralizing code '{answer}' in time!", style ="red")
                print("------------------------------------------------------------------")
                sleep(3)
                wh-= ma
                c.print("\nOh no...👺 The bomb coundn't be neutralized!", style="red")
                if wh<=0:
                    life-=1
                    if life>0:
                        print("\n")
                        deto_win()
                        print("------------------------------------------------------------------")
                        c.print("DETONARCH defeated you..😢", style ="red")
                        sleep(1)
                        print(f"King lives remaining:{life*'❤️ '}\n")
                        while life >0:
                            sleep(1)
                            renew_life = input("\nPress '0' to use another life: ")
                            if renew_life == "0":
                                sleep(2)
                                c.print("\nBattle with DETONARCH restarted....Good Luck!\n", style="blue")
                                sleep(1)
                                life = action3(life,wh=200,wa=90,mh=290,ma=80)
                                return life
                            else:
                                c.print("Invalid input. Try again..", style="red")
                    elif life == 0:
                        print("\n")
                        deto_win()
                        print("------------------------------------------------------------------")
                        sleep(1)
                        c.print("So sorry, you lost the Game..😢☠️", style ="red")
                        break
                elif wh>0:
                    sleep(1)
                    mon_att = random.randint(1,2)
                    if mon_att == 1:
                        deto_att()
                    else:
                        deto_att2()
                    sleep(2)
                    c.print(f"\nKing health decreased... by {ma} points 💥", style= "red")
                    print("\nMonster health 👺       :",mh)
                    print("King health 🧔          :",wh)
                    print("Monster bomb damage 💣  :", ma)
                    print("King attack strength ⚔️  :", wa)
                    print(f"King life 👑            : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")
                    sleep(2)
                if wh<=50 and count== True:
                    c.print("King health low. Time for the ability to kick in...!!",style="yellow")
                    count = False
                    num = random.randint(1,5)
                    ability_key = ability(num)
                    sleep(1)
                    if ability_key == "monh":
                        mh-=90
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You used the mysterious spell.... 🪄", style="magenta")
                        sleep(3)
                        c.print(f"Monster health decreased by... 90 points ✨", style = "green")
                        print("------------------------------------------------------------------","\n")
                        sleep(1)
                        if mh <=0:
                            print("\n",winning_hero_deto)
                            print("------------------------------------------------------------------")
                            sleep(1)
                            c.print("Congratulations! You have defeated DETONARCH..🎉", style="green")
                            sleep(4)
                            c.print("\nAs a token of victory, ARIMA offered KING GLENWALD the Scroll of priests 📜 and her SCEPTRE..", style="magenta")
                            sleep(4)
                            c.print("\nThe SCEPTRE grants its wielder the power to summon meteors☄️  and thunder⚡ attacks!", style="magenta")
                            sleep(5)
                            sceptre_ani()
                            sleep(1.5)
                            return life
                    elif ability_key == "wara":
                        wa+=40
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You received the battle axe.... 🪓 ", style="magenta")
                        sleep(3)
                        c.print(f"King damage boosted by... 40 points ✨", style = "green")
                        c.print("King attack increased to:",wa,style= "green")
                        print("------------------------------------------------------------------","\n")
                        sleep(1)
                    elif ability_key == "warh":
                        wh+=100
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("You used health orb.... 🔮 ", style= "magenta")
                        sleep(3)
                        c.print(f"King health boosted by... 100 points ✨", style = "green")
                        print("------------------------------------------------------------------","\n")
                        sleep(1)
                    elif ability_key == "af":
                        sleep(2)
                        print("------------------------------------------------------------------")
                        c.print("Bad luck! Ability activation failed 😞", style="magenta")
                        print("------------------------------------------------------------------","\n")
                        sleep(1)
                    print("\nMonster health 👺       :",mh)
                    print("King health 🧔          :",wh)
                    print("Monster bomb damage 💣  :", ma)
                    print("King attack strength ⚔️  :", wa)
                    print(f"King life 👑            : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")
                    sleep(2)
            elif user_answer== answer:
                sleep(2)
                c.print("\nYou neutralized the bomb!", style ="green")
                print("------------------------------------------------------------------")
                mh -= wa
                sleep(1)
                c.print("\nGreat Job...⚔️ 🛡️  You attacked DETONARCH!!", style ="green")
                if mh<=0:
                    print("\n",winning_hero_deto)
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("Congratulations! You have defeated DETONARCH..🎉", style="green")
                    sleep(4)
                    c.print("\nAs a token of victory, ARIMA offered KING GLENWALD the Scroll of priests 📜 and her SCEPTRE..", style="magenta")
                    sleep(4)
                    c.print("\nThe SCEPTRE grants its wielder the power to summon meteors☄️  and thunder⚡ attacks!", style="magenta")
                    sleep(5)
                    sceptre_ani()
                    sleep(1)
                    return life
                elif mh>0:
                    sleep(3)
                    hero_att = random.randint(1,2)
                    if hero_att ==1:
                        sword_attack2()
                    else:
                        sword_attack()
                    sleep(1)
                    c.print(f"\nMonster health decreased... by {wa} points 🗡️", style="green")
                    print("\nMonster health 👺       :",mh)
                    print("King health 🧔          :",wh)
                    print("Monster bomb damage 💣  :", ma)
                    print("King attack strength ⚔️  :", wa)
                    print(f"King life 👑            : {life*'❤️ '}\n")
                    print("------------------------------------------------------------------")
                    sleep(2)
        else:
            c.print("Invalid input. Try again..",style ="red")


def veldrek_moves(life,wh,mh,curse,pd,poison_damage,ars,ts,ms,mb):
    n= random.randint(1,3)
    if n==1:
        acc=random.randint(1,10)
        c.print("\nVELDREK used Fire Blast! ( Damage: 160 | accuracy: 60 % )", style="red")
        if acc<7:#7
            sleep(1.5)
            fire_att()
            wh-=160
            if wh<=0:
                life-=1
                if life >0:
                    print("\n------------------------------------------------------------------")
                    sleep(2)
                    c.print("VELDREK defeated you..😢", style ="red")
                    sleep(3)
                    print(veldrek_win)
                    while life >0:
                        sleep(1)
                        print(f"King lives remaining:{life*'❤️ '}\n")
                        sleep(1)
                        renew_life = input("\nPress '0' to use another life: ")
                        if renew_life == "0":
                            sleep(2)
                            c.print("\nBattle with VELDREK restarted....Good Luck!", style="blue")
                            sleep(1)

                            restart = random.randint(1,10)
                            if restart%2 ==0:
                                veldrek_moves(life,wh=800,mh=800,curse= True,pd=3,poison_damage=False,ars=10,ts=3,ms=3,mb=2)
                                return
                            else:
                                hero_moves(life,ars=10,ts=3,ms=3,wh=800,mh=800,curse=True,pd=3,poison_damage=False,mb=2)
                                return
                        else:
                            c.print("\nInvalid input. Try again..", style ="red")
                elif life == 0:
                    print("\n")
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("So sorry, you lost to VELDREK..😢☠️", style ="red")
                    sleep(3)
                    boss2()
                    sleep(2)
                    c.print(figlet.renderText("\nYou lost the game !"), style = "red")
                    return
            c.print(f"\nKing health decreased... by '160' points 💥", style= "red")
        else:
            sleep(2.5)
            c.print("\nVELDREK's attack missed!", style="green")
    elif n==2:
        acc=random.randint(1,10)
        c.print("\nVELDREK used Ice Blast! ( Damage: 100 | accuracy: 70 % )", style="red")
        if acc<8:#8
            sleep(1.5)
            hail_att()
            wh-=100
            if wh<=0:
                life-=1
                if life >0:
                    print("\n------------------------------------------------------------------")
                    sleep(2)
                    c.print("VELDREK defeated you..😢", style ="red")
                    sleep(3)
                    print(veldrek_win)
                    while life >0:
                        sleep(1)
                        print(f"King lives remaining:{life*'❤️ '}\n")
                        sleep(1)
                        renew_life = input("\nPress '0' to use another life: ")
                        if renew_life == "0":
                            sleep(2)
                            c.print("\nBattle with VELDREK restarted....Good Luck!", style="blue")
                            sleep(1)

                            restart = random.randint(1,10)
                            if restart%2 ==0:
                                veldrek_moves(life,wh=800,mh=800,curse= True,pd=3,poison_damage=False,ars=10,ts=3,ms=3,mb=2)
                                return
                            else:
                                hero_moves(life,ars=10,ts=3,ms=3,wh=800,mh=800,curse=True,pd=3,poison_damage=False,mb=2)
                                return
                        else:
                            c.print("\nInvalid input. Try again..", style ="red")
                elif life == 0:
                    print("\n")
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("So sorry, you lost to VELDREK..😢☠️", style ="red")
                    sleep(3)
                    boss2()
                    sleep(2)
                    c.print(figlet.renderText("\nYou lost the game !"), style = "red")
                    return
            c.print(f"\nKing health decreased... by '100' points 💥", style= "red")
        else:
            sleep(2.5)
            c.print("\nVELDREK's attack missed!", style="green")
    else:
        acc=random.randint(1,10)
        c.print("\nVELDREK used Poison Shot! ( Damage: 80 | accuracy: 80 % )", style="red")
        if acc<9:#9
            sleep(1.5)
            poison_att()
            wh-=80
            sleep(2)
            c.print(f"\nKing health decreased... by '80' points 💥", style= "red")
            if wh<=0:
                life-=1
                if life >0:
                    print("\n------------------------------------------------------------------")
                    sleep(2)
                    c.print("VELDREK defeated you..😢", style ="red")
                    sleep(3)
                    print(veldrek_win)
                    while life >0:
                        sleep(1)
                        print(f"King lives remaining:{life*'❤️ '}\n")
                        sleep(1)
                        renew_life = input("\nPress '0' to use another life: ")
                        if renew_life == "0":
                            sleep(2)
                            c.print("\nBattle with VELDREK restarted....Good Luck!", style="blue")
                            sleep(1)
                            restart = random.randint(1,10)
                            if restart%2 ==0:
                                veldrek_moves(life,wh=800,mh=800,curse= True,pd=3,poison_damage=False,ars=10,ts=3,ms=3,mb=2)
                                return
                            else:
                                hero_moves(life,ars=10,ts=3,ms=3,wh=800,mh=800,curse=True,pd=3,poison_damage=False,mb=2)
                                return
                        else:
                            c.print("\nInvalid input. Try again..", style ="red")
                elif life == 0:
                    print("\n")
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("So sorry, you lost to VELDREK..😢☠️", style ="red")
                    sleep(3)
                    boss2()
                    sleep(2)
                    c.print(figlet.renderText("\nYou lost the game !"), style = "red")
                    return
            poison=random.randint(1,10)
            if poison>6 and poison_damage == False:
                poison_damage=True
                sleep(3)
                c.print("\nKing is poisoned by poison shot. Its effect stays for '3' turns!", style="magenta")
                sleep(2)
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
        else:
            sleep(2.5)
            c.print("\nVELDREK's attack missed!", style="green")

    if pd < 1:
        pd=3
        poison_damage=False
        sleep(2)
        c.print("\n👑 King is healed from poison!", style="green")
    if poison_damage == True:
        pd-=1
        wh-=30
        sleep(1)
        c.print("\nKing is affected by Poison!☠️", style="magenta")
        sleep(2)
        c.print("\nKing health decreased by '30' points!", style="red")
        sleep(1)
        if wh<=0:
                life-=1
                if life >0:
                    print("\n------------------------------------------------------------------")
                    sleep(2)
                    c.print("VELDREK defeated you..😢", style ="red")
                    sleep(3)
                    print(veldrek_win)
                    while life >0:
                        sleep(1)
                        print(f"King lives remaining:{life*'❤️ '}\n")
                        sleep(1)
                        renew_life = input("\nPress '0' to use another life: ")
                        if renew_life == "0":
                            sleep(2)
                            c.print("\nBattle with VELDREK restarted....Good Luck!", style="blue")
                            sleep(1)
                            restart = random.randint(1,10)
                            if restart%2 ==0:
                                veldrek_moves(life,wh=800,mh=800,curse= True,pd=3,poison_damage=False,ars=10,ts=3,ms=3,mb=2)
                                return
                            else:
                                hero_moves(life,ars=10,ts=3,ms=3,wh=800,mh=800,curse=True,pd=3,poison_damage=False,mb=2)
                                return
                        else:
                            c.print("\nInvalid input. Try again..", style ="red")
                elif life == 0:
                    print("\n")
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("So sorry, you lost to VELDREK..😢☠️", style ="red")
                    sleep(3)
                    boss2()
                    sleep(2)
                    print()
                    c.print(figlet.renderText("You lost the game !"), style = "red")
                    return
    sleep(2)
    print("\nMonster health 👿 :",mh)
    print("King health 🧔    :",wh)
    print(f"King life 👑      : {life*'❤️ '}")
    print("------------------------------------------------------------------")

    if curse == True:
        vampire_curse= random.randint(1,10)
        if vampire_curse == 5 :
            sleep(4)
            c.print("\n🦇 VELDREK used the Vampire's Curse ability... 🦇", style ="red")
            sleep(5)
            c.print("\n👿 VELDREK's health increased by '250' points!", style ="red")
            mh+=250
            sleep(2)
            print("\nMonster health 👿 :",mh)
            print("King health 🧔    :",wh)
            print(f"King life 👑      : {life*'❤️ '}")
            print("------------------------------------------------------------------")
            curse=False
            sleep(3)
    hero_moves(life,ars,ts,ms,wh,mh,curse,pd,poison_damage,mb)
    return

def hero_moves(life,ars,ts,ms,wh,mh,curse,pd,poison_damage,mb):
    sleep(3)
    print()
    while True:
        c.print(p.fit("Choose an attack!", style="magenta", box=box.ROUNDED))
        c.print(p.fit(f"ARROW STRIKE: Press 'AS'\n---------------------------------------------------------\nDamage: 80 | Accuracy: 80% | Attacks left: {13*'➶'}", style="bright_white", box=box.ROUNDED))
        c.print(p.fit(f"THUNDER STRIKE: Press 'TS'\n---------------------------------------------------------\nDamage: 120 | Accuracy: 70% | Attacks left: {ts*'⚡'}", style="yellow", box=box.ROUNDED))
        c.print(p.fit(f"METEOR STRIKE: Press 'MS' \n---------------------------------------------------------\nDamage: 180 | Accuracy: 60% | Attacks left: {ms*'☄️ '}", style="red", box=box.ROUNDED))
        c.print(p.fit(f"SUMMON MYSTIC BEAST: Press 'MB' \n---------------------------------------------------------\nDamage: 15% - 50% | Accuracy: 100% | Summons left: {mb*'🦄 '}", style="cyan", box=box.ROUNDED))
        att = input("\nAttack: ").upper()
        if att == "AS" and ars >0:
            ars-=1
            num= random.randint(1,10)
            if num <9:#9
                mh-=80
                sleep(2)
                c.print("\nKing Glenwald used ARROW STRIKE!", style="green")
                sleep(2)
                battle3()
                sleep(2)
                if mh<=0:
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("Congratulations! You have defeated VELDREK..🎉", style="green")
                    sleep(3)
                    print()
                    c.print(figlet.renderText("You won the game !"), style = "green")
                    return
                c.print(f"\nMonster health decreased... by '80' points 🗡️", style="green")
                sleep(2)
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
                break
            else:
                sleep(2)
                c.print("\nARROW STRIKE MISSED!", style="red")
                sleep(2)
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
                break

        elif att == "TS" and ts >0: #70% Accuracy
            ts-=1
            num= random.randint(1,10)
            if num <8:#8
                mh-=120
                sleep(2)
                c.print("\nKing Glenwald used THUNDER STRIKE!", style="green")
                sleep(2)
                thunder()
                sleep(2)
                if mh<=0:
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("Congratulations! You have defeated VELDREK..🎉", style="green")
                    sleep(3)
                    print()
                    c.print(figlet.renderText("You won the game !"), style = "green")
                    return
                c.print(f"\nMonster health decreased... by '120' points 🗡️", style="green")
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
                break
            else:
                sleep(2)
                c.print("\nTHUNDER STRIKE MISSED!", style="red")
                sleep(2)
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
                break

        elif att =="MS" and ms>0: #60% Accuracy
            ms-=1
            num= random.randint(1,10)
            if num <7:#7
                mh-=180
                sleep(2)
                c.print("\nKing Glenwald used METEOR STRIKE!", style="green")
                sleep(2)
                meteor()
                sleep(2)
                if mh<=0:
                    print("------------------------------------------------------------------")
                    sleep(1)
                    c.print("Congratulations! You have defeated VELDREK..🎉", style="green")
                    sleep(3)
                    c.print(figlet.renderText("You won the game !"), style = "green")
                    return
                c.print(f"\nMonster health decreased... by '180' points 🗡️", style="green")
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
                break
            else:
                sleep(2)
                c.print("\nMETEOR STRIKE MISSED!", style="red")
                sleep(2)
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
                break
        elif att == "MB" and mb >0:
            st=random.randint(1,2)
            if st == 1:
                 stone = "unicornium"
            else:
                stone = "peganium"
            sleep(2)

            if stone == "unicornium":
                c.print(f"\nKing GLENWALD summoned the UNICORN 🦄", style="green")
                mb-=1
                sleep(3)
                unicorn()
                sleep(2)
                num = random.randint(1,10)
                if num in [1,2]:
                    s=0.15
                    d= s*mh
                    mh-=0.15*mh

                elif num in [3,4,5]:
                    s=0.2
                    d= s*mh
                    mh-=0.20*mh

                elif num in [6,7]:
                    s=0.25
                    d= s*mh
                    mh-=0.25*mh
                elif num in [8,9]:
                    s=0.3
                    d= s*mh
                    mh-=0.3*mh
                else:
                    s=0.5
                    d= s*mh
                    mh-=0.5*mh
                mh = int(mh)
                sleep(2)
                c.print(f"\nMonster health decreased by {int(s*100)} % and {int(d)} points 🗡️", style="green")
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
                break
            else:
                c.print(f"\nKing GLENWALD summoned the PEGASUS 🐴🪽", style="green")
                mb-=1
                sleep(3)
                pegasus()
                sleep(2)
                num = random.randint(1,10)
                if num in [1,2,3,4,5,6,7]:
                    s=0.2
                    d= s*mh
                    mh-=0.20*mh

                elif num in [8,9,10]:
                    s=0.5
                    d= s*mh
                    mh-=0.50*mh
                mh = int(mh)
                sleep(2)
                c.print(f"\nMonster health decreased by {int(s*100)} % and {int(d)} points 🗡️", style="green")
                print("\nMonster health 👿 :",mh)
                print("King health 🧔    :",wh)
                print(f"King life 👑      : {life*'❤️ '}")
                print("------------------------------------------------------------------")
                sleep(3)
                break
        elif att == "AS" and ars == 0:
            c.print("\n⏳ ARROW STRIKE not available. Choose another attack!\n", style ="red")
            sleep(2.5)
        elif att == "TS" and ts==0:
            c.print("\n⏳ THUNDER STRIKE not available. Choose another attack!\n", style ="red")
            sleep(2.5)
        elif att == "MS" and ms==0:
            c.print("\n⏳ METEOR STRIKE not available. Choose another attack!\n", style ="red")
            sleep(2.5)
        elif att == "MB" and mb==0:
            c.print("\n⏳ Mystic Beasts can't be summoned. Choose another attack!\n", style ="red")
            sleep(2.5)
        else:
            c.print("\nInvalid input. Try again...\n", style ="red")
            sleep(1)

    veldrek_moves(life,wh,mh,curse,pd,poison_damage,ars,ts,ms,mb)
    return


def level1(life):
    while True:
        print("\n------------------------------------------------------------------")
        c.print("CHAPTER ONE: GRINWRECK 💀",style="red")
        sleep(2)
        while True:
            start2 = input("\nPress '0' to start chapter ONE story/ press 'S' to skip: ").lower()
            if start2 == "0":
                c.print("\nUnder King Glenwald, the Glenwald army charged..!", style ="blue")
                sleep(3)
                print(hero_su_c)
                sleep(4)
                c.print("\nKing Glenwald entered GRINWRECK's underground layer...\n", style ="blue")
                sleep(6)
                c.print("The King found GRINWRECK trying to sneak away. A battle ensued between them...\n", style ="blue")
                sleep(1)
                left_life=action(life)
                return left_life
            elif start2 == "s":
                c.print("\nThe King found GRINWRECK trying to sneak away. A battle ensued between them...\n", style ="blue")
                sleep(1)
                left_life=action(life)
                return left_life
            else:
                c.print("Invalid Input. Try again...", style= "red")


def level2(life): #Level 2 contains the story and battle sequence for monster SCRUM
    sleep(3)
    print("\n------------------------------------------------------------------")
    c.print("CHAPTER TWO: SCRUM 👾" , style="red")
    sleep(2)
    c.print("\nAfter army commander GRINWRECK's defeat. The angered King VELDREK sent his army general, the alien insectoid SCRUM to face King Glenwald..", style="blue")
    sleep(10)
    while True:
        start3 = input("\nPress '0' to head into battle with SCRUM: ")
        if start3 == "0":
            c.print("\nWait! Before you head into the Battle...\n", style = "blue")
            sleep(4)
            c.print("Read the 'Scroll of Wizards📜', that contains the secret to defeating SCRUM!\n", style ="blue")
            sleep(3)
            while True:
                read = input("Press 'R' to read the 'Scroll of Wizards📜' / press 'S' to skip reading: ").lower() #For exposition and letting the player know the rules and dynamics of the battle
                if read == "r":
                    sleep(1)
                    c.print("Opening scroll....",style="blue")
                    sleep(3)
                    c.print("\n\"Unfortunately SCRUM can't be defeated normally. He is covered in a mysterious haze that protects him from attacks...", style="magenta")
                    sleep(7)
                    c.print("\n...however this haze can be cleared if you type the magic word correctly in the time limit...", style="magenta")
                    sleep(7)
                    c.print('\n..as you have the favour of Gods, you would get a "HINT" which will help you get to the magic word...', style="magenta" )
                    sleep(8)
                    c.print('\n..for Example: HINT is "GIACM" and magic word here is "MAGIC"', style="magenta")
                    sleep(7)
                    c.print('\n..hope this knowledge helps you in the battle. Best wishes!✨ "  ....End of Scroll', style="magenta")
                    sleep(6)
                    while True:
                        inp= input("\nPress 'E' to enter SCRUM's layer: ").lower()
                        if inp == "e":
                            sleep(2)
                            c.print("\nThe King entered SCRUM's layer but its covered in haze... 💨 ",style="blue")
                            sleep(5)#5
                            c.print("\nBut one can hear SCRUM moving through the dark. His ominous presence can be felt through the bones.. ",style="blue")
                            sleep(7)#7
                            c.print("\nThis haze needs to be cleared up. A magic spell should come in handy!💫", style="blue")
                            sleep(7)#7
                            left_life = action2(life) #Initiation of battle sequence
                            return left_life
                        else:
                            c.print("Invalid input.Try again..\n", style="red")
                            continue
                elif read == "s":
                    left_life = action2(life)
                    return left_life
                else:
                    c.print("Invalid input. Try again...\n", style ="red")

        else:
            c.print("Invalid input. Try again...\n", style ="red")



def level3(life):
    sleep(3)
    print("\n------------------------------------------------------------------")
    c.print("CHAPTER THREE: DETONARCH 👺" , style="red")
    sleep(2)
    c.print("\nThe defeat of army general SCRUM left the monster army very weak. But the job is far from done. DETONARCH stands between you and the monster king, VELDREK.\n", style="blue")
    sleep(8)
    while True:
        start3 = input("\nPress '0' to head into battle with DETONARCH: ")
        if start3 == "0":
            c.print("\nWho is that??... \n", style = "blue")
            sleep(4)
            c.print("The Wise Sage appeared! \n", style ="blue")
            sleep(1)
            c.print(wsage,style="yellow")
            sleep(3)
            c.print("She has an important message for you!\n", style="blue")
            sleep(3)
            while True:
                listen = input("Press 'L' to listen to the wise sage's message 👩 / press 'S' to skip: ").lower()
                if listen == "l":
                    sleep(1)
                    c.print("\nMy greetings King GLENWALD!",style="magenta")
                    sleep(2)
                    c.print("\nI am ARIMA, the wise sage from the temple of Deggendorf 🛕...", style="magenta")
                    sleep(3)
                    c.print("\n..I have been called upon by the priests to guide you in the battle with DETONARCH..", style="magenta")
                    sleep(7)
                    c.print("\n...DETONARCH posesses immense fire power. He has access to unlimited bombs 💣 which deal huge damage...", style="magenta")
                    sleep(7)
                    c.print('\n..however these bombs can be neutralised if you enter the correct code before the bomb goes off...', style="magenta" )
                    sleep(8)
                    c.print('\n..the neutralizing code is the addition of given two numbers..', style="magenta")
                    sleep(7)
                    c.print('\n..If the bomb is neutralized, DETONARCH is vulnerable to sword attacks..', style="magenta")
                    sleep(6)
                    c.print('\n..Hope this information helps you in the battle. The priests of Deggendorf pray for your victory. Good Luck King Glenwald!⭐', style="magenta")
                    sleep(2)
                    c.print("\n The wise sage vanishes....",style="blue")
                    sleep(2)
                    while True:
                        inp= input("\nPress 'E' to enter DETONARCH's layer: ").lower()
                        if inp == "e":
                            sleep(2)
                            c.print("\nKing GLENWALD entered DETONARCH's layer.. ",style="blue")
                            sleep(5)
                            c.print("\nThe King found DETONARCH prepared and waiting for him.. ",style="blue")
                            sleep(7)
                            left_life = action3(life)
                            return left_life
                        else:
                            c.print("Invalid input.Try again..\n", style="red")
                elif listen == "s":
                    left_life = action3(life)
                    return left_life
                else:
                     c.print("Invalid input. Try again...\n", style ="red")
        else:
            c.print("Invalid input. Try again...\n", style ="red")


def level4(life):
    sleep(3)
    print("\n------------------------------------------------------------------")
    c.print("FINAL CHAPTER: VELDREK 👿" , style="red")
    sleep(2)
    c.print("\nAfter defeat and loss of his most important monsters, VELDREK - the Vampire King decides to defeat King GLENWALD himself!\n", style="blue")
    sleep(5)
    c.print("King GLENWALD is ready to face VELDREK..\n", style="blue")
    sleep(3.5)
    c.print("King GLENWALD remembered about the 'Scroll of Priests 📜' that ARIMA gave him...", style ="blue")
    sleep(6)
    while True:
        read = input("\nPress 'R' to read the 'Scroll of Priests📜' / press 'S' to skip reading: ").lower()
        if read == "r":
            sleep(1)
            c.print("Opening scroll....",style="blue")
            sleep(3)
            c.print("\n\"VELDREK is the king of monsters and posseses a powerful cannon that produces ice, poison and fire blasts...", style="magenta")
            sleep(7)
            c.print("\nOut of these be specially careful of the poison blast, which can poison its receiver for 3 turns and deals damage every turn", style="magenta")
            sleep(7)
            c.print("\nNot just that, beware of VELDREK's Curse!...", style="magenta")
            sleep(7)
            c.print('\nIt allows him to regain some of his strength once per battle and it also prevents you from using your ability at low health...', style="magenta" )
            sleep(8)
            c.print('\nAlthough VELDREK is immmune to melee attacks...he is susceptible to range attacks like arrow strikes..', style="magenta")
            sleep(7)
            c.print('\n...Not just that...Sceptre of ARIMA allows you some special attacks like meteor, thunder strikes and summon mystic beasts..', style="magenta")
            sleep(8)
            c.print('\nHowever you can only use these special attacks and summon mystic beasts for a limited turns. Be mindful of that.', style="magenta")
            sleep(7)
            c.print('\nThe Priests of Deggendorf are with you. Make best use of this knowledge. Good Luck King GLENWALD!✨', style="magenta")
            sleep(7)
            c.print('\n.....End of Scroll', style="blue")
            sleep(2.5)
            while True:
                    inp= input("\nPress 'B' to battle VELDREK: ").lower()
                    if inp == "b":
                        sleep(2)
                        c.print("\nVELDREK is here...GET READY!",style="blue")
                        sleep(3)
                        start = random.randint(1,10)
                        if start%2 ==0:
                            veldrek_moves(life,wh=800,mh=800,curse=True,pd=3,poison_damage=False,ars=20,ts=3,ms=3,mb=2)
                            return
                        else:
                            hero_moves(life,ars=20,ts=3,ms=3,wh=800,mh=800,curse=True,pd=3,poison_damage=False,mb=2)
                            return
                    else:
                        c.print("Invalid input.Try again..\n", style="red")

        elif read == "s":
            while True:
                    inp= input("\nPress 'B' to battle VELDREK: ").lower()
                    if inp == "b":
                        sleep(2)
                        c.print("\nVELDREK is here...GET READY!",style="blue")
                        sleep(3)
                        start = random.randint(1,10)
                        if start%2 ==0:
                            veldrek_moves(life,wh=800,mh=800,curse=True,pd=3,poison_damage=False,ars=20,ts=3,ms=3,mb=2)
                            return
                        else:
                            hero_moves(life,ars=20,ts=3,ms=3,wh=800,mh=800,curse=True,pd=3,poison_damage=False,mb=2)
                            return
                    else:
                        c.print("Invalid input.Try again..\n", style="red")

        else:
            c.print("Invalid input. Try again...\n", style ="red")

def main():
    life=5#5
    start()

    life=level1(life)
    if life == 0:
      return
    else:
        life=level2(life)
        if life == 0:
            return
        else:
            life= level3(life)
            if life == 0:
                return
            else:
                level4(life)
                return


if __name__ == "__main__":
    main()
