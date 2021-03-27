from tkinter import *
from pygame import mixer


current_volume = 0.5

#Functions

def chill():
    # file location is supoposed to change, but due to lack of time we could not complete this. This is why the song might not play on your pc's.
    filename = "C:/Users/ashwi/OneDrive/Desktop/Project-Reboot/chill.mp3"
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg = "Green", text = "Now playing: " + str(song_title))
        volume_label.config(fg = "Green", text = "Volume: " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg = "red", text = "Error playing track")
    

def peaceful():
    # file location is supoposed to change, but due to lack of time we could not complete this. This is why the song might not play on your pc's.
    filename = "C:/Users/ashwi/OneDrive/Desktop/Project-Reboot/peaceful.mp3"
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg = "Green", text = "Now playing: " + str(song_title))
        volume_label.config(fg = "Green", text = "Volume: " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg = "red", text = "Error playing track")
    
def upbeat():
    # file location is supoposed to change, but due to lack of time we could not complete this. This is why the song might not play on your pc's.
    filename = "C:/Users/ashwi/OneDrive/Desktop/Project-Reboot/upbeat.mp3"
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg = "Green", text = "Now playing: " + str(song_title))
        volume_label.config(fg = "Green", text = "Volume: " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg = "red", text = "Error playing track")

def classic():
    # file location is supoposed to change, but due to lack of time we could not complete this. This is why the song might not play on your pc's.
    filename = "C:/Users/ashwi/OneDrive/Desktop/Project-Reboot/classical.mp3"
    current_song = filename
    song_title = filename.split("/")
    song_title = song_title[-1]

    try:
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg = "Green", text = "Now playing: best classical songs")
        volume_label.config(fg = "Green", text = "Volume: " + str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg = "red", text = "Error playing track")
    


def reduce_volume():
    try:
        global current_volume
        if(current_volume <= float(0.0)):
            volume_label.config(fg= "red", text = "Volume: Muted")
            return
        current_volume = current_volume - float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg = "green", text =  "Volume: "+ str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg = "Red", text = "Track hasnt been selected yet")

def increase_volume():
    try:
        global current_volume
        if(current_volume>= 1):
            volume_label.config(fg= "green", text = "Volume: Max")
            return
        current_volume = current_volume + float(0.1)
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg = "green", text =  "Volume: "+ str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg = "Red", text = "Track hasnt been selected yet")

def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg = "red", text="Track hasnt been selected yet")

def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg = "red", text="Track hasnt been selected yet")



root = Tk()

#title
root.title("MUSIC APP")

root.config(bg = "#1cacd4")
#geometry
root.geometry("800x700")


#APP PLAER
Label(root, text = "MUSIC APP", font = ("Verdana", 30), bg = "#1cacd4"). place(relx = 0.4)

#type of songs buttons
chill = Button(root, text = "Chill", font = ("Verdana", 20), bg = "black", fg = "white", command = chill).place(relx = 0.03, rely = 0.1, relwidth = 0.2, relheight = 0.1)
peaceful = Button(root, text = "Peaceful", font = ("Verdana", 20), bg = "black", fg = "white", command = peaceful).place(relx = 0.25, rely = 0.1, relwidth = 0.2, relheight = 0.1)
upbeat = Button(root, text = "Upbeat", font = ("Verdana", 20), bg = "black", fg = "white", command = upbeat).place(relx = 0.5, rely = 0.1, relwidth = 0.2, relheight = 0.1)
classical = Button(root, text = "Classical", font = ("Verdana", 20), bg = "black", fg = "white", command = classic).place(relx = 0.75, rely = 0.1, relwidth = 0.2, relheight = 0.1)

#while playing frame
frame = Frame(root, bg = "black").place(relx = 0.1, rely = 0.3, relwidth = 0.8, relheight = 0.55)
song_title_label = Label(frame, font = ("Verdana",20), bg = "black", fg = "white")
song_title_label.place(relx = 0.12, rely = 0.35)
volume_label = Label(frame, text = "Volume = "  + str(current_volume), font = ("Verdana", 20), bg = "black", fg = "white")
volume_label.place(relx = 0.37, rely = 0.5) 
pause_resume_label = Label(frame, text = "", font = ("Verdana", 20), bg = "black", fg = "white").place(relx = 0.37, rely = 0.6)

#volume buttons
increase_volume_button = Button(frame, text = "+", font = ("Verdana", 15), bg = "blue", fg = "white", command = increase_volume).place(relx = 0.82, rely = 0.5)
reduce_volume_button = Button(frame, text = "-", font = ("Verdana", 15), bg = "blue", fg = "white", command = reduce_volume).place(relx = 0.12, rely = 0.5)

#pause and unpause buttons
pause_button = Button(frame, text = "Pause", font = ("Verdana", 15), bg = "blue", fg = "white", command = pause).place(relx = 0.12, rely = 0.6)
unpause_button = Button(frame, text = "Resume", font = ("Verdana", 15), bg = "blue", fg = "white", command = resume).place(relx = 0.74, rely = 0.6)


  
root.mainloop()
