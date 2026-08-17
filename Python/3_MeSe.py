import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import re
# Каждая ячейка теперь — это отдельный пустой список []
data = []
item = {}
m = 0
count = 0
print(data)

def recursive_parse(element, level=0):
    global data, m, count    

    for j in range(len(element)):
        for k in range(len(element[j])):            
            
            at = element[j][k].get('name')         #Аттрибут для определения массива
            tp = element[j][k].get('type')         #Аттрибут для определения типа
            match = re.search(r'^(.+)\[(\d+)\]$', at)   #Поиск символов [] для построения массива

            if  match:                                                   #Если есть символ массива, то через цикл записывает 
                array_name = match.group(1)
                index = int(match.group(2))
                for i in range(index):
                    item = {
                    "count": count,
                    "class": element[j].tag,
                    "name": (f"{array_name}[{i}]"),#"name": element[j][k].get('name'),
                    "type": element[j][k].get('type'),
                    "caption": element[j][k].get('caption'),
                    "value": 0
                    }
                    data.insert(m, item)
                    m += 1      
                    if tp == 'unsigned char' or tp =='signed char' : count += 1
                    elif tp == 'unsigned long' or tp == 'float': count += 4
                    elif tp == 'unsigned int' : count += 2
                    #print(f"{array_name}[{i}]")
                #print(at)
            else:                                                         #Если нет символа массива
                item = {
                    "count": count,
                    "class": element[j].tag,
                    "name": at,#"name": element[j][k].get('name'),
                    "type": element[j][k].get('type'),
                    "caption": element[j][k].get('caption'),
                    "value": 0
                }
                data.insert(m, item)
                m += 1      
                if tp == 'unsigned char' or tp =='signed char' : count += 1
                elif tp == 'unsigned long' or tp == 'float': count += 4
                elif tp == 'unsigned int' : count += 2
def load_xml_file():
        """Загрузка XML файла через диалоговое окно"""
    filename = filedialog.askopenfilename(
        title="Выберите XML файл",
        filetypes=[
            ("XML files", "*.xml"),
            ("All files", "*.*")
        ],
        initialdir="./"  # Начинаем с текущей директории
    )
        
    if filename:
        self.current_file = filename
        self.status_label.config(text=f"Загрузка: {filename}", fg="orange")
        self.info_label.config(text=f"Файл: {filename}")
        self.root.update()
            
        # Парсим и заполняем таблицу
        success = self.parse_xml(filename)
            
        if success:
            self.status_label.config(text=f"✅ Загружен: {filename}", fg="green")
        else:
            self.status_label.config(text="❌ Ошибка загрузки", fg="red")     
            
def parse_xml_recursive(filename):
    """Парсинг XML с рекурсивным обходом"""
    tree = ET.parse(filename)
    root = tree.getroot()
    recursive_parse(root)

parse_xml_recursive('devices/6.15.xml')
#print(data)

#                                                       Интерфейс №1

# Создаем окно
root = tk.Tk()
root.title("Таблица из данных")
root.geometry("800x800")

# Создаем таблицу
columns = ['count', 'class', 'name', 'type', 'caption', 'value']
column_labels = {
    'count': '№',
    'class': 'Класс',
    'name': 'Имя',
    'type': 'Тип',
    'caption': 'Описание',
    'value': 'Значение'
}
# Создаем Treeview (таблицу)
tree = ttk.Treeview(root, columns=columns, show='headings')

toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)
load_btn = ttk.Button(toolbar, text="📁 Загрузить XML...", command=load_xml_file)
load_btn.pack(side=tk.LEFT, padx=5, pady=5)
# Настраиваем колонки
for col in columns:
    tree.heading(col, text=column_labels[col])
    tree.column(col, width=100, anchor='center')
tree.column('count', width=50)
tree.column('caption', width=200)

# Добавляем скролл
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)

# Размещаем
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10,pady=10)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y, pady=10)

# ============================================
# ЗАПОЛНЯЕМ ТАБЛИЦУ
# ============================================
for row in data:
    values = [
        row.get('count', ''),
        row.get('class', ''),
        row.get('name', ''),
        row.get('type', ''),
        row.get('caption', ''),
        row.get('value', '')
    ]
    tree.insert('', tk.END, values=values)

# Информация
label = tk.Label(root, text=f"Всего записей: {len(data)}", font=('Arial', 10))
label.pack(pady=5)

root.mainloop()