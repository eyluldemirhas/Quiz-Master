
import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap import style
from ttkbootstrap.constants import *
from tkinter import messagebox, mainloop
import threading
import ttkbootstrap.localization
import random
from random import shuffle
ttkbootstrap.localization.initialize_localities = bool
from sorular import sorular #soruları bu yazacağımız kodlara çektik
from  loginscreen import show_login_screen



timer_id = None
time_left=20

show_login_screen()
ttkbootstrap.Style.instance = None #Bu kodu ikinci penceredeki stil kodlarımın çalışması için yazdım

# Zamanlayıcıyı güncelleyen fonksiyon
def update_timer():
    global time_left
    global timer_id

    if time_left > 0:
        timer_label.config(text=f"Kalan Süre: {time_left} sn")
        time_left -= 1
        timer_id = root.after(1000, update_timer)
    else:
        # Süre dolduysa otomatik olarak yanlış kabul et
        feedback_label.config(text="Süre doldu! Yanlış cevap.", foreground="red")
        next_btn.config(state="normal")

# Zamanlayıcıyı durduran fonksiyon
def stop_timer():
    global timer_id
    if timer_id is not None:
        root.after_cancel(timer_id)
        timer_id = None

# Soruları gösteren fonksiyon
def show_question():
    """Soruyu ve seçenekleri düğmelere yükler."""
    question = sorular[current_qs]
    qs_label.config(text=question["soru"])  # Soruyu göster
    global time_left

    stop_timer()  # Önceki zamanlayıcıyı durdur
    time_left = 20  # Süreyi sıfırla



# Şıkları güncelle
    choices = question["sıklar"]
    for i in range(4):
        choice_button[i].config(text=choices[i], state="normal")


 # Geri bildirimi temizle
    feedback_label.config(text="")
    next_btn.config(state="disabled")

    # Zamanlayıcıyı başlat
    update_timer()

#Cevabı Kontrol eden fonksiyon

def check_answer(choice):
    question = sorular[current_qs]
    selected_choice = choice_button[choice].cget("text")

    #Cevap Eşleşiyor mu Kontrol et
    if selected_choice == question["cevap"]:
        global score
        score += 1
        score_label.config(text="Skorunuz: {}/{}".format(score, len(sorular)))
        feedback_label.config(text="Doğru!", foreground="green")

    else:
        feedback_label.config(text="Yanlış!", foreground="red")


    #Yeni soru butonunu aktif etme
    for button in choice_button:
        button.config(state="disabled")
    next_btn.config(state="normal")


#yeni soruya geçiren fonksiyon
def next_qs():
    global current_qs

    current_qs += 1

    if current_qs < len(sorular):
        show_question()

    else:
        #eğer tüm sorular bittiyse final sonuç skorunu göster
        messagebox.showinfo("Quiz Tamamlandı",
                            "Quiz Tamamlandı! Skorunuz : {}/{}".format(score,len(sorular)))
        root.destroy()

#soruların rastgele gelmesi için
random.shuffle(sorular)


#Ana pencereyi olusturuyoruz
root=ttk.Window(themename="lumen")
#root = tk.Tk()
# root.configure(background="#f0f8ff")  # Açık mavi bir arka plan
root.title("Quiz Master")
root.geometry("600x550")




#font düzenlemesi
root.style.configure(".", font=('Bahnschrift SemiBold', 16))

#Soru alanları
qs_label = ttk.Label(
    root,
    style="Custom.TLabel",
    anchor="center",
    wraplength=500,
    padding=10,
    # bootstyle = "dark",

)
qs_label.pack(pady=10)

#Seçenek Butonları
choice_button = []
for i in range(4):
    button = ttk.Button(
        root,

        command=lambda i=i: check_answer(i),
        bootstyle="outline-danger",

    )
    button.pack(pady=8)
    choice_button.append(button)

#Doğru Yanlış Olduğunu söyleyen geri dönüt

feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

score=0

#Skoru Gösteren Kısım
score_label = ttk.Label(
    root,
    text="Skorunuz:0/{}".format(len(sorular)),
    anchor="center",
    padding=10
)
score_label.pack()

# Zamanlayıcı Alanı
timer_label = ttk.Label(
    root,
    text="Kalan Süre: 20 sn",
    anchor="center",
    padding=8,
    font=("Helvetica", 14))
timer_label.pack()

#yeni soruya geçme butonu

next_btn = ttk.Button(
    root,
    text="Yeni Soru",
    command = next_qs,
    state="disabled"

)

next_btn.pack(pady=15)

#soru dizinini başlat
current_qs = 0

#İlk Soruyu Göster
show_question(

)

root.mainloop()

