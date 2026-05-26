import pygame, sys
import os
import transcrever

# Adicionar o diretório pai ao path para importar transcrever
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



pygame.init()


clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))

base_font = pygame.font.Font(None, 32) # estilo, tamanho

archive_img = pygame.image.load(r'Interface-de-usuário\arquivo.png').convert_alpha()
type_img = pygame.image.load(r'Interface-de-usuário\digitar.png').convert_alpha()

user_text = ''
archive_path = ''
typing_active_arq = False
typing_active_dig = False

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.visible = True
    
    def draw(self):
        if not self.visible:
            return False

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
    if not typing_active_arq and not typing_active_dig:
        if digitar_botao.draw():
            typing_active_dig  = True
            digitar_botao.visible = False

        if arquivo_botao.draw():
            typing_active_arq = True
            arquivo_botao.visible = False
            
    else:
        text_surface = base_font.render(user_text, True, (0, 0, 0))
        screen.blit(text_surface, (100, 100))

        info_surface = base_font.render('ESC para sair', True, (50, 50, 50))
        screen.blit(info_surface, (100, 140))
    if typing_active_arq:
            path_surface = base_font.render(archive_path, True, (0, 0, 0))
            screen.blit(path_surface, (100, 100))
    
            info_surface = base_font.render('ESC para sair', True, (50, 50, 50))
            screen.blit(info_surface, (100, 140))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and typing_active_dig:
                typing_active = False
                digitar_botao.visible = True
                arquivo_botao.visible = True
            elif typing_active_dig:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

                arquivo = open('arquivo.txt', 'w')
                arquivo.write(user_text)
                arquivo.close()

                if event.key == pygame.K_RETURN:
                    transcrever.transcrever('arquivo.txt')



            if event.key == pygame.K_ESCAPE and typing_active_arq:
                typing_active_arq = False
                digitar_botao.visible = True
                arquivo_botao.visible = True
            elif typing_active_arq:
                if event.key == pygame.K_BACKSPACE:
                    archive_path = archive_path[:-1]
                elif event.key == pygame.K_RETURN:
                    arquivo = open(archive_path, 'r')
                    content = arquivo.read()
                    content_surface = base_font.render(content, True, (0, 0, 0))
                    screen.fill((202, 228, 241))
                    screen.blit(content_surface, (100, 100))
                    arquivo.close()
                else:
                    archive_path += event.unicode
    


    pygame.display.flip()
    clock.tick(60)
