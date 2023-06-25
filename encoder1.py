import cv2 as cv
import numpy as np


def convert_to_grayscale(video):
    return video

''' 
*** Method explanation ***

    Parameters
    ----------
    -Counter
    -Video capture,
    -permission to save the frames to a folder
    - Iframe of the capture
    
    Actions
    -------
   -Reads a video frame by frame
   -Can save those frames in a folder
   -Computes the error sequence 
   
   Returns
   -------
   -Returns an error sequence
   
'''


def ReadFrames(i, capture, save_frames, Iframe):
    error_sequence = []
    while True:

        # Each frame is read
        successfully_read, frame = capture.read()

        # Escape condition
        if cv.waitKey(20) and not successfully_read:  # if all frames have been read
            break

        # Each frame is shown
        cv.imshow('Video', frame)

        # Each frame is saved
        if save_frames:
            status = cv.imwrite('VideoFramesFolder/' + 'frame' + str(i) + '.jpg', frame)

            # If there is an error in frame saving ,the user will get notified
            if not status:
                print('Frame was not saved ', status)

        # Increasing the storage counter
        i += 1

        # Compute the error |Pframe -IFrame|
        error = np.abs(frame - Iframe)

        # Add the result to the error sequence
        error_sequence.append(error)

    # Releasing resources
    capture.release()
    cv.destroyAllWindows()

    return error_sequence


'''
    *** Method explaination *** 
    
    Parameters
    ----------
    -One frame each time
    
    Actions
    -------
    -Preforms run length encoding
    
    Returns
    -------
    - the run length encoding in 2 distinct arrays
    
'''


def run_length_encode(image):
    encoded_image = []
    current_pixel = image[0][0]
    count = 0

    for row in image:
        for pixel in row:
            if pixel == current_pixel:
                count += 1
            else:
                encoded_image.append((count, current_pixel))
                current_pixel = pixel
                count = 0

    # Add the last run of pixels to the encoded image
    encoded_image.append((count, current_pixel))

    return encoded_image




def run_length_encoding(frame):
    times = []
    values = []
    encoding_counter = 1
    current_vector = []  # impossible value
    h, w, c = frame.shape

    for i in range(h):
        for j in range(w):

            # if the vector is the equal to the previous one ,increase the counter
            if np.array_equal(current_vector, frame[i][j]):

                encoding_counter += 1

            # If a different vector is found ,set the counter to zero and restart the process
            else:

                current_vector = frame[i][j]
                times.append(encoding_counter)
                values.append(current_vector)
                encoding_counter = 1

    return times, values,frame.shape


if __name__ == "__main__":

    ''' *** Lossless Decoding ***'''

    # Read the given video file
    video_capture = cv.VideoCapture('Lisa.mp4')
    successfully_read, Iframe = video_capture.read()

    height, width, channels = Iframe.shape
    print('height :', height, 'width :', width, 'channels :', channels)

    # Instantiate a counter that will be used in frame storage
    counter = 0

    # Enable or disable frame storage to a folder
    to_save_frames = False

    # Get the error sequence
    error_sequence = ReadFrames(counter, video_capture, to_save_frames, Iframe)



    times =[]
    vectors =[]

    # foreach frame in iframes use RLE encoding

    a=[]
   # for f in range(1):
    t, v ,s= run_length_encoding(error_sequence[0])
    print(s)
    print(v[0])
    for i in range(len(v)):
        for j in range(len(t)):
            a.append(v[i])
    print(np.array(a).reshape(480,852))
    times=t
    vectors=v
    '''

    print('vector[1]',vectors[0])
    print('times[1]',times[0])
    print('s',s)
   #  Decoding RLE 
    # for each encoded frame
    # for x times per vector
    decoded_sequence = []
    for i in range(len(times)):

        decoded_sequence.extend([vectors[i]]*times[i])
    img=np.array(decoded_sequence).reshape(s)

    print(img.shape)

    cols,rows=(height,width)

    column_change = 0

   # print(encoded_error_sequence[0][0][0])
    '''