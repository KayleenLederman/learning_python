#------------------------------OpenCV Introductory Tutorial-------------------------------

#OpenCV is an open source computer vision library 
#it provides software tools for computer vision and machine learning that can be used with Python
#some cool things you can do with Open CV:
	#image manipulation
	#face detection
	#counting people for crowd control
	#object recognition
	#image classification
	#color detection
	#object tracking in a video
	
#OpenCV is particularly useful for biology:
	#identifying cell types
	#tracking cell movement
	#processing and manipulating microscope images

#To install OpenCV on your computer:
	#use a task manager such as pip or homebrew to install on a macOS device
	#follow directions at to install of Windows device at:
		#https://docs.opencv.org/master/d5/de5/tutorial_py_setup_in_windows.html
	
#use statement "import cv2" to use functions from OpenCV library in your code	
import cv2
import sys

#move triple quotes down to uncover each new section of code

"""

#-----------------------------reading an image from a file--------------------------------

#first download image of bike saved as bike.png and place in directory you are working in
#imread allows you to read an image in the program and save it to a specific variable
#>0 is for color images
#0 is for grayscale images
#<0 is for images with alpha channel (changes the opacity/transparency of an image)
#color image:
my_bike_color = cv2.imread('bike.png', 1) 
#grayscale image:
my_bike_gray = cv2.imread('bike.png', 0)
#opacity reduced image:
my_bike_opaque = cv2.imread('bike.png', -1)



#make sure to check that the image was loaded properly
if my_bike_color is None:
	sys.exit('Could not read the image')
else: print('Image loaded correctly')



#---------------------------------displaying an image-------------------------------------
#the imshow function allows you to display the image you have loaded
#the first argument is the name of the window displaying the image (string) 
#the second argument is the name of the variable the image is stored in
#the waitKey function is necessary to tell your computer how long to open image for
#without it, the image will open and close before you have time to see it
#the parameter for the waitKey function is time the image is displayed in milliseconds
#if 0 or nothing is given:
	#image will remain open until you click the window displaying image and press any key
#destroyAllWindows function closes all windows if no argument given
#you can specify which window to close by putting the window name in the argument

cv2.imshow('color bike', my_bike_color)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('gray bike', my_bike_gray)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow('opaque bike', my_bike_opaque)
cv2.waitKey()
cv2.destroyAllWindows()



#--------------------------------converting colors of images------------------------------
#the cvtColor function converts an image from one color space to another
#first argument is the input image 
#second argument is the code for the type of color space conversion
	#color space is a way of classifying a color using different numerical properties
	#OpenCV has 150 color spaces to describe, manipulate, and accurately reproduce colors
	#the default is RGB - it stores the intensities of Red, Green, and Blue for each pixel
	#other popular color spaces are:
		#CMYK (Cyan, Magenta, Yellow, Black)
		#HSV (Hue, Saturation, Value)
		#GRAY

#converting color image to black and white image by changing RGB to GRAY color space
my_bike_bandw = cv2.cvtColor(my_bike_color,cv2.COLOR_RGB2GRAY)
cv2.imshow('bandw bike', my_bike_bandw)
cv2.waitKey()
cv2.destroyAllWindows()

#for more color space conversions see:
#https://machinelearningknowledge.ai/opencv-tutorial-image-colorspace-conversion-using-cv2-cvtcolor/



#-------------------------------------rotating images-------------------------------------
#the rotate can be used to rotate images
#possible arguments are:
	#cv2.ROTATE_90_CLOCKWISE
	#cv2.ROTATE_180
	#cv2.ROTATE_90_COUNTERCLOCKWISE
rotated = cv2.rotate(my_bike_color, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Rotated bike', rotated)
cv2.waitKey()
cv2.destroyAllWindows()



#--------------------------------drawing shapes on images---------------------------------
#drawing a circle
#first argument is name of image to be drawn on
#second argument is the pixel coordinates (x,y) of the circle's center
#third argument is the radius of the circle
#fourth argument is the color of the circle (B,G,R)
	#every color is made up of different values of a red, green, and blue channel
	#0 is the minimum value and 255 is the maximum value
	#black = (0,0,0)
	#white = (255,255,255)
	#blue = (255,0,0)
	#green = (0,255,0)
	#red = (0,0,255)
	#if you want a color of your choice, google 'color picker'
		#you can then move the pointer and it will tell you the value of the R,G,B channels
		#note the order is different
		#this example uses a nice shade of purple 
#fifth argument is thickness, -1 fills in the circle completely, 2 is an outline
cv2.circle(my_bike_color, (300,300), 100, (156,64,97), -1)  
cv2.imshow('circle',my_bike_color)  
cv2.waitKey()  
cv2.destroyAllWindows()	


#drawing a rectangle:
#first argument is name of image to be drawn on
#second argument is (x,y) coordinates of top left corner of rectangle
#third argument is (x,y) coordinates of bottom right corner of rectangle
#fourth argument is color of circle(B,G,R)
#fifth argument is thickness, -1 fills in rectangle, 2 is outline
cv2.rectangle(my_bike_color, (300,300), (500,600), (148,191,107), 2)  
cv2.imshow('rectangle',my_bike_color)  
cv2.waitKey()  
cv2.destroyAllWindows() 
	


#--------------------------------------saving images--------------------------------------
#the imwrite function can be used to save images to a specific location in your directory
#We will also do a status check to make sure the image is saved
#first argument is name for saved file, second argument is name of image to be saved
#we are saving the black and white bicycle image generated above
#image is saved in pwd unless complete pathway is included
#if status = True, then image is saved

status = cv2.imwrite('bandw_bike.png', my_bike_bandw)
print('Image saved?:', status)


"""
