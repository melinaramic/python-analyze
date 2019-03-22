import glob
import numpy
import matplotlib.pyplot

def plot_inflammation(x,filename):
    """Plot the minima, maxima, and average of patient inflammation data across 40 days
    usage: plot_inflammation(x=<array of floats>, filename)"""
    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(numpy.mean(x, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(numpy.max(x, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(numpy.min(x, axis=0))

    fig.tight_layout()
    
    matplotlib.pyplot.savefig(filename.replace("csv","png"))
    matplotlib.pyplot.close(fig)

def check_errors(x):
    """check for suspicious minima and maxima in patient inflammation data
    Usage check_errors(data_array)"""
    
    if numpy.max(x,axis=0)[20] == 20 and numpy.max(x,axis=0)[0] == 0:
        print ('suspicious maximum')
    if numpy.sum(numpy.min(x,axis = 0)) == 0:
        print ('suspicious minimum')
        
        
files = glob.glob('i*.csv')
files.sort()

for file in files:
    data = numpy.loadtxt(fname=file, delimiter=',')
    print(file)
    check_errors(data)
    plot_inflammation(data,file)