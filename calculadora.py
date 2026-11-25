import tkinter as tk

# Guardando os dados na calculadora
dados = {"numero1": 0, "operacao": "", "fim": False}

def digitar(numero):
    if dados["fim"]:
        lbl_mensagem.config(text="Pressione C para iniciar um novo cálculo.")
        return
    lbl_mensagem.config(text="")
    visor.insert(tk.END, numero)

def digitar_ponto():
    if dados["fim"]:
        lbl_mensagem.config(text="Pressione C para iniciar um novo cálculo.")
        return
    
    texto = visor.get()

    # Impedindo que existam dois pontos simultaneamente.
    if "." in texto:
        lbl_mensagem.config(text="O número já tem ponto.")
        return

    lbl_mensagem.config(text="")
    if texto == "":
        visor.insert(tk.END, "0.")
    else:
        visor.insert(tk.END, ".")

# Apagando o último número da operação
def apagar():
    if dados["fim"]:
        lbl_mensagem.config(text="Pressione C para iniciar um novo cálculo.")
        return
    texto = visor.get()
    if texto != "":
        visor.delete(len(texto) - 1, tk.END)

# Limpando tudo dentro do visor e reiniciando os valores
def limpar():
    visor.delete(0, tk.END)
    dados["numero1"] = 0
    dados["operacao"] = ""
    dados["fim"] = False
    lbl_mensagem.config(text="")

# Impedindo que a conta seja realizada sem o operador
def escolher_operacao(simbolo):
    if dados["fim"]:
        lbl_mensagem.config(text="Pressione C para um novo cálculo.")
        return

    texto = visor.get()

    if texto == "":
        lbl_mensagem.config(text="Digite um número antes de finalizar a operação.")
        return

    if dados["operacao"] != "":
        lbl_mensagem.config(text="Pressione = ou C.")
        return

    # Guardando o primeiro número e a operação
    dados["numero1"] = float(texto)
    dados["operacao"] = simbolo
    visor.delete(0, tk.END)
    lbl_mensagem.config(text="")

def calcular():
    if dados["fim"]:
        lbl_mensagem.config(text="Pressione C para iniciar um novo cálculo.")
        return

    texto = visor.get()

    # Evitando que o programa quebre caso não possua informações.
    if dados["operacao"] == "" or texto == "":
        lbl_mensagem.config(text="Informe os dois números e a operação.")
        return

    numero1 = dados["numero1"]
    numero2 = float(texto)
    operacao = dados["operacao"]

    if operacao == "+":
        resultado = numero1 + numero2
    elif operacao == "-":
        resultado = numero1 - numero2
    elif operacao == "×":
        resultado = numero1 * numero2
    else:
        if numero2 == 0:
            lbl_mensagem.config(text="Não é possível dividir por zero.")
            return
        resultado = numero1 / numero2

    # Arredondando para evitar excesso de zeros após o . e resultados como 10.0
    resultado = round(resultado, 10)
    if resultado == int(resultado):
        resultado = int(resultado)

    visor.delete(0, tk.END)
    visor.insert(tk.END, str(resultado))
    lbl_mensagem.config(text="")
    dados["fim"] = True

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora")

# Criando o visor e suas medidas
visor = tk.Entry(janela, width=16, justify="right", font=("Arial", 20))
visor.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Definindo parâmetros das mensagens de erro
lbl_mensagem = tk.Label(janela, text="", fg="red")
lbl_mensagem.grid(row=1, column=0, columnspan=4)

# Inserindo os botões
botao_c = tk.Button(janela, text="C", width=8, height=3, command=limpar)
botao_c.grid(row=2, column=0, padx=2, pady=2)

botao_apagar = tk.Button(janela, text="⌫", width=8, height=3, command=apagar)
botao_apagar.grid(row=2, column=1, padx=2, pady=2)

botao_dividir = tk.Button(janela, text="÷", width=8, height=3, command=lambda: escolher_operacao("÷"))
botao_dividir.grid(row=2, column=2, padx=2, pady=2)

botao_multiplicar = tk.Button(janela, text="×", width=8, height=3, command=lambda: escolher_operacao("×"))
botao_multiplicar.grid(row=2, column=3, padx=2, pady=2)

botao_7 = tk.Button(janela, text="7", width=8, height=3, command=lambda: digitar("7"))
botao_7.grid(row=3, column=0, padx=2, pady=2)

botao_8 = tk.Button(janela, text="8", width=8, height=3, command=lambda: digitar("8"))
botao_8.grid(row=3, column=1, padx=2, pady=2)

botao_9 = tk.Button(janela, text="9", width=8, height=3, command=lambda: digitar("9"))
botao_9.grid(row=3, column=2, padx=2, pady=2)

botao_subtrair = tk.Button(janela, text="-", width=8, height=3, command=lambda: escolher_operacao("-"))
botao_subtrair.grid(row=3, column=3, padx=2, pady=2)

botao_4 = tk.Button(janela, text="4", width=8, height=3, command=lambda: digitar("4"))
botao_4.grid(row=4, column=0, padx=2, pady=2)

botao_5 = tk.Button(janela, text="5", width=8, height=3, command=lambda: digitar("5"))
botao_5.grid(row=4, column=1, padx=2, pady=2)

botao_6 = tk.Button(janela, text="6", width=8, height=3, command=lambda: digitar("6"))
botao_6.grid(row=4, column=2, padx=2, pady=2)

botao_somar = tk.Button(janela, text="+", width=8, height=3, command=lambda: escolher_operacao("+"))
botao_somar.grid(row=4, column=3, padx=2, pady=2)

botao_1 = tk.Button(janela, text="1", width=8, height=3, command=lambda: digitar("1"))
botao_1.grid(row=5, column=0, padx=2, pady=2)

botao_2 = tk.Button(janela, text="2", width=8, height=3, command=lambda: digitar("2"))
botao_2.grid(row=5, column=1, padx=2, pady=2)

botao_3 = tk.Button(janela, text="3", width=8, height=3, command=lambda: digitar("3"))
botao_3.grid(row=5, column=2, padx=2, pady=2)

botao_igual = tk.Button(janela, text="=", width=8, height=3, command=calcular)
botao_igual.grid(row=5, column=3, rowspan=2, padx=2, pady=2, sticky="nsew")

botao_0 = tk.Button(janela, text="0", width=8, height=3, command=lambda: digitar("0"))
botao_0.grid(row=6, column=0, columnspan=2, padx=2, pady=2, sticky="nsew")

botao_ponto = tk.Button(janela, text=".", width=8, height=3, command=digitar_ponto)
botao_ponto.grid(row=6, column=2, padx=2, pady=2)

janela.mainloop()