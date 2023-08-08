import customtkinter
from PIL import Image
from customtkinter import CTkImage

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1289x831")
app.title('Create Academy Launcher')
app.iconbitmap('assets/logo.ico')

def button_event():
    print("button pressed")
size_button=70

news_label = customtkinter.CTkLabel(app, anchor=customtkinter.CENTER, text="NEWS", fg_color="transparent", font=('Arial', 30))
news = customtkinter.CTkFrame(app, width=404, height=600, corner_radius=30)
settings = customtkinter.CTkButton(app, anchor=customtkinter.CENTER, text="Settings", command=button_event, width=304, height=59, corner_radius=30, font=('Ariane', 30), fg_color="#444444", hover_color="#383838")
launch = customtkinter.CTkButton(app, anchor=customtkinter.CENTER, text="Launch", command=button_event, width=805, height=59, corner_radius=30, font=('Ariane', 30), fg_color="#2FA572", hover_color="#1C6344")
rem_check = customtkinter.CTkCheckBox(app, text="Remember Me", font=('Arial', 30), hover_color="#383838", fg_color="#444444")


photo_discord = CTkImage(light_image=Image.open("assets/discord.png"), dark_image=Image.open("assets/discord.png"),
                             size=(size_button, size_button))
photo_web = CTkImage(light_image=Image.open("assets/www.png"), dark_image=Image.open("assets/www.png"),
                             size=(size_button, size_button))
photo_map = CTkImage(light_image=Image.open("assets/map.png"), dark_image=Image.open("assets/map.png"),
                             size=(size_button, size_button))
photo_shop = CTkImage(light_image=Image.open("assets/shop.png"), dark_image=Image.open("assets/shop.png"),
                             size=(size_button, size_button))

discord = customtkinter.CTkButton(app, image=photo_discord, width=70, height=0, corner_radius=30, text='', fg_color="#242424", hover_color="#242424")
www = customtkinter.CTkButton(app, image=photo_web, width=70, height=0, corner_radius=30, text='', fg_color="#242424", hover_color="#242424")
map = customtkinter.CTkButton(app, image=photo_map, width=70, height=0, corner_radius=30, text='', fg_color="#242424", hover_color="#242424")
shop = customtkinter.CTkButton(app, image=photo_shop, width=70, height=0, corner_radius=30, text='', fg_color="#242424", hover_color="#242424")

news_label.place(x=200, y=52)
settings.place(x=100, y=732)
launch.place(x=454, y=732)
news.place(x=50, y=102)
discord.place(x=1189, y=152)
www.place(x=1189, y=52)
map.place(x=1189, y=352)
shop.place(x=1189, y=252)
rem_check.place(x=1029, y=682)




app.mainloop()