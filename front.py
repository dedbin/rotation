import subprocess

def rotate_display(display, rotation):
    try:
        command = [
            "powershell.exe",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            "backend\script.ps1",
            str(display),
            str(rotation)
        ]
        subprocess.run(command, check=True)
        print(f"Дисплей {display} повернут на {rotation} градусов")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка при повороте дисплея: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    display = input("Введите номер дисплея (0, 1, 2, ...): ")
    rotation = input("Введите угол поворота (0, 90, 180, 270): ")
    
    try:
        display = int(display)
        rotation = int(rotation)
        rotate_display(display, rotation)
    except ValueError:
        print("Некорректный ввод. Введите целые числа для номера дисплея и угла поворота.")
