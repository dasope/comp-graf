from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from math import *

print("Informe o numero de lados: ")
r = 1;
vertices = []
linhas = []
faces = []
facesBase = []
facesTopo = []
numeroPontos = int(input())
for i in range(0, numeroPontos + 1):
    x = r * cos(((2 * pi) / numeroPontos) * i)
    y = 0
    z = r * sin(((2 * pi) / numeroPontos) * i)
    vertices.insert(i + 1, (x, y, z))

for i in range(0, numeroPontos + 1):
    x = r * cos(((2 * pi) / numeroPontos) * i)
    y = 2
    z = r * sin(((2 * pi) / numeroPontos) * i)
    vertices.insert(i + numeroPontos, (x, y, z))

for j in range(0, numeroPontos):
    if j != numeroPontos - 1:
        linhas.insert(j, (j, j + 1))
    else:
        linhas.insert(j + numeroPontos, (j, 0))
    linhas.insert(j + numeroPontos, (j + numeroPontos, j + numeroPontos + 1))
    linhas.insert(j + numeroPontos * 2, (j, j + numeroPontos))

for l in range(0, numeroPontos):
    if l == numeroPontos - 1:
        faces.insert(l, (l, l + 1 - numeroPontos, l + 1, l + numeroPontos))
        facesBase.insert(l, l)
        facesTopo.insert(l, l + numeroPontos)
        break
    facesBase.insert(l, l)
    faces.insert(l, (l, l + 1, l + numeroPontos + 1, l + numeroPontos))
    facesTopo.insert(l, l + numeroPontos)

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))
corBase = ((1, 1, 1))
corTopo = ((0.5, 0.5, 0.5))


def calculaFace(face):
    v0 = vertices[face[0]]
    v1 = vertices[face[1]]
    v2 = vertices[face[2]]

    U = (v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2])
    V = (v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2])
    N = ((U[1] * V[2] - U[2] * V[1]), (U[2] * V[0] - U[0] * V[2]), (U[0] * V[1] - U[1] * V[0]))

    TamN = sqrt(N[0] * N[0] + N[1] * N[1] + N[2] * N[2])
    return (N[0] / TamN, N[1] / TamN, N[2] / TamN)

def Prisma():
    glBegin(GL_QUADS)
    i = 0
    for face in faces:
        if i > 7:
            i = 0
        glColor3fv(cores[i])
        glNormal3fv(calculaFace(face))
        for vertex in face:
            # glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i + 1
    glEnd()

    glBegin(GL_POLYGON)
    for vertex in facesBase:
        glColor3fv(corBase)
        glVertex3fv(vertices[vertex])
    glEnd()

    glBegin(GL_POLYGON)
    for vertex in facesTopo:
        glColor3fv(corTopo)
        glVertex3fv(vertices[vertex])
    glEnd()

    # glVertex3fv(vertices[vertex])
    glColor3fv((0, 0.5, 0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()


def abacaxi():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glRotatef(1, 1, 1, 0)
    Prisma()
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(5, timer, 1)

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, float(w) / float(h), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 1, 5, 0, 0, 0, 0, 1, 0)


def init():
    mat_ambient = (0.0, 0.0, 0.5, 1.0)
    mat_ambient = (0.4, 0.0, 0.0, 1.0)
    mat_diffuse = (1.0, 0.0, 0.0, 1.0)
    mat_specular = (0.0, 1.0, 0.0, 1.0)
    mat_shininess = (50,)
    light_position = (0.5, 0.5, 0.5)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glShadeModel(GL_FLAT)
    glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, mat_shininess)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("Solido Iluminado")
glutReshapeFunc(reshape)
glutDisplayFunc(abacaxi)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0., 0., 0., 1.)
gluPerspective(25, 800.0 / 600.0, 0.1, 50.0)
glTranslatef(0.0, 0.0, -8)
glRotatef(45, 0, 0, 0)
glutTimerFunc(50, timer, 1)
init()
glutMainLoop()