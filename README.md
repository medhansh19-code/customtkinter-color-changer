# CustomTkinter Color Changer

A Python GUI application built with CustomTkinter that allows users to dynamically change the background color through interactive color buttons.

## Overview

CustomTkinter Color Changer is a desktop graphical user interface application developed using the CustomTkinter framework.

The application provides a simple interactive interface where users can select predefined colors and dynamically update the background of the main window, label, and frame.

The project demonstrates modern GUI styling, widget configuration, callback functions, lambda expressions, layout management, and event-driven programming.

## Features

- Modern CustomTkinter interface
- Dynamic background color changing
- Five predefined colors
- Color-specific buttons
- Button hover effects
- Dynamic label background
- Dynamic frame background
- Custom text colors
- Event-driven interaction
- Simple and structured layout

## Available Colors

| Button | Color | Text Color |
|---|---|---|
| Red | Red | White |
| Green | Green | White |
| Blue | Blue | White |
| White | White | Black |
| Yellow | Yellow | Black |

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| CustomTkinter | GUI framework |
| Tkinter/Tk | Underlying GUI system |

## Project Structure

```text
customtkinter-color-changer/
│
├── main.py
└── README.md
```

## Interface Components

### Main Window

The application uses a `CTk` window as the primary container.

```python
gui = ctk.CTk()
```

The initial configuration is:

- **Title:** Color Changer App
- **Size:** 400 × 300
- **Initial Color:** White

### Label

The application displays the following message:

```text
Click a button to change the background color
```

The label background is dynamically updated whenever a color is selected.

### Frame

A `CTkFrame` is used as a container for the color buttons.

The frame background is synchronized with the selected application background color.

### Buttons

The application provides five color-selection buttons:

- Red
- Green
- Blue
- White
- Yellow

Each button has its own foreground color, text color, and hover color.

## Application Logic

The background-changing functionality is handled by the `change()` function.

```python
def change(color):
    gui.configure(fg_color=color)
    label.configure(fg_color=color)
    frame.configure(fg_color=color)
```

The function receives the selected color and applies it to the main window, label, and frame.

## Event Handling

Each button uses a callback through the `command` parameter.

For example:

```python
command=lambda: change("red")
```

When the Red button is clicked, the callback executes:

```python
change("red")
```

The same mechanism is used for the other color buttons.

## CustomTkinter Styling

CustomTkinter uses `fg_color` for widget background colors.

Example:

```python
fg_color="red"
```

Button hover states can be customized with:

```python
hover_color="#990000"
```

Text colors are controlled using:

```python
text_color="white"
```

These properties provide control over the visual appearance of individual widgets.

## Layout Management

The application uses the `pack()` geometry manager to arrange widgets.

Example:

```python
button.pack(pady=3)
```

The `pady` parameter adds vertical spacing between the buttons.

The frame acts as a container, creating a clear hierarchy between the main window and its child widgets.

## Application Flow

```text
Application Start
       │
       ▼
Create CTk Window
       │
       ▼
Configure Window
       │
       ▼
Create Label
       │
       ▼
Create Button Frame
       │
       ▼
Create Color Buttons
       │
       ▼
Start Event Loop
       │
       ▼
User Selects Color
       │
       ▼
Execute change()
       │
       ▼
Update Window
       │
       ▼
Update Label
       │
       ▼
Update Frame
```

## Requirements

- Python 3.x
- CustomTkinter

## Installation

Install CustomTkinter using pip:

```bash
pip install customtkinter
```

On systems where Python 3 is explicitly invoked:

```bash
pip3 install customtkinter
```

## Running the Application

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd customtkinter-color-changer
```

Run the application:

```bash
python main.py
```

Alternatively:

```bash
python3 main.py
```

## Technical Concepts Demonstrated

This project demonstrates:

- CustomTkinter window creation
- `CTk`
- `CTkLabel`
- `CTkButton`
- `CTkFrame`
- `fg_color`
- `hover_color`
- `text_color`
- `pack()` geometry management
- Lambda expressions
- Callback functions
- Dynamic widget configuration
- Event-driven programming
- GUI event loops

## Future Enhancements

Potential improvements include:

- Add additional colors
- Add a custom color picker
- Accept hexadecimal color values
- Add a reset button
- Add dark and light themes
- Save the selected color
- Add animated color transitions
- Improve responsive layout
- Separate GUI and application logic
- Introduce class-based architecture

## Project Status

**Status:** Initial Implementation

The current version provides dynamic background color selection using five predefined buttons and demonstrates core CustomTkinter GUI development concepts.

## License

No license is currently specified for this project.
