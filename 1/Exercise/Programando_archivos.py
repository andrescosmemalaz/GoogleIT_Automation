
file = open("F:/andres/Univerisdad/Ciclo 5/Google IT/1/Exercise/spider.txt")
# file = open("spider.txt")
# print(file.readline()) #Leer primera linea de texto
print(file.read()) #Leer todo el archivo completo 
file.close()
#Se realizarse el cierre de los archivos por 
# 3 razones principales : 

# En primer lugar, cuando un archivo está abriendo el script, el sistema de archivos 
# generalmente lo bloquea y por lo tanto ningún otro programa o scripts puede usarlo 
# hasta que haya terminado. En segundo lugar, hay un número limitado de descriptores 
# de archivos que puede crear antes de que el sistema de archivos se quede sin ellos. 
# Aunque este número puede ser alto, es posible abrir muchos archivos y agotar los 
# recursos del sistema de archivos. Esto puede suceder si estamos abriendo archivos 
# en un bucle, por ejemplo. En tercer lugar, dejar archivos abiertos colgando puede 
# conducir a condiciones de carrera que ocurren cuando varios procesos intentan modificar 
# y leer desde un recurso al mismo tiempo y pueden causar todo tipo de comportamientos inesperados. 
# Nadie gana en condiciones de carrera.

# import os
# import pathlib


# import os

# simp_path = 'spider.txt'
# abs_path = os.path.abspath(simp_path)
# print(abs_path)
# z = pathlib.PurePath(abs_path)
# print(z)
# p = pathlib.PurePath(abs_path)
# p = p.parts
# print(p)
# # file = open("spider.txt")
# # print(file.readline())


# file = "spider.txt"
# union = cwd + file 
# file = open(union)
# print(file.readline())

comments = "# Start of a new Python program"
len(comments)