import tkinter as tk
from tkinter import messagebox

# Функция добавления цифры к текущему значению в поле ввода
def add_digit(digit):
    value = calc.get()  # Получаем текущее значение из поля ввода
    if value[0] == "0" and len(value) == 1:  # Если значение "0" и это единственный символ
        value = value[1:]  # Удаляем "0"
    calc.delete(0, tk.END)  # Очищаем поле ввода
    calc.insert(tk.END, value + str(digit))  # Вставляем новое значение с добавленной цифрой

# Функция добавления операции к текущему значению в поле ввода
def add_operation(operation):
    value = calc.get()  # Получаем текущее значение из поля ввода
    if value[-1] in "+-/*":  # Если последний символ уже операция
        value = value[:-1]  # Удаляем последний символ (операцию)
    elif "+" in value or "-" in value or "/" in value or "*" in value:  # Если в значении уже есть какая-либо операция
        calculate()  # Вычисляем текущее выражение
        value = calc.get()  # Обновляем значение
    calc.delete(0, tk.END)  # Очищаем поле ввода
    calc.insert(tk.END, value + operation)  # Вставляем новое значение с добавленной операцией

# Функция выполнения вычисления
def calculate():
    value = calc.get()  # Получаем текущее значение из поля ввода
    if value[-1] in "+-/*":  # Если последний символ операция
        operation = value[-1]  # Сохраняем операцию
        value = value[:-1] + operation + value[:-1]  # Дублируем операцию для корректного вычисления
    calc.delete(0, tk.END)  # Очищаем поле ввода
    try:
        calc.insert(0, eval(value))  # Вычисляем выражение и вставляем результат
    except (NameError, SyntaxError):
        messagebox.showinfo("внимание","нужно толь цифры!")
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo("внимание", "нельзя делить на ноль")
        calc.insert(0, 0)
    # Функция очистки поля ввода
def clear():
    calc.delete(0, tk.END)  # Очищаем поле ввода
    calc.insert(0, 0)  # Вставляем "0" в качестве начального значения

# Функция создания кнопки для цифры
def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, command=lambda: add_digit(digit))  # Возвращаем кнопку с цифрой и командой добавления этой цифры

# Функция создания кнопки для операции
def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, fg="red", command=lambda: add_operation(operation))  # Возвращаем кнопку с операцией и командой добавления этой операции

# Функция создания кнопки вычисления
def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, fg="red", command=calculate)  # Возвращаем кнопку "=" с командой вычисления

# Функция создания кнопки очистки
def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, fg="red", command=clear)  # Возвращаем кнопку "C" с командой очистки

root = tk.Tk()  # Создаем главное окно приложения
root.geometry(f"240x260+100+200")  # Устанавливаем размер и позицию окна
root['bg'] = "#33ffe6"  # Устанавливаем цвет фона окна
root.title("Калькулятор")  # Устанавливаем заголовок окна

calc = tk.Entry(root, justify=tk.RIGHT, font=("Arial", 15), width=15)  # Создаем поле ввода
calc.insert(0, "0")  # Вставляем начальное значение "0"
calc.grid(row=0, column=0, columnspan=4, stick="wens")  # Размещаем поле ввода на сетке

# Размещение кнопок цифр на сетке
make_digit_button(1).grid(row=1, column=0, stick="wens", padx=5, pady=5)
make_digit_button(2).grid(row=1, column=1, stick="wens", padx=5, pady=5)
make_digit_button(3).grid(row=1, column=2, stick="wens", padx=5, pady=5)
make_digit_button(4).grid(row=2, column=0, stick="wens", padx=5, pady=5)
make_digit_button(5).grid(row=2, column=1, stick="wens", padx=5, pady=5)
make_digit_button(6).grid(row=2, column=2, stick="wens", padx=5, pady=5)
make_digit_button(7).grid(row=3, column=0, stick="wens", padx=5, pady=5)
make_digit_button(8).grid(row=3, column=1, stick="wens", padx=5, pady=5)
make_digit_button(9).grid(row=3, column=2, stick="wens", padx=5, pady=5)
make_digit_button(0).grid(row=4, column=0, stick="wens", padx=5, pady=5)


# Размещение кнопок операций на сетке
make_operation_button("+").grid(row=1, column=3, stick="wens", padx=5, pady=5)
make_operation_button("-").grid(row=2, column=3, stick="wens", padx=5, pady=5)
make_operation_button("/").grid(row=3, column=3, stick="wens", padx=5, pady=5)
make_operation_button("*").grid(row=4, column=3, stick="wens", padx=5, pady=5)

# Размещение кнопок "=" и "C" на сетке
make_calc_button("=").grid(row=4, column=2, stick="wens", padx=5, pady=5)
make_clear_button("C").grid(row=4, column=1, stick="wens", padx=5, pady=5)

# Конфигурация размеров столбцов и строк сетки
root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)

root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)

root.mainloop()  # Запуск главного цикла обработки событий