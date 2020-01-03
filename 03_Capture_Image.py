# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 16:29:08 2020

@author: sansin03
"""

import argparse
import cv2
import numpy as np


def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Handle an input stream")
    # -- Create the descriptions for the commands
    i_desc = "The location of the input file"

    # -- Create the arguments
    parser.add_argument("-i", help=i_desc)
    args = parser.parse_args()

    return args


def capture_stream(args):
    ### TODO: Handle image, video or webcam
    img_flg = True
    if args.i == 'CAM':
        args.i = 0
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        print("video mode")
    elif args.i.endswith('.jpg') or args.i.endswith('.bmp'):
        img_flg = True
        out = None
        print("camera mode")
    
    ### TODO: Get and open video capture
    cap = cv2.VideoCapture(args.i)
    cap.open(args.i)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == False:
            print("frame is not captured")
            break
        key_press = cv2.waitKey(60)
        
        frame = cv2.resize(frame, (100,100))
        frame = cv2.Canny(frame, 100, 200)
        if not img_flg:
            out.write(frame)
        else:
            cv2.imwrite("test.jpg", frame)
        if key_press == 27:
            break
    # Release everything if job is finished
    if img_flg:
        cap.release()
    else:
        out.release()
    cv2.destroyAllWindows()


def main():
    args = get_args()
    capture_stream(args)


if __name__ == "__main__":
    main()
