import tkinter as tk
import tkinter.font as tkFont
from playsound import playsound
import os
from PIL import Image, ImageTk
playsound(f"{os.getcwd()}//sounds//zero_sound.m4a")

class App:
    def __init__(self, root):
        #setting title
        root.title("Mr. Incredible")
        #setting window size
        width=736
        height=571
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        image1 = Image.open(f"{os.getcwd()}//pics//p8.png")
        image1 = image1.resize((130, 120), Image.ANTIALIAS)
        global reset_img1
        reset_img1 = ImageTk.PhotoImage(image1)
        GButton_836=tk.Button(root, image=reset_img1)
        GButton_836["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_836["font"] = ft
        GButton_836["fg"] = "#000000"
        GButton_836["justify"] = "center"
        GButton_836["text"] = "Button1"
        GButton_836.place(x=50,y=40,width=130,height=120)
        GButton_836["command"] = self.GButton_836_command

        image2 = Image.open(f"{os.getcwd()}//pics//p6.png")
        image2 = image2.resize((130, 120), Image.ANTIALIAS)
        global reset_img2
        reset_img2 = ImageTk.PhotoImage(image2)

        GButton_588=tk.Button(root, image=reset_img2)
        GButton_588["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_588["font"] = ft
        GButton_588["fg"] = "#000000"
        GButton_588["justify"] = "center"
        GButton_588["text"] = "Button2"
        GButton_588.place(x=390,y=40,width=130,height=120)
        GButton_588["command"] = self.GButton_588_command

        image3 = Image.open(f"{os.getcwd()}//pics//p5.png")
        image3 = image3.resize((130, 120), Image.ANTIALIAS)
        global reset_img3
        reset_img3 = ImageTk.PhotoImage(image3)

        GButton_271=tk.Button(root, image=reset_img3)
        GButton_271["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_271["font"] = ft
        GButton_271["fg"] = "#000000"
        GButton_271["justify"] = "center"
        GButton_271["text"] = "Button3"
        GButton_271.place(x=560,y=40,width=130,height=120)
        GButton_271["command"] = self.GButton_271_command

        image4 = Image.open(f"{os.getcwd()}//pics//p4.png")
        image4 = image4.resize((130, 120), Image.ANTIALIAS)
        global reset_img4
        reset_img4 = ImageTk.PhotoImage(image4)

        GButton_389=tk.Button(root, image=reset_img4)
        GButton_389["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_389["font"] = ft
        GButton_389["fg"] = "#000000"
        GButton_389["justify"] = "center"
        GButton_389["text"] = "Button4"
        GButton_389.place(x=50,y=170,width=130,height=120)
        GButton_389["command"] = self.GButton_389_command

        image5 = Image.open(f"{os.getcwd()}//pics//zero.jpeg")
        image5 = image5.resize((130, 120), Image.ANTIALIAS)
        global reset_img5
        reset_img5 = ImageTk.PhotoImage(image5)

        GButton_21=tk.Button(root, image=reset_img5)
        GButton_21["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_21["font"] = ft
        GButton_21["fg"] = "#000000"
        GButton_21["justify"] = "center"
        GButton_21["text"] = "Button5"
        GButton_21.place(x=50,y=300,width=130,height=120)
        GButton_21["command"] = self.GButton_21_command

        image6 = Image.open(f"{os.getcwd()}//pics//p7.png")
        image6 = image6.resize((130, 120), Image.ANTIALIAS)
        global reset_img6
        reset_img6 = ImageTk.PhotoImage(image6)

        GButton_606=tk.Button(root, image=reset_img6)
        GButton_606["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_606["font"] = ft
        GButton_606["fg"] = "#000000"
        GButton_606["justify"] = "center"
        GButton_606["text"] = "Button6"
        GButton_606.place(x=220,y=40,width=130,height=120)
        GButton_606["command"] = self.GButton_606_command

        image7 = Image.open(f"{os.getcwd()}//pics//m4.jpeg")
        image7 = image7.resize((130, 120), Image.ANTIALIAS)
        global reset_img7
        reset_img7 = ImageTk.PhotoImage(image7)

        GButton_71=tk.Button(root, image=reset_img7)
        GButton_71["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_71["font"] = ft
        GButton_71["fg"] = "#000000"
        GButton_71["justify"] = "center"
        GButton_71["text"] = "Button7"
        GButton_71.place(x=50,y=430,width=130,height=120)
        GButton_71["command"] = self.GButton_71_command

        image8 = Image.open(f"{os.getcwd()}//pics//p3.png")
        image8 = image8.resize((130, 120), Image.ANTIALIAS)
        global reset_img8
        reset_img8 = ImageTk.PhotoImage(image8)

        GButton_873=tk.Button(root, image=reset_img8)
        GButton_873["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_873["font"] = ft
        GButton_873["fg"] = "#000000"
        GButton_873["justify"] = "center"
        GButton_873["text"] = "Button8"
        GButton_873.place(x=220,y=170,width=130,height=120)
        GButton_873["command"] = self.GButton_873_command

        image9 = Image.open(f"{os.getcwd()}//pics//p2.png")
        image9 = image9.resize((130, 120), Image.ANTIALIAS)
        global reset_img9
        reset_img9 = ImageTk.PhotoImage(image9)

        GButton_73=tk.Button(root, image=reset_img9)
        GButton_73["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_73["font"] = ft
        GButton_73["fg"] = "#000000"
        GButton_73["justify"] = "center"
        GButton_73["text"] = "Button9"
        GButton_73.place(x=390,y=170,width=130,height=120)
        GButton_73["command"] = self.GButton_73_command

        image10 = Image.open(f"{os.getcwd()}//pics//p1.png")
        image10 = image10.resize((130, 120), Image.ANTIALIAS)
        global reset_img10
        reset_img10 = ImageTk.PhotoImage(image10)

        GButton_890=tk.Button(root, image=reset_img10)
        GButton_890["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_890["font"] = ft
        GButton_890["fg"] = "#000000"
        GButton_890["justify"] = "center"
        GButton_890["text"] = "Button10"
        GButton_890.place(x=560,y=170,width=130,height=120)
        GButton_890["command"] = self.GButton_890_command

        image11 = Image.open(f"{os.getcwd()}//pics//m1.jpeg")
        image11 = image11.resize((130, 120), Image.ANTIALIAS)
        global reset_img11
        reset_img11 = ImageTk.PhotoImage(image11)

        GButton_524=tk.Button(root, image=reset_img11)
        GButton_524["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_524["font"] = ft
        GButton_524["fg"] = "#000000"
        GButton_524["justify"] = "center"
        GButton_524["text"] = "Button11"
        GButton_524.place(x=220,y=300,width=130,height=120)
        GButton_524["command"] = self.GButton_524_command

        image12 = Image.open(f"{os.getcwd()}//pics//m2.jpeg")
        image12 = image12.resize((130, 120), Image.ANTIALIAS)
        global reset_img12
        reset_img12 = ImageTk.PhotoImage(image12)

        GButton_557=tk.Button(root, image=reset_img12)
        GButton_557["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_557["font"] = ft
        GButton_557["fg"] = "#000000"
        GButton_557["justify"] = "center"
        GButton_557["text"] = "Button12"
        GButton_557.place(x=390,y=300,width=130,height=120)
        GButton_557["command"] = self.GButton_557_command

        image13 = Image.open(f"{os.getcwd()}//pics//m3.jpeg")
        image13 = image13.resize((130, 120), Image.ANTIALIAS)
        global reset_img13
        reset_img13 = ImageTk.PhotoImage(image13)

        GButton_407=tk.Button(root, image=reset_img13)
        GButton_407["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_407["font"] = ft
        GButton_407["fg"] = "#000000"
        GButton_407["justify"] = "center"
        GButton_407["text"] = "Button13"
        GButton_407.place(x=560,y=300,width=130,height=120)
        GButton_407["command"] = self.GButton_407_command

        image14 = Image.open(f"{os.getcwd()}//pics//m5.jpeg")
        image14 = image14.resize((130, 120), Image.ANTIALIAS)
        global reset_img14
        reset_img14 = ImageTk.PhotoImage(image14)

        GButton_259=tk.Button(root, image=reset_img14)
        GButton_259["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_259["font"] = ft
        GButton_259["fg"] = "#000000"
        GButton_259["justify"] = "center"
        GButton_259["text"] = "Button14"
        GButton_259.place(x=220,y=430,width=130,height=120)
        GButton_259["command"] = self.GButton_259_command

        image15 = Image.open(f"{os.getcwd()}//pics//m6.jpeg")
        image15 = image15.resize((130, 120), Image.ANTIALIAS)
        global reset_img15
        reset_img15 = ImageTk.PhotoImage(image15)

        GButton_957=tk.Button(root, image=reset_img15)
        GButton_957["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_957["font"] = ft
        GButton_957["fg"] = "#000000"
        GButton_957["justify"] = "center"
        GButton_957["text"] = "Button15"
        GButton_957.place(x=390,y=430,width=130,height=120)
        GButton_957["command"] = self.GButton_957_command

        image16 = Image.open(f"{os.getcwd()}//pics//m7.jpeg")
        image16 = image16.resize((130, 120), Image.ANTIALIAS)
        global reset_img16
        reset_img16 = ImageTk.PhotoImage(image16)

        GButton_409=tk.Button(root, image=reset_img16)
        GButton_409["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_409["font"] = ft
        GButton_409["fg"] = "#000000"
        GButton_409["justify"] = "center"
        GButton_409["text"] = "Button16"
        GButton_409.place(x=560,y=430,width=130,height=120)
        GButton_409["command"] = self.GButton_409_command

    def GButton_836_command(self):
        playsound(f"{os.getcwd()}//sounds//p8_sound.m4a")

    def GButton_588_command(self):
        playsound(f"{os.getcwd()}//sounds//p6_sound.m4a")

    def GButton_271_command(self):
        playsound(f"{os.getcwd()}//sounds//p5_sound.m4a")

    def GButton_389_command(self):
        playsound(f"{os.getcwd()}//sounds//p4_sound.m4a")

    def GButton_21_command(self):
        playsound(f"{os.getcwd()}//sounds//zero_sound.m4a")

    def GButton_606_command(self):
        playsound(f"{os.getcwd()}//sounds//p7_sound.m4a")

    def GButton_71_command(self):
        playsound(f"{os.getcwd()}//sounds//m4_sound.m4a")

    def GButton_873_command(self):
        playsound(f"{os.getcwd()}//sounds//p3_sound.m4a")

    def GButton_73_command(self):
        playsound(f"{os.getcwd()}//sounds//p2_sound.m4a")

    def GButton_890_command(self):
        playsound(f"{os.getcwd()}//sounds//p1_sound.m4a")

    def GButton_524_command(self):
        playsound(f"{os.getcwd()}//sounds//m1_sound.m4a")

    def GButton_557_command(self):
        playsound(f"{os.getcwd()}//sounds//m2_sound.m4a")

    def GButton_407_command(self):
        playsound(f"{os.getcwd()}//sounds//m3_sound.m4a")

    def GButton_259_command(self):
        playsound(f"{os.getcwd()}//sounds//m5_sound.m4a")

    def GButton_957_command(self):
        playsound(f"{os.getcwd()}//sounds//m6_sound.m4a")

    def GButton_409_command(self):
        playsound(f"{os.getcwd()}//sounds//m7_sound.m4a")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
