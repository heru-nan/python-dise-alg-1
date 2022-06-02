##Instalacion

Todas las dependencias se encuentran en el archivo requirements.txt
Se uso python 3
Y las instrucciones para trabajar en el proyecto son las siguientes:

- Instalar [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
  python -m pip install --user virtualenv
  or
  python3 -m pip install --user virtualenv

Comandos en la raiz del proyecto:

- Se recomienda crear un ambiente virtual
  virtualenv venv
- Activar el ambiente virtual
  source venv/bin/activate
- Para instalar las dependencias
  pip install -r requirements.txt
- Ahora podrias ejecutar cualquiera de los scripts del proyecto

Archivos de codificacion general y decodificacion general: encode.py y decode.py

#Scripts ejecutados por terminal, dentro del ambiente virtual o con las dependencias instaladas a nivel global

##Codificacion:

    python encode.py h english.100MB

    or

    python encode.py s dna.100MB

##Decodificacion:

    python decode.py h_english.100MB d_h_english.100MB

    or

    python decode.py s_dna.100MB d_s_dna.100MB

##Experimento 1:

    python experimento_1.py dna.100MB n

    or

    python experimento_1.py english.100MB n

    n=Las veces que se ejecutara el experimento

##Experimento 2:

    python experimento_2.py h_english.100MB d_h_english.100MB

##Experimento 3:

    python experimento_3.py s dna.100MB

    or

    python experimento_3.py h dna.100MB
