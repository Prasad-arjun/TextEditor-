# Tkinter GUI code
from tkinter import *
from tkinter import PhotoImage
from tkinter import Canvas
from tkinter import ttk
from tkinter import colorchooser
from PIL import Image, ImageTk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
root = Tk()

# Load the PNG image
# Replace with the path to your PNG icon file
icon_path = "utils\content-creator.png"
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


# show tooltip


# ---------------------------File menu functions start --------------------------------
# file types
ftypes = [("Text file", ".txt"), ("Python file", ".py"), ("All Files", "*.*")]

# file open method start


def file_open():
    file_path = filedialog.askopenfilename(
        title="Open File", defaultextension=".txt", filetypes=ftypes)

    if not file_path:
        messagebox.showinfo("Alert", "Operation cancelled")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)  # Clear previous content
            text_area.insert(1.0, content)
            file.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error opening file: {str(e)}")
# file open method end

# new file start


def new_file():
    text_area.delete(1.0, tk.END)   # Clear previous content


# new file end

# save file start

def save_file_command():
    """
    Save the content of the text area to a file.

    If the content is empty, display an alert.
    Prompt the user to select a file path to save the content.
    If the user cancels the operation, display an alert.
    Otherwise, write the content to the selected file.

    Raises:
        Exception: If there is an error saving the file.

    Returns:
        None
    """
    content = text_area.get(1.0, tk.END)
    if len(content.strip()) == 0:
        messagebox.showinfo("Alert", "Nothing to save")
        return

    try:
        file_path = filedialog.asksaveasfilename(
            title="Save File", defaultextension=".txt", filetypes=ftypes)

        if not file_path:
            messagebox.showinfo("Alert", "Operation cancelled")
        else:
            with open(file_path, "rw", encoding="utf-8") as file:
                content = text_area.get(1.0, tk.END)
                file.write(content)
                file.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error saving file: {str(e)}")

# save file end

# font style fuctions start


def change_font_style(fs):
    selceted_text = text_area.tag_ranges("sel")
    if fs == "bold" and selceted_text:
        text_area.tag_add("bold", "sel.first", "sel.last")
        text_area.tag_configure("bold", font="arial 11 bold")
    elif fs == "italic" and selceted_text:
        text_area.tag_add("italic", "sel.first", "sel.last")
        text_area.tag_configure("italic", font="arial 11 italic")
    elif fs == "underline" and selceted_text:
        text_area.tag_add("underline", "sel.first", "sel.last")
        text_area.tag_configure("underline", font="arial 11 underline")
    elif fs == "fontColor" and selceted_text:
        color = colorchooser.askcolor()
        text_area.tag_add("fontColor", "sel.first", "sel.last")
        text_area.tag_configure("fontColor", foreground=color[1])
    else:
        messagebox.showinfo("Alert", "No text selected")

# font style fuctions end


# ---------------------------File menu functions end --------------------------------
icon_width = 24
icon_height = 24
new_page = resize_icon(r"utils\New.png", icon_width, icon_height)
open_file = resize_icon(r"utils\folder.png", icon_width, icon_height)
save_file = resize_icon(r"utils\icons8-save-48.png", icon_width, icon_height)
save_as_file = resize_icon(
    r"utils\icons8-save-as-48.png", icon_width, icon_height)
file_print = resize_icon(r"utils\icons8-print.gif", icon_width, icon_height)
copy_file = resize_icon(r"utils\icons8-copy-48.png", icon_width, icon_height)
cut_file = resize_icon(r"utils\icons8-scissors-48.png",
                       icon_width, icon_height)
paste_file = resize_icon(r"utils\icons8-paste-100.png",
                         icon_width, icon_height)
change_font = resize_icon(
    r"utils\icons8-choose-font-48.png", icon_width, icon_height)
change_bold = resize_icon(r"utils\icons8-bold-30.png", icon_width, icon_height)
change_italic = resize_icon(
    r"utils\icons8-italic-30.png", icon_width, icon_height)
change_underline = resize_icon(
    r"utils\icons8-underline-30.png", icon_width, icon_height)
left_align = resize_icon(
    r"utils\icons8-align-left-48.png", icon_width, icon_height)
center_align = resize_icon(
    r"utils\icons8-align-justify-48.png", icon_width, icon_height)
right_align = resize_icon(
    r"utils\icons8-align-right-48.png", icon_width, icon_height)
about_button = resize_icon(
    r"utils\icons8-about-48.png", icon_width, icon_height)
exit_button = resize_icon(
    r"utils\icons8-fire-exit-48.png", icon_width, icon_height)

# color code for the menu bar and footer
color_code = "#E5E1DA"
# Create a menu bar
menu_bar = Frame(root, bg=color_code, relief="raised")

# Create File menu
button_new_page = Button(menu_bar, image=new_page, command=new_file)
button_new_page.grid(row=0, column=0, padx=10.5, pady=10.5)

