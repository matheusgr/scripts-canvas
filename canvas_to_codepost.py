import os
import zipfile
import rarfile

alunos = {}

# students.csv:
# CANVAS_ID,EMAIL
#
for line in open("students.csv").readlines():
    line = line.strip()
    line = line.split(',')
    alunos[line[0]] = line[1]

os.makedirs('work', exist_ok=True)

for fname in os.listdir():
    if fname.lower().endswith(".zip"):
        field = 1
        if "_LATE_" in fname:
            field += 1
        userid = fname.split("_")[field]
        if userid not in alunos:
            print("MISSING .... " + fname)
            continue
        dirname = 'work' + os.sep + alunos[userid] + os.sep
        os.mkdir(dirname)
        has_file = False
        try:
            with rarfile.RarFile(fname, 'r') as zip_ref:
                fnames = [x for x in zip_ref.namelist() if x.endswith('.java')]
                if fnames:
                    has_file = True
                zip_ref.extractall(dirname, fnames)
            print("RAR", userid, dirname)
        except:
            with zipfile.ZipFile(fname, 'r') as zip_ref:
                fnames = [x for x in zip_ref.namelist() if x.endswith('.java')]
                if fnames:
                    has_file = True
                zip_ref.extractall(dirname, fnames)
        if not has_file:
            print("NO FILES! ...." + fname)
