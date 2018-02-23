from location_extraction import load_city_index, load_border_index, extract_location_metadata

''' 
    
    This script handles the run-logic for the map-wizard Skluma module. The Docker container stored as a DockerHub Image
    should store all dependency downloads. Some 'difficult' ones include the shapely and opencv (cv2) downloads, 
    Google OCR Tesseract, and libgeos-dev (C binding for shapely). 
    
    This Docker Image should always run Python3.  

    @ScriptAuthor: Tyler J. Skluzacek (skluzacek@uchicago.edu) --- DockerImage/Workflow point of contact
    @ModuleAuthor: Rohan Kumar --- Module point of contact
    
'''


def get_indices():
    """ Load the pre_built city and border indices into memory. """
    city_index = load_city_index()
    border_index = load_border_index()

    return (city_index, border_index)



def extract_map_metadata(filename):
    """ Given a file previously assumed to be a map, output (return) all feature tags. """

    indices = get_indices()
    city_index = indices[0]
    border_index = indices[1]
    metadata = extract_location_metadata(filename, border_index, city_index,path_given=True, debug=False)

    print(metadata)
    return(metadata)


# Run on file called 'testpic.png' (stored in repo).
extract_map_metadata('testpic.png')


""" Tyler and Rohan's 'messing around' code from 08/16/2017""" #TODO: Move logic to test-suite.
# from contouring import isolate_text_boxes
# import cv2
# from PIL import Image
#
# boxes = isolate_text_boxes(cv2.imread(mappy), return_contours=True)
# i = cv2.drawContours(cv2.imread(mappy), boxes, -1, (255,0,0), 2)
# Image.fromarray(i).show()
