# iOS music lock screen generator

This is a tool, that creates a iOS lock screen based on the album cover.

## Requirements

- python 3.x.x

## Installation

```powershell
pip install -r requirements.txt
```

## Usage

Put your album covers in the inputs folder, remember the names of the images must follow the given format: 

**<song_name> # <song_artist>.extension**

Then run
```powershell
python wallpaper_gen.py
```

**The script takes the current time and day, album cover and generates a random progress bar.**

**Supported file types:**

- png
- jpg
- jpeg
- gif
- bmp
- tiff

## Examples

![cover](https://raw.githubusercontent.com/MatixGX/iosMusicScreen/main/inputs/eighteen%20%23%20paywall.jpg)
![generated](https://github.com/MatixGX/iosMusicScreen/blob/main/outputs/eighteen%20%23%20paywall.png?raw=true)

![cover](https://github.com/MatixGX/iosMusicScreen/blob/main/inputs/Memory%20Reboot%20%23%20VOJ%20&%20Narvent.jpg?raw=true)
![generated](https://github.com/MatixGX/iosMusicScreen/blob/main/outputs/Memory%20Reboot%20%23%20VOJ%20&%20Narvent.png?raw=true)

Note that it is not perfect, but I tried to be as precise as possible.
