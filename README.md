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

![cover](inputs/eighteen %23 paywall.jpg?raw=true)
![generated](outputs/eighteen %23 paywall.png?raw=true)

![cover](./inputs/Memory Reboot %23 VOJ & Narvent.jpg?raw=true)
![generated](./outputs/Memory Reboot %23 VOJ & Narvent.png?raw=true)

Note that it is not perfect, but I tried to be as precise as possible.
