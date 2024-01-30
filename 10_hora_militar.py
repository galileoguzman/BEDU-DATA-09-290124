import pandas as pd

# Hora militar
# 0700 - 07:00
# 1200 - 12:00
# 1500 - 15:00

def convertir_a_datetime(hora_militar):
    hora_militar = hora_militar.zfill(4)

    horas = int(hora_militar[:2])
    minutos = int(hora_militar[2:])
    hora_completa = f'{horas:02d}:{minutos:02d}'
    return pd.to_datetime(hora_completa, format='%H:%M')

data = {
    'hora_militar': ['0700', '0900', '1200', '1500'],
    'actividades': ['desayuno', 'ejercicio', 'lectura', 'comida']
}

dataframe = pd.DataFrame(data)
print(dataframe.head())
print('------------------')

dataframe['fecha_hora'] = dataframe['hora_militar'].map(convertir_a_datetime)
print(dataframe.head())
