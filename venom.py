import random
import curses
from curses import textpad 
import time 

def main(stdscr):
	curses.curs_set(0)
	sy,sx=stdscr.getmaxyx()
	stdscr.nodelay(1)
	uy=6
	ux=9
	ly=sy-6
	lx=sx-9

	textpad.rectangle(stdscr,uy,ux,ly,lx)

	speed=0.10

	#initial snake
	box=[[sy//2,sx//2],[sy//2,sx//2-1],[sy//2,sx//2-2]]
	snake=[box[0],box[1],box[2]]

	#food position random
	fy,fx=food(uy,ux,ly,lx)
	stdscr.addstr(fy,fx,"$")

	for y,x in snake : 
		stdscr.addstr(y,x,"#")

	last_direction=curses.KEY_RIGHT
	while True: 
		key=stdscr.getch()
		if key in [curses.KEY_RIGHT,curses.KEY_LEFT,curses.KEY_DOWN,curses.KEY_UP]	  :
			direction=key
		else :
			direction=last_direction

		head=snake[0]

		if direction==curses.KEY_RIGHT and last_direction!=curses.KEY_LEFT:
			last_direction=curses.KEY_RIGHT
			new_head=[head[0],head[1]+1]
			if if_food(new_head[0],new_head[1],fy,fx)==1 :
				snake.insert(0,new_head)
				new_head=[new_head[0],new_head[1]+1]
				fy,fx=food(uy,ux,ly,lx)
				stdscr.addstr(fy,fx,"$")

		if direction==curses.KEY_LEFT and last_direction!=curses.KEY_RIGHT:
			last_direction=curses.KEY_LEFT
			new_head=[head[0],head[1]-1]
			if if_food(new_head[0],new_head[1],fy,fx)==1 :
				snake.insert(0,new_head)
				new_head=[new_head[0],new_head[1]-1]
				fy,fx=food(uy,ux,ly,lx)
				stdscr.addstr(fy,fx,"$")

		if direction==curses.KEY_UP and last_direction!=curses.KEY_DOWN:
			last_direction=curses.KEY_UP
			new_head=[head[0]-1,head[1]]
			if if_food(new_head[0],new_head[1],fy,fx)==1 :
				snake.insert(0,new_head)
				new_head=[new_head[0]-1,new_head[1]]
				fy,fx=food(uy,ux,ly,lx)
				stdscr.addstr(fy,fx,"$")

		if direction==curses.KEY_DOWN  and last_direction!=curses.KEY_UP:
			last_direction=curses.KEY_DOWN
			new_head=[head[0]+1,head[1]]
			if if_food(new_head[0],new_head[1],fy,fx)==1 :
				snake.insert(0,new_head)
				new_head=[new_head[0]+1,new_head[1]]
				fy,fx=food(uy,ux,ly,lx)
				stdscr.addstr(fy,fx,"$")

		if new_head in snake or new_head[0]==uy or new_head[0]==ly or new_head[1]==ux or new_head[1]==lx: 
			stdscr.addstr(box[0][0],box[0][1],"GAME OVER",curses.A_BLINK)
			stdscr.refresh()
			stdscr.nodelay(0)
			stdscr.getch()
			exit(0)


		snake.insert(0,new_head)

		stdscr.addstr(new_head[0],new_head[1],"#")
		stdscr.addstr(snake[-1][0],snake[-1][1]," ")
		snake.pop()
		time.sleep(speed)
			
		

def food(uy,ux,ly,lx):
	y=random.randint(uy+1,ly-1)
	x=random.randint(ux+1,lx-1)
	return y,x

def if_food(y,x,fy,fx):
	if y==fy and x==fx :
		return 1
	else :
		return 0

curses.wrapper(main)
