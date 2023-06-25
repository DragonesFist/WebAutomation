# WebAutomation
Contains codes for some basic web automation

## How to run this codes
Install python on your system - https://www.python.org/downloads/
Download and extract the code from this repo into a local folder. You can also clone this repo if you are aware of git concepts
Navigate to the code folder
Open a command prompt and type the below command in the cmd 
`pip install -r requirements.txt`
You can create a virtual environment or can install the modules globally.
Once all the modules are installed you are good to go.
If there are any errors please resolve them and install all these required modules.
Now change the path in the command prompt to the code directory.
In cmd type type the below command and hit enter.
`python DownloadYTVideos.py'
Now you should see a chrome window opening and navigating to the site and downloading the videos.


## Description of files
DownloadYTVideos.py  -- Py code file for automation.
requirements.txt -- Contains modules that needs to be installed before running py code
Links.csv -- Contains the links for the videos to be downloaded from youtube. This is not playlist link but link to the video.

## Pointers
Don't remove or reduce the sleep times in the code. This is provided to accommodate the page delays and download interactions.
After the program the chrome window will not be closed. This is done on purpose as the forced closure of chrome window can stop the current downloading video.

## Pointers when u use YTDownload.py file
Install the library using the following command in cmd
`python -m pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz`
Download the ffmpeg from https://github.com/BtbN/FFmpeg-Builds/releases . Check for windows distribution and download it.
Extract the zip folder into some location and copy the path. You should use this path in the code for ffmpeg_location key in the options dictionary.
Now you can run the code in cmd


