#RPG D&D
#Eduardo Costa Vieira

import tkinter as tk
from tkinter import ttk, messagebox
import random

BG = "#1e1e1e"
PANEL = "#2b2b2b"
FG = "#f0f0f0"

class Personagem:
    def __init__(self, nome, raca, classe):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.nivel = 1
        self.xp = 0
        self.hp_max = 100
        self.hp = 100
        self.moedas = 50
        self.ataque = 10
        self.local = "Neverwinter"
        self.inventario = ["Poção de Cura"]

class RPGApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG D&D")
        self.root.geometry("1000x650")
        self.root.configure(bg=BG)
        self.jogador = None
        self.tela_inicial()

    def limpar(self):
        for w in self.root.winfo_children():
            w.destroy()

    def adicionar_rodape(self):
        tk.Label(self.root,text="Aluno: Eduardo Costa Vieira",
                 bg=BG,fg="gray80").place(relx=0.99,rely=0.99,anchor="se")

    def tela_inicial(self):
        self.limpar()

        caixa = tk.Frame(self.root,bg=PANEL,bd=2,relief="ridge")
        caixa.place(relx=0.5,rely=0.55,anchor="center")

        tk.Label(caixa,text="RPG D&D",
                 font=("Arial",36,"bold"),
                 fg="red",bg=PANEL).pack(pady=(30,20),padx=40)

        tk.Button(caixa,text="Novo Jogo",width=25,
                  command=self.tela_criacao).pack(pady=8)
        tk.Button(caixa,text="Carregar",width=25,
                  command=self.carregar).pack(pady=8)
        tk.Button(caixa,text="Sair",width=25,
                  command=self.root.destroy).pack(pady=(8,20))

        self.adicionar_rodape()

    def tela_criacao(self):
        self.limpar()

        frame=tk.Frame(self.root,bg=PANEL,bd=2,relief="ridge")
        frame.place(relx=0.5,rely=0.55,anchor="center")

        tk.Label(frame,text="Criar Personagem",
                 font=("Arial",24,"bold"),bg=PANEL,fg="red").pack(pady=(25,15))

        nome=tk.Entry(frame,width=30); raca=tk.Entry(frame,width=30); classe=tk.Entry(frame,width=30)

        tk.Label(frame,text="Nome",bg=PANEL,fg=FG).pack(); nome.pack()
        tk.Label(frame,text="Raça",bg=PANEL,fg=FG).pack(); raca.pack()
        tk.Label(frame,text="Classe",bg=PANEL,fg=FG).pack(); classe.pack()

        def criar():
            self.jogador=Personagem(nome.get(),raca.get(),classe.get())
            self.tela_principal()

        tk.Button(frame,text="Iniciar Aventura",command=criar).pack(pady=10)
        tk.Button(frame,text="Voltar ao Menu Principal",
                  command=self.tela_inicial).pack()

    def tela_principal(self):
        self.limpar()

        moldura = tk.Frame(self.root,bg="red",bd=4)
        moldura.pack(fill="both",expand=True,padx=10,pady=10)

        painel = tk.Frame(moldura,bg=BG)
        painel.pack(fill="both",expand=True,padx=3,pady=3)

        esquerda=tk.Frame(painel,bg=PANEL)
        esquerda.pack(side="left",fill="y",padx=10,pady=10)

        tk.Label(esquerda,text="HP (Vida)",bg=PANEL,fg="white").pack()
        self.hp_bar=ttk.Progressbar(esquerda,length=220)
        self.hp_bar.pack(pady=4)

        tk.Label(esquerda,text="XP (Experiência)",bg=PANEL,fg="white").pack()
        self.xp_bar=ttk.Progressbar(esquerda,length=220)
        self.xp_bar.pack(pady=4)

        grupos = [
            ("AÇÕES",[("Combater",self.combate),("Abrir Baú",self.bau)]),
            ("LOJA E ITENS",[("Loja",self.loja),("Inventário",self.inventario),("Mapa",self.mapa)]),
            ("SISTEMA",[("Salvar",self.salvar),("Menu Principal",self.tela_inicial)])
        ]

        for titulo,bts in grupos:
            tk.Label(esquerda,text=titulo,bg=PANEL,fg="gold").pack(pady=(10,2))
            for txt,cmd in bts:
                tk.Button(esquerda,text=txt,width=20,command=cmd).pack(pady=2)

        self.log=tk.Text(painel,bg="#101010",fg="#00ff88")
        self.log.pack(side="right",fill="both",expand=True)

        self.atualizar()

    def atualizar(self):
        self.hp_bar["maximum"]=self.jogador.hp_max
        self.hp_bar["value"]=self.jogador.hp
        self.xp_bar["maximum"]=50*self.jogador.nivel
        self.xp_bar["value"]=self.jogador.xp

    def escrever(self,t):
        self.log.insert("end",t+"\n\n")
        self.log.see("end")


    def combate(self):
        criatura = random.choice(["Goblin","Orc","Esqueleto","Lobo Sombrio","Bandido"])
        acao = messagebox.askyesnocancel("Combate",f"Ah, você encontrou um {criatura}! O que você faz?\n\nSim=Atacar | Não=Defender | Cancelar=Usar Poção")

        if acao is True:
            dano=self.jogador.ataque+random.randint(1,6)
            self.jogador.xp+=25
            self.escrever(f"Você atacou e causou {dano} de dano.")
        elif acao is False:
            self.escrever("Você entrou em posição de defesa.")
        else:
            if "Poção de Cura" in self.jogador.inventario:
                self.jogador.hp=min(self.jogador.hp_max,self.jogador.hp+30)
                self.jogador.inventario.remove("Poção de Cura")
                self.escrever("Poção utilizada.")
            else:
                self.escrever("Você não possui poções.")
        self.atualizar()

    def bau(self):
        premio=random.choice([50,100,"Poção de Cura"])
        if isinstance(premio,int):
            self.jogador.moedas+=premio
        else:
            self.jogador.inventario.append(premio)
        self.escrever(f"Baú aberto. Recompensa: {premio}")

    def loja(self):
        escolha=messagebox.askyesno("Loja","Sim=Comprar Poção | Não=Vender Poção")
        if escolha:
            if self.jogador.moedas>=20:
                self.jogador.moedas-=20
                self.jogador.inventario.append("Poção de Cura")
                self.escrever("Poção comprada.")
        else:
            if "Poção de Cura" in self.jogador.inventario:
                self.jogador.inventario.remove("Poção de Cura")
                self.jogador.moedas+=10
                self.escrever("Poção vendida.")
        self.atualizar()

    def inventario(self):
        contagem = {}
        for item in self.jogador.inventario:
            contagem[item] = contagem.get(item, 0) + 1

        if not contagem:
            self.escrever("Inventário vazio.")
            return

        texto = "\n".join(f"{qtd}x {item}" for item, qtd in contagem.items())
        self.escrever("===== INVENTÁRIO =====\n" + texto)

    def mapa(self):
        locais=["Neverwinter","Floresta Sombria","Montanha dos Orcs"]
        janela=tk.Toplevel(self.root)
        janela.title("Mapa")
        tk.Label(janela,text="Escolha um destino").pack()
        for local in locais:
            tk.Button(janela,text=local,
                      command=lambda l=local:self.escolher_local(l,janela)).pack(fill="x")

    def escolher_local(self,local,janela):
        self.jogador.local=local
        self.escrever(f"Você viajou para {local}.")
        janela.destroy()

    def salvar(self):
        self.escrever("Jogo salvo com sucesso.")

    def carregar(self):
        messagebox.showinfo("Carregar","Função disponível.")

root=tk.Tk()
RPGApp(root)
root.mainloop()
