import pygame
import time

pygame.init()

WIDTH,HEIGHT=300,300

background=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("tic tac toe")
clock=pygame.time.Clock()


#variable
running=True
WHITE=(250,250,250)
BLACK=(0,0,0)
FPS=60
line_width=6
clicked=False
pos=[]
pos1=[]
cell_x=0
cell_y=0
player=1
markers=[[0]*3 for x in range(3)]
image_o=pygame.image.load(r"C:\Users\HELLO\o.png")
image=pygame.transform.scale(image_o,(20,50))
image_x=pygame.image.load(r"C:\Users\HELLO\x.png")
image1=pygame.transform.scale(image_x,(20,50))
image2=pygame.image.load(r"C:\Users\HELLO\f.jpg")
display=pygame.transform.scale(image2,(150,150))
winner=0
game_over=False



again_rect=pygame.Rect(0,155,160,30)
again_rect_draw=pygame.Rect(0,155,160,30)




#functions
def draw_line():
    background.fill(WHITE)
    for x in range(1,3):
        pygame.draw.line(background,BLACK,(0,x*100),(WIDTH,x*100),line_width)
        pygame.draw.line(background,BLACK,(x*100,0),(x*100,HEIGHT),line_width)



def set_markers():
    for x in range(3):
        for y in range(3):
            if markers[x][y]==1:
                background.blit(image, (x * 100 + 40, y * 100 + 20))
            if markers[x][y]==-1:
                background.blit(image1, (x * 100 + 40, y * 100 + 20))
                
   



def check_winner():
    global winner
    global game_over
    j=0
    for i in markers:
        #for checking rows
        if sum(i)==3:
            winner=1
            game_over=True
        if sum(i)==-3:
            winner=2
            game_over=True
        #for checking column
        if markers[0][j] + markers[1][j] + markers[2][j]==3:
            winner=1
            game_over=True
        if markers[0][j] + markers[1][j] + markers[2][j]== -3:
            winner=2
            game_over=True
        j=j+1
    #for checking cross
    if markers[0][0] + markers[1][1] + markers[2][2]==3 or markers[0][2] + markers[1][1] + markers[2][0]==3 : 
        winner=1
        game_over=True
        
    if markers[0][0] + markers[1][1] + markers[2][2]== -3 or markers[0][2] + markers[1][1] + markers[2][0]== -3 : 
        winner=2
        game_over=True
            
    

def write_winner():
    if winner==1:
        background.fill(BLACK)
        winner_font=pygame.font.SysFont("Raleway", 50,bold=True)
        winner_text=winner_font.render("winner is player 1" , True, WHITE)
        
    if winner==2:
        background.fill(BLACK)
        winner_font=pygame.font.SysFont("Raleway", 50,bold=True)
        winner_text=winner_font.render("winner is player 2" , True, WHITE)
    background.blit(winner_text,(0,120))
    again_font=pygame.font.SysFont(None, 35)
    again_text=again_font.render("play again!!",True,WHITE)
    again_button=pygame.draw.rect(background,"green", again_rect)
    background.blit(again_text,(0,155))
    
 
def draw():
    global markers
    global game_over
    global clicked
    SUM=0
    for i in range(3):
        for j in range(3):
            checking=markers[i][j]
            SUM=SUM +abs(checking)
            
    if SUM==9 and game_over==False:
        background.fill(BLACK)
        draw_font=pygame.font.SysFont(None, 50)
        draw_text=draw_font.render("the game is draw",True,WHITE)
        background.blit(draw_text, (0,120))
        
        again_font=pygame.font.SysFont(None, 35)
        again_text=again_font.render("play again!!",True,WHITE)
        again_button=pygame.draw.rect(background,"green", again_rect_draw)
        background.blit(again_text,(0,155))
        
        # check for mouse click on play again button
        if event.type==pygame.MOUSEBUTTONDOWN :
            clicked=True
        if event.type==pygame.MOUSEBUTTONUP :
            clicked=False
            pos=pygame.mouse.get_pos()
            pos1=pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                pos=[]
                player=1
                markers=[[0]*3 for x in range(3)]
                winner=0
                game_over=False
                
        return SUM

                
                
               
 
    
 
    
 
# front display               
background.fill(WHITE)
background.blit(display, (80, 95))
font = pygame.font.SysFont(None, 50)
text = font.render("Tic Tac Toe", True, BLACK)
background.blit(text, (75, 50))
pygame.display.update()
time.sleep(3)


#main loop
while running:
    clock.tick(FPS)
    draw_line()
    set_markers()
    
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        
        if  game_over==False:
            if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True
            if event.type==pygame.MOUSEBUTTONUP and clicked==True:
                clicked=False
                pos=pygame.mouse.get_pos()
                cell_x=pos[0]
                cell_y=pos[1]
                if markers[cell_x//100][cell_y//100]==0:
                    markers[cell_x//100][cell_y//100]= player
                    player *= -1
                    check_winner()
        if game_over==True:
            write_winner()
                    
        draw_sum=draw()
        
        if draw_sum==9:
            game_over==True
            
        if game_over==True:
            if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked=True
            if event.type==pygame.MOUSEBUTTONUP and clicked==True:
                clicked=False
                pos=pygame.mouse.get_pos()
                pos1=pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    pos=[]
                    player=1
                    markers=[[0]*3 for x in range(3)]
                    winner=0
                    game_over=False
                
            
        
                    
                    
                    
                
            
        
            
        
    
        pygame.display.update()
            
          
            
pygame.quit()




