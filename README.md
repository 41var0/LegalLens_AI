# LegalLens AI
___

Este proyecto se basa en la creación de varios contenedores de docker en lo que se
manejan distintas operaciones. Desde la llamada a una API (FastAPI), la presentación web
de un servicio (DJango) y el manejo de inteligencia artificial (Google) para revisar 
distintos documentos legales. 

## Prerequisitos
Se requiera los siguientes elementos para iniciar el proyecto. 
- Docker

## IMPORTANTE
Es muy importante destacar que si en nuestra plataforma es Windows tendremos que añadir
una configuración adicional a git:
```commandline
git config --global core.autocrlf input
```
Sin este comando, uno de los archivos del proyecto no funciona es correctamente, ya que
el propio git reconvertirá el archivo con algunos caracteres de escape de Windows, lo que
no funciona bien en máquinas Linux. [Lind de Stackoverflow](https://stackoverflow.com/a/40537078)

## Ejecucion del proyecto
El proyecto lo iniciaremos desde el archivo dcuba.bat o escribiendo y ejecutando
manualmente desde la consola:
```commandline
docker-compose up --build
```

## Uso
Una vez hice la estoy ejecutado el proyecto, podremos acceder a él a partir de [localhost](http://localhost). 

