import sys
#import parallel
from PIL import Image
import numpy as np
import math
import common
import pygtk
import gtk
import time, sched
from threading import Thread
from util import GTKScheduler

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



        w = gtk.Window()
        im1 = self.con_ims[0][0]
        im1.show()
#im2 = self.con_ims[1][0]
#       im2.show()
        w.add(im1)


        w.show_all();
        w.fullscreen();

        gs = GTKScheduler.GTKScheduler()
        gs.schedule(5.34957, w.unfullscreen, ())
        gs.schedule(3.34957, im1.hide, ())
        gtk.main()
        print 'sup'
        s.run()



#       w.add(im2)


    def prepare(self):
        mask = [range(2*i*self.bar_width,(2*i+1)*self.bar_width) for i in range(0, self.nbars)]
        mask = [i for j in mask for i in j] # Flatten arrays
        mask = [i for i in mask if i < self.width]

        con_to_ind, self.ind_seq = common.stim_ind(self.con_seq)
        ncontrasts = len(con_to_ind)

        contrast_template= np.zeros((self.height, self.width), dtype=np.uint8)
        
        self.con_ims = ncontrasts*[[None,None]]

        for c, i in con_to_ind.iteritems():
            low, high = con_vals(c)

            contrast_template[:, :] = low
            contrast_template[:, mask] = high
           
            self.con_ims[i][0] = self.array_to_gtkim(contrast_template)

            contrast_template[:, :] = high
            contrast_template[:, mask] = low
            
            self.con_ims[i][1] = self.array_to_gtkim(contrast_template)


    def array_to_gtkim(self,arr):
        buf_from_arr = gtk.gdk.pixbuf_new_from_array
        im_from_buf = gtk.image_new_from_pixbuf
        rgb = gtk.gdk.COLORSPACE_RGB

        print arr.shape
        im = im_from_buf(buf_from_arr(np.dstack((arr,arr,arr)), rgb, 8))
        return im
        




def con_vals(c):
    return int(255*(.5 - c/2)), int(255*(.5 + c/2))
