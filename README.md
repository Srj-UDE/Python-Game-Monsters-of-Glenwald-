# Monsters of Glenwald
#### Video Demo: https://youtu.be/V5NkMXvHumY?si=A8VEVwsV5hyqIEKI
#### Description:

**Monsters of Glenwald** is a single player story based game, where a King fights several monsters to protect his kingdom.

**The game features**
- Engaging gameplay and characters with interesting lore and backstories
- ASCII character designs and supporting animations
- Increasing difficulty with each wave of monsters
- Power-ups with ability at low health
- The game helps its players develop their problem solving skills, analytical and strategic thinking

The game starts by establishing the lore and story of its characters. It displays the Kingdom of Glenwald, King Glenwald, and characters of the monster army, namely Grinwreck, Scrum, Detonarch, and Veldrek. It introduces the core plot of the game: the battle between the King and the monsters. It also has a skip option that lets the player skip the story and move directly to next level.

**Level One**
Level One is the battle with the first monster, Grinwreck. The monster and King both start with a fixed value of attack and health points. Additionally, the King has 5 lives in total that can be used in case the player loses any battle. The player loses the game if they run out of these 5 lives. As the first battle starts, the player is asked to choose and type a number between 0 and 10. If the player enters an invalid number or letter, that invalid input is caught, and an "Invalid Input. Try again..." message is displayed, prompting the player to enter again. Meanwhile, in the code, the random module is used to generate a random integer between 0 and 10. If both the player's input and the random integer are even-even or odd-odd pairs, the King attacks and decreases the monster's health. This continues until the monster or the King runs out of health. To make the game more interesting, if the King's health reaches a critically low level, he activates his ability, which can boost his attack, health, decrease the monster’s health, or even fail—it's randomly decided. If the player wins, the story continues further; if the player loses, he/she can use one of the 5 lives to restart the battle.

**Level Two**
Level Two is the battle with Scrum. As the story progresses, it explains to the player how the battle dynamics will function. Here as well, there is an option to skip the story. The monster and King both start with a fixed value of attack and health points. Additionally, the King carries forward his lives from the previous level. The battle requires the player to guess a magic word by unscrambling jumbled letters in 20 seconds. If successful, the King attacks and decreases the monster’s health, and vice versa if not successful. This continues until the monster or the King runs out of health. The King also retains his ability feature from Level One. On winning, the player moves to Level Three. This level was designed to help the player improve important cognitive (brain) skills, especially those related to language, memory, and problem-solving.

**Level Three**
Level Three is the battle with the monster Detonarch. As the story progresses, it explains to the player the battle dynamics with Detonarch. Here as well, there is an option to skip the story. The monster and King both start with a fixed value of attack and health points. Additionally, the King carries forward his lives from the previous level. During the battle, the player is asked to solve a math addition problem in 20 seconds. If successful, the King attacks and decreases the monster’s health, and vice versa if the player fails to solve the math problem. Here as well, the King retains his ability feature. Upon defeating Detonarch, the King receives special items and rewards and progresses to the last level. This level improves mathematical problem-solving ability.

**Level Four**
The final level of the game lets the player battle the monster boss, Veldrek. The story explains the battle features. The monster and King both start with a fixed value of attack and health points. Additionally, the King carries forward his lives from the previous levels. The battle starts either with Veldrek attacking or the player choosing an attack to start the battle. Each attack has its own unique characteristics and should be used strategically. In this level, all the attacks have attack animations that make the game more fun, and they are the highlight of this game. Each animation is meticulously crafted by designing each scene individually and putting them together with rich.live(). Upon defeating Veldrek, the player is greeted with a victory animation—or an animation of the monster winning in the opposite case. The game ends with an ASCII art displaying whether the player won or lost the game. This was **Monsters of Glenwald**.


Creating this game taught me valuable lessons in game loops, input handling, animation, and player feedback mechanics.
It was also a fun and creative way to practice programming logic and polish my Python skills.

The other files in the project folder (thunder.py,unicorn.py,win.py,zanimation1.py......etc) include character designs and stop motion animations for the game.
