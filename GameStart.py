import pygame
import random
pygame.init()#default constructuctor of pygame is called
#to set window size
window_width=700
window_height=800
#to call the screen and save it in the object
screen=pygame.display.set_mode((window_height,window_width))
#setting the title of window
pygame.display.set_caption("Gaming Arena")



#to print text on screen
def message_to_screen(msg,color,i,j,size):
    #Font #size #Bold # Italic
    font=pygame.font.SysFont("Calibri",size,False,False)
    #text #Antialias-> for smoothness  #color
    screen_text=font.render(msg,True,color)
    #blit-.to display screen text i,j->starting point for the text top left corner
    screen.blit(screen_text,[i,j])



#to print text on screen
def message_to_screen1(msg,color,i,h,w,size):
    font=pygame.font.SysFont("Calibri",size,False,False)
    screen_text=font.render(msg,True,color)
    screen.blit(screen_text,[h,w+i])
#for background design
def draw_background():
    #coordinates  
    pygame.draw.circle(screen,'red',[400,400],50)
    pygame.draw.polygon(screen,'brown',[(800,500),(700,400),(600,500)])
    pygame.draw.polygon(screen,'brown',[(700,500),(600,400),(500,500)])
    pygame.draw.polygon(screen,'brown',[(600,500),(500,400),(400,500)])
    pygame.draw.polygon(screen,'brown',[(500,500),(400,400),(300,500)])
    pygame.draw.polygon(screen,'brown',[(400,500),(300,400),(200,500)])
    pygame.draw.polygon(screen,'brown',[(300,500),(200,400),(100,500)])
    pygame.draw.polygon(screen,'brown',[(200,500),(100,400),(0,500)])

def drawrect(screen,x,y):
	if x<=0:
		x=0
	if x>=699:
		x=699
	pygame.draw.rect(screen,(0,255,0),[x,y,100,20])

def snake(blockSize,snakelist):
	t=0
	for size in snakelist:
		pygame.draw.rect(screen,'black',[size[0],size[1],blockSize,blockSize],2,border_radius=7)
		if t==len(snakelist)-1:
			pygame.draw.circle(screen,(0,0,0),(size[0]+10,size[1]+5),2)
		t+=1
	
#To add X and O's
def clicked(i,turn):
    if i==1:
        message_to_screen(turn,'red',210,175,55)
    elif i==2:
        message_to_screen(turn,'Red',320,175,55)
    elif i==3:
        message_to_screen(turn,'Red',520,175,55)
    elif i==4:
        message_to_screen(turn,'Red',210,290,55)
    elif i==5:
        message_to_screen(turn,'Red',320,290,55)
    elif i==6:
        message_to_screen(turn,'Red',520,290,55)
    elif i==7:
        message_to_screen(turn,'Red',210,490,55)
    elif i==8:
        message_to_screen(turn,'Red',320,490,55)
    else:
        message_to_screen(turn,'Red',520,490,55)



def start_snake_game():
        
    window_width=800
    window_height=700
    w_s_h=200
    w_s_w=20
    w_w=window_width-220
    w_h=window_height-40
    clock =pygame.time.Clock()
    FPS=5
    blockSize=20
    noPixel=0
    prev=5
    pygame.display.update()
    gameExit=False
    gameOver=False
    lead_x=(w_w+w_s_h)/2
    lead_y=w_h/2
    change_pixels_x=0
    change_pixels_y=0
    snakelist=[]
    snakeLength=1
    randomAppleX=round(random.randrange(w_s_h+blockSize,w_w+w_s_h-blockSize*2))
    randomAppleY=round(random.randrange(w_s_w+blockSize,w_h+w_s_w-blockSize*2))
    x=1
    while not gameExit:
        if gameOver==True:
            message_to_screen("GAME OVER",'red',250,300,50)
            pygame.display.update()
            pygame.time.delay(3001)
            screen.fill('white')
            message_to_screen("GAME OVER",'black',200,300,50)
            message_to_screen("**********************",'green',200,350,40)
            message_to_screen("YOUR SCORE",'red',200,400,40)
            message_to_screen(str(snakeLength),'black',200,450,40)
            message_to_screen("**********************",'green',200,500,40)
            FPS=10
            x=1
            pygame.display.update()
            pygame.time.delay(3001)
            gameExit=True

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    change_pixels_x=-blockSize
                    change_pixels_y=noPixel
                elif event.key==pygame.K_RIGHT:
                    change_pixels_y=noPixel
                    change_pixels_x=blockSize
                elif event.key==pygame.K_UP:
                    change_pixels_x=noPixel
                    change_pixels_y=-blockSize
                elif event.key==pygame.K_DOWN:
                    change_pixels_y=blockSize
                    change_pixels_x=noPixel
        lead_y+=change_pixels_y
        lead_x+=change_pixels_x
        if lead_x>=w_w+w_s_h-20 or lead_x<w_s_h or lead_y>=w_h+w_s_w-20 or lead_y<w_s_w:
            gameOver=True
            continue
        screen.fill('white')
        AppleThickness=20
        print([(randomAppleX),(randomAppleY),AppleThickness,AppleThickness])

        pygame.draw.rect(screen,'red',[randomAppleX,randomAppleY,AppleThickness,AppleThickness])
        pygame.draw.rect(screen,'green',[200,20,window_width-220,window_height-40],20)
        allspriteslist=[]
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snakelist.append(allspriteslist)
        if len(snakelist)>snakeLength:
            del snakelist[0]
        for eachSegment in snakelist[:-1]:
            if eachSegment==allspriteslist:#
                gameOver=True
        snake(blockSize,snakelist)
        pygame.display.update()
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX=round(random.randrange(w_s_h+blockSize,w_w+w_s_h-blockSize*2)/10.0)*10.0
                randomAppleY = round(random.randrange(w_s_w+blockSize,w_h+w_s_w-blockSize*2)/10.0)*10.0
                snakeLength += 1
        if(snakeLength>=prev*2):
            prev=snakeLength
            FPS=1.5*FPS
            x+=1
        level="LEVEL "+str(x)
        score="SCORE::::"+str(snakeLength)
        speed="SPEED::::"+str(x)+"X"
        message_to_screen1(level,'black',5,15,10,15)
        message_to_screen1(score,'black',5,15,35,15)
        message_to_screen1(speed,'red',5,15,55,15)
        pygame.display.update()
        clock.tick(FPS)

