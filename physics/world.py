class World:

    def __init__(self, gravity):
        self.gravity = gravity
        self.bodies = []

    #TODO: Tem que ver a formula
    def checkCollisionAABBCircle(self, aabb, circle):
        return False

    #TODO: Lembrando que body.position é o CENTRO do retângulo
    def checkCollisionAABB(self, aabb1, aabb2):
        return False

    #TODO: Distancia dos dois tem q ser menor que a soma dos raios
    def checkCollisionCircle(self, circle1, circle2):
        return (circle1.position - circle2.position).length() < circle1.size + circle2.size

    def update(self, delta):
        for body in self.bodies:
            nextPos = body.position + body.velocity

            if len(self.bodies) > 1:
                for  body2 in self.bodies:
                    if body2 != body:

                        if body.shape == 'rect':
                            if body2.shape == 'circle':
                                if not checkCollisionAABBCircle(body, body2):
                                    #Não colidiu
                                    body.position = nextPos
                                else:
                                    #TODO: Calcula a normal, e reseta a velocidade
                                    pass
                            if body2.shape == 'rect':
                                if not checkCollisionAABB(body, body2):
                                    #Não colidiu
                                    body.position = nextPos
                                else:
                                    pass
                                    #TODO: Calcula a normal, reseta a velocidade

                        elif body.shape == 'circle':
                            if body2.shape == 'circle':
                                if not checkCollisionCircle(body, body2):
                                    #Não colidiu
                                    body.position = nextPos
                                else:
                                    #TODO: Calcula a normal, e reseta a velocidade
                                    pass
                            if body2.shape == 'rect':
                                if not checkCollisionAABBCircle(body2, body):
                                    #Não colidiu
                                    body.position = nextPos
                                else:
                                    pass
                                    #TODO: Calcula a normal, reseta a velocidade
            else:
                body.position = nextPos
                            

        pass

    def addBody(self, body):
        self.bodies.append(body)

    def render(self, renderer):
        for body in self.bodies:
            body.render(renderer)
        pass