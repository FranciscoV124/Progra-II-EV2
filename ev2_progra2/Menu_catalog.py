# menu_catalog.py
from typing import List
from ElementoMenu import CrearMenu
from Ingrediente import Ingrediente
from IMenu import IMenu

def get_default_menus() -> List[IMenu]:
    return [
        CrearMenu(
            "Completo",
            [
                Ingrediente("Vienesa","unid", 1),
                Ingrediente("Pan de completo","unid", 1),
                Ingrediente("Palta","kg",0.5),
                Ingrediente("Tomate","kg",0.2),
            ],
            precio=1800,
            icono_path="IMG/icono_hotdog_sin_texto_64x64.png",
        ),
        CrearMenu(
            "Chorrillana",
            [
                Ingrediente("Papas fritas", "kg", 0.5),
                Ingrediente("Carne", "kg", 0.3),
                Ingrediente("Cebolla", "kg", 0.1),
                Ingrediente("Huevos", "unid", 2),
            ],
            precio=6000,
            icono_path="IMG/icono_chorrillana_64x64.png",
        ),
        CrearMenu(
            "Cola",
            [
                Ingrediente("Cola", "botella", 1),
            ],
            precio=1200,
            icono_path="IMG/icono_cola_64x64.png",
        ),
        CrearMenu(
            "Cola lata",
            [
                Ingrediente("Cola lata", "lata", 1),
            ],
            precio=900,
            icono_path="IMG/icono_cola_lata_64x64.png",
        ),
        CrearMenu(
            "Empanada queso",
            [
                Ingrediente("Empanada queso", "unid", 1),
            ],
            precio=1500,
            icono_path="IMG/icono_empanada_queso_64x64.png",
        ),
        CrearMenu(
            "Hamburguesa",
            [
                Ingrediente("Pan de hamburguesa", "unid", 1),
                Ingrediente("Carne hamburguesa", "unid", 1),
                Ingrediente("Queso", "unid", 1),
                Ingrediente("Lechuga", "hoja", 2),
                Ingrediente("Tomate", "rodaja", 2),
            ],
            precio=2500,
            icono_path="IMG/icono_hamburguesa_negra_64x64.png",
        ),
        CrearMenu(
            "Papas fritas",
            [
                Ingrediente("Papas fritas", "kg", 0.3),
            ],
            precio=1800,
            icono_path="IMG/icono_papas_fritas_64x64.png",
        ),
    ]