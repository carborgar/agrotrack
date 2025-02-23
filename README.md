# AgroTrack

AgroTrack es una aplicación para la gestión de parcelas agrícolas, permitiendo registrar campos, maquinaria, productos
agrícolas, trabajos realizados y cosechas.

## Características

- **Gestión de parcelas**: Registra parcelas con su área, cultivo y año de plantación.
- **Maquinaria**: Administra equipos como pulverizadores con su capacidad.
- **Productos**: Control de fertilizantes y fitosanitarios con diferentes tipos de dosis.
- **Trabajos agrícolas**: Planifica tareas como fertirrigación y pulverización, asignando productos y maquinaria.
- **Recolección**: Registra las cosechas por parcela y fecha.
- **Cálculo de aplicación**: Calcula automáticamente la cantidad de producto a aplicar según la capacidad de la máquina
  y la dosis establecida.

## Instalación

### Requisitos

- Python 3.8+
- Django 5.0

### Pasos

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd agrotrack
   ```

2. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Aplica las migraciones y crea el superusuario:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. Inicia el servidor:
   ```bash
   python manage.py runserver
   ```

## Modelos Principales

### `Field` (Parcelas)

Registra información sobre las parcelas: nombre, área, cultivo y año de plantación.

### `Machine` (Maquinaria)

Gestiona maquinaria como pulverizadores con su capacidad en litros.

### `Product` (Productos)

Permite registrar fertilizantes y fitosanitarios con distintos tipos de dosis:

- kg/1000L de agua
- kg/ha
- L/ha

### `Task` (Trabajos agrícolas)

Define tareas como fertirrigación y pulverización, asignadas a parcelas y maquinaria.

### `Harvest` (Recolección)

Registra la cantidad cosechada en una fecha específica.

## Uso

La aplicación permite visualizar los trabajos pendientes del año en curso por defecto. También se pueden consultar
trabajos de años anteriores.

---
Desarrollado con Django.
