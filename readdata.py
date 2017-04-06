# Code to read lammps data file.
structpath = '/home/subham/bicrystal_structures/'
filepath = structpath+'data.albicrystal.s5.102.010.0'
f = open(filepath,'r')
for line in f:
    txt = f.readline()
# txt = f.read()
f.close()
