"""Read lammps data file function"""
def readfile(filepath):
    """
    (str) -> class
    function to read lammps output files
    >>> contents = readfile('data.somefile')
    That's all
    """
    # try statement in python jumps to except when specified error occurs and \
    # then jumps back to try to continue the rest until another error occurs
    while True: # need an infinite loop in order to introduce 'break '
        try:
            fid = open(filepath, 'r')
            break
        except (FileNotFoundError, UnboundLocalError, IOError):
            print('File not found!')
            break
    #else:
    #    print('File loaded successfully')

    class Mydata:
        """ data file arranged in this class"""
        def __init__(self):
            self.natoms = []
            self.atomtypes = []
            self.boxdims = []
            self.masses = []
            self.atoms = []
            self.velocities = []

    # initiate the class, necessary modules, and variables
    data = Mydata()
    #import numpy as np
    boxvar = []
    massvar = []
    atomsvar = []
    velsvar = []
    # loop over the lines in file and store them in resp. variables
    for line in fid:
        lline = line.rstrip()
        # skip if line is empty
        if lline:
            '''# skip line if it doesn't start with numeral
            if(not(lline[0].isnumeric())):
                continue'''
            llinearr = lline.split(' ')
            # now process the lines starting with numeric value
            try:
                float(llinearr[0])
            except:
                continue
            else:
                if llinearr[-1] == 'atoms': # implies no. atoms and atom type lines
                    data.natoms = int(llinearr[0])    #########################1
                elif llinearr[-1] == 'types':
                    data.atomtypes = int(llinearr[0]) #########################2
                elif 'hi' in llinearr[-1]: #like xhi yhi zhi
                    boxvar.append([float(i) for i in llinearr[0:2]])
                elif len(llinearr) == 2:
                    try:
                        float(llinearr[-1])
                    except:
                        pass
                    else:
                        massvar.append(float(llinearr[-1]))
                elif len(llinearr) == 8:
                    atomsvar.append([float(i) for i in llinearr])
                elif len(llinearr) == 4:
                    velsvar.append([float(i) for i in llinearr])
                data.boxdims = boxvar                 #########################3
                data.masses = massvar                 #########################4
                data.atoms = atomsvar                 #########################5
                data.velocities = velsvar             #########################6
    fid.close()
    return data
