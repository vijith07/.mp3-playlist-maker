from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as cr7
import pygame

playlist = []

class Application(Frame):
    
    def __init__(self,master):
        super(Application, self).__init__(master)
        
        
        self.playlistbox = Listbox(self, width = 80, height = 10, selectmode = SINGLE) 
        for song in playlist:
            self.playlistbox.insert(END, song)
            
        self.grid(rowspan=3, columnspan=10)
        self.playlistbox.grid(row = 1)
        self.startButton = Button(self, text = 'Start', command = self.start)
        self.loopButton = Button(self, text = 'Loop', command = self.loop)
        self.addButton = Button(self, text = 'Add', command = self.add)
        self.pauseButton = Button(self, text = 'Pause', command = self.pause)
        self.resumeButton = Button(self, text = 'Play', command = self.resume)
        self.stopButton = Button(self, text = 'Stop', command = self.stop)
        self.startButton.grid(row=3, column = 2)
        self.stopButton.grid(row=3, column = 3)
        self.loopButton.grid(row=4, column = 2)
        self.addButton.grid(row=4, column = 3)
        self.pauseButton.grid(row=3, column = 0)
        self.resumeButton.grid(row=4, column = 0)
        self.pack()
        
        
        pygame.init()

    def start(self):
        if(len(playlist) == 0):
            cr7.showinfo('virus', 'No soongs added\nClick Add to add songs.')
            cr7.showinfo('virus', 'Select the song before you hit Start.')
        else:    
            pygame.mixer.music.stop()
        
            selectedSongs = self.playlistbox.curselection()
            global playlistbox
            playIt = playlist[int(selectedSongs[0])]
            pygame.mixer.music.load(playIt)
            pygame.mixer.music.play(0, 0.0)
    def stop(self):
        pygame.mixer.music.stop()
        
    def pause(self):
        pygame.mixer.music.pause()
    def resume(self):
        pygame.mixer.music.unpause()
    def loop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1,0.0)

    def add(self):
        file = tk.askopenfilenames(initialdir='D:\DOWNLOADS\music')  
        songsTuple = root.splitlist(file)   
        songsList = list(songsTuple)        
        
        for song in songsList:              
            playlist.append(song)          
            songArray = song.split('/')     
            SONG = songArray[len(songArray)-1]
            self.playlistbox.insert(END, SONG)
        
root = Tk()
root.title('mp3 player')
root.geometry('800x242')
app = Application(root)
app.mainloop()
