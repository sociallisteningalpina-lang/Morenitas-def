#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Clasificador de Temas para Comentarios de Campañas
Personalizable por campaña/producto
"""

import re
from typing import Callable

def create_topic_classifier() -> Callable[[str], str]:
    """
    Retorna una función de clasificación de temas personalizada para la campaña 
    Bon Yurt Morenitas (efecto Mandela/nostalgia).
    
    Returns:
        function: Función que toma un comentario (str) y retorna un tema (str)
    
    Usage:
        classifier = create_topic_classifier()
        tema = classifier("Está muy caro, antes valía menos")
        # tema = 'Quejas de Precio'
    """
    
    def classify_topic(comment: str) -> str:
        """
        Clasifica un comentario sobre Bon Yurt Morenitas en categorías específicas.
        
        Args:
            comment: Texto del comentario a clasificar
            
        Returns:
            str: Nombre del tema asignado
        """
        comment_lower = str(comment).lower()
        
        # CATEGORÍA 1: Quejas de Precio (muy común en los datos)
        if re.search(
            r'\bcaro\b|\bcostoso\b|precio|vale|atraco|ladr[oó]n|estafa|'
            r'\$\d+|5000|4500|4200|cuesta|costar|imposible.*comer|'
            r'muy costoso|tan costoso|por las nubes|un ri[ñn][óo]n|'
            r'careros|bajen.*precio|vale mas|trae menos',
            comment_lower
        ):
            return 'Quejas de Precio'
        
        # CATEGORÍA 2: Nostalgia y Recuerdos Positivos
        if re.search(
            r'infancia|ni[ñn]o|ni[ñn]a|recuerdo|cuando era|'
            r'antes|antiguamente|en esa [eé]poca|35 a[ñn]os|'
            r'marcando.*ni[ñn]ez|hace.*a[ñn]os|1988|de ni[ñn][oa]|'
            r'mi padre.*tra[ií]a|buenos? recuerdo|'
            r'primera presentaci[oó]n|aprend[ií] a comer',
            comment_lower
        ):
            return 'Nostalgia y Recuerdos Positivos'
        
        # CATEGORÍA 3: Crítica de Calidad del Producto (contenido, sabor, consistencia)
        if re.search(
            r'trae menos|viene menos|medio vasito|mitad.*vac[ií]o|'
            r'pura agua|parece agua|no trae casi nada|menos de la mitad|'
            r'se cuentan las hojuelas|traía m[aá]s|cuando era[ns]? ricos?|'
            r'espesito|cuando.*sab[ií]a|ya no sabe|sabor a remedio|'
            r'puro az[uú]car|melado|basura|mierda|maluco|p[eé]simo|'
            r'sellos negros|calavera|veneno|diabetes|coma diab[eé]tico',
            comment_lower
        ):
            return 'Crítica de Calidad del Producto'
        
        # CATEGORÍA 4: Opinión Positiva del Producto
        if re.search(
            r'\brico\b|delicioso|sabroso|vale la pena|simplemente delicioso|'
            r'mi.*favorito|me encanta|lo compro|lo compraba|'
            r'nunca.*cambia|[eé]l sabor|👍|❤️|😋|'
            r'quiero probar|me gustar[ií]a probar',
            comment_lower
        ):
            return 'Opinión Positiva del Producto'
        
        # CATEGORÍA 5: Engagement con Influencer/Famoso (referencias a actores, personajes)
        if re.search(
            r'emilio|iriarte|walter|blanco|laisa|umaña|violeta|'
            r'los reyes|a bestia|abestia|met[aá]stasis|'
            r'di mi nombre|diego|actor|personaje|novela|'
            r'ecomoda|petrista|petro|capitalismo|izquierdista|'
            r'peso pluma|kevin johansen|gatos?|michis?|gatitos?|peludos',
            comment_lower
        ):
            return 'Engagement con Influencer/Famoso'
        
        # CATEGORÍA 6: Comentarios sobre Accesibilidad/Lujo (no podían comprarlo antes)
        if re.search(
            r'lujo|nunca ten[ií]a para|no tomaba.*caro|'
            r'toca probar.*uno|imposible.*comer|'
            r'de adulta.*al a[ñn]o|vine.*de grande|'
            r'mi mam[aá].*nunca|para los ricos?|no adopt[ae]n',
            comment_lower
        ):
            return 'Comentarios sobre Accesibilidad/Lujo'
        
        # CATEGORÍA 7: Comentarios sobre Promoción/Marketing
        if re.search(
            r'promoci[oó]n|premio|dependencia|tajalapiz|'
            r'efecto mandela|deber[ií]an hacer|publicidad|'
            r'inteligencia artificial|\bIA\b|propaganda|'
            r'aprovech[aá]ndose.*ni[ñn]os',
            comment_lower
        ):
            return 'Comentarios sobre Promoción/Marketing'
        
        # CATEGORÍA 8: Disponibilidad y Distribución
        if re.search(
            r'd[oó]nde.*consigo|d[oó]nde.*comprar|'
            r'sacaron.*departamento|antioquia|no gust[oó]|'
            r'cuando sale|ya no vende',
            comment_lower
        ):
            return 'Disponibilidad y Distribución'
        
        # CATEGORÍA 9: Interacciones Simples y Fuera de Tema
        if re.search(
            r'^jaja+$|^ja+$|^am[eé]n$|^si$|^no$|^\?+$|'
            r'^❤+$|^✨+$|^\[sticker\]$|'
            r'gracias a dios|hermosos?|bendiga|belleza|bellos?|'
            r'tan lindos?|que lindos?|firmes con|like.*comentario',
            comment_lower
        ) or len(comment_lower.split()) < 4:
            return 'Interacciones Simples y Fuera de Tema'
        
        # CATEGORÍA 10: Otros Comentarios del Producto Alpina (kumis, leche, otros)
        if re.search(
            r'kumis|leche|alpina|producto.*alpina|'
            r'empresa|marca|yogur|yogurt',
            comment_lower
        ):
            return 'Otros Productos Alpina'
        
        # CATEGORÍA DEFAULT: Otros
        return 'Otros'
    
    return classify_topic


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear el clasificador
    classifier = create_topic_classifier()
    
    # Probar con algunos comentarios de ejemplo
    test_comments = [
        "$5000 un vasito de estos es un atraco",
        "Como los de mi infancia",
        "Ahora trae menos y parece agua",
        "Delicioso como siempre",
        "Eres Iriarte el de Los Reyes",
        "Nunca tenía para comprarlo de niño",
        "Deberían hacer una promoción buena",
        "❤️❤️",
        "El kumis es pura agua"
    ]
    
    print("=== PRUEBA DEL CLASIFICADOR ===\n")
    for comment in test_comments:
        tema = classifier(comment)
        print(f"Comentario: '{comment}'")
        print(f"Tema: {tema}\n")
# ============================================================================
# METADATA DE LA CAMPAÑA (OPCIONAL)
# ============================================================================

CAMPAIGN_METADATA = {
    'campaign_name': 'Alpina - Kéfir',
    'product': 'Kéfir Alpina',
    'categories': [
        'Preguntas sobre el Producto',
        'Comparación con Kéfir Casero/Artesanal',
        'Ingredientes y Salud',
        'Competencia y Disponibilidad',
        'Opinión General del Producto',
        'Fuera de Tema / No Relevante',
        'Otros'
    ],
    'version': '1.0',
    'last_updated': '2025-11-20'
}


def get_campaign_metadata() -> dict:
    """Retorna metadata de la campaña"""
    return CAMPAIGN_METADATA.copy()
