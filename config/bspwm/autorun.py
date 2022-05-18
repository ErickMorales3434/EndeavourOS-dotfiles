#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

def main():
    directorios = ["Documentos","Descargas","Imágenes","Música","Vídeos"]
    for directorio in directorios:
        busqueda = subprocess.run(["cp -r -u -v ~/{} /run/media/erick/1DT/LINUX".format(directorio)],shell=True,capture_output=True)

    if busqueda.returncode == 0:
            subprocess.run(['''dunstify "Backup datos personales" "La copia se ha finalizado con exito 🙂" -u normal'''],shell=True)
        # borrado = subprocess.run(["rm -r ~/{}/*".format(directorio)],shell=True,capture_output=True)
        
    #     if borrado.returncode == 0:

    #     else:
    #         subprocess.run(['''dunstify "Backup datos personales" "Algo a salido mal, vuelva a intentarlo"'''],shell=True)
    else:
        subprocess.run(['''dunstify "Backup datos personales" "Algo a salido mal, vuelva a intentarlo"'''],shell=True)
        
            
if __name__ == "__main__":
    main()
