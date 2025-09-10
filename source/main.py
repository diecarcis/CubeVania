import keyboard
import random
import time
import os

backgrnd_mod=[]
backgrnd_mod.append([
	'',
	'                                                                                 ',
	'                                                                                 ',
	'                                                                                 ',
	'                                                                                 ',
	'                                                              .##                ',
	'                                                               H#                ',
	'                                                               H#                ',
	'                              ########################         H#                ',
	'                                                               H#           #####',
	'                                                               H#                ',
	'                                                               H#                ',
	'                                                               H                 ',
	'                                                               H                 ',
	'                                                               H######           ',
	'                                                               H#                ',
	'                                                               H#                ',
	'                                                               H#                ',
	'                                                               H#           HHHHH',
	'                                                               H#                ',
	'                                                               H#                ',
	'                                                               H#                ',
	'                                                               H#                ',
	' #####################################################################      #####',])

act_backgrnd=0
enemy_bullets=[]

class ui:
	def prat(obj,x=0,y=0):
		for i in range(len(obj)):
			if y!=0:
				ui.gt(x+i,y)
			print(obj[i])

	def gt(x,y):
		print(f'\033[{x};{y}H',end='')

	def print_backgrnd(x,y):
		backgrnd_temp=backgrnd_mod[act_backgrnd]
		ui.gt(1,1)
		for i in range(1,len(backgrnd_temp)):
			for j in range(1,len(backgrnd_temp[i])):
				if backgrnd_temp[i][j]=='.':
					if(backgrnd_temp[i+1][j]=='#'):print('▲',end='')
					elif(backgrnd_temp[i-1][j]=='#'):print('▼',end='')
					else:print('.',end='')
				elif i>=player.x and i<=player.x+1 and j>=player.y and j<=player.y+3:
					print(player.mod[i-player.x][j-player.y],end='')
				elif backgrnd_temp[i][j]==' ':
					print(' ',end='')
				elif backgrnd_temp[i][j]=='#':
					print('▒',end='')
				elif backgrnd_temp[i][j]=='H':
					print('░',end='')
				else:print(backgrnd_temp[i][j],end='')
			print()

class player():
	mod=[
		'████',
		'████']
	jump_time=0
	lives=3
	x=21
	y=1

	def control():
		# if player.dir('left')=='stair' or player.dir('right')=='stair':
		# 	if keyboard.is_pressed('w') and not player.dir('up'):
		# 		player.x-=1
		# 	if keyboard.is_pressed('s') and not player.dir('down'):
		# 		player.x+=1

		if keyboard.is_pressed('a') and not player.dir('left'):
			player.y-=1
		if keyboard.is_pressed('d') and not player.dir('right'):
			player.y+=1

		# if player.dir('up')=='block' or player.dir('down')=='stair':
		# 	player.jump_time=0

		if keyboard.is_pressed('space'):
			if player.dir('down') and not player.dir('up'):
				player.jump_time=7
				return
		if player.jump_time==0 and not player.dir('down'):#  and player.dir('left')!='stair' and player.dir('right')!='stair':
			player.x+=1

		if player.jump_time>0:
			player.x-=1
			player.jump_time-=1
			# if not keyboard.is_pressed('space'):
			# 	player.jump_time=0
			# 	return

	def dir(wall_dir):
		if wall_dir=='up':
			if backgrnd_mod[act_backgrnd][player.x-1][player.y]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x-1][player.y+1]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x-1][player.y+2]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x-1][player.y+3]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x-1][player.y]=='H':return 'stair'
			if backgrnd_mod[act_backgrnd][player.x-1][player.y+1]=='H':return 'stair'
			if backgrnd_mod[act_backgrnd][player.x-1][player.y+2]=='H':return 'stair'
			if backgrnd_mod[act_backgrnd][player.x-1][player.y+3]=='H':return 'stair'
		if wall_dir=='down':
			if backgrnd_mod[act_backgrnd][player.x+2][player.y]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x+2][player.y+1]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x+2][player.y+2]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x+2][player.y+3]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x+2][player.y]=='H':return 'stair'
			if backgrnd_mod[act_backgrnd][player.x+2][player.y+1]=='H':return 'stair'
			if backgrnd_mod[act_backgrnd][player.x+2][player.y+2]=='H':return 'stair'
			if backgrnd_mod[act_backgrnd][player.x+2][player.y+3]=='H':return 'stair'
		if wall_dir=='left':
			if backgrnd_mod[act_backgrnd][player.x][player.y-1]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x+1][player.y-1]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x][player.y-1]=='H':return 'stair'
			if backgrnd_mod[act_backgrnd][player.x+1][player.y-1]=='H':return 'stair'
		if wall_dir=='right':
			if backgrnd_mod[act_backgrnd][player.x][player.y+4]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x+1][player.y+4]=='#':return 'block'
			if backgrnd_mod[act_backgrnd][player.x][player.y+4]=='H':return 'stair'
			if backgrnd_mod[act_backgrnd][player.x+1][player.y+4]=='H':return 'stair'
		return False

	def check_hitbox():
		backgrnd_temp=backgrnd_mod[act_backgrnd]
		for i in range(2):
			for j in range(4):
				for k in enemy_bullets:
	  				if k['x']==i and k['y']==j:
	  					player_lives-=1;
	  					enemy_bullets.remove(k)
				if backgrnd_temp[player.x+i][player.y+j]=='.':
					game.over=True

class game:
	over=False

	def loop():
		while 1:
			player.control()
			ui.print_backgrnd(0,0)
			player.check_hitbox()
			#backgrnd.check_borders()
			if game.over:
				return
			time.sleep(0.03)
	
	def end_game():
		if over:
			xd

def main():
	os.system('cls')
	game.loop()
	if game.over==True:
		print('game over')
		time.sleep(1)
		os.system('C:\\Users\\dieca\\Documents\\Programming\\Python\\untitled.py')

if __name__=='__main__':
	main()

'''
▓▒░

█▀▄

▲►▼◄

┬├┤┼┴ 

┼--┼
┼--┼
┼--┼
┼--┼
┼--┼
┼--┼
┼--┼
┼--┼
┼--┼
┼--┼


'                                                           ',
'##############                                             ',
'             #                                             ',
'             #                                             ',
'             #                              ###############',
'             #                              #              ',
'             ################################              ',

 
▄▄▄
███


'''
