import tkinter as tk
import customtkinter as ctk
import math
import time
from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import RegexMatchError, VideoUnavailable, MembersOnly, VideoRegionBlocked, VideoPrivate, LiveStreamError, RecordingUnavailable

class GUI:

  def __init__(self, window):
    window.geometry("350x275")
    window.title("Pytube Runner")

    urlFrame = ctk.CTkFrame(window)
    urlLabel = ctk.CTkLabel(urlFrame, text="URL:")
    urlEntry = ctk.CTkEntry(urlFrame, width=260)

    optionsFrame = ctk.CTkFrame(window)
    notice = ctk.CTkLabel(optionsFrame, text="These two features are unfortunately\nbroken upstream at the moment.")
    isPlaylist = ctk.BooleanVar()
    playlistChk = ctk.CTkCheckBox(optionsFrame, text="Playlist?", state=tk.DISABLED, variable=isPlaylist, onvalue=True, offvalue=False, checkbox_width=15, checkbox_height=15)
    isAgeRestricted = ctk.BooleanVar()
    ageRestrictedChk = ctk.CTkCheckBox(optionsFrame, text="Age Restricted?", state=tk.DISABLED, variable=isAgeRestricted, onvalue=True, offvalue=False, checkbox_width=15, checkbox_height=15)

    output = ctk.CTkTextbox(window, height=125, width=250)
    runButton = ctk.CTkButton(window, text="Run", command=lambda: self.runScript(window, runButton, urlEntry, isPlaylist, isAgeRestricted, output))

    urlFrame.pack(padx=10, pady=5)
    urlLabel.pack(side="left", padx=5)
    urlEntry.pack()
    optionsFrame.pack(padx=10, pady=5)
    notice.pack(side="top", padx=10)
    playlistChk.pack(side="left", padx=5)
    ageRestrictedChk.pack(side="right", padx=5)
    runButton.pack()
    output.pack(side="bottom")

    output.insert(ctk.END, "Note: The console will be frozen while it\ndownloads (for now).\n")
    window.mainloop()

  def getVal(self, component):
    return component.get()
    
  def runScript(self, runButton, urlEntry, playlistVar, ageRestrictedVar, output):
    runButton["state"] = "disabled"
    url = self.getVal(urlEntry)
    isPlaylist, isAgeRestricted = self.getVal(playlistVar), self.getVal(ageRestrictedVar)

    runner = PytubeRunner()
    # output.insert(ctk.END, "Starting, please wait...\n")
    runner.run(url, isPlaylist, isAgeRestricted, output)
    # threading seems overkill for this, but keeping button toggling for now...
    runButton["state"] = 'normal'


class PytubeRunner:

  def getAgeRestricted(self, url):
    return YouTube("\'"+url+"\'", use_oauth=True, allow_oauth_cache=True)

  def getVideo(self, youtubeObj):
    # You can delete '.get_highest_resolution()' and set "resolution='360p'" (or whatever resolution you like) inside '.filter()'.
    # 'output_path' can be anything you'd like! './' tells the script to create the 'Ripped Videos' folder wherever the script file is.
    youtubeObj.streams.filter().get_highest_resolution().download(output_path="./Ripped Videos/")

  def getPlaylist(self, url):
    playlist = Playlist("\'"+url+"\'")
    for video in playlist.videos:
      print(video)
      video.streams.first().download()
    for vid_url in playlist.video_urls:
      print(vid_url)
      self.getVideo(YouTube("\'"+vid_url+"\'"))
  
  def getTime(self, seconds):
    mins = math.floor(seconds / 60)
    secs = round(seconds % 60, 2)

    if mins == 0:
      return str(secs) + "s"
    else:
      return str(mins) + "m " + str(secs) + "s"

  def run(self, url, isPlaylist, isAgeRestricted, output):
    try:
      start = time.time()

      # The script can't handle age restricted videos without authenticating an account.
      if isPlaylist: 
        self.getPlaylist(url)
      elif isAgeRestricted:
        self.getVideo(self.getAgeRestricted(url))
      else:
        self.getVideo(YouTube("\'"+url+"\'"))

      end = time.time()

    except AttributeError:
      output.insert(ctk.END, "\nAttribute Error! Two things can cause this to happen:\n1) You modified the params in .filter() and they're failing.\n2) YouTube broke pytube again, so you need to reinstall it or wait for a fixed version.")
      return
    
    except RegexMatchError:
      output.insert(ctk.END, "\nInvalid link! Please try again.\n")
      return
    
    except LiveStreamError:
      output.insert(ctk.END, "\nVideo is a live stream, which isn't supported by pytube.\n")
      return
    
    except RecordingUnavailable:
      output.insert(ctk.END, "\nThere's no live stream recording available for this video.\n")
      return
    
    except VideoPrivate:
      output.insert(ctk.END, "\nVideo is private, which isn't supported by pytube. Please try a different one.\n")
      return
    
    except VideoRegionBlocked:
      output.insert(ctk.END, "\nVideo is region-blocked, which isn't supported by pytube. Please try a different one.\n")
      return
    
    except MembersOnly:
      output.insert(ctk.END, "\nVideo is Members Only. Please try a different one.\n")
      return
    
    except VideoUnavailable:
      output.insert(ctk.END, "\nThe video is unavailable.")
      return
    
    except:
      output.insert(ctk.END, "\nUncaught error! It could be that YouTube broke pytube again. You may need to reinstall it, update cipher.py with the version in this repo, or wait for a fixed version.")
      return

    output.insert(ctk.END, "All done. Took " + self.getTime(end-start) + ".\n")


if __name__ == "__main__":
  gui = GUI(ctk.CTk())