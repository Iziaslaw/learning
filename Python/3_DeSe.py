import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import xml.etree.ElementTree as ET
import re

class XMLTableApp:
    """Приложение для загрузки XML и отображения в таблице"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("XML Viewer с выбором файла")
        self.root.geometry("1000x700")
        
        # Переменные
        self.current_file = None
        self.data = []
        self.tree = None
        self.array_data = {}  # Для хранения массивов
        
        # Создаем интерфейс
        self.create_widgets()
        
        # Статус
        self.status_label.config(text="Загрузите XML файл", fg="blue")
    
    def create_widgets(self):
        """Создание всех виджетов"""
        # ============================================
        # Верхняя панель с кнопками
        # ============================================
        toolbar = tk.Frame(self.root)
        toolbar.pack(fill=tk.X, padx=5, pady=5)
        
        # Кнопка выбора XML файла
        self.load_btn = tk.Button(
            toolbar, 
            text="📁 Выбрать XML файл", 
            command=self.load_xml_file,
            bg="#4CAF50", 
            fg="white",
            font=('Arial', 10, 'bold'),
            padx=10,
            pady=5
        )
        self.load_btn.pack(side=tk.LEFT, padx=5)
        
        # Кнопка обновления
        self.refresh_btn = tk.Button(
            toolbar, 
            text="🔄 Обновить", 
            command=self.refresh_table,
            bg="#2196F3", 
            fg="white",
            padx=10,
            pady=5
        )
        self.refresh_btn.pack(side=tk.LEFT, padx=5)
        
        # Кнопка экспорта
        self.export_btn = tk.Button(
            toolbar, 
            text="📊 Экспорт CSV", 
            command=self.export_csv,
            bg="#FF9800", 
            fg="white",
            padx=10,
            pady=5
        )
        self.export_btn.pack(side=tk.LEFT, padx=5)
        
        # Кнопка очистки
        self.clear_btn = tk.Button(
            toolbar, 
            text="🗑️ Очистить", 
            command=self.clear_all,
            bg="#f44336", 
            fg="white",
            padx=10,
            pady=5
        )
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Статус
        self.status_label = tk.Label(
            toolbar, 
            text="Готов", 
            font=('Arial', 10),
            fg="green"
        )
        self.status_label.pack(side=tk.RIGHT, padx=10)
        
        # ============================================
        # Информационная панель
        # ============================================
        info_frame = tk.Frame(self.root)
        info_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.info_label = tk.Label(
            info_frame, 
            text="Файл не загружен", 
            font=('Arial', 9),
            fg="gray"
        )
        self.info_label.pack(side=tk.LEFT)
        
        self.count_label = tk.Label(
            info_frame, 
            text="Записей: 0", 
            font=('Arial', 9),
            fg="gray"
        )
        self.count_label.pack(side=tk.RIGHT)
        
        # ============================================
        # Таблица (Treeview)
        # ============================================
        table_frame = tk.Frame(self.root)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.create_table(table_frame)
        
        # ============================================
        # Нижняя панель с дополнительной информацией
        # ============================================
        bottom_frame = tk.Frame(self.root)
        bottom_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.detail_label = tk.Label(
            bottom_frame, 
            text="", 
            font=('Arial', 9),
            fg="gray"
        )
        self.detail_label.pack(side=tk.LEFT)
    
    def create_table(self, parent):
        """Создание таблицы Treeview"""
        # Определяем колонки
        self.columns = ('count', 'class', 'name', 'type', 'caption', 'value', 'is_array')
        column_labels = {
            'count': '№',
            'class': 'Класс',
            'name': 'Имя',
            'type': 'Тип',
            'caption': 'Описание',
            'value': 'Значение',
            'is_array': 'Массив'
        }
        
        # Создаем Treeview
        self.tree = ttk.Treeview(parent, columns=self.columns, show='headings')
        
        # Настраиваем колонки
        for col in self.columns:
            self.tree.heading(col, text=column_labels.get(col, col))
            width = 50 if col == 'count' else 80 if col == 'is_array' else 150
            self.tree.column(col, width=width, anchor='center')
        
        # Увеличиваем ширину для некоторых колонок
        self.tree.column('caption', width=200)
        self.tree.column('name', width=150)
        
        # Добавляем скролл
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Размещаем
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Привязываем событие выбора строки
        self.tree.bind('<<TreeviewSelect>>', self.on_item_select)
    
    def load_xml_file(self):
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
    
    def parse_xml(self, filename):
        """
        Парсинг XML файла и заполнение данных
        
        Returns:
            bool: успех операции
        """
        try:
            # Парсим XML
            tree = ET.parse(filename)
            root = tree.getroot()
            
            # Очищаем старые данные
            self.data = []
            self.array_data = {}
            
            # Парсим устройство
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
            
            # Заполняем таблицу
            self.fill_table()
            
            # Обновляем информацию
            self.count_label.config(text=f"Записей: {len(self.data)}")
            
            # Показываем информацию о массивах
            if self.array_data:
                arrays_info = f"Найдено массивов: {len(self.array_data)}"
                self.detail_label.config(text=arrays_info, fg="green")
            
            return True
            
        except ET.ParseError as e:
            messagebox.showerror("Ошибка парсинга", f"Неверный формат XML:\n{str(e)}")
            return False
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить файл:\n{str(e)}")
            return False
    
    def get_type_size(self, tp):
        """Определение размера типа данных"""
        type_sizes = {
            'unsigned char': 1,
            'signed char': 1,
            'unsigned int': 2,
            'signed int': 2,
            'unsigned long': 4,
            'signed long': 4,
            'float': 4,
            'double': 8,
        }
        return type_sizes.get(tp, 0)
    
    def fill_table(self):
        """Заполнение таблицы данными"""
        # Очищаем таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Заполняем данными
        for row in self.data:
            values = [
                row.get('count', ''),
                row.get('class', ''),
                row.get('name', ''),
                row.get('type', ''),
                row.get('caption', ''),
                row.get('value', ''),
                row.get('is_array', '')
            ]
            self.tree.insert('', tk.END, values=values)
    
    def refresh_table(self):
        """Обновление таблицы"""
        if self.current_file:
            self.parse_xml(self.current_file)
        else:
            messagebox.showinfo("Информация", "Сначала выберите XML файл")
    
    def clear_all(self):
        """Очистка всех данных"""
        # Очищаем таблицу
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Очищаем данные
        self.data = []
        self.array_data = {}
        self.current_file = None
        
        # Обновляем статус
        self.status_label.config(text="Очищено", fg="blue")
        self.info_label.config(text="Файл не загружен")
        self.count_label.config(text="Записей: 0")
        self.detail_label.config(text="")
    
    def export_csv(self):
        """Экспорт данных в CSV"""
        if not self.data:
            messagebox.showwarning("Предупреждение", "Нет данных для экспорта")
            return
        
        filename = filedialog.asksaveasfilename(
            title="Сохранить как CSV",
            defaultextension=".csv",
            filetypes=[
                ("CSV files", "*.csv"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                import csv
                with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
                    writer = csv.writer(f)
                    
                    # Заголовки
                    headers = ['№', 'Класс', 'Имя', 'Тип', 'Описание', 'Значение', 'Массив']
                    writer.writerow(headers)
                    
                    # Данные
                    for row in self.data:
                        writer.writerow([
                            row.get('count', ''),
                            row.get('class', ''),
                            row.get('name', ''),
                            row.get('type', ''),
                            row.get('caption', ''),
                            row.get('value', ''),
                            row.get('is_array', '')
                        ])
                
                messagebox.showinfo("Успех", f"Данные сохранены в:\n{filename}")
                
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить:\n{str(e)}")
    
    def on_item_select(self, event):
        """Обработка выбора строки в таблице"""
        selected = self.tree.selection()
        if selected:
            values = self.tree.item(selected[0], 'values')
            if values:
                name = values[2]
                tp = values[3]
                caption = values[4]
                
                # Обновляем детальную информацию
                detail = f"Выбран: {name} (тип: {tp}"
                if caption:
                    detail += f", описание: {caption}"
                detail += ")"
                self.detail_label.config(text=detail, fg="blue")

# ============================================
# ЗАПУСК ПРИЛОЖЕНИЯ
# ============================================

if __name__ == "__main__":
    root = tk.Tk()
    app = XMLTableApp(root)
    root.mainloop()