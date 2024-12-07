import os
import shutil

def copy_static_files(static_dir, build_dir):
    if not os.path.exists(static_dir):
        raise FileNotFoundError(f"O diretório '{static_dir}' não foi encontrado.")

    for root, dirs, files in os.walk(static_dir):
        relative_path = os.path.relpath(root, static_dir)
        
        target_path = os.path.join(build_dir, relative_path)

        os.makedirs(target_path, exist_ok=True)

        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(target_path, file)

            shutil.copy2(source_file, destination_file)
            print(f"Copiado: {source_file} -> {destination_file}")