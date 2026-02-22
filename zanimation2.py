from rich.live import Live
from time import sleep
from zdetonarch import bl21,bl22,bl23,bl24,bl2ds1,bl2ds2,bl2ds3,bl2ds4, da1,da2,da3,da4,da5,da6,da7,da8,da1_c,da4_c,da7_,da8_,da9_,da5_c,da6_c,da7_c,da8_c,da9_c,da10_c
from zchar import heroani1,heroani2,heroani3,sg1,sg2,sg3,sg4,sg5,sg1_1
from rich.console import Console
c=Console()
def sceptre_ani():
    for _ in range(1):
        with Live(sg1, refresh_per_second=10, screen=True) as live:
            sleep(0.5)
            live.update(sg1_1)
            sleep(0.2)
            live.update(sg2)
            sleep(0.7)
            live.update(sg3)
            sleep(0.5)
            live.update(sg4)
            sleep(0.5)
            live.update(sg5)
            sleep(3)
#sceptre_ani()

def sword_attack():
    for _ in range(5):
        with Live(bl21, refresh_per_second=10, screen=True) as live:
            sleep(0.1)
            live.update(bl22)
            sleep(0.1)
            live.update(bl23)
            sleep(0.1)
            live.update(bl24)
            sleep(0.2)

#sword_attack()
def sword_attack2():
    #c.print("King used double sword attack",style="green")
    for _ in range(5):
        with Live(bl2ds1, refresh_per_second=10, screen=True) as live:
            sleep(0.2)
            live.update(bl2ds2)
            sleep(0.2)
            live.update(bl2ds3)
            sleep(0.2)
            live.update(bl2ds4)
            sleep(0.2)
#sword_attack2()


def hero_celebration():
    #c.print("King used double sword attack",style="green")
    for _ in range(10):
        with Live(heroani1, refresh_per_second=10, screen=True) as live:
            sleep(0.3)
            live.update(heroani2)
            sleep(0.05)
            live.update(heroani3)
            sleep(0.3)


#hero_celebration()
def deto_att():
    #c.print("King used double sword attack",style="green")
    for _ in range(3):
        with Live(da1, refresh_per_second=10, screen=True) as live:
            sleep(0.2)
            #live.update(da2)
            #sleep(0.3)
            #live.update(da3)
            #sleep(0.3)
            live.update(da4)
            sleep(0.2)
            live.update(da5)
            sleep(0.2)
            live.update(da6)
            sleep(0.2)
            live.update(da7)
            sleep(0.2)
            live.update(da8)
            sleep(0.2)

#deto_att()

def deto_att2():
    #c.print("King used double sword attack",style="green")
    for _ in range(3):
        with Live(da1, refresh_per_second=10, screen=True) as live:
            sleep(0.2)
            #live.update(da2)
            #sleep(0.3)
            #live.update(da3)
            #sleep(0.3)
            live.update(da4)
            sleep(0.2)
            live.update(da5)
            sleep(0.2)
            live.update(da6)
            sleep(0.2)
            live.update(da7_)
            sleep(0.2)
            live.update(da8_)
            sleep(0.2)
            live.update(da9_)
            sleep(0.2)
#deto_att2()
def deto_win():
    #c.print("King used double sword attack",style="green")
    for _ in range(5):
        with Live(da1_c, refresh_per_second=10, screen=True) as live:
            sleep(0.3)
            #live.update(da2)
            #sleep(0.3)
            #live.update(da3)
            #sleep(0.3)
            live.update(da4_c)
            sleep(0.3)
            live.update(da5_c)
            sleep(0.3)
            #live.update(da6_c)
            #sleep(0.2)
            live.update(da7_c)
            sleep(0.3)
            live.update(da8_c)
            sleep(0.3)
            live.update(da9_c)
            sleep(0.3)
            live.update(da10_c)
            sleep(0.2)
#deto_win()
