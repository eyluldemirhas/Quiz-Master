import ttkbootstrap as ttk

#Oyuna Başlamadan Önce ki Giriş Ekranı

def show_login_screen():

    login_screen = ttk.Window(themename="lumen")
    login_screen.title("Quiz Master")
    login_screen.geometry("500x300")

    def start_game():

        login_screen.destroy()

    # Mesaj ve Başla Butonu
    welcome_label = ttk.Label(
        login_screen,
        text="Quiz Master'a Hoş Geldiniz!",
        anchor="center",
        # font=("Helvetica", 18)
    )
    login_screen.style.configure(".", font=('Bahnschrift SemiBold', 20))
    welcome_label.pack(pady=30)

    start_button = ttk.Button(
        login_screen,
        text="Oyna",
        command=start_game,
        bootstyle="outline-danger",
        padding="20,10",

    )
    start_button.pack(pady=20)

    login_screen.mainloop()  # Giriş ekranını çalıştır

