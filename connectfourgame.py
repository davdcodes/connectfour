import pygame

pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Connect Four!")
board = [[0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
player = 0

# ------------------------------------------------------- Misc Methods -------------------------------------------------------------

def getPos():
       return pygame.mouse.get_pos()

def getSpot():
    pos = getPos()[0]
    return pos // 100

def isOnButt():
    if getPos()[0] >= 520 and getPos()[0] <= 680 and getPos()[1] >= 20 and getPos()[1] <= 80:
        return True
    else:
        return False
    
def checkWin(board,player):

    # check victory by horizontal
    for i in range (0,4):
        for j in range (0,6):
            currspot = board[i][j]
            if currspot == 0:
                continue
            if currspot == board[i+1][j] and currspot == board[i+2][j] and currspot == board[i+3][j]:
                return True

            
    # check victory by vertical 
    for i in range (0,7):
        for j in range (0,3):
            currspot = board[i][j]
            if currspot == 0:
                continue
            if currspot == board[i][j+1] and currspot == board[i][j+2] and currspot == board[i][j+3]:
                return True
            
    # check victory by normal diagonal
    for i in range (0,4):
        for j in range (0,3):
            currspot = board[i][j]
            if currspot == 0:
                continue
            if currspot == board[i+1][j+1] and currspot == board[i+2][j+2] and currspot == board[i+3][j+3]:
                return True
            
    # check victory by weird diagonal
    for i in range (3,7):
        for j in range (0,2):
            currspot = board[i][j]
            if currspot == 0:
                continue

            if currspot == board[i-1][j+1] and currspot == board[i-2][j+2] and currspot == board[i-3][j+3]:
                return True
            
    return False

# ------------------------------------------------------------- Draw Methods ----------------------------------------------------------

def drawEnd(player):
    # announce winner
    font = pygame.font.SysFont(None, 60)
    if player == 0:
        text = font.render('YELLOW PLAYER WINS!', True, (255,255,0))
    else:
        text = font.render('RED PLAYER WINS!', True, (255,0,0))
    screen.blit(text, (15, 30))

    # replay button
    if isOnButt():
        pygame.draw.rect(screen, (130, 153, 191), pygame.Rect(520, 20, 160, 60))
    else:
        pygame.draw.rect(screen, (167, 184, 212), pygame.Rect(520, 20, 160, 60))

    # cursor
    pygame.draw.circle(screen,(255,255,255),getPos(), 5)

def drawPiece(player):
    # draw the current piece in motion
    if player == 0:
        pygame.draw.circle(screen, (255,0,0), ((50 + getSpot()*100),50), 40)
    else:
        pygame.draw.circle(screen,(255,255,0), ((50 + getSpot()*100),50), 40)
    pygame.draw.circle(screen,(255, 255, 255), (getPos()[0],50), 5)


def drawGame(board):
    # wipe board clean
    screen.fill((0,0,0))
    # draw in all spaces
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(0, 100, 700, 600))
    for i in range(0,7):
        for j in range(0,6):
            curritem = board[i][j]
            if curritem == 1:
                pygame.draw.circle(screen, (255,0,0), (50 + 100*(i), 700 - (50 + 100*(j))), 40) # red space
            elif curritem == 2:
                pygame.draw.circle(screen, (255,255,0), (50 + 100*(i), 700 - (50 + 100*(j))), 40) # yellow space
            else:
                pygame.draw.circle(screen, (0,0,0), (50 + 100*(i), 700 - (50 + 100*(j))), 40) # empty space

# ------------------------------------------------------ Actual Game --------------------------------------------------------------

running = True
while running == True:
    for event in pygame.event.get():
        isGameOver = checkWin(board,player)
        if not isGameOver and event.type == pygame.MOUSEBUTTONUP:
            if board[getSpot()][5] == 0:
                i = 0
                while board[getSpot()][i] != 0:
                    i += 1
                if player == 0:
                    board[getSpot()][i] = 1
                else:
                    board[getSpot()][i] = 2

                player += 1
                player %= 2

        if isGameOver and isOnButt() and event.type == pygame.MOUSEBUTTONUP:
            isGameOver = False
            board = [[0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
            player = 0

        drawGame(board)
        if not isGameOver:
            drawPiece(player)
        else:
            drawEnd(player)
        
        if event.type == pygame.QUIT:
            running = False
        pygame.display.update()
        
pygame.quit()