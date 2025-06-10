# Juego-formativa
## *1. Descripción General*  
El programa es un juego de batalla por turnos desarrollado en Python, que utiliza los principios de *Programación Orientada a Objetos (POO)* y una interfaz gráfica con *Tkinter*. Permite a dos jugadores seleccionar personajes (Guerrero, Mago o Arquero) y enfrentarlos en un combate donde cada uno tiene habilidades especiales.  


## *2. Características Principales*  

### *2.1. Personajes y Habilidades*  
Cada personaje tiene estadísticas únicas y habilidades especiales:  

| *Personaje* | *Vida* | *Ataque* | *Defensa* | *Habilidad Especial* |
|--------------|---------|------------|------------|-----------------------|
| *Guerrero* | 100     | 50         | 60         | +20% de daño en cada ataque. |
| *Mago*     | 60      | 70         | 30         | Ignora la defensa del enemigo. |
| *Arquero*  | 70      | 50         | 40         | Doble daño si su ataque > defensa del enemigo. |

### *2.2. Mecánica del Juego*  
- *Turnos alternados*: Los jugadores se atacan por turnos hasta que uno queda sin vida.  
- *Sistema de daño*:  
  - *Guerrero*: Aumenta su daño base en un 20%.  
  - *Mago*: Ignora la defensa del rival.  
  - *Arquero*: Hace doble daño si su ataque supera la defensa del oponente.  
- *Validación de vida*: La vida no puede ser menor que 0 ni mayor que 100.  


## *3. Interfaz Gráfica (Tkinter)*  

### *3.1. Pantalla Principal*  
- Permite seleccionar:  
  - Tipo de personaje (Guerrero, Mago, Arquero).  
  - Nombre personalizado para cada jugador.  
- Muestra las estadísticas base de cada personaje.  

### *3.2. Pantalla de Batalla*  
- *Vista de personajes*:  
  - Barra de vida dinámica.  
  - Estadísticas (ataque, defensa).  
  - Descripción de la habilidad especial.  
- *Registro de combate*:  
  - Muestra los ataques realizados y el daño infligido.  
- *Botones*:  
  - *"Atacar"*: Ejecuta el turno del jugador actual.  
  - *"Volver al Menú"*: Reinicia el juego.  


## *4. Principios de POO Aplicados*  

| *Concepto*       | *Aplicación en el Juego* |
|--------------------|---------------------------|
| *Herencia*       | Guerrero, Mago y Arquero heredan de la clase base Personaje. |
| *Polimorfismo*   | Cada personaje implementa su propio método atacar() con lógica única. |
| *Encapsulamiento*| Atributos como vida, ataque y defensa son privados y se acceden mediante getters/setters. |
| *Abstracción*    | La clase Personaje define métodos generales que las subclases implementan. |


## *5. Flujo del Juego*  
1. *Selección de personajes*: Cada jugador elige su personaje y nombre.  
2. *Combate por turnos*:  
   - El jugador 1 ataca primero.  
   - El juego calcula el daño según las habilidades.  
   - Se alternan turnos hasta que un personaje es derrotado.  
3. *Fin del juego*: Se anuncia al ganador y se permite reiniciar.  
