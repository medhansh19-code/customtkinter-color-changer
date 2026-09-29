import customtkinter as ctk
# Import the customtkinter library.
# CustomTkinter is an extension of Tkinter used to create modern
# and customizable graphical user interfaces in Python.
# "ctk" is used as a short alias for customtkinter.


gui = ctk.CTk()
# CTk() creates the main application window.
# "gui" stores the reference to the main window.


gui.title("Color Changer App")
# title() sets the title displayed in the window's title bar.


gui.geometry("400x300")
# geometry() defines the initial size of the application window.
# "400x300" means 400 pixels wide and 300 pixels high.


gui.configure(fg_color="white")
# configure() changes the properties of the main window.
# fg_color specifies the foreground/background color used by CustomTkinter.
# The initial background color of the application is white.


def change(color):
    # Define a function named change().
    # The "color" parameter receives the color selected by the user.

    gui.configure(fg_color=color)
    # Change the background color of the main application window.

    label.configure(fg_color=color)
    # Change the background color of the label
    # so that it matches the main window.

    frame.configure(fg_color=color)
    # Change the frame background to the same selected color.
    # This makes the frame visually blend with the application background.


label = ctk.CTkLabel(
    gui,
    text="Click a button to change the background color",
    font=("Arial", 14),
    text_color="black",
    fg_color="white"
)
# CTkLabel() creates a text label.
# "gui" specifies that the label belongs to the main window.
# text defines the message displayed to the user.
# font specifies the font family and size.
# text_color defines the color of the text.
# fg_color defines the initial background color of the label.


label.pack(pady=20)
# pack() places the label inside the main window.
# pady=20 adds 20 pixels of vertical spacing around the label.


frame = ctk.CTkFrame(
    gui,
    fg_color="white"
)
# CTkFrame() creates a container used to organize the buttons.
# The frame initially uses the same white background as the main window.


frame.pack(pady=10)
# Places the frame inside the main window.
# pady=10 adds vertical spacing around the frame.


red_button = ctk.CTkButton(
    frame,
    text="Red",
    width=100,
    fg_color="red",
    hover_color="#990000",
    text_color="white",
    command=lambda: change("red")
)
# Creates the Red button inside the frame.
# fg_color="red" gives the button a red background.
# hover_color defines the color shown when the mouse moves over the button.
# text_color="white" makes the button text white.
# command calls change("red") when the button is clicked.


red_button.pack(pady=3)
# Places the Red button inside the frame.
# pady=3 adds vertical spacing around the button.


green_button = ctk.CTkButton(
    frame,
    text="Green",
    width=100,
    fg_color="green",
    hover_color="#006600",
    text_color="white",
    command=lambda: change("green")
)
# Creates the Green button.
# Clicking the button changes the application background to green.


green_button.pack(pady=3)
# Places the Green button inside the frame.


blue_button = ctk.CTkButton(
    frame,
    text="Blue",
    width=100,
    fg_color="blue",
    hover_color="#000099",
    text_color="white",
    command=lambda: change("blue")
)
# Creates the Blue button.
# Clicking the button changes the application background to blue.


blue_button.pack(pady=3)
# Places the Blue button inside the frame.


white_button = ctk.CTkButton(
    frame,
    text="White",
    width=100,
    fg_color="white",
    hover_color="#dddddd",
    text_color="black",
    command=lambda: change("white")
)
# Creates the White button.
# The button uses black text because the background is white.
# Clicking it changes the application background to white.


white_button.pack(pady=3)
# Places the White button inside the frame.


yellow_button = ctk.CTkButton(
    frame,
    text="Yellow",
    width=100,
    fg_color="yellow",
    hover_color="#cccc00",
    text_color="black",
    command=lambda: change("yellow")
)
# Creates the Yellow button.
# The button uses black text for better visibility against the yellow background.
# Clicking it changes the application background to yellow.


yellow_button.pack(pady=3)
# Places the Yellow button inside the frame.


gui.mainloop()
# Starts CustomTkinter's event loop.
# It keeps the application running and waits for user interactions
# such as button clicks, mouse events, keyboard input, and window events.