#this is ping pong game
def start_ping_pong():
    #position of bar to play x,y
    rect_x=400
    rect_y=580
    #Speed of ball->refresh rate position of ball will change in 1/60th second
    Fps=60
    #parameter of changing position of bar how much left or right
    rect_change_x=0
    #position of ball x,y
    ball_x=50
    ball_y=50
    #ratio of change of position of ball wrt to fps
    ball_change_x=5
    ball_change_y=5
    #score of game
    score=0
    #done will become true when game will end and break the loop
    done=False
    #will change with every fps
    #will refresh fps
    #Clock object can help us make sure our program runs at a certain maximum FPS
    clock=pygame.time.Clock()
    while not done:
        message_to_screen("WELCOME TO PING PONG","blue",0,0,50)
        pygame.display.update()	
        for event in pygame.event.get():
            #to close ping pong game
            if event.type==pygame.QUIT:
                done=True
            #keydown->if we have clicked a key
            elif event.type==pygame.KEYDOWN:
                #if left if pressed ->position is changed by 6 units either on left or on right
                if event.key==pygame.K_LEFT:
                    rect_change_x=-6
                elif event.key==pygame.K_RIGHT:
                    rect_change_x=6
            else:
                rect_change_x=0
        screen.fill("black")
        #to change rectangle position
        rect_x+=rect_change_x
        if rect_x>699:
            rect_x=699
        if rect_x<0:
            rect_x=0
        #for ball movement 
        ball_x+=ball_change_x
        ball_y+=ball_change_y
        if ball_x<0:
            ball_x=0
            #to reflect ball after it touches the wall
            ball_change_x=ball_change_x*-1
        if ball_x>785:
            ball_x=785
            ball_change_x=ball_change_x*-1
        if ball_y<0:
            ball_y=0
            ball_change_y=ball_change_y*-1
        if ball_y>=600-15:
            message_to_screen("GAME OVER","Red",200,300,50)
            pygame.display.update()	
            #to delay screen for 3 seconds
            pygame.time.delay(3001)
            done=True
        #Condition when ball touches the bar
        #first condition ball is betwwn starting and ending point 
        #third condition ball is touching the bar
        if ball_x+15>=rect_x and ball_x<=rect_x+100 and ball_y==565:
            ball_change_y=ball_change_y*-1
            score=score+1
        
    
        
        #to create the ball with its coordinates
        pygame.draw.rect(screen,"white",[ball_x,ball_y,15,15])
        #to create bar 
        drawrect(screen,rect_x,rect_y)
        #Score display
        message_to_screen("Score"+str(score),"white",600,100,15)
        
        pygame.display.flip()
        clock.tick(Fps)


