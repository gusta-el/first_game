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
````
	
Por padrão, estamos criando todas as classes de cena dentro da pasta "scenes"
	
Lembrando que sempre que um novo estado for criado, este deverá ser adicionado à classe [```Manager```](https://github.com/gusta-el/first_game#Manager)
	
### Renderer
(```renderer.py```)

Esta classe é simplesmente um _wrapper_ que facilita e gerencia recursos de renderização sem ter que nos preocupar com problemas comuns da renderização do Pygame