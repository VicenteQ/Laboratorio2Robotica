from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

left_motor = robot.getDevice('left wheel motor')
right_motor = robot.getDevice('right wheel motor')
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# ¡Ahora sí funcionará porque le instalamos el hardware!
pen = robot.getDevice('pen')
pen.write(True)
pen.setInkColor(0x00FF00, 1.0) # Tinta color verde brillante

# Variables de tiempo para calcular las figuras
TIEMPO_LADO = 2.0
TIEMPO_GIRO_90 = 0.85 
inicio_cuadrado = 14.0 

while robot.step(timestep) != -1:
    tiempo = robot.getTime()
    
    # DESAFÍO 1: Recta (0 a 3 segundos)
    if tiempo < 3.0:
        left_motor.setVelocity(4.0)
        right_motor.setVelocity(4.0)
        
    # DESAFÍO 2: Curva (3 a 7 segundos)
    elif tiempo < 7.0:
        left_motor.setVelocity(5.0)
        right_motor.setVelocity(2.0)
    # DESAFÍO 3: Círculo (7 a 13 segundos)
    elif tiempo < 13.0:
        left_motor.setVelocity(4.0)
        right_motor.setVelocity(0.0)
        
    # Pausa de 1 segundo para frenar antes del cuadrado
    elif tiempo < inicio_cuadrado:
        left_motor.setVelocity(0.0)
        right_motor.setVelocity(0.0)
        
    # DESAFÍO OPCIONAL: Cuadrado (14 segundos en adelante)
    else:
        tiempo_relativo = tiempo - inicio_cuadrado
        duracion_ciclo = TIEMPO_LADO + TIEMPO_GIRO_90
        tiempo_en_ciclo = tiempo_relativo % duracion_ciclo
        ciclo_actual = int(tiempo_relativo / duracion_ciclo)
        
        if ciclo_actual < 4:
            if tiempo_en_ciclo < TIEMPO_LADO:
                left_motor.setVelocity(4.0)   # Avanza recto
                right_motor.setVelocity(4.0)
            else:
                left_motor.setVelocity(-3.0)  # Gira en el lugar
                right_motor.setVelocity(3.0)
        else:
            left_motor.setVelocity(0.0)       # Termina y se detiene
            right_motor.setVelocity(0.0)