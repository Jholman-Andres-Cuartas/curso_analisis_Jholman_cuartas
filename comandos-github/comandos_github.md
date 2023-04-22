# GITHUB

# El archivo .gitignore

Evitar que Git siga a ciertos archivos y directorios
https://www.toptal.com/developers/gitignore
https://github.com/github/gitignore

    Otros ejemplos de patrones para indicar archivos a no seguir
    No seguir todos los archivos que finalicen con alguna vocal:
    *.[aeiouAEIOU]

    Ignorar el archivo claves.txt localizado en la raíz del proyecto:
    /clave.txt

    Ignorar el archivo claves.txt localizado en la la carpeta /claves:
    claves/clave.txt

    Ignorar todos los archivos de la carpeta documentacion:
    documentacion/

# # # Comandos Github

git --version
git --help

# Si queremos ver los datos de configuración que modificamos y otros que se inicializaron por defecto podemos nuevamente ejecutar el comando 'config' pasando el parámetro --list:

git config --list

# Si necesitamos obtener una ayuda de un comando de git debemos llamar al comando "help" y pasar el nombre del comando que necesitamos consultar, luego Git nos abre el navegador con datos de la ayuda que se encuentran en forma local sin la necesidad de acceder a internet:

git help config

# comando status

# El comando para determinar qué archivos están en qué estado es el comando status. Si ejecuta este comando inmediatamente después de crear un repositorio, por ejemplo ejecutemos el comando del repositorio creado en proyecto1:

git status

# Para comenzar a rastrear un archivo nuevo debemos utilizar el comando add:

• git add programa1.py

# Por ejemplo si queremos eliminar el archivo programa1.py para que git lo deje de seguir:

git rm programa1.py

# De forma similar para cambiar el nombre de un archivo que estamos siguiendo con git debemos utilizar un comando:

git mv programa2.py programafinal.py

# Creación de alias para comandos Git

git config --global alias.ci commit

Luego de ejecutar este comando podemos ejecutar el comando commit con el alias ci.
git ci

Otros ejemplos de alias:
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.st status

En el caso que necesitemos modificar un alias, simplemente lo volvemos a crear con el mismo nombre:
git config --global alias.ct commit

Si lo queremos borrar al alias debemos pasar el parámetro --unset:
git config --global --unset alias.st

# PARA RESOLVER CONFLICTOS

$ git merge --abort
$ git rebase --abort

# COMANDOS BÁSICOS

Configurar usuario a nivel global:
git config --global user.email tuemail@ejemplo.com
git config --global user.name "Diego Moisset"

    git config --global user.email diegomoisset@gmail.com

    Recordemos que podemos conocer todos los valores almacenados en configuración mediante:
    git config --list

Configurar usuario a nivel local de un repositorio en particular
git config --local user.email tuemail@ejemplo.com

Inicializar un repositorio:
git init

Verificar el status para visualizar el estado del área de trabajo:
git status

Añadir un archivo en concreto al área de ensayo:
git add <archivo>
git add index.html

    Nota: si queremos registrar todos los archivos de golpe podemos ejecutar el comando:
    git add .

Añadir todos los archivos y cambios:
git add -A

Registrar los cambios realizando un commit:
git commit -m "mensaje de confirmación"
• git commit -m "se añade el archivo programa1.py al proyecto"

    Nota: para registrar directamente al área de repositorio local sin ejecutar git add se puede
    ejecutar el comando commit con el parámetro -a:
    git commit -a -m 'Ejemplo mensaje'

    Podemos saltear el área de preparación agregando un parámetro (-a) al comando commit:
    git commit -a -m "se borraron la última línea de los archivos programa1.py y programa2.py"

