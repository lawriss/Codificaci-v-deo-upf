import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import cv2
import functions_gui
from tkinter import filedialog

# Create a window
root = tk.Tk()
root.title("LauraTube")
root.geometry("1200x700")
# background image
img = Image.open("gui_images/light.png")
img = img.resize((1200, 700), Image.LANCZOS)
background_img = ImageTk.PhotoImage(img)
canvas = tk.Canvas(root, width=1200, height=700)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=background_img)
canvas.background = background_img

# insert logo picture LauraTube
image = Image.open("gui_images/logo.png")  # Replace "example_image.jpg" with your image file
desired_width = 150
desired_height = 70
resized_image = image.resize((desired_width, desired_height), Image.LANCZOS)
img = ImageTk.PhotoImage(resized_image)
label = Label(root, image = img)
label.place(x=550, y=20)

# define different font properties
text_font = ("Verdana", 15, "bold")
steel_pink_hex = "#89538C"
button_font = ("Verdana", 20, "bold")
sky_blue_hex = "#4682B4"
loaded_path_font = ("Verdana", 10, "italic")
grey_hex = "#757275"

# get input/output path functions
def get_input_vid_path():
    global p1
    p1 = filedialog.askopenfilename() #filedialog.askopenfilename()
    label = tk.Label(root, text='You are loading the following video: \n'+p1, fg=grey_hex, font=loaded_path_font)
    label.place(x=70, y=200)
def get_output_vid_path():
    global p2
    p2 = entry.get()
    label = tk.Label(root, text='The output file name will be: ' + p2, fg=grey_hex, font=loaded_path_font)
    label.place(x=70, y=340)


# 1. CHOOSE VIDEO
label = tk.Label(root, text="1. Choose an input video file you want to manipulate", fg=steel_pink_hex, font=text_font)
label.place(x=70, y=100)
button = tk.Button(root, text="SEARCH", command=get_input_vid_path, bg="blue", fg=sky_blue_hex, font=button_font, relief=tk.RAISED)
button.place(x=70, y=140)

# 2. WRITE OUTPUT PATH
label = tk.Label(root, text="2. write output video path:", fg=steel_pink_hex, font=text_font)
label.place(x=70, y=250)
entry = tk.Entry(root)
entry.place(x=70, y=290)
button = tk.Button(root, text="OK", command=get_output_vid_path, fg=sky_blue_hex, font=button_font,)
button.place(x=300, y=290)

# 3. APPLY TRANSFORMATION
label = tk.Label(root, text="3. Select the transformation you want to apply to the selected video:", fg=steel_pink_hex, font=text_font)
label.place(x=70, y=400)

# 3.1. TRANSFORMATION BUTTONS
def button_hist():
    functions_gui.generate_histogram(p1, p2)
    label = tk.Label(root, text='Histogram video "'+p2+'" generated!', fg=grey_hex, font=loaded_path_font)
    label.place(x=265, y=450)
def button_vectors():
    functions_gui.video_vectors(p1, p2)
    label = tk.Label(root, text='Motion-vectors video "'+p2+'" generated!', fg=grey_hex, font=loaded_path_font)
    label.place(x=335, y=510)
def button_mp3():
    functions_gui.download_mp3(p1, p2)
    label = tk.Label(root, text='Audio "'+p2+'" extracted!', fg=grey_hex, font=loaded_path_font)
    label.place(x=315, y=565)

b1 = tk.Button(root, text="HISTOGRAM", command=button_hist, fg=sky_blue_hex, font=button_font)
b1.place(x=70, y=440)

b2 = tk.Button(root, text="MOTION VECTORS", command=button_vectors, fg=sky_blue_hex, font=button_font)
b2.place(x=70, y=500)

b4 = tk.Button(root, text="DOWNLOAD MP3", command=button_mp3, fg=sky_blue_hex, font=button_font,)
b4.place(x=70, y=560)


# functions to display the video
def update_video():
    ret, frame = cap.read()
    if ret:
        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to ImageTk format
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the label with the new frame
        label_vid.imgtk = imgtk
        label_vid.configure(image=imgtk)

    # Schedule the update after 10 milliseconds
    label_vid.after(10, update_video)

