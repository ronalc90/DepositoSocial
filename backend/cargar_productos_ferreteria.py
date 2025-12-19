import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
django.setup()

from productos.models import Producto, Categoria

# Limpiar productos existentes
Producto.objects.all().delete()
Categoria.objects.all().delete()

# Crear categorías
categorias_data = [
    {"nombre": "Herramientas Eléctricas", "descripcion": "Taladros, sierras, lijadoras", "orden": 1},
    {"nombre": "Herramientas Manuales", "descripcion": "Martillos, destornilladores, llaves", "orden": 2},
    {"nombre": "Pinturas y Accesorios", "descripcion": "Pinturas, brochas, rodillos", "orden": 3},
    {"nombre": "Plomería", "descripcion": "Tuberías, conexiones, grifería", "orden": 4},
    {"nombre": "Electricidad", "descripcion": "Cables, interruptores, luminarias", "orden": 5},
    {"nombre": "Construcción", "descripcion": "Cemento, arena, ladrillos", "orden": 6},
]

print("🗂️  Creando categorías...")
for cat_data in categorias_data:
    cat, created = Categoria.objects.get_or_create(
        nombre=cat_data['nombre'],
        defaults=cat_data
    )
    if created:
        print(f"  ✅ {cat.nombre}")

# Productos con imágenes realistas de Unsplash
productos_data = [
    {
        "categoria": "Herramientas Eléctricas",
        "subcategoria": "Taladros",
        "marca": "DeWalt",
        "nombre": "Taladro Percutor Inalámbrico 20V",
        "descripcion": "Taladro percutor profesional con batería de litio 20V. Incluye 2 baterías, cargador y maletín. Motor sin escobillas para mayor durabilidad. 13mm mandril metálico.",
        "presentaciones": ["Kit Completo", "Solo Herramienta"],
        "uso": "Construcción/Hogar",
        "caracteristicas": ["20V batería litio", "Motor sin escobillas", "2 velocidades", "Luz LED", "13mm mandril"],
        "precio": 450000,
        "imagen": "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=500",
        "activo": True,
    },
    {
        "categoria": "Herramientas Eléctricas",
        "subcategoria": "Sierras",
        "marca": "Makita",
        "nombre": "Sierra Circular 7-1/4 pulgadas 1800W",
        "descripcion": "Sierra circular profesional con motor de 1800W. Disco de 7-1/4 pulgadas. Corte a 90° hasta 65mm. Incluye guía paralela y llave.",
        "presentaciones": ["Unidad"],
        "uso": "Construcción",
        "caracteristicas": ["1800W potencia", "5500 RPM", "Corte 65mm", "Guía láser", "Freno eléctrico"],
        "precio": 385000,
        "imagen": "https://images.unsplash.com/photo-1572981779307-38b8cabb2407?w=500",
        "activo": True,
    },
    {
        "categoria": "Herramientas Manuales",
        "subcategoria": "Llaves",
        "marca": "Stanley",
        "nombre": "Juego de Llaves Combinadas 12 Piezas",
        "descripcion": "Set de 12 llaves combinadas métricas. Acero cromo vanadio forjado. Acabado cromado. Medidas de 8mm a 19mm.",
        "presentaciones": ["Juego 12 pzs"],
        "uso": "Automotriz/Mecánica",
        "caracteristicas": ["Acero cromo vanadio", "Acabado cromado", "8-19mm", "Estuche incluido"],
        "precio": 125000,
        "imagen": "https://images.unsplash.com/photo-1530124566582-a618bc2615dc?w=500",
        "activo": True,
    },
    {
        "categoria": "Herramientas Manuales",
        "subcategoria": "Martillos",
        "marca": "Truper",
        "nombre": "Martillo de Uña 16 oz Mango Fibra",
        "descripcion": "Martillo de uña con cabeza forjada. Mango de fibra de vidrio antideslizante. 16 onzas. Ideal para carpintería.",
        "presentaciones": ["Unidad"],
        "uso": "Carpintería",
        "caracteristicas": ["16 oz", "Mango fibra vidrio", "Cabeza forjada", "Agarre antideslizante"],
        "precio": 45000,
        "imagen": "https://images.unsplash.com/photo-1567294515635-b3d91c3e3a2a?w=500",
        "activo": True,
    },
    {
        "categoria": "Pinturas y Accesorios",
        "subcategoria": "Pinturas",
        "marca": "Pintuco",
        "nombre": "Viniltex Advanced Galón Blanco",
        "descripcion": "Pintura vinílica premium para interiores. Antibacterial. Ultra lavable. Bajo olor. Rendimiento 40-45 m²/galón.",
        "presentaciones": ["Galón", "Cuñete 5 gal", "1/4 Galón"],
        "uso": "Interior",
        "caracteristicas": ["Antibacterial", "Ultra lavable", "Bajo olor", "Secado rápido", "Acabado mate"],
        "precio": 95000,
        "imagen": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=500",
        "activo": True,
    },
    {
        "categoria": "Pinturas y Accesorios",
        "subcategoria": "Rodillos",
        "marca": "Corona",
        "nombre": "Rodillo Profesional 9\" con Extensión",
        "descripcion": "Rodillo profesional para pintura. Incluye mango telescópico extensible hasta 2.5m. Pelo sintético 13mm.",
        "presentaciones": ["Unidad"],
        "uso": "Pintura",
        "caracteristicas": ["9 pulgadas", "Extensión 2.5m", "Pelo sintético", "Lavable"],
        "precio": 38000,
        "imagen": "https://images.unsplash.com/photo-1562259949-e8e7689d7828?w=500",
        "activo": True,
    },
    {
        "categoria": "Plomería",
        "subcategoria": "Grifería",
        "marca": "FV",
        "nombre": "Mezclador Monocomando Lavamanos",
        "descripcion": "Grifería monocomando para lavamanos. Acabado cromado. Cartucho cerámico. Incluye desagüe automático.",
        "presentaciones": ["Unidad"],
        "uso": "Baño",
        "caracteristicas": ["Acabado cromado", "Cartucho cerámico", "Desagüe automático", "Instalación fácil"],
        "precio": 180000,
        "imagen": "https://images.unsplash.com/photo-1620626011761-996317b8d101?w=500",
        "activo": True,
    },
    {
        "categoria": "Plomería",
        "subcategoria": "Tuberías",
        "marca": "Pavco",
        "nombre": "Tubería PVC Sanitaria 4\" x 3m",
        "descripcion": "Tubería PVC sanitaria color naranja. 4 pulgadas diámetro. Longitud 3 metros. Norma NTC 1339.",
        "presentaciones": ["Tubo 3m"],
        "uso": "Construcción",
        "caracteristicas": ["4 pulgadas", "3 metros", "PVC sanitario", "Norma NTC 1339"],
        "precio": 42000,
        "imagen": "https://images.unsplash.com/photo-1581244277943-fe4a9c777189?w=500",
        "activo": True,
    },
    {
        "categoria": "Electricidad",
        "subcategoria": "Cables",
        "marca": "Centelsa",
        "nombre": "Cable THHN #12 AWG x 100m",
        "descripcion": "Cable de cobre THHN calibre 12. Rollo de 100 metros. 600V. Certificado RETIE. Color negro.",
        "presentaciones": ["Rollo 100m"],
        "uso": "Instalaciones Eléctricas",
        "caracteristicas": ["Calibre #12", "Cobre", "600V", "RETIE", "100 metros"],
        "precio": 185000,
        "imagen": "https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=500",
        "activo": True,
    },
    {
        "categoria": "Electricidad",
        "subcategoria": "Interruptores",
        "marca": "Bticino",
        "nombre": "Interruptor Doble 15A Blanco",
        "descripcion": "Interruptor doble de sobreponer. 15 amperios. Color blanco. Incluye tornillos de fijación.",
        "presentaciones": ["Unidad"],
        "uso": "Instalaciones Eléctricas",
        "caracteristicas": ["15 amperios", "Sobreponer", "Color blanco", "Contactos de plata"],
        "precio": 12000,
        "imagen": "https://images.unsplash.com/photo-1621905251918-48416bd8575a?w=500",
        "activo": True,
    },
    {
        "categoria": "Construcción",
        "subcategoria": "Cemento",
        "marca": "Argos",
        "nombre": "Cemento Gris Uso General 50kg",
        "descripcion": "Cemento Portland gris para uso general. Bulto de 50 kilogramos. Ideal para mampostería, pañetes y concretos.",
        "presentaciones": ["Bulto 50kg"],
        "uso": "Construcción",
        "caracteristicas": ["50 kg", "Uso general", "Alta resistencia", "Fraguado normal"],
        "precio": 32000,
        "imagen": "https://images.unsplash.com/photo-1590856029826-c7a73142bbf1?w=500",
        "activo": True,
    },
    {
        "categoria": "Herramientas Eléctricas",
        "subcategoria": "Lijadoras",
        "marca": "Bosch",
        "nombre": "Lijadora Orbital 250W",
        "descripcion": "Lijadora orbital eléctrica 250W. Base de lijado 115x230mm. Incluye sistema de recolección de polvo y papel lija.",
        "presentaciones": ["Unidad"],
        "uso": "Carpintería",
        "caracteristicas": ["250W", "12000 rpm", "Recolector polvo", "Ergonómica"],
        "precio": 195000,
        "imagen": "https://images.unsplash.com/photo-1572981779307-38b8cabb2407?w=500",
        "activo": True,
    },
    {
        "categoria": "Herramientas Manuales",
        "subcategoria": "Destornilladores",
        "marca": "Stanley",
        "nombre": "Juego Destornilladores 6 Piezas",
        "descripcion": "Set de 6 destornilladores magnéticos. 3 planos + 3 estrella. Mangos ergonómicos. Punta cromada.",
        "presentaciones": ["Juego 6 pzs"],
        "uso": "General",
        "caracteristicas": ["6 piezas", "Punta magnética", "Mango ergonómico", "Cromado"],
        "precio": 55000,
        "imagen": "https://images.unsplash.com/photo-1530124566582-a618bc2615dc?w=500",
        "activo": True,
    },
    {
        "categoria": "Pinturas y Accesorios",
        "subcategoria": "Brochas",
        "marca": "Purdy",
        "nombre": "Brocha Angular 2\" Profesional",
        "descripcion": "Brocha angular profesional 2 pulgadas. Cerda sintética de alta calidad. Mango de madera barnizado.",
        "presentaciones": ["Unidad"],
        "uso": "Pintura",
        "caracteristicas": ["2 pulgadas", "Cerda sintética", "Corte angular", "Mango madera"],
        "precio": 28000,
        "imagen": "https://images.unsplash.com/photo-1562259949-e8e7689d7828?w=500",
        "activo": True,
    },
    {
        "categoria": "Electricidad",
        "subcategoria": "Luminarias",
        "marca": "Philips",
        "nombre": "Panel LED 60x60cm 48W Luz Blanca",
        "descripcion": "Panel LED ultra delgado 60x60cm. 48W consumo. 4000 lúmenes. Luz blanca 6500K. Vida útil 50000 horas.",
        "presentaciones": ["Unidad"],
        "uso": "Iluminación",
        "caracteristicas": ["48W", "4000 lúmenes", "6500K", "50000 horas", "Ultra delgado"],
        "precio": 85000,
        "imagen": "https://images.unsplash.com/photo-1565008447742-97f6f38c985c?w=500",
        "activo": True,
    },
]

print("\n📦 Creando productos de ferretería...")
for prod_data in productos_data:
    prod, created = Producto.objects.get_or_create(
        nombre=prod_data['nombre'],
        marca=prod_data['marca'],
        defaults=prod_data
    )
    if created:
        print(f"  ✅ {prod.marca} - {prod.nombre}")

print("\n✅ ¡Productos de ferretería cargados!")
print(f"📊 Total categorías: {Categoria.objects.count()}")
print(f"📦 Total productos: {Producto.objects.count()}")
