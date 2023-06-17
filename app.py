
import customtkinter
from PIL import Image
import os

from customtkinter import filedialog

import mycam
import encoder
from CTkMessagebox import CTkMessagebox

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if file_path:
        image_label.configure(text="Selected: " + file_path)

        # Open the image file
        image = Image.open(file_path)

        # Get the custom name from the input field
        custom_name = entry.get()

        # Save the image with the custom name in "C" directory
        save_path = f"data/{custom_name}.jpg"
        image.save(save_path)
        print(save_path)

        save_label.configure(text="Image Saved to: " + save_path)

image_path="assets"
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


face_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "face.png")),
dark_image=Image.open(os.path.join(image_path, "face.png")), size=(30, 30))

upload_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "upload.png")),
dark_image=Image.open(os.path.join(image_path, "upload.png")), size=(20, 20))

encode_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "encode.png")),
dark_image=Image.open(os.path.join(image_path, "encode.png")), size=(30, 30))

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")
app.title("Face Recognition")
app.geometry("520x350")
app.maxsize(680,420)
app.minsize(520,340)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

def ask_encoding():
    # get yes/no answers
    msg = CTkMessagebox(title="Encoding...", message="Click 'Yes' to Start. \nPlease be patient, good things take time",
                        icon="info", option_1="Cancel", option_2="No", option_3="Yes")
    response = msg.get()
    
    if response=="Yes":
        encoder.myencoder()      
    else:
        pass

btn_frame = customtkinter.CTkFrame(master=app ,width=500 )
btn_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew" ,columnspan=2)
btn_frame.grid_columnconfigure((0,1), weight=1)
btn_frame.grid_rowconfigure(0, weight=1)

   
# Use CTkButton instead of tkinter Button
cam_btn = customtkinter.CTkButton(btn_frame, text="Camera", command=mycam.webCam,image=face_image , font=customtkinter.CTkFont(size=25, weight="bold"), height=40)
cam_btn.grid(row=0, column=0,padx=(20,10), pady=20, sticky="news")

encode_btn = customtkinter.CTkButton(btn_frame, text="Encode", command=ask_encoding,image=encode_image , font=customtkinter.CTkFont(size=25, weight="bold"), height=40)
encode_btn.grid(row=0, column=1,padx=(10,20), pady=20, sticky="news")

label = customtkinter.CTkLabel(master=app, text="1: Camera:: to quite press 'q' \n2: Encode:: images name used as ID")
label.grid(row=1, column=0,padx=20, pady=(0,10), sticky="news", columnspan=2)
# label = customtkinter.CTkLabel(master=app, text="CTkLabel")
# label.grid(row=0, column=1,padx=20, pady=20, sticky="ew")

entry = customtkinter.CTkEntry(app, placeholder_text="First Enter Name of Person Then Select Image")
entry.grid(row=2, column=0,padx=20, pady=(0,10), sticky="ew" ,columnspan=2)

save_img_btn = customtkinter.CTkButton(master=app, text="Select Image", command=open_file,image=upload_image , font=customtkinter.CTkFont(size=15, weight="bold"), height=40)
save_img_btn.grid(row=3, column=0,padx=20, pady=5, sticky="news", columnspan=2)

image_label = customtkinter.CTkLabel(master=app, text="Image Path:")
image_label.grid(row=4, column=0,padx=20, pady=(0,5), sticky="e")

save_label = customtkinter.CTkLabel(master=app, text="Image Saved to:")
save_label.grid(row=4, column=1,padx=20, pady=(0,5), sticky="w")






app.mainloop()