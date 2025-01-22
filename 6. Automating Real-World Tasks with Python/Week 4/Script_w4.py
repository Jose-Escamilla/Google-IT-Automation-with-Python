#!/usr/bin/env python3

# Google IT Automation with Python Professional Certificate
# José Escamilla
# 22 Ene 2025

import logging

# Configura el sistema de logging
logging.basicConfig(level=logging.INFO)

def analyze_logins(username, current_day_logins, average_day_logins, alert_threshold=3):
    # Validación de entradas
    if current_day_logins < 0 or average_day_logins <= 0:
        logging.error("Los intentos de inicio de sesión no pueden ser negativos o cero.")
        return None

    # Mostrar información detallada
    logging.info(f"Intentos de inicio de sesión actuales para {username} es: {current_day_logins}")
    logging.info(f"Promedio de intentos de inicio de sesión por día para {username} es: {average_day_logins}")
    
    # Calcular el ratio de los intentos del día actual sobre el promedio diario
    login_ratio = current_day_logins / average_day_logins
    
    # Retornar el ratio calculado
    return login_ratio

# Llamada a la función y almacenamiento del resultado en la variable `login_analysis`
login_analysis = analyze_logins("ejones", 9, 3)

# Condicional que muestra una alerta si la actividad de inicio de sesión es mayor a la normal
if login_analysis is not None:
    if login_analysis >= 3:
        logging.warning(f"Alerta! La cuenta {username} tiene más actividad de inicio de sesión de lo normal.")
