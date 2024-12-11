from tkinter import *
import base64

# Initialize the Tkinter window
root = Tk()  # Create the root window
root.geometry("650x250")  # Set the dimensions of the window
root.resizable(0, 0)  # Make the window non-resizable
root.title("DataFlair - Message Encode and Decode")  # Title of the window

# Add labels
Label(root, text="ENCODE <> DECODE", font="arial 20 bold").pack()
Label(root, text="KNOW IN A MORE SIMPLE WAY", font="arial 16 bold").pack(side=BOTTOM)

# Initialize variables for inputs and results
Text = StringVar()
private_key = StringVar()
mode = StringVar()
Result = StringVar()

# Define the encode function
def Encode(key, message):
    enc = []
    for i in range(len(message)):
        key_c = key[i % len(key)]  # Repeat the key to match the message length
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))  # Character-wise encoding
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()  # Encode in base64

# Define the decode function
def Decode(key, message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()  # Decode base64 message
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))  # Character-wise decoding
    return "".join(dec)

# Define the function to set the mode and trigger encoding/decoding
def Mode():
    if mode.get() == "e":  # If mode is 'e' (encode)
        Result.set(Encode(private_key.get(), Text.get()))
    elif mode.get() == "d":  # If mode is 'd' (decode)
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set("Invalid Mode")

# Function to reset all fields
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

# GUI Elements
Label(root, text="MESSAGE", font="arial 12 bold").place(x=60, y=60)
Entry(root, textvariable=Text, font="arial 10", bg="ghost white").place(x=290, y=60)

Label(root, text="KEY", font="arial 12 bold").place(x=60, y=90)
Entry(root, textvariable=private_key, font="arial 10", bg="ghost white").place(x=290, y=90)

Label(root, text="MODE (e-encode, d-decode)", font="arial 12 bold").place(x=60, y=120)
Entry(root, textvariable=mode, font="arial 10", bg="ghost white").place(x=290, y=120)

Button(root, text="RESULT", font="arial 12 bold", bg="LightGray", command=Mode).place(x=60, y=150)
Entry(root, textvariable=Result, font="arial 10", bg="ghost white").place(x=290, y=150)

Button(root, text="RESET", font="arial 12 bold", bg="LimeGreen", command=Reset).place(x=150, y=190)
Button(root, text="EXIT", font="arial 12 bold", bg="OrangeRed", command=root.destroy).place(x=300, y=190)

# Run the application
root.mainloop()