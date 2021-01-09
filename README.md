*Tested on Ldplayer with 1920 x 1080 resolution on a desktop of 3440 x 1440 windows pc*

### Set up

1. Download and install python - https://www.python.org/downloads/
2. Download the package in this repository: https://github.com/eatwithforks/e7shoprefresher/archive/main.zip
3. Unzip the package 
    - For windows
        - Right click and unzip
    - For MAC OSX
        - `tar -zxvf main.zip`
4. Open terminal 
    - For Windows
        - click the start button
        - search for `CMD`
        - Right-click and run as administrator
    - For MAC OSX
        - command + space (to open up spotlight)
        - search for `terminal`
        
5. Install python modules required
    - `pip install keyboard`
    - `pip install pyautogui`
    - `pip install pillow`
    - `pip install opencv-python`
6. Open up your game (agnostic to bluestacks and LD player)
7. Open the shop
8. Make sure your game window is completely visible for the image locator to be able to find the buttons.

### USAGE

9. In your terminal
    - `cd <path_to_folder>` 
        -   For example: `cd C:\Users\username\Downloads\e7shoprefresher`
    - `python main.py --resolution 4k`
        - Supports `4k` and `1080p` values

```   
usage: main.py [-h] [--resolution RESOLUTION]

optional arguments:
  -h, --help            show this help message and exit
  --resolution RESOLUTION
                        choose 4k or 1080p
```
