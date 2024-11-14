import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import barcode
from barcode.writer import ImageWriter
import io

# Função para gerar o código de barras
def gerar_codigo_barras():
    texto = entrada_texto.get()
    if not texto:
        messagebox.showwarning("Entrada inválida", "Digite algum texto para gerar o código de barras.")
        return
    
    try:
        # Gera o código de barras como imagem
        cod_barras = barcode.get('code128', texto, writer=ImageWriter())
        buffer = io.BytesIO()
        cod_barras.write(buffer)
        
        # Converte a imagem para exibição no tkinter
        buffer.seek(0)
        imagem = Image.open(buffer)
        imagem_tk = ImageTk.PhotoImage(imagem)
        
        # Atualiza a exibição da imagem
        label_imagem.config(image=imagem_tk)
        label_imagem.image = imagem_tk
        
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível gerar o código de barras: {e}")

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Gerador de Código de Barras")
janela.configure(bg="#e0f7fa")

# Estilos
estilo_botao = {"font": ("Helvetica", 12, "bold"), "bg": "#00695c", "fg": "white"}
estilo_label = {"font": ("Helvetica", 12), "bg": "#e0f7fa", "fg": "#00695c"}

# Campo de entrada de texto
label_texto = tk.Label(janela, text="Digite o texto para o código de barras:", **estilo_label)
label_texto.pack(pady=10)
entrada_texto = ttk.Entry(janela, width=40, font=("Helvetica", 12))
entrada_texto.pack(pady=5)

# Botão para gerar o código de barras
botao_gerar = tk.Button(janela, text="Gerar Código de Barras", command=gerar_codigo_barras, **estilo_botao)
botao_gerar.pack(pady=15)

# Label para exibir o código de barras gerado
label_imagem = tk.Label(janela, bg="#e0f7fa")
label_imagem.pack(pady=10)

# Inicia a aplicação
janela.mainloop()
