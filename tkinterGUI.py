from tkinter import *
import cv2
master = Tk()

def insertFace():
	cap = cv2.VideoCapture(0)
	cap.set(3,640) #width=640
	cap.set(4,480) #height=480

	if cap.isOpened():
	    a,frame = cap.read()
	    cap.release() #releasing camera immediately after capturing picture
	    if a and frame is not None:
	        cv2.imwrite('img3.jpg', frame)

'''
def insertFace():

def deleteFace():

def showAttendance():

def updateFace():
'''


captureImage = Button(master, text="Capture an Image", command=insertFace)
captureImage.pack()


deleteImage = Button(master, text="Delete a Face", command=deleteFace)
deleteImage.pack()

attendance = Button(master, text = "Show full class attendance", command = showAttendance )
attendance.pack()

updateImage = Button(master, text="Update a Face", command=updateFace)
updateImage.pack()




mainloop()
