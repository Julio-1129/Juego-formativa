import tkinter as tk
from tkinter import messagebox, ttk
import random

class Personaje:
    def __init__(self, vida, ataque, defensa, nombre):
        self._vida = vida
        self._ataque = ataque
        self._defensa = defensa
        self.nombre = nombre
        self.nombre_clase = "Personaje"
    
    @property
    def vida(self):
        return self._vida
    
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self._vida = 0
        elif valor > 100:
            self._vida = 100
        else:
            self._vida = valor
    
    @property
    def ataque(self):
        return self._ataque
    
    @ataque.setter
    def ataque(self, valor):
        self._ataque = valor
    
    @property
    def defensa(self):
        return self._defensa
    
    @defensa.setter
    def defensa(self, valor):
        self._defensa = valor
    
    def atacar(self, objetivo):
        # Método base que será sobrescrito por las subclases
        danio = max(0, self.ataque - objetivo.defensa)
        objetivo.vida -= danio
        return f"{self.nombre} ataca a {objetivo.nombre} causando {danio} de daño."
    
    def esta_vivo(self):
        return self.vida > 0
    
    def __str__(self):
        return f"{self.nombre} ({self.nombre_clase}) - Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa}"

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(100, 50, 60, nombre)  # Estadísticas actualizadas
        self.nombre_clase = "Guerrero"
    
    def atacar(self, objetivo):
        # Guerrero: 20% más de daño
        danio_base = max(0, self.ataque - objetivo.defensa)
        danio = int(danio_base * 1.2)
        objetivo.vida -= danio
        return f"{self.nombre} (Guerrero) golpea con fuerza bruta a {objetivo.nombre} causando {danio} de daño."

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(60, 70, 30, nombre)  # Estadísticas actualizadas
        self.nombre_clase = "Mago"
    
    def atacar(self, objetivo):
        # Mago: ignora la defensa
        danio = self.ataque
        objetivo.vida -= danio
        return f"{self.nombre} (Mago) lanza un hechizo a {objetivo.nombre} causando {danio} de daño (ignora defensa)."

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(70, 50, 40, nombre)  # Estadísticas actualizadas
        self.nombre_clase = "Arquero"
    
    def atacar(self, objetivo):
        # Arquero: doble daño si ataque > defensa
        if self.ataque > objetivo.defensa:
            danio = (self.ataque - objetivo.defensa) * 2
            objetivo.vida -= danio
            return f"{self.nombre} (Arquero) dispara una flecha precisa a {objetivo.nombre} causando {danio} de daño (doble daño)."
        else:
            danio = max(0, self.ataque - objetivo.defensa)
            objetivo.vida -= danio
            return f"{self.nombre} (Arquero) dispara una flecha a {objetivo.nombre} causando {danio} de daño."

# El resto del código (clases JuegoBatalla e InterfazJuego) permanece igual...

class JuegoBatalla:
    def __init__(self):
        self.personaje1 = None
        self.personaje2 = None
        self.turno = 1
    
    def crear_personaje(self, tipo, nombre, jugador):
        if tipo == "Guerrero":
            personaje = Guerrero(nombre)
        elif tipo == "Mago":
            personaje = Mago(nombre)
        elif tipo == "Arquero":
            personaje = Arquero(nombre)
        
        if jugador == 1:
            self.personaje1 = personaje
        else:
            self.personaje2 = personaje
    
    def realizar_turno(self):
        if self.turno == 1:
            atacante = self.personaje1
            defensor = self.personaje2
        else:
            atacante = self.personaje2
            defensor = self.personaje1
        
        mensaje = atacante.atacar(defensor)
        resultado = f"{mensaje}\n{defensor.nombre} ahora tiene {defensor.vida} de vida."
        
        if not defensor.esta_vivo():
            resultado += f"\n\n¡{defensor.nombre} ha sido derrotado! ¡{atacante.nombre} gana la batalla!"
        
        self.turno = 2 if self.turno == 1 else 1
        return resultado
    
    def batalla_terminada(self):
        return not self.personaje1.esta_vivo() or not self.personaje2.esta_vivo()

