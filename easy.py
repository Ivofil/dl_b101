import os

def change_dir (path):
    """
    Функция, меняющая директорию
    """
    try:
        os.chdir(path)
        print (f"Успешно перешли в папку: {path}")
    except FileNotFoundError:
        print (f"{path} - папки не существует")


def fld_dir(path):
    """
    Функция, отображающая папки текущей директории
    """
    for fld in os.listdir(path):
        if os.path.isdir(fld):
            print(f"Папка: {fld}, путь: {os.path.abspath(fld)}")
        else:
            print(f"Файл: {fld}, путь: {os.path.abspath(fld)}")

            
def del_dir(name):
    """
    Функция, удаляющая папку
    """
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.rmdir(dir_path)
        print(f"Удалена папка: {dir_path}") 
    except FileNotFoundError:
        print("Папка отстутствует")
        
#del_dir("NEW3")
                
            
def new_dir(name):
    """
    Функция, создающая папку
    """
    dir_path = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dir_path)
        print(f"Создана папка: {dir_path}") 
    except FileExistsError as es:
        print("Папка уже создана")

#new_dir("NEW2")

 

 

 
