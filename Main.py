
from tkinter import messagebox
from tkinter import *
from tkinter.filedialog import askopenfilename
import tkinter
from PIL import ImageTk, Image
import CartoonImage
import Filter
from Filter import *
from CartoonImage import *
import cv2
import PIL.Image, PIL.ImageTk

# Initialize main window
main = tkinter.Tk()
main.title("Cartooning Of An Image")
main.geometry("1000x600")
global image_file

# Set the display size for the images
display_size = (500, 500)
#input and preprocess
def uploadImage():
    global image_file
    image_file = askopenfilename(initialdir="images")
    datasetpath.config(text=image_file)

    # Resize and display the selected image
    img = Image.open(image_file)
    img = img.resize(display_size, Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label.config(image=img)
    label.image = img  # Keep a reference


def createCartoon():
    img_rgb = cv2.imread(image_file)

    # Apply cartoon filter from Filter class
    wf = Filter()
    cartoon1 = wf.createCartoon(img_rgb)
    cartoon1_resized = cv2.resize(cartoon1, display_size)
    cv2.imshow("Cartoonified Image - Style 1", cartoon1_resized)
    cv2.imwrite("output/cartoon1.jpg", cartoon1)

    # Apply cartoon filter from CartoonImage class
    c = CartoonImage()
    cartoon2 = c.createCartoon(img_rgb)
    cartoon2_resized = cv2.resize(cartoon2, display_size)
    cv2.imshow("Cartoonified Image - Style 2", cartoon2_resized)
    cv2.imwrite("output/cartoon2.jpg", cartoon2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# GUI Buttons and Labels
uploadbutton = Button(main, text="Upload Image", command=uploadImage)
uploadbutton.place(x=350, y=100)


datasetpath = Label(main)
datasetpath.place(x=350, y=150)

cartoonbutton = Button(main, text="Cartoonify An Image", command=createCartoon)
cartoonbutton.place(x=350, y=200)

# Display a default image or placeholder
img = Image.open("cart1.jpg")
img = img.resize(display_size, Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
label = Label(main, image=img)
label.image = img  # Keep a reference
label.place(x=250, y=250)

main.config(bg='brown')
main.mainloop()