Ver los commits realizados:
git log
git log --online

    Nota: el parámetro pretty nos permite mostrar todos los commit en una sola línea para una mejor
    visualización.
    git log --pretty=oneline

    El comando log proporciona gran cantidad de opciones. Veamos algunas de las más usadas. Primero podemos indicar cuantos commit mostrar. Por ejemplo para mostrar los últimos tres commit:
    git log -3

    Otra opción es el parámetro -p, que muestra las diferencias introducidas en cada confirmación:
    git log -p -2

    Otra opción es el parámetro -p, que muestra las diferencias introducidas en cada confirmación:
    git log -p -2

    El parámetro --stat imprime tras cada confirmación una lista de archivos modificados, indicando cuántos han sido modificados y cuántas líneas han sido añadidas y eliminadas para cada uno de ellos, y un resumen de toda esta información.
    Otro parámetro es --pretty, al cual le podemos asignar distintos valores (oneline, full, email, short, etc.), veamos con el valor oneline:
    git log --pretty=oneline

    La opción oneline imprime cada confirmación en una única línea, lo que puede resultar útil si estás analizando gran cantidad de confirmaciones:

    También podemos consultar confirmaciones por rango de fechas:
    git log --since="2022-12-01" --until="2022-12-16"

    Podemos consultar todos los commit de un determinado autor:
    git log --author="Diego Moisset"

# Trabajar con remotos

Clonar un repositorio:
git clone <https://link-con-nombre-del-repositorio>
git clone https://github.com/git/git.git

Ver los remotos asociados actualmente al repositorio:
git remote -v

Subir cambios a un remoto (Importante: git push solamente carga los cambios que
han sido confirmados)
git push
git push <nombre-remoto>
git push <nombre-remoto> <nombre-rama>

Recibir actualizaciones de un repositorio remoto:
git pull <nombre-remoto>

Configurar un remoto en un repositorio ya existente:
git remote add origin <https://link-con-nombre-del-repositorio>

# COMANDOS AVANZADOS

# Ramas

Ver ramas:
git branch
git branch --list

Crear una nueva rama:
git branch <nombre-de-la-rama>

    Por ejemplo ahora queremos implementar la funcionalidad de login a nuestro sitio web, en lugar de modificar la rama 'master', procedemos a crear una rama llamada 'login':
    git branch login

Borrar una rama:
git branch -d <nombre-de-la-rama>

Cambiar el área de trabajo hacia una rama:
git checkout <nombre-de-la-rama>

Crear y cambiar el área de trabajo hacia una rama:
git checkout -b <nombre-de-tu-rama>

    Como podemos comprobar tenemos dos ramas: 'master' y 'login'. Con un asterisco se muestra en la que estamos posicionados, cualquier cambio que hagamos se hará sobre dicha rama.
    Para cambiarnos de rama debemos ejecutar el comando checkout y el nombre de la rama:
    git checkout login

    Cuando activamos la otra rama podemos comprobar con checkout que la rama activa es la de login:
    git checkout

    Creamos ahora en la rama login 2 archivos y los confirmamos:
    git add login1.html
    git add login2.html
    git commit -m "Agregamos los archivos de login"

# Fusionar ramas

1 - Colocarse en la rama a fusionar:
git checkout dev

    Seguidamente nos arrepentimos del cambio y queremos volver al último estado que habíamos confirmado (commit) en nuestro repositorio. Para volver atrás debemos ejecutar el siguiente comando:
    git checkout -- programa3.py

2 - Actualizar la rama
git fetch

3 - Fusionar la rama
git merge <nombre-de-la-rama>

    Si ya tenemos implementado la funcionalidad de login, podemos fusionar la rama 'login' a la rama 'master' mediante el comando 'merge':
    git merge login

    Cuando fusionamos una rama, la misma no se borra, podemos comprobar que sigue existiendo ejecutando el comando checkout:
    git branch
    Si queremos borrar definitivamente una rama lo debemos hacer con el comando:
    git branch -d login

# Revertir commits

Obtener el id del commit a revertir:
git log --oneline

Revertir el commit por su id:
git revert aabc7cf

# En Git Bash podemos trabajar con ramas haciendo uso de los comandos:

Ver las ramas: git branch -a
● Crear una nueva rama: git branch testing
● Cambiar a una rama: git checkout testing
● Crear y cambiar a una rama: git checkout -b testing
● Fusionar una rama: git merge testing (primero git checkout a la rama
donde queremos fusionar)
● Borrar una rama: git branch -d testing
