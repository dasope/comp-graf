from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

print("Quantidade de lados do prisma:")
r = 1
vertices = []
linhas = []
faces = []
facesBase = []
facesTopo = []
numeroPontos = int(input())
for i in range(0,numeroPontos+1):
    x = r*cos(((2*pi)/numeroPontos)*i)
    y = 0
    z = r*sin(((2*pi)/numeroPontos)*i)
    vertices.insert(i+1,(x,y,z))

for i in range(0,numeroPontos+1):
    x = r*cos(((2*pi)/numeroPontos)*i)
    y = 2
    z = r*sin(((2*pi)/numeroPontos)*i)
    vertices.insert(i+numeroPontos,(x,y,z))
   
for j in range(0,numeroPontos):
    if j != numeroPontos -1:
        linhas.insert(j,(j,j+1))
    else:
        linhas.insert(j+numeroPontos,(j,0))
    linhas.insert(j+numeroPontos,(j+numeroPontos,j+numeroPontos+1))
    linhas.insert(j+numeroPontos*2,(j,j+numeroPontos))

for l in range(0, numeroPontos):
    if l == numeroPontos-1:
        faces.insert(l,(l,l+1-numeroPontos,l+1,l+numeroPontos))
        facesBase.insert(l, l)
        facesTopo.insert(l, l+numeroPontos)
        break
    facesBase.insert(l, l)
    faces.insert(l,(l,l+1,l+numeroPontos+1,l+numeroPontos))
    facesTopo.insert(l, l+numeroPontos)

cores = ( (1,0,0),(0,1,0),(0,0,1),(1,1,0),(0,1,1),(1,0,1),(1,0.5,0.5),(0.5,1,0.5),(0.5,0.5,1))
corBase = ((1,1,1))

def Prisma():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        if i > 9:
            i = 0
        glColor3fv(cores[i])
        for vertex in face:
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glBegin(GL_POLYGON)
    for vertex in facesBase:
        glColor3fv(corBase)
        glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_POLYGON)
    for vertex in facesTopo:
        glColor3fv(corBase)
        glVertex3fv(vertices[vertex])
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()

def pol():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(0.5,1,1,0.5)
    Prisma()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5,timer,1)

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Prisma com N lados!")
glutDisplayFunc(pol)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(25,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-12)
glRotatef(0,50,0,0)
glutTimerFunc(5,timer,1)
glutMainLoop()
