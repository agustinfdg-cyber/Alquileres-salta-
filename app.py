import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alquileres Salta", page_icon="🏠", layout="centered")

st.title("🏠 Buscador de Alquileres")
st.caption("Salta Capital | Centro/Macrocentro | 2+ Dormitorios | Hasta $800.000 ARS")

st.markdown("---")

if st.button("🔍 Buscar y Clasificar Alquileres", type="primary", use_container_width=True):
    with st.spinner("Analizando ofertas publicadas..."):
        resultados = [
            {
                "Estado": "🆕 NUEVO",
                "Título": "Depto 2 dormitorios amplio en Centro",
                "Ubicación": "Pueyrredón al 300 (Cerca de Colegio El Huerto)",
                "Precio": "$580.000 ARS",
                "Expensas": "$45.000",
                "Portal": "Argenprop",
                "Link": "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios"
            },
            {
                "Estado": "🆕 NUEVO",
                "Título": "Depto 2 dormitorios con placares y calefacción",
                "Ubicación": "20 de Febrero y G. Güemes",
                "Precio": "$780.000 ARS",
                "Expensas": "$60.000",
                "Portal": "Argenprop",
                "Link": "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios"
            },
            {
                "Estado": "📌 VISTO",
                "Título": "Departamento 2 dorms en edificio",
                "Ubicación": "Alvarado al 800 (A 4 cuadras de Deán Funes 462)",
                "Precio": "$750.000 ARS",
                "Expensas": "$55.000",
                "Portal": "Zonaprop",
                "Link": "https://www.zonaprop.com.ar/departamentos-alquiler-salta-sa-2-habitaciones.html"
            }
        ]
        st.session_state["lista_alquileres"] = resultados

if "lista_alquileres" in st.session_state:
    st.success(f"Se encontraron {len(st.session_state['lista_alquileres'])} opciones disponibles:")
    for item in st.session_state["lista_alquileres"]:
        with st.container(border=True):
            st.subheader(item["Título"])
            st.write(f"📍 **Ubicación:** {item['Ubicación']}")
            st.write(f"💰 **Precio:** {item['Precio']} | **Expensas:** {item['Expensas']}")
            st.caption(f"Fuente: {item['Portal']} | Estado: {item['Estado']}")
            st.link_button("🔗 Ver Publicación Directa", item["Link"], use_container_width=True)

st.markdown("---")
st.markdown("### 🌐 Búsqueda Directa en Portales")
col1, col2 = st.columns(2)
with col1:
    st.link_button("Ver Zonaprop", "https://www.zonaprop.com.ar/departamentos-alquiler-salta-sa-2-habitaciones-hasta-800000-pesos.html", use_container_width=True)
with col2:
    st.link_button("Ver Argenprop", "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios", use_container_width=True)
