import cv2, math, ctypes, time, sys, os
import leap.Leap as Leap
import numpy as np
#import Leap
from PIL import Image
import numpy as np
from pprint import pprint
from concurrent.futures import ThreadPoolExecutor
import updater
import re
def convert_distortion_maps(image):

    distortion_length = image.distortion_width * image.distortion_height
    xmap = np.zeros(distortion_length//2, dtype=np.float32)
    ymap = np.zeros(distortion_length//2, dtype=np.float32)

    for i in range(0, distortion_length, 2):
        xmap[distortion_length//2 - i//2 - 1] = image.distortion[i] * image.width
        ymap[distortion_length//2 - i//2 - 1] = image.distortion[i + 1] * image.height

    xmap = np.reshape(xmap, (image.distortion_height, image.distortion_width//2))
    ymap = np.reshape(ymap, (image.distortion_height, image.distortion_width//2))

    #resize the distortion map to equal desired destination image size
    resized_xmap = cv2.resize(xmap,
                              (image.width, image.height),
                              0, 0,
                              cv2.INTER_LINEAR)
    resized_ymap = cv2.resize(ymap,
                              (image.width, image.height),
                              0, 0,
                              cv2.INTER_LINEAR)

    #Use faster fixed point maps
    coordinate_map, interpolation_coefficients = cv2.convertMaps(resized_xmap,
                                                                 resized_ymap,
                                                                 cv2.CV_32FC1,
                                                                 nninterpolation = False)

    return coordinate_map, interpolation_coefficients

def undistort(image, coordinate_map, coefficient_map, width, height):
    destination = np.empty((width, height), dtype = np.ubyte)

    #wrap image data in numpy array
    i_address = int(image.data_pointer)
    ctype_array_def = ctypes.c_ubyte * image.height * image.width
    # as ctypes array
    as_ctype_array = ctype_array_def.from_address(i_address)
    # as numpy array
    as_numpy_array = np.ctypeslib.as_array(as_ctype_array)
    img = np.reshape(as_numpy_array, (image.height, image.width))

    #remap image to destination
    destination = cv2.remap(img,
                            coordinate_map,
                            coefficient_map,
                            interpolation = cv2.INTER_LINEAR)

    #resize output to desired destination size
    destination = cv2.resize(destination,
                             (width, height),
                             0, 0,
                             cv2.INTER_LINEAR)
    return destination

def run(debug = False):

    
    controller = Leap.Controller()
    time.sleep(2)
    print(controller.is_connected)
    controller.set_policy_flags(Leap.Controller.POLICY_IMAGES)
    counter = -20
    maps_initialized = False
    previous_sum = 0
    current_sum = 0
    baseline = 0

    executor = ThreadPoolExecutor(max_workers = 1)
    id_ = ''
    with open('id.txt','r+') as f:
        id_ = f.readline()

    id_ = re.search(r'(\d+)',id_).group(0)
    print('the real id is',id_)
    # Set the baseline
    print('Calibrating, please wait...')
    while counter < 0:
        frame = controller.frame()
        image = frame.images[0]
        if image.is_valid:
            if not maps_initialized:
                left_coordinates, left_coefficients = convert_distortion_maps(frame.images[0])
                right_coordinates, right_coefficients = convert_distortion_maps(frame.images[1])

                maps_initialized = True

            undistorted_left = undistort(image, left_coordinates, left_coefficients, 400, 400)
            undistorted_right = undistort(image, right_coordinates, right_coefficients, 400, 400)


            newsum = sum([image.data[i] for i in range(0,image.width*image.height,50)])
            #print('Counter:', counter, '| Val:', newsum)
            if counter >= -17:
                baseline += newsum
            # ba = bytearray(image.data)
            # print(sum(ba))
            counter += 1
            # cv2.imshow('Left Camera', undistorted_left)
            # cv2.imshow('Right Camera', undistorted_right)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        #print(counter)

    baseline /= 17
    mult = 1.03
    print('Done!')
    if debug:
        print('Baseline: {:,}, Threashhold: {}'.format(baseline,baseline*mult))
    onspike = False
    while(True):
        frame = controller.frame()
        #print(frame.current_frames_per_second)
        image = frame.images[0]
        if image.is_valid:
            if not maps_initialized:
                left_coordinates, left_coefficients = convert_distortion_maps(frame.images[0])
                right_coordinates, right_coefficients = convert_distortion_maps(frame.images[1])

                maps_initialized = True

            undistorted_left = undistort(image, left_coordinates, left_coefficients, 400, 400)
            undistorted_right = undistort(image, right_coordinates, right_coefficients, 400, 400)

            #display images

            #buffer_size = image.bytes_per_pixel * image.width * image.height
            #print(sum([image.data[i] for i in range(0,image.width*image.height,20)]))
            #pprint(image.data_pointer)
            if counter % 1 == 0:
                previous_sum = current_sum
                current_sum = sum([image.data[i] for i in range(0,image.width*image.height,50)])
                # print('{:,}'.format(current_sum), '|', '{:,}'.format(current_sum - previous_sum))
                if debug:
                    print(abs(current_sum))#-previous_sum))
                if(abs(current_sum) >  mult * baseline) and previous_sum != 0 and not onspike:
                    print('Trashed!')
                    executor.submit(updater.addone, id_)
                    onspike = True
                elif not abs(current_sum) > mult * baseline:
                    onspike = False
                counter = 0

            # ba = bytearray(image.data)
            # print(sum(ba))
            counter += 1
            if debug:
                cv2.imshow('Left Camera', undistorted_left)
                cv2.imshow('Right Camera', undistorted_right)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def main():
    controller = Leap.Controller()
    time.sleep(2)
    print(controller.is_connected)
    controller.set_policy_flags(Leap.Controller.POLICY_IMAGES)
    try:
        #run(controller)
        run()
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == '__main__':
    main()
