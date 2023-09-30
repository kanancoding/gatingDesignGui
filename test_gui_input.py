from gatingDesignGUI import DesignGUI
import glob,easygui

image = "welcome.gif"
msg = "With one do you like to input data"
title = "Welcome to gating calculate program"
choices = ["Input data by manual","Input data from file"]
reply = easygui.buttonbox(msg,title=title, image=image, choices=choices)
# inp = "input"
inp = "file" if reply == choices[1] else "input"
imgs = glob.glob("images/*.jpg")
gui = DesignGUI(inp)  # or "file"
gui.setImages(imgs)
gui.run()
     

