# Tkinter GUI code
from tkinter import *
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import ttk
from PIL import Image, ImageTk
root = Tk()

# Load the PNG image
icon_path = "utils\content-creator.png"  # Replace with the path to your PNG icon file
icon_image = PhotoImage(file=icon_path)

# Set the window icon
root.iconphoto(True, icon_image)
root.title("NextGen TextEditor")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size to match the screen dimensions
root.geometry(f"{screen_width}x{screen_height}")

# Resize function using Pillow
def resize_icon(path, width, height):
    original_image = Image.open(path)
    resized_image = original_image.resize((width, height),  Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

icon_width = 50
icon_height = 50
new_page = resize_icon(r"utils\New.png", icon_width, icon_height)
open_file = resize_icon(r"utils\folder.png", icon_width, icon_height)
save_file = resize_icon(r"utils\icons8-save-48.png", icon_width, icon_height)
save_as_file = resize_icon(r"utils\icons8-save-as-48.png", icon_width, icon_height)
file_print = resize_icon(r"utils\icons8-print.gif", icon_width, icon_height)
copy_file = resize_icon(r"utils\icons8-copy-48.png", icon_width, icon_height)
cut_file = resize_icon(r"utils\icons8-scissors-48.png", icon_width, icon_height)
paste_file = resize_icon(r"utils\icons8-paste-100.png", icon_width, icon_height)
change_font = resize_icon(r"utils\icons8-choose-font-48.png", icon_width, icon_height)
change_bold = resize_icon(r"utils\icons8-bold-30.png", icon_width, icon_height)
change_italic = resize_icon(r"utils\icons8-italic-30.png", icon_width, icon_height)
change_underline = resize_icon(r"utils\icons8-underline-30.png", icon_width, icon_height)
left_align = resize_icon(r"utils\icons8-align-left-48.png", icon_width, icon_height)
center_align = resize_icon(r"utils\icons8-align-justify-48.png", icon_width, icon_height)
right_align = resize_icon(r"utils\icons8-align-right-48.png", icon_width, icon_height)
about_button = resize_icon(r"utils\icons8-about-48.png", icon_width, icon_height)
exit_button = resize_icon(r"utils\icons8-fire-exit-48.png", icon_width, icon_height)

menu_bar_color = (232, 216, 196)
# Create a menu bar
menu_bar = Frame(root,bg="#%02x%02x%02x" % menu_bar_color)

# Create File menu
button_new_page = Button(menu_bar, image=new_page)
button_new_page.grid(row=0, column=0,padx=10.5,pady=10.5)

button_open_file = Button(menu_bar, image=open_file)
button_open_file.grid(row=0, column=1,padx=10.5,pady=10.5)

button_save_file = Button(menu_bar, image=save_file)
button_save_file.grid(row=0, column=2,padx=10.5,pady=10.5)

button_save_as_file = Button(menu_bar, image=save_as_file)
button_save_as_file.grid(row=0, column=3,padx=10.5,pady=10.5)

button_print_file = Button(menu_bar, image=file_print )
button_print_file.grid(row=0, column=4,padx=10.5,pady=10.5)

separator1 = ttk.Separator(menu_bar, orient="vertical")
separator1.grid(row=0, column=5, sticky="ns",padx=10.5,pady=10.5)

edit_button_copy = Button(menu_bar, image=copy_file)
edit_button_copy.grid(row=0, column=6,padx=10.5,pady=10.5)

edit_button_cut = Button(menu_bar, image=cut_file)
edit_button_cut.grid(row=0, column=8,padx=10.5,pady=10.5)

edit_button_paste = Button(menu_bar, image=paste_file)
edit_button_paste.grid(row=0, column=8,padx=10.5,pady=10.5)

separator2 = ttk.Separator(menu_bar, orient="vertical")
separator2.grid(row=0, column=9, sticky="ns",padx=10.5,pady=10.5)

button_font = Button(menu_bar, image=change_font)
button_font.grid(row=0, column=10,padx=10.5,pady=10.5)

button_bold = Button(menu_bar, image=change_bold)
button_bold.grid(row=0, column=11,padx=10.5,pady=10.5)

button_Italic = Button(menu_bar, image=change_italic)
button_Italic.grid(row=0, column=12,padx=10.5,pady=10.5)

button_underline = Button(menu_bar, image=change_underline)
button_underline.grid(row=0, column=13,padx=10.5,pady=10.5)

separator3 = ttk.Separator(menu_bar, orient="vertical")
separator3.grid(row=0, column=14, sticky="ns",padx=10.5,pady=10.5)

align_left = Button(menu_bar, image=left_align)
align_left.grid(row=0, column=15,padx=10.5,pady=10.5)

align_center = Button(menu_bar, image=center_align)
align_center.grid(row=0, column=16,padx=10.5,pady=10.5)

align_right = Button(menu_bar, image=right_align)
align_right.grid(row=0, column=17,padx=10.5,pady=10.5)

separator4 = ttk.Separator(menu_bar, orient="vertical")
separator4.grid(row=0, column=18, sticky="ns",padx=11,pady=11)

button_about = Button(menu_bar, image=about_button)
button_about.grid(row=0, column=19,padx=11,pady=11)

separator5 = ttk.Separator(menu_bar, orient="vertical")
separator5.grid(row=0, column=20, sticky="ns",padx=11,pady=11)

button_exit = Button(menu_bar, image=exit_button)
button_exit.grid(row=0, column=21,padx=11,pady=11)


menu_bar.grid(row=0, column=0, sticky="w")


#TextArea
text_area = Text(root, wrap="word", width=150, height=33)
text_area.grid(row=1, column=0, pady=15)

def resize_icon_footer(path, width, height):
    original_image = Image.open(path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)

icon_width1 = 33
icon_height1 = 30
summarise_text = resize_icon_footer(r"utils\icons8-pages-48.png", icon_width1, icon_height1)
read_text = resize_icon_footer(r"utils\icons8-read-48.png", icon_width1, icon_height1)
speech_to_text = resize_icon_footer(r"utils\icons8-microphone-48.png", icon_width1, icon_height1)
text_to_speech = resize_icon_footer(r"utils\icons8-speaker-48.png", icon_width1, icon_height1)
text_translate = resize_icon_footer(r"utils\icons8-translation-100.png", icon_width1, icon_height1)

#Footer
footer = Frame(root, bg="#%02x%02x%02x" % menu_bar_color)
footer.grid(row=2, column=0, sticky="ew", pady=(10, 0))


button1 = Button(footer, image=summarise_text)
button1.pack(side=RIGHT, padx=10,pady= 10)

button2 = Button(footer, image=read_text)
button2.pack(side=RIGHT, padx=10,pady= 10)

button3 = Button(footer, image=speech_to_text)
button3.pack(side=RIGHT, padx=10,pady= 10)

button4 = Button(footer, image=text_to_speech)
button4.pack(side=RIGHT, padx=10,pady= 10)

button5 = Button(footer, image=text_translate)
button5.pack(side=RIGHT, padx=10,pady= 10)

root.rowconfigure(2, weight=5)

root.state("zoomed")
root.mainloop()
