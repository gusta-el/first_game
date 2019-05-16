# first_game
1º Semestre: jogo do Banin e do Alan


## História

Aqui vai a história do Jogo

## Estrutura de classes

O arquivo python a ser rodado é o ```pystarter.py```, que também pode ser rodado executando o arquivo ```roda.bat```

### Manager
(```manager.py```)

Esta é a classe que gerencia os States a partir de uma lista de objetos State, e um index que representa qual state está sendo renderizado no momento.
	
### State
(```states/state.py```)

Esta é uma classe abstrata que contém apenas as definições de um estado de jogo (Ex. menu, primeira fase, opções, tela de game over, etc)
Cada State contém suas própria rotinas individuais de ```start()```, ```update()```, ```render()``` e ```input()```
Sempre que um novo estado for criado, será necessário criar uma classe que extende esta classe State no seguinte formato:
	
```python
from scenes.scene import Scene

class NomeDaCena(Scene):

def start(self):
    pass

def input(self, keys):
    pass

def update(self, delta):
    pass

def render(self, renderer):
    pass
```
	
Por padrão, estamos criando todas as classes de cena dentro da pasta "scenes"
	
Lembrando que sempre que um novo estado for criado, este deverá ser adicionado à classe [```Manager```](https://github.com/gusta-el/first_game#Manager)
	
### Renderer
(```renderer.py```)

Esta classe é simplesmente um _wrapper_ que facilita e gerencia recursos de renderização sem ter que nos preocupar com problemas comuns da renderização do Pygame.

Métodos da classe ```Renderer```:

- ```drawLine(x1, y1, x2, y2)```: Desenha uma linha do ponto (x1, y1) até o ponto (x2, y2)
- ```drawRect(x, y, w, h)```: Desenha a borda de um retângulo com o canto superior esquerdo no ponto (x, y), com w de largura e h de altura
- ```fillRect(x, y, w, h):```: Preenche a borda de um retângulo com o canto superior esquerdo no ponto (x, y), com w de largura e h de altura
- ```drawCircle(x, y, radius)```: Desenha uma borda de um círculo com centro em (x, y) e "radius" de raio
- ```fillCircle(x, y, radius)```: Preenche um círculo com centro em (x, y) e "radius" de raio
- ```setColor(r, g, b, a)```: Define a cor que os próximos desenhos serão feitos
- ```drawTexture(texture, x, y, w, h, rotation=0, off_x=0, off_y=0)```: Desenha uma textura com centro na posição (x, y), altura h e largura w, com determinada rotação (opcional), e deslocamento x e y (off_x, off_y) também opcional

### Como criar objetos

Toda nova funcionalidade deve ser pensada visando orientação a objetos.
Os objetos por padrão devem ser criados na pasta "objects".
Crie um arquivo com qualquer nome, e declare a estrutura de classe desta forma:

```python
import pygame
class NomeDaClasse:

    def __init__(self):
        #Esse é o construtor, declare suas propriedades aqui no estilo:
        self.minha_propriedade = "algum valor"

    def render(self, renderer):
        #Aqui vai o código de como o objeto será renderizado
        pass

    def update(self, delta):
        #Aqui vai toda a estrutura lógica que deve ser feito todo frame (como movimentação de personagem, contagem de tempo, etc)
        pass

    def input(self, event):
        #Este método é chamado sempre que alguma ação é feita por parte do usuário (movimentação e clique de mouse, clique de teclas do teclado, etc). A estrutura do objeto ```event``` pode ser visto nesta documentação: https://www.pygame.org/docs/ref/event.html

        #Alguns exemplos:

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #Aqui significa que o usuário clicou o botão da seta direcional esquerda
                pass

        pass


```

Lista de todos os ```event.type``` e suas variáveis internas:

- QUIT             none
- ACTIVEEVENT      gain, state
- KEYDOWN          unicode, key, mod
- KEYUP            key, mod
- MOUSEMOTION      pos, rel, buttons
- MOUSEBUTTONUP    pos, button
- MOUSEBUTTONDOWN  pos, button
- JOYAXISMOTION    joy, axis, value
- JOYBALLMOTION    joy, ball, rel
- JOYHATMOTION     joy, hat, value
- JOYBUTTONUP      joy, button
- JOYBUTTONDOWN    joy, button
- VIDEORESIZE      size, w, h
- VIDEOEXPOSE      none
- USEREVENT        code

#### Colocar os objetos em uma cena

Depois de definido a classe de objeto criada, é necessário colocar uma instância deste objeto em alguma cena. Atualmente temos definido uma única cena chamada ```DefaultScene```. Para que o objeto seja renderizado corretamente, é necessário criar a instância, e chamar os métodos da seguinte forma:

```python
from objects.nomedoarquivo import NomeDaClasse
class DefaultScene(Scene):

    def start(self):
        ...
        self.objeto = NomeDaClasse(parametros)
        ...

    def input(self, event):
        ...
        self.objeto.input(event)
        ...

    def update(self, delta):
        ...
        self.objeto.update(delta)
        ...

    def render(self, renderer):
        ...
        self.objeto.render(renderer)
        ...
```

### Física e detecção de colisão

Atualmente existe uma classe chamada ```Body``` que representa um corpo com colisão AABB (Axis Aligned Bounding Box). Para atrelar um corpo a um objeto, o objeto criado deve ser uma especialização da classe ```Body```, tendo como sua declaração a seguinte estrutura:

```python

from physics.body import Body
class MeuObjeto(Body):

    def __init__(self, parametros):
        super().__init__(pygame.Vector2(Posição X, Posição Y), 'rect', pygame.Vector2(Largura, Altura), 'dynamic') #Objetos "dynamic" podem ser movidos, enquanto objetos "static" são fixos no mapa e não se movem (feito para economizar processamento)
    ... resto da classe

    def collide(self, other):
        return True
```

Ao definir esta estrutura, as seguintes propriedades ficarão disponíveis dentro do objeto:

- ```self.position```: Posição do objeto, (no caso, simplesmente desenhe a textura nesta posição ao invés de ter outra variável de posição só para a textura). Use somente para VER a posiçaõ do objeto, e não para DEFINIR ela (vide propriedade a baixo)
- ```self.velocity```: Velocidade do objeto (é recomendável movimentar o objeto por esta variável ao invés de definir a posição dele manualmente, a biblioteca de física já lida com isso)

#### Detecção de colisão

O método ```collide(other)``` receberá um evento de quando este objeto colidiu com algum outro objeto.
Dentro deste método você pode fazer alguma ação quando certo objeto colide com outro objeto (Ex. um projétil atinge o jogador, destruindo o projétil, e causando dano). A colisão pode ser desligada (os objetos atravessam entre si) caso o retorno desta função seja ```False```. Por padrão, sempre retorne ```True``` no final deste método

#### Classe World

Para que a colisão seja calculada corretamente, dentro da classe da cena (no caso padrão, a cena é a ```DefaultScene```) é necessário ter uma instância da classe ```World``` que é um objeto que armazena todos os outros objetos que contém colisão, ele é o responsável por fazer o cálculo e atualizar as posições dos objetos.

Para registrar um objeto dentro do mundo, para que seus cálculos sejam feitos, dentro do método ```start()``` na classe ```DefaultScene``` (depois da inicialização do ```World```), use o código:

```python
from objects.nomedoarquivo import NomeDaClasse

class DefaultScene(Scene):

    def start(self):
        self.objeto = MeuObjeto()
        self.world = World(Vector2(0, 0))
        self.world.addBody(self.objeto)

    ...
```

Dentro do objeto de física, caso queira que a caixa de colisão seja desenhada (para propósitos de teste), apenas chame a função (dentro da classe do SEU objeto criado):

```python
    def render(self, renderer):
        super().render(renderer)
```