class InterfazJuego:
    def __init__(self, root):
        self.root = root
        self.root.title("Batalla de Personajes")
        self.root.geometry("800x600")
        
        self.juego = JuegoBatalla()
        
        self.crear_menu_principal()
    
    def crear_menu_principal(self):
        self.limpiar_pantalla()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=50)
        
        tk.Label(self.frame, text="BATALLA DE PERSONAJES", font=("Arial", 20)).pack(pady=20)
        
        # Jugador 1
        frame_jugador1 = tk.Frame(self.frame)
        frame_jugador1.pack(pady=10)
        
        tk.Label(frame_jugador1, text="Jugador 1:", font=("Arial", 12)).pack(side=tk.LEFT)
        
        self.tipo_jugador1 = tk.StringVar(value="Guerrero")
        opciones = ["Guerrero", "Mago", "Arquero"]
        tk.OptionMenu(frame_jugador1, self.tipo_jugador1, *opciones).pack(side=tk.LEFT, padx=10)
        
        tk.Label(frame_jugador1, text="Nombre:").pack(side=tk.LEFT)
        self.nombre_jugador1 = tk.Entry(frame_jugador1)
        self.nombre_jugador1.pack(side=tk.LEFT)
        self.nombre_jugador1.insert(0, "Jugador 1")
        
        # Jugador 2
        frame_jugador2 = tk.Frame(self.frame)
        frame_jugador2.pack(pady=10)
        
        tk.Label(frame_jugador2, text="Jugador 2:", font=("Arial", 12)).pack(side=tk.LEFT)
        
        self.tipo_jugador2 = tk.StringVar(value="Mago")
        tk.OptionMenu(frame_jugador2, self.tipo_jugador2, *opciones).pack(side=tk.LEFT, padx=10)
        
        tk.Label(frame_jugador2, text="Nombre:").pack(side=tk.LEFT)
        self.nombre_jugador2 = tk.Entry(frame_jugador2)
        self.nombre_jugador2.pack(side=tk.LEFT)
        self.nombre_jugador2.insert(0, "Jugador 2")
        
        # Botón de inicio
        tk.Button(self.frame, text="Comenzar Batalla", command=self.iniciar_batalla, 
                    font=("Arial", 14), bg="#4CAF50", fg="white").pack(pady=30)
        
        # Información de personajes
        info_frame = tk.Frame(self.frame)
        info_frame.pack(pady=20)
        
        tk.Label(info_frame, text="Estadísticas base:", font=("Arial", 12, "underline")).grid(row=0, columnspan=3)
        
        tk.Label(info_frame, text="Guerrero: Vida 100, Ataque 50, Defensa 60").grid(row=1, column=0, sticky="w", padx=10)
        tk.Label(info_frame, text="Habilidad: +20% de daño").grid(row=2, column=0, sticky="w", padx=10)
        
        tk.Label(info_frame, text="Mago: Vida 60, Ataque 70, Defensa 30").grid(row=1, column=1, sticky="w", padx=10)
        tk.Label(info_frame, text="Habilidad: Ignora defensa").grid(row=2, column=1, sticky="w", padx=10)
        
        tk.Label(info_frame, text="Arquero: Vida 70, Ataque 50, Defensa 40").grid(row=1, column=2, sticky="w", padx=10)
        tk.Label(info_frame, text="Habilidad: Doble daño si ataque > defensa").grid(row=2, column=2, sticky="w", padx=10)
    
    def iniciar_batalla(self):
        nombre1 = self.nombre_jugador1.get() or "Jugador 1"
        nombre2 = self.nombre_jugador2.get() or "Jugador 2"
        
        self.juego.crear_personaje(self.tipo_jugador1.get(), nombre1, 1)
        self.juego.crear_personaje(self.tipo_jugador2.get(), nombre2, 2)
        
        self.mostrar_pantalla_batalla()
    
    def mostrar_pantalla_batalla(self):
        self.limpiar_pantalla()
        
        # Frame principal
        self.battle_frame = tk.Frame(self.root)
        self.battle_frame.pack(fill=tk.BOTH, expand=True)
        
        # Personaje 1 (izquierda)
        self.frame_pj1 = tk.Frame(self.battle_frame, padx=20, pady=20, bg="#f0f0f0")
        self.frame_pj1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.actualizar_info_personaje(self.juego.personaje1, self.frame_pj1)
        
        # Separador central
        tk.Frame(self.battle_frame, width=2, bg="gray").pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        # Personaje 2 (derecha)
        self.frame_pj2 = tk.Frame(self.battle_frame, padx=20, pady=20, bg="#f0f0f0")
        self.frame_pj2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.actualizar_info_personaje(self.juego.personaje2, self.frame_pj2)
        
        # Área de registro de batalla
        self.log_frame = tk.Frame(self.root, height=150, bg="white")
        self.log_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.log_text = tk.Text(self.log_frame, wrap=tk.WORD, state=tk.DISABLED)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        scroll = tk.Scrollbar(self.log_text)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_text.config(yscrollcommand=scroll.set)
        scroll.config(command=self.log_text.yview)
        
        # Botón de ataque
        self.btn_atacar = tk.Button(self.root, text="Atacar", command=self.ejecutar_turno, 
                                    font=("Arial", 14), bg="#2196F3", fg="white")
        self.btn_atacar.pack(pady=10)
        
        # Botón de volver al menú
        tk.Button(self.root, text="Volver al Menú", command=self.crear_menu_principal, 
                    font=("Arial", 10), bg="#607D8B", fg="white").pack(pady=5)
        
        # Mostrar mensaje inicial
        self.agregar_log(f"¡Comienza la batalla entre {self.juego.personaje1.nombre} ({self.juego.personaje1.nombre_clase}) " +
                            f"y {self.juego.personaje2.nombre} ({self.juego.personaje2.nombre_clase})!")
        self.agregar_log(f"{self.juego.personaje1.nombre} ataca primero.")
    
    def actualizar_info_personaje(self, personaje, frame):
        # Limpiar frame
        for widget in frame.winfo_children():
            widget.destroy()
        
        # Mostrar información del personaje
        tk.Label(frame, text=personaje.nombre, font=("Arial", 16, "bold")).pack()
        tk.Label(frame, text=personaje.nombre_clase, font=("Arial", 12)).pack()
        
        # Barra de vida
        vida_frame = tk.Frame(frame)
        vida_frame.pack(pady=10)
        
        tk.Label(vida_frame, text="Vida:").pack(side=tk.LEFT)
        
        self.vida_var = tk.IntVar(value=personaje.vida)
        vida_bar = ttk.Progressbar(vida_frame, variable=self.vida_var, maximum=100, length=200)
        vida_bar.pack(side=tk.LEFT, padx=5)
        tk.Label(vida_frame, textvariable=tk.StringVar(value=f"{personaje.vida}/100")).pack(side=tk.LEFT)
        
        # Estadísticas
        stats_frame = tk.Frame(frame)
        stats_frame.pack(pady=10)
        
        tk.Label(stats_frame, text=f"Ataque: {personaje.ataque}").grid(row=0, column=0, sticky="w", padx=10)
        tk.Label(stats_frame, text=f"Defensa: {personaje.defensa}").grid(row=1, column=0, sticky="w", padx=10)
        
        # Habilidad especial
        habilidad_frame = tk.Frame(frame, relief=tk.GROOVE, borderwidth=2)
        habilidad_frame.pack(pady=10, fill=tk.X)
        
        tk.Label(habilidad_frame, text="Habilidad Especial:", font=("Arial", 10, "bold")).pack()
        if isinstance(personaje, Guerrero):
            tk.Label(habilidad_frame, text="+20% de daño en cada ataque").pack()
        elif isinstance(personaje, Mago):
            tk.Label(habilidad_frame, text="Ignora la defensa del enemigo").pack()
        elif isinstance(personaje, Arquero):
            tk.Label(habilidad_frame, text="Doble daño si ataque > defensa").pack()
    
    def ejecutar_turno(self):
        if self.juego.batalla_terminada():
            return
        
        resultado = self.juego.realizar_turno()
        self.agregar_log(resultado)
        
        # Actualizar las barras de vida
        self.actualizar_info_personaje(self.juego.personaje1, self.frame_pj1)
        self.actualizar_info_personaje(self.juego.personaje2, self.frame_pj2)
        
        if self.juego.batalla_terminada():
            self.btn_atacar.config(state=tk.DISABLED)
            ganador = self.juego.personaje1 if self.juego.personaje1.esta_vivo() else self.juego.personaje2
            self.agregar_log(f"\n¡{ganador.nombre} ha ganado la batalla!")
        else:
            siguiente = self.juego.personaje1 if self.juego.turno == 1 else self.juego.personaje2
            self.agregar_log(f"\nTurno de {siguiente.nombre}...")
    
    def agregar_log(self, mensaje):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, mensaje + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
    
    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazJuego(root)
    root.mainloop()