def update_video_root():
    ret, frame = cap_root.read()
    if ret:
        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to ImageTk format
        img = Image.fromarray(frame_rgb)
        imgtk = ImageTk.PhotoImage(image=img)

        # Update the label with the new frame
        label_vid_root.imgtk = imgtk
        label_vid_root.configure(image=imgtk)

    # Schedule the update after 10 milliseconds
    label_vid_root.after(10, update_video_root)


# 2. BUTTON TO GET VIDEO INPUT
def reprod_input():
    global p3
    p3 = filedialog.askopenfilename()  # filedialog.askopenfilename()
    label = tk.Label(reproductor, text='You are loading the following video: \n' + p3, font=("Verdana", 12, "italic"))
    label.place(x=380, y=200)

    # I tried but this menu finally doesn't work :(
'''    global options1
    global options2
    options1 = tk.Button(reproductor, text="MODIFY VIDEO CODEC")
    options1.place(x=200, y=300)
    options2 = tk.Button(reproductor, text="MODIFY VIDEO RESOLUTION")
    options2.place(x=700, y=300)

    global dropdown_menu1
    dropdown_menu1 = tk.Menu(reproductor, tearoff=0)
    dropdown_menu1.add_command(label="VP8", command=functions_gui.convert_VP8(p3))
    dropdown_menu1.add_command(label="VP9", command=functions_gui.convert_VP9(p3))
    dropdown_menu1.add_command(label="h265", command=functions_gui.convert_h265(p3))

    global dropdown_menu2
    dropdown_menu2 = tk.Menu(reproductor, tearoff=0)
    dropdown_menu2.add_command(label="720p", command=functions_gui.convert_720p(p3))
    dropdown_menu2.add_command(label="480p", command=functions_gui.convert_480p(p3))
    dropdown_menu2.add_command(label="360x240", command=functions_gui.convert_360x240(p3))
    dropdown_menu2.add_command(label="160x120", command=functions_gui.convert_160x120(p3))

    options1.bind("<Button-1>", show_dropdown1)
    options2.bind("<Button-1>", show_dropdown2)'''


def play_video():
    global cap
    global label_vid
    cap = cv2.VideoCapture(p3)
    label_vid = tk.Label(reproductor)
    label_vid.place(x=400, y=250)
    # Start updating the video frames
    update_video()


'''def show_dropdown1(event):
    # Get the coordinates of the button to place the menu
    x, y = options1.winfo_rootx(), options1.winfo_rooty() + options1.winfo_height()
    # Display the dropdown menu at the calculated coordinates
    dropdown_menu1.post(x, y)
def show_dropdown2(event):
    # Get the coordinates of the button to place the menu
    x, y = options2.winfo_rootx(), options2.winfo_rooty() + options2.winfo_height()
    # Display the dropdown menu at the calculated coordinates
    dropdown_menu2.post(x, y)'''


# 1. NEW WINDOW OPENING: VIDEO REPRODUCTOR
def video_reprod():
    #global p3
    global reproductor
    reproductor = tk.Toplevel(root)
    reproductor.title("VIDEO REPRODUCTOR")
    reproductor.geometry("1100x600")
    reproductor.configure(bg="lightblue")

    button = tk.Button(reproductor, text="Choose input video file", command=reprod_input, font=("Verdana", 18, "bold"))
    button.place(x=420, y=140)

def play_video_root():
    global display
    display = tk.Toplevel(root)
    display.title("display")
    display.geometry("800x500")
    global cap_root
    global label_vid_root
    cap_root = cv2.VideoCapture(p2)
    label_vid_root = tk.Label(display)
    label_vid_root.place(x=0, y=0)
    # Start updating the video frames
    update_video_root()


# EXTRA BUTTONS
# OPEN VIDEO COMPARATOR WINDOW
original_image = Image.open("gui_images/video_comparator_logo.png")
resized_image = original_image.resize((400, 150))  # Adjust the size as needed
img_vid = ImageTk.PhotoImage(resized_image)
b5 = tk.Button(root, image=img_vid, command=video_reprod)
b5.place(x=700, y=150)

