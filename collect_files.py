import sys
import os
input_dir=sys.argv[1]
output_dir=sys.argv[2]
if not os.path.exists('input_dir') or not os.path.isdir('input_dir'):
    print("Не существует или не является директорией")
if not os.path exists('output_dir') or not os.path.isdir('output_dir'):
    os.mkdir('output_dir')