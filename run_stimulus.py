import sys
import presenter as p
import marker as m

marker_dict = {
    'baparallel' : (m.baparallel.BAParallelMarker, 'BAlert with parallel port'),
    #'emotiv' :  (m.emotiv.EmotivMarker, 'Emotiv')
}

present_dict = {
    'contrast' : (p.contrast.ContrastPresenter, 'Contrast experiment for light therapy')
}

if __name__ == "__main__":
    marker_type = sys.argv[1]
    presenter_type = sys.argv[2]
    
    marker = marker_dict[marker_type][0]()
    marker.prepare()

    presenter = present_dict[presenter_type][0](marker, *sys.argv[3:])
    presenter.prepare()

    presenter.run()
