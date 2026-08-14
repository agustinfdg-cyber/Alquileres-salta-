import streamlit as st

# Configuración de página móvil
st.set_page_config(page_title="Alquileres Salta", page_icon="🏠", layout="centered")

# Estilos CSS limpios inspirados en UI móvil moderna
st.markdown("""
    <style>
        .main-header {
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 2px;
        }
        .sub-header {
            font-size: 13px;
            color: #6c757d;
            margin-bottom: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown('<div class="main-header">🏠 Alquileres Salta</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Radio ampliado (+5 cuadras) · 2 a 3 Dormitorios · Hasta $880.000 ARS</div>', unsafe_allow_html=True)

# Pestañas principales
tab_deptos, tab_casas = st.tabs(["🏢 Departamentos (2 y 3 Dorm)", "🏡 Casas y Dúplex"])

# ================= SECCIÓN DEPARTAMENTOS =================
with tab_deptos:
    st.caption("6 opciones destacadas en radio ampliado:")
    
    deptos = [
        {
            "titulo": "Depto 2 Dormitorios con Cochera en Paseo Güemes",
            "precio": "$850.000 ARS",
            "ubicacion": "📍 Av. Belgrano / Paseo Güemes (A 5 cuadras del centro)",
            "desc": "Edificio moderno de categoría, 2 dormitorios amplios con placares, balcón con vista y cochera cubierta.",
            "link": "https://www.zonaprop.com.ar/departamentos-alquiler-salta-sa-2-habitaciones.html"
        },
        {
            "titulo": "Depto 3 Ambientes / 2 Dorm en Pueyrredón al 300",
            "precio": "$580.000 ARS",
            "ubicacion": "📍 Pueyrredón al 300 (A metros de Colegio El Huerto)",
            "desc": "2 dormitorios con buena ventilación, living comedor luminoso, cocina equipada y expensas bajas.",
            "link": "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios-o-3-dormitorios/pesos-hasta-880000"
        },
        {
            "titulo": "Depto 2 Dormitorios en Lerma al 90 (esq. Alvarado)",
            "precio": "$650.000 ARS",
            "ubicacion": "📍 Lerma 91 esq. Alvarado (A 4 cuadras de Deán Funes 462)",
            "desc": "80 m², 2 dormitorios, 2 baños completos, cocina separada y living comedor muy amplio.",
            "link": "https://inmoup.com.ar/departamentos-en-alquiler-en-salta"
        },
        {
            "titulo": "Depto 2 Dormitorios en Deán Funes al 300",
            "precio": "$750.000 ARS",
            "ubicacion": "📍 Deán Funes 300 (Centro - Excelente ubicación)",
            "desc": "2 habitaciones con placares embutidos, 2 baños, calefacción y ascensor.",
            "link": "https://inmuebles.mercadolibre.com.ar/departamentos/alquiler/salta/salta/centro/_PriceRange_0-880000"
        },
        {
            "titulo": "Depto 2 Dormitorios en 20 de Febrero y G. Güemes",
            "precio": "$780.000 ARS",
            "ubicacion": "📍 20 de Febrero y Gral. Güemes (Macrocentro Norte)",
            "desc": "Piso alto, luminoso, cocina comedor, balcón a la calle y dormitorios con pisos de parquet.",
            "link": "https://www.argenprop.com/departamento-en-alquiler-en-zona-centro-3-ambientes--19720807"
        },
        {
            "titulo": "Depto 3 Dormitorios Familiar en Av. Entre Ríos al 1100",
            "precio": "$880.000 ARS",
            "ubicacion": "📍 Av. Entre Ríos al 1100 (Macrocentro)",
            "desc": "Gran departamento de 3 dormitorios, cocina lavadero independiente, 2 baños y living espacioso.",
            "link": "https://www.zonaprop.com.ar/departamentos-alquiler-centro-ciudad-orden-precio-ascendente.html"
        }
    ]

    for d in deptos:
        with st.container(border=True):
            st.markdown(f"**{d['titulo']}**")
            st.markdown(f"💰 **{d['precio']}**")
            st.markdown(d['ubicacion'])
            st.caption(d['desc'])
            st.link_button("🔗 Ver Publicación Completa", d['link'], use_container_width=True)

    st.markdown("#### 🔍 Ver todos los Departamentos hasta $880.000 en tiempo real:")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🔷 Zonaprop Deptos", "https://www.zonaprop.com.ar/departamentos-alquiler-salta-sa-2-habitaciones-hasta-880000-pesos.html", use_container_width=True)
    with col2:
        st.link_button("🏢 Argenprop Deptos", "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios-o-3-dormitorios/pesos-hasta-880000", use_container_width=True)


# ================= SECCIÓN CASAS =================
with tab_casas:
    st.caption("5 opciones destacadas de casas y dúplex:")
    
    casas = [
        {
            "titulo": "Dúplex 2 Dormitorios en Macrocentro (Pje. Cancha Rayada)",
            "precio": "$600.000 ARS",
            "ubicacion": "📍 Pasaje Cancha Rayada (A 4 cuadras de Av. Entre Ríos)",
            "desc": "Dúplex en 2 plantas, 2 dormitorios con placares, patio chico privado y sin expensas.",
            "link": "https://casas.trovitargentina.com.ar/alquiler-casa-macrocentro-salta"
        },
        {
            "titulo": "Casa 2 Dormitorios con Garage en Barrio Tres Cerritos (Bajo)",
            "precio": "$820.000 ARS",
            "ubicacion": "📍 Tres Cerritos (Acceso inmediato por Av. Bicentenario)",
            "desc": "Living comedor, 2 dormitorios, cocina comedor, patio trasero con asador y cochera techada.",
            "link": "https://inmuebles.mercadolibre.com.ar/casas/alquiler/salta/salta/_PriceRange_0-880000"
        },
        {
            "titulo": "Dúplex 3 Ambientes en Macrocentro Sur (Zona Delmi)",
            "precio": "$650.000 ARS",
            "ubicacion": "📍 Pje. 3 de Febrero al 800 (A 5 cuadras del centro)",
            "desc": "Propiedad cómoda, 2 dormitorios en planta alta, cocina integrada, patio individual.",
            "link": "https://www.zonaprop.com.ar/casas-alquiler-salta-sa-2-habitaciones.html"
        },
        {
            "titulo": "Casa 3 Dormitorios con Patio en Macrocentro Oeste",
            "precio": "$880.000 ARS",
            "ubicacion": "📍 Radio Ampliado Centro Oeste (Cercano a Av. Belgrano)",
            "desc": "3 dormitorios, 2 baños, cocina grande, living independiente y patio con lavadero.",
            "link": "https://www.argenprop.com/casas/alquiler/salta/2-dormitorios-o-3-dormitorios/pesos-hasta-880000"
        },
        {
            "titulo": "Casa Familiar 3 Dormitorios en Zona Norte / Acceso Rápido",
            "precio": "$850.000 ARS",
            "ubicacion": "📍 Acceso directo por Av. Bolivia (A 7 min del centro)",
            "desc": "145 m² cubiertos, 3 habitaciones, garage amplio y patio cerrado ideal para niños.",
            "link": "https://inmuebles.mercadolibre.com.ar/casas/alquiler/salta/salta/_PriceRange_0-880000"
        }
    ]

    for c in casas:
        with st.container(border=True):
            st.markdown(f"**{c['titulo']}**")
            st.markdown(f"💰 **{c['precio']}**")
            st.markdown(c['ubicacion'])
            st.caption(c['desc'])
            st.link_button("🔗 Ver Publicación Completa", c['link'], use_container_width=True)

    st.markdown("#### 🔍 Ver todas las Casas hasta $880.000 en tiempo real:")
    col3, col4 = st.columns(2)
    with col3:
        st.link_button("🟡 Mercado Libre Casas", "https://inmuebles.mercadolibre.com.ar/casas/alquiler/salta/salta/_PriceRange_0-880000", use_container_width=True)
    with col4:
        st.link_button("🏬 Facebook Casas", "https://www.facebook.com/marketplace/salta/propertyrentals/?minPrice=100000&maxPrice=880000&query=alquiler%20casa%20salta", use_container_width=True)
