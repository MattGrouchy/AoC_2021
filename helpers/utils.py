# make a generic function for retrieving input data.

def load_data(pathname):
    ''' function to read input data'''
    f = open(pathname, 'r')
    data = [line.strip() for line in f.readlines()]
    f.close()

    return data
