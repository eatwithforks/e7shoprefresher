*Tested on Ldplayer with 1920 x 1080 and 3440 x 1440 with 280 dpi*

*Tested on BlueStacks 5 with 1920 x 1080p with 240 dpi.*

### Set up

1. Download and install python - https://www.python.org/downloads/
2. Open CMD terminal with *administrator privileges*
3. Install python modules required
    - `pip install keyboard`
    - `pip install pyautogui`
    - `pip install pillow`
    - `pip install opencv-python`
4. Open the game shop with emulator at 1080p resolution setting
    - 280 DPI for LDplayer
    - 240 DPI for BlueStacks 

### Usage

In your terminal
- `cd <path_to_folder>` for example: `cd C:\Users\username\Downloads\e7shoprefresher`
- `python main.py --resolution ld-4k` *supports `ld-4k`, `ld-1080p`, and `bs-1080p` values*

### Help

```   
usage: main.py [-h] [--resolution RESOLUTION]

optional arguments:
  -h, --help            show this help message and exit
  --resolution RESOLUTION
                        choose ld-4k, ld-1080p, or bs-1080p
```
