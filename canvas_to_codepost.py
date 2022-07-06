import os
import zipfile
import rarfile
import tarfile

alunos = {}

# students.csv - CANVASID,EMAIL
# 12345678,a@example.com
for line in open("students.csv").readlines():
    line = line.strip()
    line = line.split(',')
    alunos[line[0]] = line[1]

os.makedirs('work', exist_ok=True)

def descompress(open_f, list_f, name_f, has_file, ok):
    try:
        with open_f(fname) as zip_ref:
            fnames = [x for x in list_f(zip_ref) if name_f(x).lower().endswith('.java')]
            if fnames:
                has_file = True
            zip_ref.extractall(dirname, fnames)
        print("OK", userid, dirname)
        return True, has_file
    except:
        return ok, has_file


for fname in os.listdir():
    if fname.lower().endswith(".zip") or fname.lower().endswith(".gz") or fname.lower().endswith(".rar"):
        field = 1
        if "_LATE_" in fname:
            field += 1
        userid = fname.split("_")[field]            
        if "_question_" in fname:  # it is a quiz
            for userid_c in alunos:
                if userid_c in fname:
                    userid = userid_c
        if userid not in alunos:
            print("MISSING .... " + fname)
            continue
        dirname = 'work' + os.sep + alunos[userid] + os.sep
        if os.path.isdir(dirname):
            continue
        os.mkdir(dirname)
        has_file = False
        ok = False
        ok, has_file = descompress(lambda x: tarfile.open(x), lambda y: y.getmembers(), lambda x: x.name, has_file, ok)
        ok, has_file = descompress(lambda x: rarfile.RarFile(x, 'r'), lambda y: y.namelist(), lambda x: x, has_file, ok)
        ok, has_file = descompress(lambda x: zipfile.ZipFile(x, 'r'), lambda y: y.namelist(), lambda x: x, has_file, ok)
        if not has_file or not ok:
            print("NO FILES! ...." + fname)