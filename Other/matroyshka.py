import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import os


def swap(fname, destroy):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    if destroy:
        os.remove(fname)
    return data


def load_image_data():
    data = {}
    os.system('ls Images >> images.txt')
    imat_list = swap('images.txt', True)
    for image in imat_list:
        i = image.split('out')[1].split('.')[0]
        data[int(i)] = np.array(plt.imread('Images/'+image))
    return data


def create_images(argv):
    test_video = 'herm.mp4'
    frame_rate = 20
    if '-v' in argv:
        test_video = argv[2]
        argv.pop(0)
        argv.pop(0)
    if '-fr' in argv:
        frame_rate = int(input('Enter frame rate: '))
    # Use FFMpeg to dissect video into still images
    cmd_input_preproc = 'ffmpeg -loglevel quiet -i ' + test_video + ' -vf fps=' + \
                        str(frame_rate) + ' Images/out%d.png'
    os.system('mkdir Images')
    os.system(cmd_input_preproc)
    return frame_rate, test_video


def extract_data_from_image(payload_file):
    raw_data = swap(payload_file, False)
    blob = ''
    for line in raw_data:
        blob += line
    data = ''.join(['\\x%s' % ord(c) for c in list(blob)])
    print '[' + str(len(data.split('\\x'))) + ' bytes in payload]'
    return data


def recombine_image_bytes(raw):
    print "Recombining "+str(len(raw.split('\\x')))+' bytes'
    return ''.join(['%s' % chr(int(c)) for c in raw.split('\\x')[1:]])


def encode_images(image_data, payload_file, extension):
    sorted_keys = np.array(image_data.keys()).sort()
    # Get data from payload file, and start dividing it
    # into a block for each image (evenly distributed)
    readable = ['.txt', '.c', '.py', '.java', '.cpp']
    if extension in readable:
        data = extract_data_from_image(payload_file)
        # MAKE SURE DATA CAN BE RECOMBINED!


def main():
    t0 = time.time()  # start the clock
    # Create Stego slides
    frame_rate, test_video = create_images(sys.argv)
    print "Image Folder Created and Populated. ["+str(time.time()-t0)+'s]'
    # Now Load the Images
    raw_images = load_image_data()
    print '\033[1m\033[31m<'+str(len(raw_images.keys())) + \
          ' Images Loaded From ' + test_video+'>\033[0m' +\
          "\t[" + str(time.time() - t0) + 's]'
    payload = '../polyglots/glot.py'
    encode_images(raw_images, payload, '.py')
    cmd_recombine = 'ffmpeg -i Images/out%d.png -c:v libx264 -vf fps=' + \
                    str(frame_rate) + ' -pix_fmt yuv420p out.mp4'
    # Clean Up
    os.system('ls Images/ | while read n; do rm Images/$n; done; rmdir Images')


if __name__ == '__main__':
    main()
