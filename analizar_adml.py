import xml.etree.ElementTree as ET

# Parsear el archivo XML ADML
tree = ET.parse('adml.xml')  # Reemplaza 'ruta_del_archivo.xml' con la ubicación de tu archivo ADML
root = tree.getroot()

# Extraer información de componentes
for component in root.findall(".//adml:component", namespaces={"adml": "http://example.com/adml"}):
    component_id = component.get("id")
    component_name = component.find("adml:name", namespaces={"adml": "http://example.com/adml"}).text
    component_description = component.find("adml:description", namespaces={"adml": "http://example.com/adml"}).text
    print(f"Componente ID: {component_id}")
    print(f"Nombre: {component_name}")
    print(f"Descripción: {component_description}")
    print("<-------------------------------------------------------->")
    
    # Extraer información de interfaces
    interfaces = component.findall(".//adml:interface", namespaces={"adml": "http://example.com/adml"})
    for interface in interfaces:
        interface_id = interface.get("id")
        interface_name = interface.find("adml:name", namespaces={"adml": "http://example.com/adml"}).text
        interface_description = interface.find("adml:description", namespaces={"adml": "http://example.com/adml"}).text
        print(f"  - Interface ID: {interface_id}")
        print(f"  - Nombre: {interface_name}")
        print(f"  - Descripción: {interface_description}")
        print("<-------------------------------------------------------->")

# Extraer información de relaciones
for relation in root.findall(".//adml:relation", namespaces={"adml": "http://example.com/adml"}):
    relation_source = relation.find("adml:source", namespaces={"adml": "http://example.com/adml"}).get("id")
    relation_target = relation.find("adml:target", namespaces={"adml": "http://example.com/adml"}).get("id")
    relation_type = relation.find("adml:type", namespaces={"adml": "http://example.com/adml"}).text
    relation_description = relation.find("adml:description", namespaces={"adml": "http://example.com/adml"}).text
    print(f"Relación: {relation_type}")
    print(f"Fuente: {relation_source}")
    print(f"Destino: {relation_target}")
    print(f"Descripción: {relation_description}")
    print("<-------------------------------------------------------->")
