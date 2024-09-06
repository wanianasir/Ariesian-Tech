Here is a detailed description of my project **Simple Calculator using GUI**:
This Python code implements a **Graphical User Interface (GUI)-based calculator** using the `Tkinter` module. The calculator allows users to perform basic arithmetic operations, including addition, subtraction, multiplication, and division. Additionally, it supports functionalities like clearing the screen and removing the last character (backspace).

Here’s a detailed breakdown of each part of the code, explaining its purpose and design:

**1.Importing the Tkinter Library**
```python
from tkinter import *
```
- The code starts by importing the `Tkinter` module, the standard Python library for creating graphical user interfaces. We import all its classes and functions to facilitate the creation of the calculator's GUI elements.

---

**2.Global Variables**
```python
first_number = second_number = operator = None
```
- These global variables store the values for the **first operand**, **second operand**, and the **operator** (e.g., `+`, `-`, `*`, `/`). They are used to hold data across multiple button clicks during a calculation.

---

**3.Functions**

#### `get_digit(digit)`
```python
def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)
```
- **Purpose**: This function is called whenever a digit button (0–9) is pressed. 
- **Functionality**:
  - It retrieves the current value from the calculator display (`result_label`), appends the pressed digit, and updates the display with the new value.

---

#### `clear()`
```python
def clear():
    result_label.config(text='')
```
- **Purpose**: This function clears the display when the "C" (clear) button is pressed.
- **Functionality**:
  - It resets the text of `result_label` to an empty string, effectively clearing the calculator screen.

---

#### `get_operator(op)`
```python
def get_operator(op):
    global first_number, operator
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')
```
- **Purpose**: This function is triggered when an operator button (`+`, `-`, `*`, `/`) is clicked.
- **Functionality**:
  - The value currently on the display is stored as the **first operand** (`first_number`), and the selected operator (`op`) is saved to the global `operator` variable.
  - The display is then cleared, allowing the user to input the second operand.

---

#### `get_result()`
```python
def get_result():
    global first_number, second_number, operator
    second_number = int(result_label['text'])
    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(first_number / second_number))
```
- **Purpose**: This function is triggered when the equals (`=`) button is pressed. It performs the calculation based on the operator selected and the two operands.
- **Functionality**:
  - The value currently on the display is stored as the **second operand** (`second_number`).
  - Depending on the operator, the corresponding arithmetic operation is performed, and the result is displayed.
  - For division, if the second operand is `0`, it prevents division by zero by displaying an "Error" message.

---

#### `backspace()`
```python
def backspace():
    current = result_label['text']
    if current:
        result_label.config(text=current[:-1])
```
- **Purpose**: This function handles the **Backspace** operation, removing the last character from the display.
- **Functionality**:
  - It retrieves the current value on the display and slices off the last character, then updates the display accordingly.

---

### 4. **Creating the Main Window**
```python
root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(True, True)
root.configure(bg='black')
```
- **Purpose**: This part of the code initializes the main application window (`root`) using `Tk()`.
- **Functionality**:
  - The title is set to "Calculator".
  - The window size is set to `280x380` pixels.
  - The `resizable()` method allows the window to be resized by the user.
  - The background color is set to **black**.

---

### 5. **Creating the Display (Result Label)**
```python
result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=10, pady=(50, 25), sticky='w')
result_label.config(font=('verdana', 30, 'bold'))
```
- **Purpose**: This is the display area where numbers and results are shown.
- **Functionality**:
  - A `Label` widget is created with a black background and white text.
  - The display spans across all columns in the first row (`columnspan=10`) and has padding applied for better spacing.
  - The font used is **Verdana**, with a large, bold style for visibility.

---

### 6. **Creating Buttons for Digits and Operators**
```python
btn7 = Button(root, text='7', bg='#00a65a', fg='white', width=5, height=2, command=lambda: get_digit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('verdana', 14))
# Similar code for other buttons...
```
- **Purpose**: These are the buttons that the user interacts with to input digits, operators, and perform actions.
- **Functionality**:
  - Each button is created using the `Button` widget, with a custom size (`width`, `height`) and color scheme.
  - The `command` parameter specifies the function to be called when the button is clicked. A **lambda** function is used to pass arguments (like the digit) to the corresponding function.
  - Buttons are placed on the window using the `grid()` method, allowing for a structured layout.

---

### 7. **Adding the Backspace Button**
```python
btn_backspace = Button(root, text='←', bg='#00a65a', fg='white', width=5, height=2, command=backspace)
btn_backspace.grid(row=5, column=0, columnspan=4, sticky='nsew')
btn_backspace.config(font=('verdana', 14))
```
- **Purpose**: This button provides the backspace functionality, allowing users to delete the last entered character.
- **Functionality**:
  - The button has the same styling as other buttons and is placed at the bottom of the grid.
  - The `command` is set to the `backspace()` function.

---

### 8. **Main Loop**
```python
root.mainloop()
```
- **Purpose**: This line starts the **Tkinter event loop**, allowing the application to respond to user inputs. The program will keep running until the window is closed.

---

### Summary
This calculator is a simple yet effective GUI application built using **Tkinter**. It supports all the essential arithmetic operations, including:
- **Addition**, **Subtraction**, **Multiplication**, and **Division**.
- Error handling for division by zero.
- Additional functionalities like **Backspace** and **Clear**.
  
The buttons are neatly arranged in a grid layout, and the display is easy to read due to the large font size. This structure makes the code modular and scalable, allowing for future extensions or modifications with ease.
