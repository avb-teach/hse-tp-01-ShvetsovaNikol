import os
import sys
import shutil
# команды отсюда https://habr.com/ru/companies/selectel/articles/547290/
input_dir=sys.argv[1]
output_dir=sys.argv[2]
if not os.path.exists(input_dir) or not os.path.exists(input_dir):
    print("Не существует или не является директорией")
    sys.exit(1)
if not  os.path.exists(output_dir) or not os.path.exists(output_dir):
    os.mkdirs(output_dir)
def novoeimya(name, dest):
    bs, ext = os.path.splitext(name)
    cdd=name 
    i=0
    while os.path.exists(os.path.join(dest, cdd)):
        i+=1
        cdd=f"{bs}{i}{ext}"
    return cdd
# функция novoeimya https://stackoverflow.com/questions/13852700/create-file-but-if-name-exists-add-number#:~:text=def%20nextnonexistent,%28root%2C%20i%2C%20ext
for root, dirs, files in os.walk(input_dir):
    for imyafile in files:
        pathscr=os.path.join(root, imyafile)
        nname=novoeimya(imyafile, output_dir)
        pathdest=os.path.join(output_dir, nname)
        shutil.copy2(pathscr, pathdest)
# проход по всем папкам https://stackoverflow.com/questions/19777292/recursively-copy-and-flatten-a-directory-with-python/19777568#19777568
# перенос файла https://docs.python.org/3/library/shutil.html

