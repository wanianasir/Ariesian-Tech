from tkinter import *


# Initialize variables for storing first number, second number, and operator
first_number=second_number=operator=None


# Function to get the digit when a button is pressed
def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)
 
    
# Function to clear the display
def clear():
    result_label.config(text='')
    
    
# Function to get the operator (+, -, *, /)
def get_operator(op):
    global first_number,operator
    
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')
    
    
# Function to get the result and perform the calculation
def get_result():
    global first_number,second_number,operator
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
            
            
# Function for backspace to remove the last character
def backspace():
    current = result_label['text']
    if current:  # Check if the string is not empty
        result_label.config(text=current[:-1])  # Remove the last character
        
            
# Create the main window  
root=Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(True,True)
root.configure(bg='black')

# Create the result label
result_label=Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0)
result_label.grid(row=0,column=0,columnspan=10,pady=(50,25),sticky='w')
result_label.config(font=('verdana',30,'bold'))


# Create buttons for digits, operators, and clear
# Add the didgit seven button
btn7=Button(root,text='7',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

# Add the digit eight button
btn8=Button(root,text='8',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

# Add the digit nine button
btn9=Button(root,text='9',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

# Add the addition button
btn_add=Button(root,text='+',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('+'))
btn_add.grid(row=1,column=3)
btn_add.config(font=('verdana',14))


# Add the digit four button
btn4=Button(root,text='4',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

# Add the digit five button
btn5=Button(root,text='5',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

# Add the digit six button
btn6=Button(root,text='6',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

# Add the subtraction button
btn_sub=Button(root,text='-',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('-'))
btn_sub.grid(row=2,column=3)
btn_sub.config(font=('verdana',14))


# Add the digit one button
btn1=Button(root,text='1',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

# Add the digit two button
btn2=Button(root,text='2',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

# Add the digit three button
btn3=Button(root,text='3',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

# Add the multiplication button
btn_mul=Button(root,text='*',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('*'))
btn_mul.grid(row=3,column=3)
btn_mul.config(font=('verdana',14))


# Add the clear button
btn_clr=Button(root,text='C',bg='#00a65a',fg='white',width=5,height=2,command=lambda :clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('verdana',14))

# Add the digit zero button
btn0=Button(root,text='0',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

# Add the equal button
btn_equal=Button(root,text='=',bg='#00a65a',fg='white',width=5,height=2,command=get_result)
btn_equal.grid(row=4,column=2)
btn_equal.config(font=('verdana',14))

# Add the division button
btn_div=Button(root,text='/',bg='#00a65a',fg='white',width=5,height=2,command=lambda :get_operator('/'))
btn_div.grid(row=4,column=3)
btn_div.config(font=('verdana',14))


# Add the Backspace button
btn_backspace = Button(root, text='←', bg='#00a65a', fg='white', width=5, height=2, command=backspace)
btn_backspace.grid(row=5, column=0, columnspan=4, sticky='nsew')
btn_backspace.config(font=('verdana', 14))


# Run the main loop
root.mainloop()