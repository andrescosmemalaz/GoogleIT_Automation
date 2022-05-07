# import os 
# os.remove("novel.txt")
# #Eliminar el archivo existente
# import os
# # os.rename("first_draft.txt", "finished_masterpiece.txt")
# print(os.path.exists("spider.txt"))

import os
file= "file.dat"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
	print(os.path.isfile(file))

# import os

# # w = os.path.abspath("spider.txt")

# # print(os.getcwd())
# # os.mkdir("new_dir")

# z = os.listdir("website")

# print(z)


