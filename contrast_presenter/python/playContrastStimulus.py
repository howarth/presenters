import sys, parallel
import Image
import numpy as np
import math


def main():
  args = dict()

  with open(sys.argv[1]) as f:
    for line in f:
      arg = line.split(":")
      arg = [s.strip() for s in arg]
      if arg[0] == "contrast_seq":
        args[arg[0]] = [float(i) for i in arg[1].split(" ")]
      else:
        args[arg[0]] = float(arg[1])

  ncontrasts = len(args['contrast_seq']);
  width = args['width'];
  height = args['height'];
  bar_width = int(args['bar_width'])

  nbars = int(math.ceil(width/bar_width))
  mask = [range(2*i*bar_width,(2*i+1)*bar_width) for i in range(0, nbars)]
  mask = [i for j in mask for i in j] # Flatten arrays
  mask = [i for i in mask if i < width]
  print mask

  contrasts = np.zeros((width, height, 2, ncontrasts), dtype=np.uint8)
  contrasts[:, mask] = 150;
  img = Image.fromarray(contrasts);
  img.save('sup.png');

  for 
  
  print args


main()
