import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import re  # Импортируем регулярные выражения

# Глобальные счетчики
row_counter = 0
item_idx_counter = 0
#onEp = 0

def parse_to_tree(xml_element, parent_tree_id="", parent_node=None):
    """Рекурсивно заполняет Treeview данными из XML, разворачивая массивы типа parametr[3]"""
    global row_counter, item_idx_counter
    
    node_text = xml_element.tag
    name_attr = xml_element.attrib.get('name', '')
    onEp = 0                                                                                                          #++
    #if parent_node is not None and parent_node.tag == "ram":
        #print(f"[Найдено в RAM] Элемент: <{node_text}>, Name: '{name_attr}', Родитель: <{parent_node.tag}>")
    # Регулярное выражение ищет шаблон: любое_имя[число] в конце строки
    # Например: "parametr[3]" -> группа 1: "parametr", группа 2: "3"
    match = re.search(r'^(.+)\[(\d+)\]$', name_attr)
    
    if node_text == 'item' and match:
        
        # Если это item и имя является массивом
        base_name = match.group(1)      # "parametr"
        array_size = int(match.group(2)) # 3
        
        # Разворачиваем массив в цикл от 0 до array_size - 1
        for i in range(array_size):
            
            item_display_num = str(item_idx_counter)
            if xml_element.attrib.get('type', '') == 'unsigned char' : item_idx_counter += 1
            if xml_element.attrib.get('type', '') == 'signed char' : item_idx_counter += 1
            if xml_element.attrib.get('type', '') == 'unsigned long' : item_idx_counter += 4
            if xml_element.attrib.get('type', '') == 'float' : item_idx_counter += 4
            if xml_element.attrib.get('type', '') == 'unsigned int' : item_idx_counter += 2
            
            # Формируем новое индексированное имя, например "parametr[0]"
            indexed_name = f"{base_name}[{i}]"
            
            #item_idx_counter += 1
            # Остальные атрибуты берем без изменений
            el_type = xml_element.attrib.get('type', '')
            
            caption = xml_element.attrib.get('caption', '')
            value = xml_element.attrib.get('value', '')

            row_tag = "evenrow" if row_counter % 2 == 0 else "oddrow"
            row_counter += 1
            
            # Вставляем элемент массива в таблицу
            current_tree_id = table.insert(
                parent_tree_id, 
                tk.END, 
                text=node_text, 
                values=(item_display_num, indexed_name, el_type, caption, value),
                tags=(row_tag,)
            )
            
            # Если у исходного элемента-массива были дочерние узлы (например, mode или mask),
            # мы копируем их внутрь каждого элемента развернутого массива
            for child in xml_element:
                parse_to_tree(child, current_tree_id, parent_node=xml_element)
                
    else:
        # Стандартная обработка для обычных элементов (не массивов)
        name_or_addr = name_attr if name_attr else xml_element.attrib.get('address', '')
        el_type = xml_element.attrib.get('type', '')
        caption = xml_element.attrib.get('caption', '')
        value = xml_element.attrib.get('value', '')
        
        if node_text == 'item':
            #if parent_node.tag == 'EPROM' and onEp == 0 : item_idx_counter = 8192; onEp += 1;
            item_display_num = str(item_idx_counter)            
            
            print(parent_node.tag)
            if xml_element.attrib.get('type', '') == 'unsigned char' : item_idx_counter += 1
            if xml_element.attrib.get('type', '') == 'signed char' : item_idx_counter += 1
            if xml_element.attrib.get('type', '') == 'unsigned long' : item_idx_counter += 4
            if xml_element.attrib.get('type', '') == 'float' : item_idx_counter += 4
            if xml_element.attrib.get('type', '') == 'unsigned int' : item_idx_counter += 2
            
        else:
            item_display_num = ""

        row_tag = "evenrow" if row_counter % 2 == 0 else "oddrow"
        row_counter += 1
        
        current_tree_id = table.insert(
            parent_tree_id, 
            tk.END, 
            text=node_text, 
            values=(item_display_num, name_or_addr, el_type, caption, value),
            tags=(row_tag,)
        )
        
        # Рекурсивный обход детей для обычного элемента
        for child in xml_element:
            parse_to_tree(child, current_tree_id, parent_node=xml_element)


def load_xml_file():
    """Открывает диалоговое окно проводника и загружает выбранный XML"""
    global row_counter, item_idx_counter
    
    file_path = filedialog.askopenfilename(
        title="Выберите XML файл конфигурации",
        filetypes=[("XML файлы", "*.xml"), ("Все файлы", "*.*")]
    )
    
    if not file_path:
        return
        
    try:
        # Для демонстрации парсим тестовую строку, если файл не выбран на диске. 
        # В реальности всегда читаем file_path:
        tree = ET.parse(file_path)
        root_node = tree.getroot()
        
        for item in table.get_children():
            table.delete(item)
            
        row_counter = 0
        item_idx_counter = 0
        
        parse_to_tree(root_node)
        
        for child_id in table.get_children():
            table.item(child_id, open=True)
            
        device_caption = root_node.attrib.get('caption', 'Устройство')
        root_window.title(f"Конфигурация устройства: {device_caption}")
        
    except ET.ParseError:
        messagebox.showerror("Ошибка", "Выбранный файл не является валидным XML или поврежден!")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось прочитать файл:\n{str(e)}")


# --- БЛОК СОЗДАНИЯ ИНТЕРФЕЙСА (UI) ---
root_window = tk.Tk()
root_window.title("Проводник конфигураций устройства")
root_window.geometry("920x500")

toolbar = tk.Frame(root_window, bd=1, relief=tk.RAISED)
toolbar.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

load_btn = ttk.Button(toolbar, text="📁 Загрузить XML...", command=load_xml_file)
load_btn.pack(side=tk.LEFT, padx=5, pady=5)

style = ttk.Style()
style.configure("Treeview", rowheight=25, ttk_gridlines=True)

columns = ("item_num", "attr_name", "attr_type", "attr_caption", "attr_val")
table = ttk.Treeview(root_window, columns=columns, show=["tree", "headings"])
table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

table.tag_configure("evenrow", background="#f9f9f9")
table.tag_configure("oddrow", background="#ffffff")

table.heading("#0", text="Элемент / XML Тег", anchor=tk.W)
table.column("#0", width=150, minwidth=120)

table.heading("item_num", text="№ item")
table.column("item_num", width=60, minwidth=50, anchor=tk.CENTER)

table.heading("attr_name", text="name / address")
table.column("attr_name", width=120, anchor=tk.W)

table.heading("attr_type", text="type")
table.column("attr_type", width=120, anchor=tk.W)

table.heading("attr_caption", text="caption")
table.column("attr_caption", width=350, anchor=tk.W)

table.heading("attr_val", text="value")
table.column("attr_val", width=80, anchor=tk.CENTER)

# Запустим изначально встроенную демонстрацию, чтобы сразу видеть результат
demo_xml = """<device name="IK11" caption="ИК-11">
    <ram>
        <item name="dID" type="unsigned int" caption="Ид контр "/>
        <item name="parametr[3]" type="int" caption="Массив датчиков">
            <mode value="1" caption="Активен"/>
        </item>
	</ram>
    <EPROM address="8192">
        <item name="deviceDefault" caption="Если == 0xFF -> восстановление EPROM по умолчанию" type="unsigned char"/>
        <item name="deviceFlashed" type="unsigned char"/>
    </EPROM>
</device>"""
parse_to_tree(ET.fromstring(demo_xml))
for child_id in table.get_children():
    table.item(child_id, open=True)

root_window.mainloop()
