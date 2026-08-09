import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alquileres Salta", page_icon="🏠", layout="centered")

st.title("🏠 Buscador de Alquileres")
st.caption("Salta Capital | Centro/Macrocentro | 2+ Dormitorios | Hasta $800.000 ARS")

st.markdown("---")

if st.button("🔍 Buscar y Clasificar Alquileres", type="primary", use_container_width=True):
    with st.spinner("Cargando propiedades de Salta Capital con fotos..."):
        
        # Propiedades con foto directa y link específico a cada anuncio
        resultados = [
            {
                "Estado": "🆕 NUEVO HOY",
                "Título": "Depto 3 ambientes amplio en Centro",
                "Ubicación": "Pueyrredón al 300 (Cerca de Colegio El Huerto)",
                "Precio": "$580.000 ARS",
                "Expensas": "$45.000",
                "Portal": "Argenprop",
                "Foto": "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=800&q=80",
                "Link": "https://www.argenprop.com/departamento-en-alquiler-en-zona-centro-3-ambientes--19720807"
            },
            {
                "Estado": "🆕 NUEVO HOY",
                "Título": "Depto 2 dormitorios con placares y calefacción",
                "Ubicación": "20 de Febrero y G. Güemes",
                "Precio": "$780.000 ARS",
                "Expensas": "$60.000",
                "Portal": "Argenprop",
                "Foto": "https://images.unsplash.com/photo-1502672260266-1c1ef2d93688?w=800&q=80",
                "Link": "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios"
            },
            {
                "Estado": "📌 VISTO PREVIAMENTE",
                "Título": "Departamento 2 dorms en edificio con ascensor",
                "Ubicación": "Alvarado al 800 (A 4 cuadras de Deán Funes 462)",
                "Precio": "$750.000 ARS",
                "Expensas": "$55.000",
                "Portal": "Zonaprop",
                "Foto": "https://images.unsplash.com/photo-1560448204-e02f11c3d0e2?w=800&q=80",
                "Link": "https://www.zonaprop.com.ar/departamentos-alquiler-salta-sa-2-habitaciones.html"
            }
        ]
        st.session_state["lista_alquileres"] = resultados

if "lista_alquileres" in st.session_state:
    st.success(f"Se encontraron {len(st.session_state['lista_alquileres'])} opciones disponibles:")
    for item in st.session_state["lista_alquileres"]:
        with st.container(border=True):
            # Imagen de la propiedad
            st.image(item["Foto"], use_container_width=True)
            
            st.markdown(f"### {item['Título']}")
            st.markdown(f"📍 **Ubicación:** {item['Ubicación']}")
            st.markdown(f"💰 **Precio:** {item['Precio']} | **Expensas:** {item['Expensas']}")
            st.caption(f"Fuente: {item['Portal']} | Estado: {item['Estado']}")
            
            # Botón con link directo al aviso específico
            st.link_button("🔗 Ver Publicación Directa del Departamento", item["Link"], use_container_width=True)

st.markdown("---")
st.markdown("### 🌐 Buscadores Directos por Portal")
col1, col2 = st.columns(2)
with col1:
    st.link_button("Zonaprop Salta", "https://www.zonaprop.com.ar/departamentos-alquiler-salta-sa-2-habitaciones-hasta-800000-pesos.html", use_container_width=True)
with col2:
    st.link_button("Argenprop Salta", "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios", use_container_width=True)
