import pygame, random

negro = (0, 0, 0)
blanco = (255, 255, 255)
verde = (0, 255, 0)

pygame.init()
pygame.mixer.init()
pantalla = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Rocket Destroyer')
clock = pygame.time.Clock()

class jugador(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load('jugador.png').convert()
    self.image = pygame.transform.scale(self.image, (140, 140))
    self.image.set_colorkey(negro)
    self.rect = self.image.get_rect()
    self.rect.centerx = 400
    self.rect.bottom = 600
    self.velocidad_x = 0
    self.vida = 100

  def update(self):
    self.velocidad_x = 0
    tecla = pygame.key.get_pressed() 
    if tecla[pygame.K_LEFT]:
      self.velocidad_x = -5
    elif tecla[pygame.K_RIGHT]:
      self.velocidad_x = 5
    
    self.rect.x += self.velocidad_x
    if self.rect.right > 800:
        self.rect.right = 800
    if self.rect.left < 0:
        self.rect.left = 0

  def disparo(self):
      laser = Laser(self.rect.centerx, self.rect.top)
      sprites.add(laser)
      laseres.add(laser)
      laser_sonido.play()

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('laser1.png')
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.velocidad_y = -10

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.bottom < 0:
            self.kill()

class meteoro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(imagenes_meteoro)
        self.image.set_colorkey(negro)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.velocidad_y = random.randrange(1, 10)
        self.velocidad_x = random.randrange(-5, 5)

    def update(self):
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_x
        if self.rect.left == -30 or self.rect.right == 830 or self.rect.top > 600:
            self.rect.x = random.randrange(800 - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.velocidad_y = random.randrange(1, 10)
            self.velocidad_x = random.randrange(-5, 5)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, centro):
        super().__init__()
        self.image = imagenes_explosion[0]
        self.rect = self.image.get_rect()
        self.rect.center = centro
        self.frame = 0
        self.actualizacion = pygame.time.get_ticks()
        self.ratio_frames = 50

    def update(self):
        ahora = pygame.time.get_ticks()
        if ahora - self.actualizacion > self.ratio_frames:
            self.actualizacion = ahora
            self.frame += 1
            if self.frame == len(imagenes_explosion):
                self.kill()
            else:
                centro = self.rect.center
                self.image = imagenes_explosion[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = centro

def barra_vida(superficie, x, y, porcentaje):
    llenar = (porcentaje/100)*100
    borde = pygame.Rect(x, y, 100, 10)
    llenar = pygame.Rect(x, y, llenar, 10)
    pygame.draw.rect(superficie, verde, llenar)
    pygame.draw.rect(superficie, blanco, borde, 2)


def pantalla_fin():
    texto(pantalla, 'Destroyer Rocket', 65, 400, 150)
    texto(pantalla, '¡A que no duras mas de 1 minuto!', 27, 400, 300)
    texto(pantalla, 'Presiona alguna tecla', 20, 400, 450)
    pygame.display.flip()
    espera = True
    while espera:
        clock.tick(60)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYUP:
                espera = False

def texto(superficie, texto, tamaño, x, y):
    fuente = pygame.font.SysFont('serif', tamaño)
    superficie_texto = fuente.render(texto, True, blanco)
    texto_recta = superficie_texto.get_rect()
    texto_recta.midtop = (x, y)
    superficie.blit(superficie_texto, texto_recta)

def pausa():
    pausado = True
    texto(pantalla, 'juego en Pausa', 65, 400, 150)
    texto(pantalla, 'Presiona la tecla "p" para continuar', 40, 400, 300)
    pygame.display.flip()
    while pausado:
        pygame.mixer.music.set_volume(0.1)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pausado = False
                ejecutandose = False
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_p:
                    pausado = False
                    pygame.mixer.music.set_volume(0.4)
                    pygame.mixer.music.play(loops = -1)
                
imagenes_meteoro = []
rutas_meteoros = ['meteoro_grande1.png','meteoro_grande2.png','meteoro_grande3.png','meteoro_grande4.png', 'meteoro_mediano1.png','meteoro_mediano2.png', 'meteoro_pequeño1.png', 'meteoro_pequeño2.png']

for img in rutas_meteoros:
    imagenes_meteoro.append(pygame.image.load(img).convert())

fondo = pygame.image.load('fondo.png').convert()

imagenes_explosion = []

for i in range(1, 10):
    imagen = 'explosion_normal{}.png'.format(i)
    imagen = pygame.image.load(imagen).convert()
    imagen.set_colorkey(negro)
    imagen = pygame.transform.scale(imagen, (70, 70))
    imagenes_explosion.append(imagen)


laser_sonido = pygame.mixer.Sound('laser_sonido.ogg')
musica = pygame.mixer.Sound('musica.ogg')
explosion_sonido = pygame.mixer.Sound('explosion.wav')
pygame.mixer.music.load('musica.ogg')
pygame.mixer.music.set_volume(0.4)

pygame.mixer.music.play(loops = -1)

fin = True

ejecutandose = True
while ejecutandose:
  if fin:
      pantalla_fin()
      fin = False
      sprites = pygame.sprite.Group()
      meteoros = pygame.sprite.Group()
      laseres = pygame.sprite.Group()

      Jugador = jugador()
      sprites.add(Jugador)

      for i in range(10):
        Meteoro = meteoro()
        sprites.add(Meteoro)
        meteoros.add(Meteoro)
  clock.tick(60)
  for evento in pygame.event.get():
    if evento.type == pygame.QUIT:
      ejecutandose = False
    elif evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_p:
            pausa()
        elif evento.key == pygame.K_SPACE:
            Jugador.disparo()
            
  sprites.update()

  choque = pygame.sprite.groupcollide(meteoros, laseres, True, True)
  for i in choque:
    explosion = Explosion(i.rect.center)
    sprites.add(explosion)
    Meteoro = meteoro()
    sprites.add(Meteoro)
    meteoros.add(Meteoro)
    explosion_sonido.play()

  choque = pygame.sprite.spritecollide(Jugador, meteoros, True)
  for i in choque:
      Jugador.vida -= 10
      Meteoro = meteoro()
      sprites.add(Meteoro)
      meteoros.add(Meteoro)
      if Jugador.vida == 0:
          fin = True

  sprites.draw(pantalla)

  pantalla.blit(fondo, [0, 0])

  sprites.draw(pantalla)

  barra_vida(pantalla, 5, 5, Jugador.vida)

  pygame.display.flip()
pygame.quit()
