import pygame
from constants import *
from Vector import *
import colorsys
import math



def hsv2rgb(h,s,v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))
def Sigmoid(x):
    return 1 / (1 + math.exp(-x))

class Point:
    def __init__(self, position, previousPosition, radius=3, color=(240, 240, 240)):
        self.position = position
        self.previousPosition = previousPosition
        self.radius = radius
        self.color = (hsv2rgb((position.x+position.y)/1000 , 1, 1) )
        self.isClicked = False

    def update(self):
        #compute velocity
        vel = self.position - self.previousPosition

        vel.x *= Friction
        vel.y += G
        vel.y *= Friction

        #set the previous position
        self.previousPosition = self.position
        #update our current position
        self.position = self.position + vel


    def HandleEvents(self, toggle=False, lockNodes=None, joints=None, i_vert= None, bSpace=False):
        if toggle == False:
            if pygame.mouse.get_pressed()[0]:
                mousePosition = pygame.mouse.get_pos()
                m = Vector2(mousePosition[0], mousePosition[1])
                dist = Distance(m, self.position)
                if dist < 10:
                    toggle = True
                    self.isClicked = True

        if self.isClicked == True:
            mousePosition = pygame.mouse.get_pos()
            self.position = Vector2(mousePosition[0], mousePosition[1])
            if pygame.mouse.get_pressed()[1]:
                if self not in lockNodes:
                    lockNodes.append(self)
                else:
                    lockNodes.remove(self)

            if bSpace == True:
                for joint in joints:
                    if i_vert in joint:
                        joints.remove(joint)
                        break




        self.color = (hsv2rgb((self.position.x+self.position.y)/1000 , 1, 1) )


    def Bound(self):
        vel = self.position - self.previousPosition
        if self.position.x < self.radius:
            self.position.x = self.radius
            self.previousPosition.x = self.position.x + vel.x
        if self.position.x > Width-self.radius:
            self.position.x = Width-self.radius
            self.previousPosition.x = self.position.x + vel.x

        if self.position.y < self.radius:
            self.position.y = self.radius
            self.previousPosition.y = self.position.y + vel.y
        if self.position.y > Height-self.radius:
            self.position.y = Height-self.radius
            self.previousPosition.y = self.position.y + vel.y

    def Draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position.TuplePosition(), self.radius)

class Polygon:
    def __init__(self,vertices=[Point(Vector2(10, 10), Vector2(0, 0), 3)], joints=[Vector2(0, -1)],static=[],  lineThickness = 4, color=(0, 0, 0)):
        self.vertices = vertices
        self.joints = joints
        self.color = color
        self.static = static
        self.dists = [ Distance( self.vertices[self.joints[i][0]].position, self.vertices[self.joints[i][1]].position ) for i in range(len(self.joints))]
        self.lineThickness = lineThickness
        self.showPoint = True
    def Update(self, toggle, bSpace):
        for vertice in self.vertices:
            if not vertice in self.static:
                vertice.Bound()
                vertice.update()
            vertice.HandleEvents(toggle, self.static, self.joints, self.vertices.index(vertice), bSpace)
        # self.ConstraintPolygon()


    def ConstraintPolygon(self):
        for i in range(len(self.joints)):
            ln = self.dists[i]
            dist = Distance(self.vertices[self.joints[i][0]].position, self.vertices[self.joints[i][1]].position)
            d_pos = self.vertices[self.joints[i][0]].position - self.vertices[self.joints[i][1]].position
            dl = ln - dist
            current =  d_pos * 0.5  * dl/dist
            pos1 = self.vertices[self.joints[i][0]]
            pos2 = self.vertices[self.joints[i][1]]

            if not (pos1 in self.static or pos2 in self.static):
                self.vertices[self.joints[i][0]].position = self.vertices[self.joints[i][0]].position + current
                self.vertices[self.joints[i][1]].position = self.vertices[self.joints[i][1]].position - current
            if not pos1 in self.static and pos2 in self.static:
                self.vertices[self.joints[i][0]].position = self.vertices[self.joints[i][0]].position + Vector2(current.x * 2, current.y * 2)
            if not pos2 in self.static and pos1 in self.static:
                self.vertices[self.joints[i][1]].position = self.vertices[self.joints[i][1]].position - Vector2(current.x * 2, current.y * 2)
                # self.vertices[self.joints[i][1]].position = (self.vertices[self.joints[i][0]].position - current) * 2


    def Draw(self, screen):
        if len(self.vertices) < 2:
            print("the polygon class must have more than two point")
            return
        for i in range(len(self.joints)):
            start_pos = self.vertices[self.joints[i][0]].position.TuplePosition()
            end_pos = self.vertices[self.joints[i][1]].position.TuplePosition()
            pygame.draw.line(screen, self.color, start_pos, end_pos, self.lineThickness)

        if self.showPoint == True:
            for i in range(len(self.vertices)):
                    self.vertices[i].Draw(screen)

def Box(position, s,  length, thickness, color=(255, 23, 50)):
        vertices = [Point(position, position-1, s),
                    Point(Vector2(position.x + length, position.y), Vector2(position.x-1+length, position.y-1), s),
                    Point(position+length, position - 1 + length, s),
                    Point(Vector2(position.x , position.y+ length), Vector2(position.x-1, position.y-1+length), s)]

        joints = [[0, 1], [1, 2], [2, 3], [3, 0], [2, 0], [1, 3]]

        return Polygon(vertices, joints, thickness, color)

def Rope(position, length, n, radius=3, thickness=3, color=(53, 180, 200)):
    x = position.x
    y = position.y
    vertices = [Point(Vector2(x + length * i , y), Vector2(x-10, y), radius) for i in range(n)]
    joints = [ [i, i+1] for i in range(len(vertices)-1)]
    static = [vertices[0], vertices[-1]]

    return Polygon(vertices, joints,static, thickness, color)

def Cloth(position, horiz, vertiz, t=20, radius= 5, thickness=3, vertical=True, horizontal=True, Diagonal1=False, Diagonal2=False,showPoint=False, color=(240, 240, 240)):
    x , y = position.x, position.y
    vertices = []
    for j in range(vertiz):
        for i in range(horiz):
            vertices.append( Point(Vector2(x+i*t, y+j*t), Vector2(x+i*t, y+j*t), radius ) )

    joints = []

    # Horizontal connection
    if horizontal == True:
        for i in range(len(vertices)-1):
            if i % horiz != horiz -1:
                joints.append([i, i+1])
    # Vertical connection
    if vertical == True:
        for i in range(len(vertices) - horiz):
            joints.append( [i, i+horiz] )

    #first diagonal connection
    if Diagonal1 == True:
        for i in range(len(vertices) - horiz-1):
            if i %horiz != horiz-1:
                joints.append( [i, i + horiz + 1] )
    # second diagonal connection
    if Diagonal2 ==True:
        for i in range(len(vertices) - horiz):
            if i % horiz != 0:
                joints.append( [i, i+horiz-1] )

    static = [vertices[0], vertices[horiz//2], vertices[horiz-1]]


    return Polygon(vertices, joints, static, thickness, color)
