import customtkinter
import tkinter
from revisar_cliente import check_cliente
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry(f'{1360}x{768}')
app.title('Revisar Clientes')

def button_callback():
    try:
        print("Verificando", entry_1.get())
        total = check_cliente(ip=entry_1.get())
        dialog = customtkinter.CTkToplevel()
        dialog.geometry('1280x720')
        dialog.title("resultado")

        frame_2 = customtkinter.CTkFrame(master=dialog)
        frame_2.pack(pady=20,padx=20,fill="both",expand=True)

        textbox = customtkinter.CTkTextbox(master=frame_2, width=400,height=720)
        textbox.pack(pady=10, padx=10)
        textbox.insert("0.0", f"{total}")
    except:
        return 'Ocurrio un error'

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.CENTER,text="Ingresa la IP")
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Ingresar la IP")
entry_1.pack(pady=10, padx=10)

button_1 = customtkinter.CTkButton(text='VERIFICAR',master=frame_1, command=button_callback)
button_1.pack(pady=10, padx=10)

app.mainloop()