import tkinter as tk

# Create the root window
root = tk.Tk()

# Create a label to show a prompt for user input
label = tk.Label(root, text="Enter a number:")
label.pack()

# Create an input field for the user to enter a number
input_field = tk.Entry(root)
input_field.pack()

# Create a function that will be called when the user clicks the "Show result" button
def show_result():
    # Get the value entered in the input field
    input_value = input_field.get()

    # Convert the input value to an integer
    input_value = int(input_value)

    # Calculate the result of the operation
    result = input_value * 2

    # Create a label to show the result
    result_label = tk.Label(root, text=f"Result: {result}")
    result_label.pack()

# Create a button that will call the show_result function when clicked
button = tk.Button(root, text="Show result", command=show_result)
button.pack()

# Start the main event loop
root.mainloop()