import os
import shutil
import subprocess

def build_and_copy_files(react_project_folder, source_folder, destination_folder):
    # Cambia el directorio de trabajo al de la carpeta del proyecto de React
    os.chdir(react_project_folder)

    npm_path = "C:\\Users\\Jose\\AppData\\Roaming\\nvm\\v18.17.1\\npm.cmd"
    # Ejecuta el comando 'npm run build'
    subprocess.run([npm_path, 'run', 'build'], check=True)

    # Vuelve al directorio de trabajo original
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    # Obtiene la lista de archivos y directorios en la carpeta de origen
    items = os.listdir(source_folder)

    # Elimina archivos y directorios existentes en la carpeta de destino
    existing_items = os.listdir(destination_folder)
    for existing_item in existing_items:
        item_path = os.path.join(destination_folder, existing_item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)

    # Itera sobre cada elemento en la carpeta de origen
    for item in items:
        # Crea la ruta completa del elemento de origen
        source_item = os.path.join(source_folder, item)

        # Crea la ruta completa del elemento de destino
        destination_item = os.path.join(destination_folder, item)

        # Copia el elemento de la carpeta de origen a la carpeta de destino
        if os.path.isfile(source_item):
            shutil.copy2(source_item, destination_item)
        elif os.path.isdir(source_item):
            shutil.copytree(source_item, destination_item)

    print("¡Compilación y copia de archivos completadas con éxito!")

react_project_folder = "D:\\Code\\React\\projects\\Cantare"
source_folder = "D:\\Code\\React\\projects\\Cantare\\dist"
destination_folder = "D:\\Code\\Projects\\Cantare\\Cantare-BackEnd\\public"

build_and_copy_files(react_project_folder, source_folder, destination_folder)
