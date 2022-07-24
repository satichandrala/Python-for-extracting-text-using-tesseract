#!/usr/bin/env python
# coding: utf-8

# ### This code contains *two ways* to make a pdf from an image using Python
# - The **first one** is using a **basic method**(need to specify path) with img2pdf library (you need to pip install img2pdf incase you never installed it before. )
#    - The image I used is one of the random images in the first case. 
#    - Here, you give the path to your image file and where to save the pdf and the name you want to give it.
#    
# - The **second** is making using **Tkinter to make a GUI (Graphical User Interface)**.
#   - Once you run the code, you'll get the GUI displayed. (we use the similar as above with img2pdf library, but a little better since this makes life a bit easier at the click of a button (Ofcourse the one we created, :trollface:)
#   - With second one, you don't need to give a path, rather you can click the buttons from GUI
#   - After that, select your image and click on convert and save, in the directory you want to save.
#   - Once converted, the path to the pdf is displayed. You can check and verify the same

# In[ ]:


# Import required Libraries
from tkinter import *
from tkinter import filedialog
import img2pdf
from PIL import Image
import os
from tkinter import ttk


# In[ ]:


img_path = "C:/Users/satic/Downloads/Disclaimer.jpg"
pdf_path = "C:/Users/satic/Downloads/Disclaimer.pdf"
image = Image.open(img_path)
 #converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)
  
# opening or creating pdf file
file = open(pdf_path, "wb")

  
# writing pdf files with chunks
file.write(pdf_bytes)
  
# closing image file
image.close()
  
# closing pdf file
file.close()

# output
print("Successfully made pdf file")



# In[ ]:


win = Tk()
win.geometry('500x500')
def select_file():
    global images
    images= filedialog.askopenfilenames(initialdir = "",title = "Select Images")
    Label(win, text= images).pack()
def image_to_pdf():
            f = filedialog.asksaveasfile(mode = 'wb', defaultextension= '*.pdf')
            f.write(img2pdf.convert(images))
            Label(frame,text="Conversion to Pdf done, Check your file").pack()
# Adding Labels and Buttons
Label(win, text= "Image to Pdf Converter", font="Garamond 20 bold").pack(pady = 30)
ttk.Button (win, text= "Click to Select Images",command = select_file).pack(ipadx = 10)
frame = Frame(win)
frame.pack()
ttk.Button(frame, text= "Click to Convert and save as", command = image_to_pdf).pack(side = LEFT, pady=20, ipadx = 10)
win.mainloop() 



# %%
