*Tested on Ldplayer with 1920 x 1080 resolution on a desktop of 3440 x 1440 windows pc*

### Set up

1. Download and install python - https://www.python.org/downloads/
2. Open CMD terminal with *administrator privileges*
3. Install python modules required
    - `pip install keyboard`
    - `pip install pyautogui`
    - `pip install pillow`
    - `pip install opencv-python`
4. Open the game shop with emulator at 1080p resolution setting (agnostic to bluestacks and LD player)

### Usage

In your terminal
- `cd <path_to_folder>` for example: `cd C:\Users\username\Downloads\e7shoprefresher`
- `python main.py --resolution 4k` *supports `4k` and `1080p` values*

### Help

```   
usage: main.py [-h] [--resolution RESOLUTION]

optional arguments:
  -h, --help            show this help message and exit
  --resolution RESOLUTION
                        choose 4k or 1080p
```
