import math
import time
import subprocess
from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import RegexMatchError, VideoUnavailable, MembersOnly, VideoRegionBlocked, VideoPrivate, LiveStreamError, RecordingUnavailable

class PytubeRunner:

  def close(self):
    print("\nClosing now.", end=" ")
    for i in [3,2,1]:
      time.sleep(1)
      print(str(i)+"...", end=" ")
    time.sleep(0.5)
      
  def reinstallPytube(self):
    print("") # Whitespace for readability.
    pipCheck = subprocess.Popen('python -c "import pip"')
    if pipCheck.wait() == 0:
      reinstall = subprocess.Popen('pip install --upgrade --force-reinstall pytube', start_new_session=True)
      reinstall.wait()
      print("\nPlease relaunch the script.")
    else: # Likely a ModuleNotFoundError.
      print("You don't have pip installed for this version of Python! The download link is in the README file.")

  def confirmReinstall(self):
    confirmation = input("\n> Reinstall pytube now? (Remember to replace cipher.py again!) [y/n]: ")
    if confirmation.lower() == "y":
      self.reinstallPytube()
    else: 
      print("\nPlease relaunch after checking params, installing a newer version of pytube, and/or replacing cipher.py again.")

  def getAgeRestricted(self, url):
    return YouTube("\'"+url+"\'", use_oauth=True, allow_oauth_cache=True)

  def getVideo(self, youtubeObj):
    # You can delete '.get_highest_resolution()' and set "resolution='360p'" (or whatever resolution you like) inside '.filter()'.
    # 'output_path' can be anything you'd like! './' tells the script to create the 'Ripped Videos' folder wherever the script file is.
    youtubeObj.streams.filter().get_highest_resolution().download(output_path="./Ripped Videos/")

  def getPlaylist(self, url):
    playlist = Playlist("\'"+url+"\'")
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

  def run(self):
    url = input('> Paste a YouTube url here: ')

    try:
      start = time.time()

      # If you aren't trying to snag age restricted content, use this line.
      yt = YouTube("\'"+url+"\'")

      # The single video download function.
      self.getVideo(yt)

      end = time.time()
      print("All done. Took " + self.getTime(end-start) + "\n")
      self.run()

    except AttributeError:
      print("\nAttribute Error! Two things can cause this to happen:\n1) You modified the params in .filter() and they're failing.\n2) YouTube broke pytube again, so you need to reinstall it or wait for a fixed version.")
      self.confirmReinstall()
      self.close()
    
    except RegexMatchError:
      print("Invalid link! Please try again.\n")
      self.run()
    
    except LiveStreamError:
      print("Video is a live stream, which isn't supported by pytube.\n")
      self.run()
    
    except RecordingUnavailable:
      print("There's no live stream recording available for this video.\n")
      self.run()
    
    except VideoPrivate:
      print("Video is private, which isn't supported by pytube. Please try a different one.\n")
      self.run()
    
    except VideoRegionBlocked:
      print("Video is region-blocked, which isn't supported by pytube. Please try a different one.\n")
      self.run()
    
    except MembersOnly:
      print("Video is Members Only. Please try a different one.\n")
      self.run()
    
    except VideoUnavailable:
      print("The video is unavailable.")
      self.run()
    
    except:
      print("\nUncaught error! It could be that YouTube broke pytube again, so you need to reinstall it, update cipher.py with the version in this repo, or wait for a fixed version.")
      self.confirmReinstall()
      self.close()

if __name__ == "__main__":
  runner = PytubeRunner()
  runner.run()