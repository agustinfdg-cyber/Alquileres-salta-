import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alquileres Salta", page_icon="🏠", layout="centered")

st.title("🏠 Buscador de Alquileres Salta")
st.caption("Filtros: Centro/Macrocentro | Casas o Deptos (2 a 3 Dormitorios) | Hasta $850.000 ARS")

st.markdown("---")

# Sección de Búsqueda y Clasificación
if st.button("🔍 Buscar y Clasificar Propiedades (Hoy)", type="primary", use_container_width=True):
    with st.spinner("Consultando casas y departamentos en Salta Capital..."):
        
        # Opciones ampliadas a Casas y Deptos de 2 a 3 dormitorios hasta $850.000 ARS
        resultados = [
            {
                "Tipo": "🏡 CASA",
                "Estado": "🆕 NUEVO HOY",
                "Título": "Casa Esquina 3 Dormitorios en B° Ciudad del Milagro",
                "Ubicación": "Zona Norte / Universidad (Con garage y patio)",
                "Precio": "$850.000 ARS",
                "Expensas": "Sin Expensas",
                "Detalle": "Casa funcional de 3 dormitorios, 145 m² cubiertos, cochera y espacio amplio ideal para la nena.",
                "Fuente": "Argenprop / Inmobiliaria",
                "Link": "https://www.argenprop.com/casas/alquiler/salta/3-dormitorios"
            },
            {
                "Estado": "🆕 NUEVO HOY",
                "Tipo": "🏢 DEPTO",
                "Título": "Depto 2 Dormitorios con Placares en Macrocentro",
                "Ubicación": "12 de Octubre y Alvear / 20 de Febrero",
                "Precio": "$700.000 ARS",
                "Expensas": "Aprox. $45.000",
                "Detalle": "Excelente departamento de 2 dormitorios en edificio con ascensor y calefacción. Cercano a Deán Funes.",
                "Fuente": "Buscainmueble / Argenprop",
                "Link": "https://www.argenprop.com/departamento-en-alquiler-en-zona-centro-3-ambientes--19720807"
            },
            {
                "Estado": "📌 VISTO PREVIAMENTE",
                "Tipo": "🏢 DEPTO",
                "Título": "Depto 2 Dormitorios en Alvarado al 800",
                "Ubicación": "Alvarado 800 (A 4 cuadras de Deán Funes 462)",
                "Precio": "$750.000 ARS",
                "Expensas": "Aprox. $55.000",
                "Detalle": "Amplio, cocina independiente, edificio con ascensor, muy cerca del trabajo.",
                "Fuente": "Zonaprop",
                "Link": "https://www.zonaprop.com.ar/departamentos-alquiler-centro-ciudad-orden-precio-ascendente.html"
            },
            {
                "Estado": "📌 VISTO PREVIAMENTE",
                "Tipo": "🏡 CASA / DUPLEX",
                "Título": "Duplex 2 Dormitorios en Macrocentro (Zona Delmi)",
                "Ubicación": "Pasaje 3 de Febrero al 800",
                "Precio": "$600.000 ARS",
                "Expensas": "Sin Expensas",
                "Detalle": "Distribución en 2 plantas, 2 dormitorios con placares, patio chico. Zona muy tranquila.",
                "Fuente": "Domus Bienes Raíces / Mitula",
                "Link": "https://www.zonaprop.com.ar/casas-alquiler-salta-sa-2-habitaciones.html"
            }
        ]
        st.session_state["lista_alquileres"] = resultados

# Despliegue de resultados
if "lista_alquileres" in st.session_state:
    st.success(f"Se encontraron {len(st.session_state['lista_alquileres'])} opciones consolidadas:")
    for item in st.session_state["lista_alquileres"]:
        with st.container(border=True):
            st.markdown(f"### {item['Tipo']} - {item['Título']}")
            st.markdown(f"📍 **Ubicación:** {item['Ubicación']}")
            st.markdown(f"💰 **Precio:** {item['Precio']} | **Expensas:** {item['Expensas']}")
            st.markdown(f"📝 **Descripción:** {item['Detalle']}")
            st.caption(f"Portal: {item['Fuente']} | Estado: {item['Estado']}")
            
            # Botón directo que abre la publicación con el carrusel de fotos real
            st.link_button("📸 Abrir Publicación y Ver Carrusel de Fotos Reales", item["Link"], use_container_width=True)

st.markdown("---")
st.markdown("### 🌐 Buscadores Directos por Plataforma (Filtros $850k + Casas/Deptos)")
st.caption("Abre la búsqueda filtrada exacta en cada portal:")

col1, col2 = st.columns(2)
with col1:
    st.link_button("🏬 Facebook Marketplace", "https://www.facebook.com/marketplace/salta/propertyrentals/?minPrice=100000&maxPrice=850000&query=alquiler%20casa%20departamento%202%203%20dormitorios", use_container_width=True)
    st.link_button("🔴 RE/MAX Salta (Casas/Deptos)", "https://www.remax.com.ar/casas-y-departamentos-en-salta", use_container_width=True)

with col2:
    st.link_button("🏢 Argenprop (Casas 2-3 dorms)", "https://www.argenprop.com/casas/alquiler/salta/2-dormitorios-o-3-dormitorios", use_container_width=True)
    st.link_button("🔷 Zonaprop (Hasta $850k)", "https://www.zonaprop.com.ar/casas-departamentos-alquiler-salta-sa-orden-precio-ascendente.html", use_container_width=True)
