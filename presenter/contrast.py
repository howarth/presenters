import sys
#import parallel
from PIL import Image
import numpy as np
import math
import common

'''
This program is given a text file as input. The file defines the stimuli.
Each line in the file is of the form:

    parameter: value

'''

class ContrastPresenter:

    def __init__(self, marker, *input_args):
        stim_fname = input_args[0]
        print input_args

        # Read arguments in from file 
        args = dict();
        with open(stim_fname) as f:
            for line in f:
                arg = line.split(":")
                arg = [s.strip() for s in arg]
                if arg[0] in ["contrast_seq", 'marker_seq']:
                    args[arg[0]] = [float(i) for i in arg[1].split(" ")]
                else:
                    args[arg[0]] = float(arg[1])

        self.con_seq = args['contrast_seq'];
        self.width = args['width'];
        self.height = args['height'];
        self.bar_width = int(args['bar_width'])
        self.nbars = int(math.ceil(self.width/self.bar_width))
        pass


    def run(self):
        pass 


    def prepare(self):
        mask = [range(2*i*self.bar_width,(2*i+1)*self.bar_width) for i in range(0, self.nbars)]
        mask = [i for j in mask for i in j] # Flatten arrays
        mask = [i for i in mask if i < self.width]

        con_to_ind, self.ind_seq = common.stim_ind(self.con_seq)
        ncontrasts = len(con_to_ind)

        contrast_template= np.zeros((self.height, self.width), dtype=np.float)
        
        self.con_ims = ncontrasts*[[None,None]]

        for c, i in con_to_ind.iteritems():
            low, high = con_vals(c)

            contrast_template[:, :] = low
            contrast_template[:, mask] = high
           
            self.con_ims[i][0] = Image.fromarray(contrast_template)

            contrast_template[:, :] = high
            contrast_template[:, mask] = low

            self.con_ims[i][1] = Image.fromarray(contrast_template)


        print self.con_ims


def con_vals(c):
    return 255*(.5 - c/2), 255*(.5 + c/2)
