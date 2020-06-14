# Sistema de reserva de horas médicas para centros de salud.

Con el fin de continuar el proceso de aprendizaje del framework Django, es que me planteo la idea de iniciar un sistema de reserva de horas médicas para centros de salud, proyecto que decidí dividir en dos hitos. El primero consiste en presentarle a los usuarios externos (pacientes) una interfaz que les permita escoger la especialidad médica de su interés, para luego tener la opción de escoger a un médico y hacer una reserva de hora según disponibilidad, proceso que se confirma con la recepción de un mensaje en el correo eléctronico del paciente. El segundo hito consistirá en realizar la interfaz que permita administrar la base de datos de médicos por parte de un usuario interno encargado y la de gestión de horas médicas (CRUD) según cada caso (tarea normalmente realizada por secretarias o asistentes).

## Demo

Pendiente

## Instalación Local

1. Lo primero es obtener el código fuente
```
git clone https://github.com/eduardocalabrano/reserva_horas_medicas.git
```

2. Es necesario tener python instalado (idealmente 3.8 o superior).

3. Crear un entorno virtual dentro del proyecto clonado y ejecutarlo
```
python -m venv nombre_entorno
nombre_entorno\Scripts\activate
```

4. Instalar todo lo indicado en el archivo requirements
```
pip install -r requirements.txt
```

5. Crear las tablas para los modelos en base de datos local
```
python manage.py migrate
```
6. Ejecutar el servidor local
```
python manage.py runserver
```

7. Se recomienda poblar la base de datos con médicos y citas médicas antes de intentar hacer pruebas.


## Capturas

![](https://i.postimg.cc/x1t1WZfj/001.png)
![](https://i.postimg.cc/N0FjYxF6/002.png)
![](https://i.postimg.cc/k5HX5tRk/005.png)
![](https://i.postimg.cc/C1fMnLjd/007.png)