button_open_file = Button(menu_bar, image=open_file, command=file_open)
button_open_file.grid(row=0, column=1, padx=10.5, pady=10.5)

button_save_file = Button(menu_bar, image=save_file, command=save_file_command)
button_save_file.grid(row=0, column=2, padx=10.5, pady=10.5)

button_save_as_file = Button(menu_bar, image=save_as_file)
button_save_as_file.grid(row=0, column=3, padx=10.5, pady=10.5)

button_print_file = Button(menu_bar, image=file_print)
button_print_file.grid(row=0, column=4, padx=10.5, pady=10.5)

separator1 = ttk.Separator(menu_bar, orient="vertical")
separator1.grid(row=0, column=5, sticky="ns", padx=10.5, pady=10.5)

edit_button_copy = Button(menu_bar, image=copy_file)
edit_button_copy.grid(row=0, column=6, padx=10.5, pady=10.5)

edit_button_cut = Button(menu_bar, image=cut_file)
edit_button_cut.grid(row=0, column=8, padx=10.5, pady=10.5)

edit_button_paste = Button(menu_bar, image=paste_file)
edit_button_paste.grid(row=0, column=8, padx=10.5, pady=10.5)

separator2 = ttk.Separator(menu_bar, orient="vertical")
separator2.grid(row=0, column=9, sticky="ns", padx=10.5, pady=10.5)

button_font = Button(menu_bar, image=change_font,
                     command=lambda: change_font_style("fontColor"))
button_font.grid(row=0, column=10, padx=10.5, pady=10.5)

button_bold = Button(menu_bar, image=change_bold,
                     command=lambda: change_font_style("bold"))
button_bold.grid(row=0, column=11, padx=10.5, pady=10.5)

button_Italic = Button(menu_bar, image=change_italic,
                       command=lambda: change_font_style("italic"))
button_Italic.grid(row=0, column=12, padx=10.5, pady=10.5)

button_underline = Button(menu_bar, image=change_underline,
                          command=lambda: change_font_style("underline"))
button_underline.grid(row=0, column=13, padx=10.5, pady=10.5)

separator3 = ttk.Separator(menu_bar, orient="vertical")
separator3.grid(row=0, column=14, sticky="ns", padx=10.5, pady=10.5)

align_left = Button(menu_bar, image=left_align)
align_left.grid(row=0, column=15, padx=10.5, pady=10.5)

align_center = Button(menu_bar, image=center_align)
align_center.grid(row=0, column=16, padx=10.5, pady=10.5)

align_right = Button(menu_bar, image=right_align)
align_right.grid(row=0, column=17, padx=10.5, pady=10.5)

separator4 = ttk.Separator(menu_bar, orient="vertical")
separator4.grid(row=0, column=18, sticky="ns", padx=11, pady=11)

button_about = Button(menu_bar, image=about_button)
button_about.grid(row=0, column=19, padx=11, pady=11)

separator5 = ttk.Separator(menu_bar, orient="vertical")
separator5.grid(row=0, column=20, sticky="ns", padx=11, pady=11)

button_exit = Button(menu_bar, image=exit_button)
button_exit.grid(row=0, column=21, padx=11, pady=11)


menu_bar.grid(row=0, column=0, sticky="ew")


# TextArea
text_area = Text(root, wrap="word", font="verdana 11", width=140,
                 height=35.4, padx=8, pady=4, relief="sunken")
text_area.grid(row=1, column=0,)


def resize_icon_footer(path, width, height):
    original_image = Image.open(path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(resized_image)


icon_width1 = 24
icon_height1 = 24
summarise_text = resize_icon_footer(
    r"utils\icons8-pages-48.png", icon_width1, icon_height1)
read_text = resize_icon_footer(
    r"utils\icons8-read-48.png", icon_width1, icon_height1)
speech_to_text = resize_icon_footer(
    r"utils\icons8-microphone-48.png", icon_width1, icon_height1)
text_to_speech = resize_icon_footer(
    r"utils\icons8-speaker-48.png", icon_width1, icon_height1)
text_translate = resize_icon_footer(
    r"utils\icons8-translation-100.png", icon_width1, icon_height1)

# Footer
footer = Frame(root, bg=color_code, relief="raised")
footer.grid(row=2, column=0, sticky="ew", pady=0)


button1 = Button(footer, image=summarise_text)
button1.pack(side=RIGHT, padx=10, pady=10)

button2 = Button(footer, image=read_text)
button2.pack(side=RIGHT, padx=10, pady=10)

button3 = Button(footer, image=speech_to_text)
button3.pack(side=RIGHT, padx=10, pady=10)

button4 = Button(footer, image=text_to_speech)
button4.pack(side=RIGHT, padx=10, pady=10)

button5 = Button(footer, image=text_translate)
button5.pack(side=RIGHT, padx=10, pady=10)

root.rowconfigure(2, weight=2)
root.rowconfigure(3, weight=1)

root.state("zoomed")
root.mainloop()
