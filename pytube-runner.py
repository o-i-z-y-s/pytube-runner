import time
import subprocess
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable, MembersOnly, VideoRegionBlocked, VideoPrivate, LiveStreamError, RecordingUnavailable

class PytubeRunner:

  def close(self):
    print("\nClosing now.", end=" ")
    for i in [3,2,1]:
      time.sleep(1)
      print(str(i)+"...", end=" ")
    time.sleep(0.5)

  def run(self):
    url = input('> Paste a YouTube video url here: ')

    try:
      start = time.time()

      # A few notes about this next line (where the magic happens):
      ## 'progressive=True' will always save audio and video in one file, but will only go up to 720p. 'adaptive=True' will download higher resolutions than 'progressive=True', but I don't guarantee it will have both video and audio in one file.
      ## You can delete '.get_highest_resolution()' and set "resolution='360p'" (or whatever resolution you like) inside '.filter()'.
      ## 'output_path' can be anything you'd like! './' creates the 'Ripped Videos' folder wherever the script file is.
      YouTube("\'"+url+"\'").streams.filter(progressive=True,file_extension='mp4').get_highest_resolution().download(output_path="./Ripped Videos/")

      end = time.time()
      print("All done. Took "+str(round(end-start,2))+"s\n")
      self.run()

    except AttributeError:
      print("\nAttribute Error! Two things can cause this to happen:\n1) You modified the params in .filter() and they're failing.\n2) YouTube broke pytube again, so you need to reinstall it or wait for a fixed version.")

      confirmation = input("\n> Reinstall pytube now? [y/n]: ")
      if confirmation.lower() == "y":
        print("")

        reinstall = subprocess.Popen('pip install --upgrade --force-reinstall pytube', start_new_session=True)
        reinstall.wait()

        print("\nPlease relaunch the script.")
      else: 
        print("\nPlease relaunch after checking params and/or installing a newer version of pytube.")
      
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

if __name__ == "__main__":
  runner = PytubeRunner()
  runner.run()