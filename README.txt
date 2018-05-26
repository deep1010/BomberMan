-> PLease install requirements.txt using sudo -H pip3 install -r requirements.txt
 
->	Controls For game :- 
		Move Player ==> w,a,s,d
		Plant Bomb  ==> b

->	Diffferent classes have been used for board,bomberman,enemy,wall,brick,bomb.

->	The Bomberman initially spawns at top left corner of game-board with random number of bricks and 4 enemies.

->	BomberMan and enemy will move same speed and frames are considered with keypresses.

->	The randomised movement of enemy is implemented as follows:-
		It will keep on moving in one specific direction until it finds hinderence.

->	Live update of enemies remaining,current score,lives remaining and level you are playing.

->	Once you kill all the enemies , you will move to next level with more number of enemies and new bricks

->	After Completing all the levels ,the game ends.

->	Only one bomb can be planted at a time. Another bomb can be planted only after it explodes
