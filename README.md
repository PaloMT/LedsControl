@ -0,0 +1,58 @@
# Controlador en Python para Conexión por Firmata a Arduino y Detección de Manos con Cámara 🖐️📷

Este proyecto proporciona archivos en Python que permiten controlar una conexión por Firmata a un Arduino y utilizar una cámara para la detección de manos. El Arduino puede ser utilizado para interactuar con dispositivos físicos, mientras que la detección de manos a través de la cámara puede ser utilizada para realizar acciones basadas en gestos.

## Características 🛠️

- **Control por Firmata:** Utiliza la biblioteca `pyfirmata` de Python para establecer una conexión por Firmata con un Arduino, permitiendo el control de dispositivos físicos conectados al Arduino desde el programa en Python.

- **Detección de Manos:** Utiliza una biblioteca de detección de objetos o gestos basada en visión por computadora para detectar manos en tiempo real a través de una cámara.

- **Interfaz con Arduino:** Proporciona una interfaz entre el programa en Python y el Arduino, permitiendo enviar comandos y recibir datos para controlar dispositivos conectados.

## Arduinno ⚙️

`Componentes utilizados:`                                 `Procedimiento:`
- 5 leds de cualquier color                              - conectar los leds al negativo, y el negativo al gnd
- Protoboard                                             - En el lado positivo conectar las resistencias
- Placa de arduino uno                                   - Conectar el lado positivo con el pin deseado
- 5 resistencias de 220Ω
- Cables

## Requisitos 📦
- Python 3.x instalado en tu sistema.
- Bibliotecas Python: 
    `time`:permite parar el programa por unos segundos
    `pyfirmata`:permite la conexión con la placa de arduino
    `opencv`: programa de deteccion de manos
    `mediapipe`: programa de deteccion de manos

## Uso 📝

1. **Clonar el Repositorio:** Clona este repositorio en tu sistema local utilizando Git.

2. **Instalar Dependencias:** Instala las dependencias necesarias utilizando pip o conda. Por ejemplo: `pip install pyfirmata opencv-python`.

3. **Conectar Arduino:** Conecta tu Arduino al ordenador y carga un sketch de Firmata en él utilizando el IDE de Arduino. En este proyecto se ha utilifado el StandartFirmata

4. **Ejecutar el Programa:** Ejecuta el programa Python proporcionado. Asegúrate de seleccionar el puerto COM correcto y los pines de los leds para la conexión con el Arduino.

5. **Detección de Manos:** La cámara se activará y comenzará a detectar manos en tiempo real. Puedes interactuar con el Arduino enviando comandos desde el programa Python.

## Modificaciones al proyecto original 😊

- Da igual el dedo que muevas, la luz de respectivo dedo se va a iluminar
- Inclusion de códigos para que las luces hagan movimientos diferentes
    · 🤘 para que las luces se iluminen y apaguen en cascada
    · 🤟 y las luces parpadearán 
    · 🤙 para que las luces se enciendan de fuera hacia dentro


## Créditos 🙌

Este proyecto fue basado en el proyecto de PICAIO SAS y está inspirado en proyectos similares de la comunidad de visión por computadora y Arduino. Modificado por PaloMT

## Licencia 📝

Este proyecto está bajo la licencia [MIT](LICENSE).