# EXIT CUKI BOTTON
original_image = Image.open("gui_images/exit.png")
resized_image = original_image.resize((50, 50))  # Adjust the size as needed
img_exit = ImageTk.PhotoImage(resized_image)
button_exit = tk.Button(root, image=img_exit, command=root.quit)
button_exit.place(x=1120, y=20)

# 4. SEE OUTPUT VIDEO
label = tk.Label(root, text="4. See generated video", fg=steel_pink_hex, font=text_font)
label.place(x=70, y=620)
b6 = tk.Button(root, text="View output video", command=play_video_root, fg='black', font=("Verdana", 15, "bold"))
b6.place(x=300, y=615)


def favor():
    global reproductor
    carta = tk.Toplevel(root)
    carta.title("Motivation letter")
    carta.geometry("1100x600")

    # background image
    imgcern = Image.open("gui_images/cern.jpg")
    imgcern = imgcern.resize((1200, 700), Image.LANCZOS)
    background_imgcern = ImageTk.PhotoImage(imgcern)
    canvascern = tk.Canvas(carta, width=1200, height=700)
    canvascern.pack()
    canvascern.create_image(0, 0, anchor=tk.NW, image=background_imgcern)
    canvascern.background = background_imgcern

    # letter
    cern_text = "Hola Javi, \n Espero que hayas llegado a este punto después de seguir el recorrido dentro la interfaz que he diseñado, es decir: 'X-MAS VERSION' --> pulsar la imagen del regalo. \n Si no es así y estás leyendo esto a través de la captura de pantalla, \nte acabas de hacer spoiler jeje. \n\nBueno, a lo que iba. Soy Laura Ruiz (he ido la mayoría de veces a clase pero creo que no recuerdas mi nombre porque no participo mucho activamente. \nTe quería pedir un favor, ya que eres un profesor muy cercano y me ayudarías mucho. \nEste verano me gustaría participar En el 'CERN Summer Student Programme 2024'. Este programa consiste en hacer unas prácticas en el CERN \n(European Organization for Nuclear Research), en Suiza durante los 3 meses de verano. \nBuscan ingenieros (informáticos o similares, como es mi caso de Ingeniería en \nSistemas Audiovisuales) para participar activamente en proyectos relacionados más con la parte de software, lo cual contribuye al estudio nuclear que se desarrolla en el CERN. \nAdemás de impartir formaciones juntamente con alumnos de otras partes del mundo. \nSinceramente creo que es una oportunidad increíble para aprender yponer a prueba \nlas habilidades que he aprendido a lo largo de estos 4 años, además de ganar experiencia y relacionarme \ncon gente en otro idioma en otro país.\nPara aplicar me piden 2 cartas de recomendación (motivation letters) \nen inglés, y había pensado en si me podrías hacer el favor de escribirme una.\nTe dejo mi correo (laura.ruiz17@estudiant.upf.edu) para que me comentes qué opinas.\n Te lo agradezco!!\n - Laura R."
    label = tk.Label(carta, text=cern_text, font=("Verdana", 10))
    label.place(x=50, y=150)

def xmas_button():
    message = "If your name is Javi,\n and want to give the best Christmas present \nto your student, click here!!!"
    label = tk.Label(root, text=message, fg='red', font=text_font)
    label.place(x=700, y=400)

    image_path = "gui_images/present.png"
    img = Image.open(image_path)
    img = img.resize((150, 150), Image.LANCZOS)  # Resize the image as needed
    image_button = ImageTk.PhotoImage(img)
    new_button = tk.Button(root, image=image_button, command=favor)
    new_button.image = image_button  # Keep a reference to prevent image garbage collection
    new_button.place(x=820, y=500)

show_present_button = tk.Button(root, text="X-MAS VERSION", fg="red", width=10, command=xmas_button, font=button_font)
show_present_button.place(x=900, y=30)

# end
root.mainloop()