# openCV personal documentation 

Welcome to Davids personal openCV docs. 
I made this to learn the basics of openCV. In this section it is all about how to capture elements. Below I will try to document how to capture a video stream from the webcam, how to feed images and videos into openCV and eventually, how to capture a livestream from a drone. 

## basic common setup 

Obviously, we need to import openCV first. 
Confusingly, openCV is called cv2 during setup and install. 
Naturally, this means we can grab it with ``` pip install cv2 ``` and in the file import it with ``` import cv2 as cv ```. 

## Webcam capture 


### Video capture 

### Image capture 
For loading an image into the environment with opencv installed all that is needed is to read out the file. 
``` img = cv.findImage("name_of_img") ``` this will find the image if it is in the same repo, of course if not a proper path needs to be added in front of the image name. This creates an image object, which we will use further down below to operate on. 

Optionally, we can feed some additional parameters into the readout, where we can decide already some stuff about the way the image is saved. First, the default option is ``` img = cv.findImage("name", IMREAD_COLOR) ``` this is essentially the same like not feeding in any parameter and just means its stored using 8bit color format BGR. Alternatively, and most useful for heavy analysis later on, we can also call the image like so: ``` img = cv.findImage("name", IMREAD_GRAYSCALE) ``` this will simply store the image in its greyscaling or to use the opencv speak: it will store it at intensity 1. 
Of course, sometimes we want to change nothing from the image we read out, in this case all that is needed is the parameter: ``` img = cv.findImage("name", IMREAD_UNCHANGED) ```. 

If an image is supposed to be shown, a concept that is important all throughout openCV is necessary, namely the key press to interupt whatever operation had been ongoing. This can be implemented using the wait key function: ``` q = cv.waitKey(0) ``` A few notes are useful here. The parameter is deciding how long to wait for the user to press a key. 0 means it will wait forever, since this is not a good habit to form I personally prefer (60) which means the image is displayed for a minute or until a user presses the interrupt key. Also I really like using q for this, as it matches with a lot of linux logic, which usually does use Q for interrupt logic. 
``` cv.imshow("title of img", img)``` is the code that is required for actually showing the image. The first parameter is the title with the second being the object we created earlier. 

Finally, perhaps we want to save an image, creatively the function for that is called imwrite and is simply called as follows: ``` cv.imwrite("new name") ```. A trick taught by the official tutorial at the time of writing is also to save only if the s key is pressed. This can be achieved by the following snippet: 
``` if k == ord("s"): ``` imagine an indentation below: 
        ``` cv.imwrite("name.png", img) ```. 
