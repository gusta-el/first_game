import pygame, math

class World:

    def __init__(self, gravity):
        self.gravity = gravity
        self.bodies = []



        print("Teste, representando 10, 4 em termos de (1, 0)")
        print(self.termsOf(pygame.Vector2(10, 4), pygame.Vector2(1, 0)))

    #TODO: Tem que ver a formula
    def checkCollisionAABBCircle(self, aabb, circle):
        rect = pygame.Rect(aabb.position.x - aabb.size.x/2, aabb.position.y - aabb.size.y/2, aabb.size.x, aabb.size.y)
        return self.collision_rc(rect.x, rect.y, rect.width, rect.height, circle.position.x, circle.position.y, circle.size)

    #TODO: Lembrando que body.position é o CENTRO do retângulo
    def checkCollisionAABB(self, aabb1, aabb2):
        a1 = pygame.Rect(aabb1.position.x - aabb1.size.x/2, aabb1.position.y - aabb1.size.y/2, aabb1.size.x, aabb1.size.y)
        a2 = pygame.Rect(aabb2.position.x - aabb2.size.x/2, aabb2.position.y - aabb2.size.y/2, aabb2.size.x, aabb2.size.y)

        dfx = a1.x - a2.x
        dfy = a1.y - a2.y

        return False if not a1.colliderect(a2) else (dfx, dfy)

    #TODO: Distancia dos dois tem q ser menor que a soma dos raios
    def checkCollisionCircle(self, circle1, circle2):
        res = (circle1.position - circle2.position).length() < circle1.size + circle2.size
        return False if not res else circle2.position - circle1.position

    def collision_rc(self, rleft, rtop, width, height,   # rectangle definition
                center_x, center_y, radius):  # circle definition
        """ Detect collision between a rectangle and circle. """

        # complete boundbox of the rectangle
        rright, rbottom = rleft + width/2, rtop + height/2

        # bounding box of the circle
        cleft, ctop     = center_x-radius, center_y-radius
        cright, cbottom = center_x+radius, center_y+radius

        # trivial reject if bounding boxes do not intersect
        if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
            return False  # no collision possible

        # check whether any point of rectangle is inside circle's radius
        for x in (rleft, rleft+width):
            for y in (rtop, rtop+height):
                # compare distance between circle's center point and each point of
                # the rectangle with the circle's radius
                if math.hypot(x-center_x, y-center_y) <= radius:
                    return True  # collision detected

        # check if center of circle is inside rectangle
        if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
            return True  # overlaid

        return False  # no collision detected

    def update(self, delta):
        for body in self.bodies:
            lastPos = pygame.math.Vector2(body.position)
            body.position += body.velocity

            if len(self.bodies) > 1 and body.bodyType == 'dynamic':
                for  body2 in self.bodies:
                    if body2 != body:

                        if body.shape == 'rect':
                            #NÃO FUNCIONA
                            if body2.shape == 'circle':
                                if self.checkCollisionAABBCircle(body, body2):
                                    body.position = lastPos
                                    body.velocity = pygame.math.Vector2(0, 0)
                                    body.position += body.velocity
                                    break

                            if body2.shape == 'rect':
                                c = self.checkCollisionAABB(body, body2)
                                if isinstance(c, tuple) :
                                    body.position = lastPos

                                    print(c)

                                    if(abs(c[0]) > abs(c[1])):
                                        if(c[0] > 0):
                                            body.position.x = body2.position.x + body2.size.x/2 + body.size.x/2
                                            body.velocity.x = 0
                                        else:
                                            body.position.x = body2.position.x - body2.size.x/2 - body.size.x/2
                                            body.velocity.x = 0
                                    elif(abs(c[0]) < abs(c[1])):
                                        if(c[1] > 0):
                                            body.position.y = body2.position.y + body2.size.y/2 + body.size.y/2
                                            body.velocity.y = 0
                                        else:
                                            body.position.y = body2.position.y - body2.size.y/2 - body.size.y/2
                                            body.velocity.y = 0

                                    body.position += body.velocity

                                    break

                        elif body.shape == 'circle':
                            if body2.shape == 'circle':
                                c = self.checkCollisionCircle(body, body2)
                                if isinstance(c, pygame.Vector2):
                                    body.position = lastPos
                                    
                                    t = self.termsOf(body.velocity, c)
                                    #Limpa

                                    t.y = 0

                                    #Transforma de volta
                                    v = self.termsOf(pygame.Vector2(1, 0), c)
                                    t = self.termsOf(t, v)
                                    
                                    body.velocity = t

                                    #body.position += body.velocity
                                    break

                            #NÃO FUNCIONA
                            if body2.shape == 'rect':
                                if self.checkCollisionAABBCircle(body2, body):
                                    body.position = lastPos
                                    body.velocity = pygame.math.Vector2(0, 0)
                                    body.position += body.velocity
                                    break
                            

        pass

    #https://yutsumura.com/express-a-vector-as-a-linear-combination-of-other-vectors/#Solution
    def termsOf(self, vec, term):
        cd = term.rotate(90)

        print("Termo " + str(term) + ", vetor perp " + str(cd))

        x = term.x
        y = term.y
        xd = cd.x
        yd = cd.y 
        r = vec.x
        s = vec.y

        a = (r + (s*xd/(yd-y) - (r*xd*y/(x*yd - x*y))))/x
        print("a: " + str(a))
        b = (s*x - r*y)/(x*yd-x*y)
        print("b: " + str(b))

        return pygame.Vector2(a, b)

    def addBody(self, body):
        self.bodies.append(body)

    def render(self, renderer):
        for body in self.bodies:
            body.render(renderer)
        pass