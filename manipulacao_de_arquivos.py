import zipfile
import csv
import json
import xml.etree.ElementTree as ET


# Comprimir arquivos em um arquivo zip
def compress_files(zip_file, files):
    with zipfile.ZipFile(zip_file, 'w') as zf:
        for file in files:
            zf.write(file)

# Descomprimir arquivos de um arquivo zip
def decompress_files(zip_file, destination):
    with zipfile.ZipFile(zip_file, 'r') as zf:
        zf.extractall(destination)

# Ler dados de um arquivo CSV
def read_csv(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

# Escrever dados em um arquivo CSV
def write_csv(file_path, data):
    with open(file_path, 'w') as csv_file:
        writer = csv.writer(csv_file)
        for row in data:
            writer.writerow(row)


# Ler dados de um arquivo JSON
def read_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        print(data)

# Escrever dados em um arquivo JSON
def write_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)


# Ler dados de um arquivo XML
def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    for element in root:
        print(element.tag, element.attrib, element.text)

# Escrever dados em um arquivo XML
def write_xml(file_path, data):
    root = ET.Element('root')
    for item in data:
        element = ET.SubElement(root, item['tag'], attrib=item['attrib'])
        element.text = item['text']
    
    tree = ET.ElementTree(root)
    tree.write(file_path)

