# import the necessary packages
from imutils.video import VideoStream
import csv 
from pyzbar import pyzbar
from get_flight_id import get_flight
from get_flight_info import get_infor
from read_csv import read_query_output
from datetime import datetime
from send_link import link
from clean import clean_db
import argparse
import datetime
import imutils
import time
import cv2
import mysql.connector




def scan():
    # construct the argument parser and parse the arguments
    start = time.time()
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
	    help="path to output CSV file containing barcodes")
    args = vars(ap.parse_args())

    # initialize the video stream and allow the camera sensor to warm up
    # print("[INFO] starting video stream...")
    vs = VideoStream(src=0,resolution = (1280,720)).start()
    # vs = VideoStream(usePiCamera=True,resolution=(960, 720),framerate=30).start()
    time.sleep(0.5)

    # open the output CSV file for writing and initialize the set of
    # barcodes found thus far
    csv = open(args["output"], "w")
    found = set()
    scanning = True
    # loop over the frames from the video stream
    while scanning:
	    # grab the frame from the threaded video stream and resize it to
	    # have a maximum width of 400 pixels
	    frame = vs.read()
	    frame = imutils.resize(frame, width=720)

	    # find the barcodes in the frame and decode each of the barcodes
	    barcodes = pyzbar.decode(frame)
	    # loop over the detected barcodes
	    for barcode in barcodes:
		    # extract the bounding box location of the barcode and draw
		    # the bounding box surrounding the barcode on the image
		    (x, y, w, h) = barcode.rect
		    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

		    # the barcode data is a bytes object so if we want to draw it
		    # on our output image we need to convert it to a string first
		    barcodeData = barcode.data.decode("utf-8")
		    barcodeType = barcode.type

		    # draw the barcode data and barcode type on the image
		    text = "{} ({})".format(barcodeData, barcodeType)
		    cv2.putText(frame, text, (x, y - 10),
			    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

		    # if the barcode text is currently not in our CSV file, write
		    # the timestamp + barcode to disk and update the set
		    if barcodeData not in found:
			    #csv.write("{},{}\n".format(datetime.datetime.now(),
				    #barcodeData))
                            csv.write("{}\n".format(barcodeData))
			    csv.flush()
			    found.add(barcodeData)
		    scanning = False
		    break
	
	    # show the output frame
	    cv2.imshow("Barcode Scanner", frame)
	    key = cv2.waitKey(1) & 0xFF

	    # if the `q` key was pressed, break from the loop
	    if key == ord("q"):
		    break
	

    csv.close()
    cv2.destroyAllWindows()
    vs.stop()
    while True: 
	    if scanning != True:
		    name = read_query_output()
		    break
	
    flight_id = gate_no(name[0])
    infor = gate_infor(flight_id[0])
    gate = infor[0]
    status = infor[1]
    board = infor[2]
    departure = infor[3]
    dest = infor[4]
    #print ("Gate number is {}".format(gate[0]))
    #print ("Location on x_coord is {}".format(x[0]))
    #print ("Location on y_coord is {}".format(y[0]))

    info_file = open("info_file.txt","w+")
    info_file.write(name[0] + '\n')
    info_file.write(flight_id[0] + '\n')
    info_file.write(str(gate[0]) + '\n')
    info_file.write(status[0] + '\n')
    info_file.write(str(board[0]) + '\n')
    info_file.write(str(departure[0]) + '\n')
    info_file.write(dest[0] + '\n')
    info_file.close()

    clean_db() 
    link(flight_id[0])
    
    return({'gate_no':gate,'flight_id':flight_id,'status':status,'boarding_time':board,
    'depature_time':departure,'destination':dest})
    

scan()
