import os
import shutil
to_dir='C:/Users/KskYm/Downloads'
from_dir='C:/Users/KskYm/Deskop/imageFiles'
list=os.listdir(from_dir)
for file in list:
  root,extension=os.path.splitext(file)
  if extension=='':
    continue
  if extension in [ '.txt', '.doc', '.docx', '.pdf']:
    path1=from_dir + '/' + file
    path2=to_dir + '/' + 'imageFiles'
    path3=to_dir + '/' + 'imageFiles' + file

    if os.path.exists(path2):
      print('Moving' + file + '...')
      shutil.move(path1,path3)
    else:
      os.makedirs(path2)
      print('Moving' + file + '...')
      shutil.move(path1,path3)
    
