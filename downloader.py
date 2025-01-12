import tkinter as tk
from tkinter import messagebox, ttk
import subprocess


programas = [
    ("Google Chrome", "winget install --id Google.Chrome"),
    ("Java", "winget install --id Oracle.Java"),
    ("PowerShell", "winget install --id Microsoft.PowerShell"),
    ("Adobe Reader", "winget install --id Adobe.Acrobat.Reader.32-bit"),
    ("Microsoft Office", "winget install --id Microsoft.Office"),
    ("WinRAR", "winget install --id RARLab.WinRAR"),
    ("AnyDesk", "winget install --id AnyDesk.AnyDesk"),
    ("Steam", "winget install --id Valve.Steam"),
    ("VsCode", "winget install --id Microsoft.Visualstudiocode"),
    ("OperaGx", "winget install --id Opera.Operagx"),
    ("Telegram", "winget install --id Telegram.Telegramdesktop"),
    ("Power BI", "winget install --id Microsoft.Powerbi"),
    ("CPU-Z", "winget install --id Cpuid.Cpu-z")
    
]


def instalar_programas():
    selecionados = [programa for programa, var in checkboxes.items() if var.get()]
    
    if not selecionados:
        messagebox.showwarning("Aviso", "Selecione ao menos um programa!")
        return

    
    barra_progresso["maximum"] = len(selecionados)
    barra_progresso["value"] = 0
    log_text.delete(1.0, tk.END)  
    
    for programa in selecionados:
        nome, comando = programa
        try:
            log_text.insert(tk.END, f"Iniciando instalação de {nome}...\n")
            log_text.see(tk.END)
            janela.update()

            
            subprocess.run(comando, shell=True, check=True)
            log_text.insert(tk.END, f"{nome} instalado com sucesso!\n")
        except subprocess.CalledProcessError as e:
            log_text.insert(tk.END, f"Erro ao instalar {nome}: {e}\n")
        finally:
            barra_progresso["value"] += 1
            janela.update_idletasks()

    messagebox.showinfo("Conclusão", "Todos os programas selecionados foram instalados.")


janela = tk.Tk()
janela.title("Instalador de Programas")
janela.geometry("400x600")
janela.config(bg="#8e3b4e")  

frame = tk.Frame(janela, bg="#8e3b4e")
frame.pack(pady=10, fill=tk.BOTH, expand=True)


checkboxes = {}
for nome, comando in programas:
    var = tk.BooleanVar()
    checkboxes[(nome, comando)] = var

   
    linha = tk.Frame(frame, bg="#8e3b4e")
    linha.pack(anchor="w", pady=5)

    
    tk.Checkbutton(linha, text=nome, variable=var, font=("Arial", 12), fg="#f4f4f4", bg="#8e3b4e", selectcolor="#001f3d").pack(side="left", padx=5)


btn_instalar = tk.Button(janela, text="Instalar", command=instalar_programas, font=("Arial", 12), bg="#001f3d", fg="white", relief="solid", padx=10, pady=5)
btn_instalar.pack(pady=10)


barra_progresso = ttk.Progressbar(janela, length=400, mode="determinate", style="TProgressbar")
barra_progresso.pack(pady=20)


log_frame = tk.Frame(janela, bg="#2e3b4e")
log_frame.pack(fill=tk.BOTH, expand=True, pady=10)

log_text = tk.Text(log_frame, wrap=tk.WORD, height=10, font=("Courier", 10), fg="white", bg="#001f3d")
log_text.pack(fill=tk.BOTH, expand=True)


style = ttk.Style()
style.configure("TProgressbar",
                thickness=20,
                barcolor="#8CAF50",  
                background="#555555")  

janela.mainloop()