def start_tic_tac_toe():
    done=False
    x_turn=True
    pygame.display.update()	
    pos=[]
    while not done:
        screen.fill("Black")
        message_to_screen("WELCOME TO TIC TAC TOE","White",0,0,50)
        if x_turn:
            message_to_screen("X's turn","Red",300,60,35)
        else:
            message_to_screen("Y's turn","Red",300,60,35)
        pygame.draw.line(screen,"white",(275,200),(275,600),1)
        pygame.draw.line(screen,"white",(475,200),(475,600),1)
        pygame.draw.line(screen,"white",(150,275),(650,275),1)
        pygame.draw.line(screen,"white",(150,475),(650,475),1)
        
        for i in pos:
            clicked(i[0],i[1])
        
        pygame.display.update()	
        if(len(pos)==9):
            screen.fill('WHITE')
            message_to_screen("GAME DRAW","Red",250,300,75)
            pygame.display.update()	
            pygame.time.delay(3001)
            done=True
            continue
        
        for i in pos:
            for j in pos:
                if(i==j):
                    continue
                if(i[1]!=j[1]):
                    continue
                for k in pos:
                    if k==i or k==j:
                        continue
                    if(i[1]!= k[1]):
                        continue
                    sum=i[0]+j[0]+k[0]
                    if(sum %3)==0:
                        pygame.time.delay(2001)
                        screen.fill('WHITE')
                        message_to_screen(turn+" WON","Red",250,300,75)
                        pygame.display.update()	
                        pygame.time.delay(5001)
                        done=True
                        
                    if( done==True):
                        break
                if( done==True):
                    break

            if( done==True):
                break
        if(done==True):
            break
        turn='X'
        if not x_turn:
            turn='O'
        
        for event in pygame.event.get():
            #to close ping pong game
            if event.type==pygame.QUIT:
                done=True
            if event.type== pygame.MOUSEMOTION or event.type==pygame.MOUSEBUTTONDOWN:
            #for checking current mouse position result will be in tupple 
                mouse=pygame.mouse.get_pos()
            #mouse[0]-> x position mouse[1]->y position
                if mouse[0]in range ( 150,275) and  mouse[1]in range ( 200,275) and (1,'X') not in pos and (1,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 1')
                        pos.append((1,turn))
                        x_turn=not x_turn
                elif mouse[0]in range ( 275,475) and  mouse[1]in range ( 200,275) and (2,'X') not in pos and (2,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 2')
                        pos.append((2,turn))
                        x_turn=not x_turn
                        #start_snake_game()

                elif mouse[0]in range ( 475,650) and  mouse[1]in range ( 200,275) and (3,'X') not in pos and (3,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 3')
                        pos.append((3,turn))
                        x_turn=not x_turn
                        #start_snake_game()
                elif mouse[0]in range ( 150,275) and  mouse[1]in range ( 275,475) and (4,'X') not in pos and (4,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 4')
                        pos.append((4,turn))
                        x_turn=not x_turn
                        #start_snake_game()

                elif mouse[0]in range ( 275,475) and  mouse[1]in range ( 275,475) and (5,'X') not in pos and (5,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 5')
                        pos.append((5,turn))
                        x_turn=not x_turn
                        #start_snake_game()

                elif mouse[0]in range ( 475,650) and  mouse[1]in range ( 275,475) and (6,'X') not in pos and (6,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 6')
                        pos.append((6,turn))
                        x_turn=not x_turn
                        #start_snake_game()

                elif mouse[0]in range ( 150,275) and  mouse[1]in range ( 475,600) and (7,'X') not in pos and (7,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 7')
                        pos.append((7,turn))
                        x_turn=not x_turn
                        #clicked()

                elif mouse[0]in range ( 275,475) and  mouse[1]in range ( 475,600) and (8,'X') not in pos and (8,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 8')
                        pos.append((8,turn))
                        x_turn=not x_turn

                elif mouse[0]in range ( 475,650) and  mouse[1]in range ( 475,600) and (9,'X') not in pos and (9.,'O') not in pos:
                    #whwnever rmouse will be in this position range it will become hand
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                    #to check whwether mouse button is clicked or not
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        print('you clicked 9')
                        pos.append((9,turn))
                        x_turn=not x_turn
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                
        
        
            
        pygame.display.update()


#to run game until condition is true
while True:
    #to set new screen everytime we play a game
    screen=pygame.display.set_mode((window_height,window_width))
    screen.fill("white")
    #msg_passed color->black coordinates->200,200 size->30 
    message_to_screen('Welcome to gaming alley','black',200,200,30)
    message_to_screen('We have many options to play from:','black',200,240,15)
    message_to_screen('1. Fidget Spinner ','blue',200,260,20)
    message_to_screen('2. Ping Pong Game ','blue',200,285,20)
    message_to_screen('3. Tic tac toe ','blue',200,310,20)
    draw_background()
    pygame.display.update()
    #capture mouse and keyboard input
    for event in pygame.event.get():
        #for checking mouse motion and mouse button
        if event.type== pygame.MOUSEMOTION or event.type==pygame.MOUSEBUTTONDOWN:
            #for checking current mouse position result will be in tupple 
            mouse=pygame.mouse.get_pos()
            #mouse[0]-> x position mouse[1]->y position
            if mouse[0]in range ( 200,330) and  mouse[1]in range ( 260,275):
                #whwnever rmouse will be in this position range it will become hand
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                #to check whwether mouse button is clicked or not
                if event.type==pygame.MOUSEBUTTONDOWN:
                    
                    start_snake_game()
            elif mouse[0]in range ( 200,370) and  mouse[1]in range ( 285,300):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    start_ping_pong()
            elif mouse[0]in range ( 200,370) and  mouse[1]in range ( 310,325):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    start_tic_tac_toe()

            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        #event are mouse movement 
        if event.type == pygame.QUIT:
                pygame.quit()
                exit()