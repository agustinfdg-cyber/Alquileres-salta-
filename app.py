import streamlit as st

# Configuración de página móvil
st.set_page_config(page_title="Alquileres Salta", page_icon="🏠", layout="centered")

# Estilos CSS personalizados inspirados en la maqueta
st.markdown("""
    <style>
        .main-header {
            font-size: 26px;
            font-weight: 700;
            margin-bottom: 2px;
        }
        .sub-header {
            font-size: 14px;
            color: #6c757d;
            margin-bottom: 20px;
        }
        .prop-card {
            background-color: #ffffff;
            border: 1px solid #e9ecef;
            border-radius: 16px;
            padding: 18px;
            margin-bottom: 16px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        }
        .prop-title {
            font-size: 18px;
            font-weight: 600;
            color: #212529;
            margin-bottom: 6px;
        }
        .prop-badge {
            display: inline-block;
            padding: 4px 10px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            background-color: #e7f5ff;
            color: #1971c2;
            margin-bottom: 10px;
        }
        .prop-price {
            font-size: 17px;
            font-weight: 700;
            color: #2b8a3e;
            margin-bottom: 6px;
        }
        .prop-location {
            font-size: 14px;
            color: #495057;
            margin-bottom: 4px;
        }
        .prop-desc {
            font-size: 13px;
            color: #868e96;
            margin-top: 8px;
            margin-bottom: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Encabezado
st.markdown('<div class="main-header">🏠 Alquileres Salta</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">2 a 3 Dormitorios · Centro / Macrocentro · Hasta $850.000 ARS</div>', unsafe_allow_html=True)

# Pestañas estilo botones principales (como en la maqueta)
tab_deptos, tab_casas = st.tabs(["🏢 Departamentos (2 y 3 Dorm)", "🏡 Casas y Dúplex"])

# ================= SECCIÓN DEPARTAMENTOS =================
with tab_deptos:
    st.caption("Opciones destacadas en edificios con ascensor / seguridad:")
    
    deptos = [
        {
            "badge": "ZONA CENTRO",
            "titulo": "Depto 2 Dormitorios en Lerma al 90",
            "precio": "$650.000 ARS",
            "ubicacion": "📍 Lerma 91 esq. Alvarado (A 4 cuadras de Deán Funes)",
            "desc": "80 m², 2 dormitorios, 2 baños completos, cocina separada y living comedor.",
            "fuente": "InmoUP / Inmobiliaria",
            "link": "https://inmoup.com.ar/departamentos-en-alquiler-en-salta"
        },
        {
            "badge": "CERCANO A TRABAJO",
            "titulo": "Depto 2 Dormitorios en Deán Funes al 300",
            "precio": "$750.000 ARS",
            "ubicacion": "📍 Deán Funes 300 (Centro)",
            "desc": "2 dormitorios con placares, cocina equipada, muy luminoso, excelente conectividad.",
            "fuente": "Mercado Libre Inmuebles",
            "link": "https://inmuebles.mercadolibre.com.ar/departamentos/alquiler/salta/salta/centro/_PriceRange_0-850000"
        },
        {
            "badge": "AMPLIO",
            "titulo": "Depto 3 Ambientes / 2 Dorm en Pueyrredón al 300",
            "precio": "$580.000 ARS",
            "ubicacion": "📍 Pueyrredón al 300 (Cerca de Colegio El Huerto)",
            "desc": "2 dormitorios cómodos, edificio seguro, balcón y excelente ventilación.",
            "fuente": "Argenprop",
            "link": "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios-o-3-dormitorios/pesos-hasta-850000"
        }
    ]

    for d in deptos:
        with st.container(border=True):
            st.markdown(f"**{d['titulo']}**")
            st.markdown(f"💰 **{d['precio']}**")
            st.markdown(d['ubicacion'])
            st.caption(d['desc'])
            st.link_button("🔗 Ver Publicación Completa", d['link'], use_container_width=True)

    st.markdown("#### 🔍 Ver todos los Departamentos filtrados hasta $850.000:")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🔷 Zonaprop Deptos", "https://www.zonaprop.com.ar/departamentos-alquiler-centro-ciudad-orden-precio-ascendente.html", use_container_width=True)
    with col2:
        st.link_button("🏢 Argenprop Deptos", "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios-o-3-dormitorios/pesos-hasta-850000", use_container_width=True)


# ================= SECCIÓN CASAS =================
with tab_casas:
    st.caption("Opciones con patio / espacio independiente:")
    
    casas = [
        {
            "badge": "MACROCENTRO",
            "titulo": "Dúplex 2 Dormitorios en Zona Pueyrredón",
            "precio": "$600.000 ARS",
            "ubicacion": "📍 Pasaje Cancha Rayada (Cerca de Av. Entre Ríos)",
            "desc": "Distribución en 2 plantas, 2 dormitorios, patio chico privado, sin expensas.",
            "fuente": "Trovit / Directo",
            "link": "https://casas.trovitargentina.com.ar/alquiler-casa-macrocentro-salta"
        },
        {
            "badge": "3 DORMITORIOS",
            "titulo": "Casa 3 Dormitorios con Cochera y Patio",
            "precio": "$850.000 ARS",
            "ubicacion": "📍 Zona Norte / Acceso Rápido Centro",
            "desc": "145 m², 3 habitaciones, living comedor amplio, garage techado y patio.",
            "fuente": "Argenprop Casas",
            "link": "https://www.argenprop.com/casas/alquiler/salta/2-dormitorios-o-3-dormitorios/pesos-hasta-850000"
        }
    ]

    for c in casas:
        with st.container(border=True):
            st.markdown(f"**{c['titulo']}**")
            st.markdown(f"💰 **{c['precio']}**")
            st.markdown(c['ubicacion'])
            st.caption(c['desc'])
            st.link_button("🔗 Ver Publicación Completa", c['link'], use_container_width=True)

    st.markdown("#### 🔍 Ver todas las Casas filtradas hasta $850.000:")
    col3, col4 = st.columns(2)
    with col3:
        st.link_button("🟡 Mercado Libre Casas", "https://inmuebles.mercadolibre.com.ar/casas/alquiler/salta/salta/_PriceRange_0-850000", use_container_width=True)
    with col4:
        st.link_button("🏬 Facebook Casas", "https://www.facebook.com/marketplace/salta/propertyrentals/?minPrice=100000&maxPrice=850000&query=alquiler%20casa%20salta", use_container_width=True)
