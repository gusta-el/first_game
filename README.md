# first_game
1? Semestre: jogo do Banin e do Alan


## Hist?ria

Aqui vai a hist?ria do Jogo

## Estrutura de classes

O arquivo python a ser rodado ? o ```pystarter.py```, que tamb?m pode ser rodado executando o arquivo ```roda.bat```

### Manager (```manager.py```)

	Esta ? a classe que gerencia os States a partir de uma lista de objetos State, e um index que representa qual state est? sendo renderizado no momento.
	
### State (```states/state.py```)
	
	Esta ? uma classe abstrata que cont?m apenas as defini??es de um estado de jogo (Ex. menu, primeira fase, op??es, tela de game over, etc)
	Cada State cont?m suas pr?pria rotinas individuais de ```start()```, ```update()```, ```render()``` e ```input()```
	Sempre que um novo estado for criado, ser? necess?rio criar uma classe que extende esta classe State no seguinte formato:
	
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
	
	Por padr?o, estamos criando todas as classes de cena dentro da pasta "scenes"
	
	Lembrando que sempre que um novo estado for criado, este dever? ser adicionado ? classe [```Manager```](https://github.com/gusta-el/first_game#Manager)
	
### Renderer

	Esta classe ? simplesmente um _wrapper_ que facilita e gerencia recursos de renderiza??o sem ter que nos preocupar com problemas comuns da renderiza??o do Pygame