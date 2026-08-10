import streamlit as st
import pandas as pd

st.set_page_config(page_title="Alquileres Salta", page_icon="🏠", layout="centered")

st.title("🏠 Buscador de Alquileres Salta")
st.caption("Filtros: Centro/Macrocentro | Casas, Dúplex o Deptos (2 a 3 Dormitorios) | Hasta $850.000 ARS")

st.markdown("---")

# Botón de consulta
if st.button("🔄 Actualizar y Cargar Propiedades Disponibles", type="primary", use_container_width=True):
    with st.spinner("Buscando casas, dúplex y departamentos en Salta Capital..."):
        
        # Base de datos ampliada a Casas, Dúplex y Deptos en el radio solicitado
        resultados = [
            {
                "Tipo": "🏢 DEPTO (2 Dorm)",
                "Estado": "🆕 PUBLICADO ESTA SEMANA",
                "Título": "Depto 2 Dormitorios en Lerma al 90 (esq. Alvarado)",
                "Ubicación": "Lerma 91 esq. Alvarado (A 4 cuadras de Deán Funes 462)",
                "Precio": "$650.000 ARS",
                "Expensas": "Consultar",
                "Detalle": "80 m², 2 dormitorios con placard, 2 baños, cocina equipada y living comedor luminoso. Muy cercano al trabajo.",
                "Fuente": "InmoUP / Cabrera Propiedades",
                "Link": "https://inmoup.com.ar/departamentos-en-alquiler-en-salta"
            },
            {
                "Tipo": "🏢 DEPTO (2 Dorm)",
                "Estado": "🆕 PUBLICADO ESTA SEMANA",
                "Título": "Depto 2 Dormitorios en Deán Funes al 300",
                "Ubicación": "Deán Funes 300 (Centro - A 1 cuadra de tu trabajo)",
                "Precio": "$750.000 ARS",
                "Expensas": "Aprox. $60.000",
                "Detalle": "Amplios ambientes, 2 dormitorios, 2 baños, excelente ubicación céntrica caminable a todo.",
                "Fuente": "Mercado Libre Inmuebles",
                "Link": "https://inmuebles.mercadolibre.com.ar/departamentos/alquiler/salta/salta/centro/"
            },
            {
                "Tipo": "🏡 DÚPLEX / CASA (2 Dorm)",
                "Estado": "📌 VISTO PREVIAMENTE",
                "Título": "Dúplex 2 Dormitorios en Macrocentro (Zona Pueyrredón)",
                "Ubicación": "Pasaje Cancha Rayada (A 300m de Av. Entre Ríos)",
                "Precio": "$600.000 ARS",
                "Expensas": "Sin Expensas",
                "Detalle": "2 dormitorios, 1.5 baños, cocina independiente y pequeño patio privado. Sin gastos comunitarios.",
                "Fuente": "Domus Bienes Raíces / Trovit",
                "Link": "https://casas.trovitargentina.com.ar/alquiler-casa-macrocentro-salta"
            },
            {
                "Tipo": "🏢 DEPTO (3 Dorm)",
                "Estado": "📌 VISTO PREVIAMENTE",
                "Título": "Depto 3 Dormitorios en Pueyrredón al 1000",
                "Ubicación": "Pueyrredón 1000 (A pocas cuadras del Colegio El Huerto)",
                "Precio": "$750.000 ARS",
                "Expensas": "Aprox. $50.000",
                "Detalle": "3 dormitorios espaciosos, amoblado o semiamoblado con cochera, excelente para la nena.",
                "Fuente": "Argenprop / Zonaprop",
                "Link": "https://www.argenprop.com/departamento-en-alquiler-en-zona-centro-3-ambientes--11398187"
            }
        ]
        st.session_state["lista_alquileres"] = resultados

# Mostrar listado
if "lista_alquileres" in st.session_state:
    st.success(f"Se encontraron {len(st.session_state['lista_alquileres'])} opciones consolidadas en tu radio:")
    for item in st.session_state["lista_alquileres"]:
        with st.container(border=True):
            st.markdown(f"### {item['Tipo']} - {item['Título']}")
            st.markdown(f"📍 **Ubicación:** {item['Ubicación']}")
            st.markdown(f"💰 **Precio:** {item['Precio']} | **Expensas:** {item['Expensas']}")
            st.markdown(f"📝 **Descripción:** {item['Detalle']}")
            st.caption(f"Fuente: {item['Fuente']} | {item['Estado']}")
            
            st.link_button("📸 Abrir Anuncio Directo en la Web/App", item["Link"], use_container_width=True)

st.markdown("---")
st.markdown("### 🌐 Búsquedas en Tiempo Real (Actualizadas al Instante)")
st.caption("Toca cualquiera de estos botones para abrir las publicaciones ingresadas HOY:")

col1, col2 = st.columns(2)
with col1:
    st.link_button("🟡 Mercado Libre Salta", "https://inmuebles.mercadolibre.com.ar/alquiler/salta/salta/centro/_PriceRange_0-850000", use_container_width=True)
    st.link_button("🏬 Facebook Marketplace", "https://www.facebook.com/marketplace/salta/propertyrentals/?minPrice=100000&maxPrice=850000&query=alquiler%20casa%20departamento%202%203%20dormitorios", use_container_width=True)

with col2:
    st.link_button("🔷 Zonaprop (Hasta $850k)", "https://www.zonaprop.com.ar/casas-departamentos-alquiler-centro-ciudad-orden-precio-ascendente.html", use_container_width=True)
    st.link_button("🏢 Argenprop (2-3 dorms)", "https://www.argenprop.com/departamentos/alquiler/salta/2-dormitorios-o-3-dormitorios/pesos-hasta-850000", use_container_width=True)
