from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance
import os
import datetime
import random

# Sorry if the code is messy, I tried to make it clean however after some time it just got really crappy. I'm not a python expert, but I tried by best. Have fun!
# If you liked, please give me a star, it would really help <3


def make_wallpaper(name, song_name, song_artist, song_duration, current_sec):

    WIDTH, HEIGHT = (1080, 1920)
    thumbnail_path = os.path.join(os.getcwd(), "inputs", name)
    img = Image.open(thumbnail_path).convert("RGB")

    # get the background
    thumbnail_blur = img.filter(ImageFilter.BoxBlur(200))
    enhancer = ImageEnhance.Brightness(thumbnail_blur)
    thumbnail_blur = enhancer.enhance(0.8)
    thumbnail_blur = thumbnail_blur.resize([HEIGHT, HEIGHT])

    gradient = Image.new("RGBA", (WIDTH, HEIGHT), color=0)
    gradient.paste(thumbnail_blur, (0, 0))

    # add current time
    now = datetime.datetime.now()
    FONT_NAME = "font.otf"
    FONT_BOLD_NAME = "font-bold.ttf"
    font = ImageFont.truetype("assets/" + FONT_BOLD_NAME, WIDTH / 5)
    font_date = ImageFont.truetype("assets/" + FONT_NAME, WIDTH / 15)

    text_layer = Image.new("RGBA", (WIDTH, HEIGHT), color=0)
    text_draw = ImageDraw.Draw(text_layer)
    clock_str = f"{str(now.hour).zfill(2)}:{str(now.minute).zfill(2)}"

    day_of_the_week = ""
    if now.weekday() == 0:
        day_of_the_week = "Monday"
    elif now.weekday() == 1:
        day_of_the_week = "Tuesday"
    elif now.weekday() == 2:
        day_of_the_week = "Wednesday"
    elif now.weekday() == 3:
        day_of_the_week = "Thursday"
    elif now.weekday() == 4:
        day_of_the_week = "Friday"
    elif now.weekday() == 5:
        day_of_the_week = "Saturday"
    elif now.weekday() == 6:
        day_of_the_week = "Sunday"

    month = ""
    if now.date().month == 1:
        month = "January"
    elif now.date().month == 2:
        month = "February"
    elif now.date().month == 3:
        month = "March"
    elif now.date().month == 4:
        month = "April"
    elif now.date().month == 5:
        month = "May"
    elif now.date().month == 6:
        month = "June"
    elif now.date().month == 7:
        month = "July"
    elif now.date().month == 8:
        month = "August"
    elif now.date().month == 9:
        month = "September"
    elif now.date().month == 10:
        month = "October"
    elif now.date().month == 11:
        month = "November"
    elif now.date().month == 12:
        month = "December"

    day_str = f"{day_of_the_week}, {month} {now.date().day}"
    _, _, w, h = text_draw.textbbox(
        (0, 0),
        clock_str,
        font=font,
    )

    clock_pos_x = (WIDTH - w) / 2
    clock_pos_y = HEIGHT / 7

    text_draw.text(
        (clock_pos_x, clock_pos_y),
        clock_str,
        font=font,
        fill=(255, 255, 255),
    )

    _, _, w, h = text_draw.textbbox(
        (0, 0),
        day_str,
        font=font_date,
    )

    text_draw.text(
        ((WIDTH - w) / 2, clock_pos_y - (clock_pos_y / 5)),
        day_str,
        font=font_date,
        fill=(255, 255, 255),
    )

    width, height = img.size
    newsize = (0, 0)
    if WIDTH < HEIGHT:
        new_width = WIDTH - (WIDTH / 4)
        factor = new_width / width
        newsize = (int(new_width), int(height * factor))
    elif HEIGHT < WIDTH:
        new_height = HEIGHT - (HEIGHT / 4)
        factor = new_height / height
        newsize = (int(width * factor), int(new_height))

    img_resized = img.resize(newsize)

    final_image = gradient.copy()
    x_size, y_size = img_resized.size
    final_image.paste(
        img_resized,
        (int((WIDTH - x_size) / 2), int((HEIGHT - y_size) / 2)),
    )

    # making the text layer half alpha

    datas = text_layer.getdata()
    CLOCK_TRANSPARENCY = 220
    new_datas = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_datas.append((255, 255, 255, CLOCK_TRANSPARENCY))
        else:
            new_datas.append(item)
    text_layer.putdata(new_datas)

    # adding the clock to the background
    final_image = Image.alpha_composite(final_image, text_layer)

    play_box = Image.new("RGBA", (WIDTH, HEIGHT), color=0)
    play_draw = ImageDraw.Draw(play_box)
    play_box_width = (WIDTH / 20) * 17
    play_box_height = HEIGHT / 6
    play_box_start_x = (WIDTH - play_box_width) / 2
    play_box_start_y = (HEIGHT / 4) * 3.1
    play_draw.rounded_rectangle(
        (
            play_box_start_x,
            play_box_start_y,
            play_box_start_x + play_box_width,
            play_box_start_y + play_box_height,
        ),
        fill=(255, 255, 255),
        radius=play_box_width / 15,
    )

    # creating the controls box
    song_name_font = ImageFont.truetype("assets/" + FONT_BOLD_NAME, WIDTH / 25)
    song_author_font = ImageFont.truetype("assets/" + FONT_NAME, WIDTH / 25)
    song_dur_font = ImageFont.truetype("assets/" + FONT_NAME, WIDTH / 40)

    _, _, w, h = play_draw.textbbox(
        (0, 0),
        song_name,
        font=song_name_font,
    )

    play_draw.text(
        ((WIDTH - w) / 2, play_box_start_y + 30),
        song_name,
        font=song_name_font,
        fill=(0, 0, 0),
    )

    _, _, w, h = play_draw.textbbox(
        (0, 0),
        song_artist,
        font=song_author_font,
    )

    play_draw.text(
        ((WIDTH - w) / 2, play_box_start_y + 30 + h),
        song_artist,
        font=song_author_font,
        fill=(30, 30, 30),
    )

    current_str = f"{current_sec//60}:{str(current_sec%60).zfill(2)}"

    _, _, w, h = play_draw.textbbox(
        (0, 0),
        current_str,
        font=song_dur_font,
    )

    play_draw.text(
        (play_box_start_x + 40, (play_box_start_y + play_box_height / 2) - h / 4),
        current_str,
        font=song_dur_font,
        fill=(0, 0, 0),
    )

    play_draw.rounded_rectangle(
        (
            play_box_start_x + 110,
            play_box_start_y + play_box_height / 2,
            play_box_start_x + play_box_width - 110,
            (play_box_start_y + play_box_height / 2) + 20,
        ),
        radius=10,
        fill=(200, 200, 200),
    )
    bar_max_width = play_box_width - 220

    play_bar_width = (current_sec * bar_max_width) / song_duration

    play_draw.rounded_rectangle(
        (
            play_box_start_x + 110,
            play_box_start_y + play_box_height / 2,
            play_box_start_x + play_box_width - 110 - (bar_max_width - play_bar_width),
            (play_box_start_y + play_box_height / 2) + 20,
        ),
        radius=10,
        fill=(0, 0, 0),
    )

    until_end_str = f"-{(song_duration-current_sec)//60}:{str((song_duration-current_sec)%60).zfill(2)}"
    _, _, w, h = play_draw.textbbox(
        (0, 0),
        until_end_str,
        font=song_dur_font,
    )

    play_draw.text(
        (
            play_box_start_x + play_box_width - (w + 40),
            (play_box_start_y + play_box_height / 2) - h / 4,
        ),
        until_end_str,
        font=song_dur_font,
        fill=(0, 0, 0),
    )

    contorls_img = Image.open("assets/controls.png")
    play_box = Image.alpha_composite(play_box, contorls_img)

    datas = play_box.getdata()

    CONTROLS_TRANSPARENCY = 150
    BAR_TRANSPARENCY = 150

    new_data = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            new_data.append((255, 255, 255, CONTROLS_TRANSPARENCY))
        elif item[0] == 200 and item[1] == 200 and item[2] == 200:
            new_data.append((200, 200, 200, BAR_TRANSPARENCY))
        else:
            new_data.append(item)
    play_box.putdata(new_data)

    final_image = Image.alpha_composite(final_image, play_box)
    return final_image


# For all the files in the inputs folder create a wallpaper
# Set the author and title by following the image naming scheme: <song_name> # <song_author>.extension
# Note that the progress bar is randomly generated every time
if __name__ == "__main__":
    for file in os.scandir("inputs"):
        name = file.name.split(".")[0]
        duration = random.randint(10, 240)
        current_sec = random.randint(0, duration)
        img = make_wallpaper(
            file.name, name.split("#")[0], name.split("#")[1], duration, current_sec
        )
        img.save(f"outputs/{file.name.split('.')[0]}.png")
