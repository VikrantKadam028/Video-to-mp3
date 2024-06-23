import moviepy.editor as me
from tkinter.filedialog import * #tkinder-> create GUI
                                 #filedialog-> open the file dialog box to select file

vid = askopenfilename() #allows to open file dialog box and select the video.
video = me.VideoFileClip(vid) #Loads the video

aud = video.audio #extract the audio part
aud.write_audiofile("demo.mp3") #gives a name
print("SUCCESSFULLY CONVERTED!")