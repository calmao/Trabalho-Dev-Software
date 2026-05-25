import pygame, sys

pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))

base_font = pygame.font.Font(None, 32) # estilo, tamanho

archive_img = pygame.image.load(r'Interface-de-usuário\arquivo.png').convert_alpha()
type_img = pygame.image.load(r'Interface-de-usuário\digitar.png').convert_alpha()

user_text = ''
typing_active = False

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
    
    def draw(self):
        action = False

        # obter posição do cursor
        
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos): # se o cursor estiver sobre o botão, verificar se o mouse foi clicado
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: # se o mouse for clicado e o botão não tiver sido clicado antes, definir clicked como True
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        
        # desenhar botão
    
        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
# instanciar botões
digitar_botao = Button(100, 200,type_img, 0.5)
arquivo_botao = Button(100, 450, archive_img, 0.5)


while True:
    screen.fill((202, 228, 241))
    if digitar_botao.draw():
        typing_active = not typing_active

    # renderizar texto (mostra sempre)
    text_surface = base_font.render(user_text, True, (0, 0, 0))
    screen.blit(text_surface, (400, 400))
    if arquivo_botao.draw():
        print('arquivo')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and typing_active:
            if event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                user_text += event.unicode
    


    pygame.display.flip()
    clock.tick(60)