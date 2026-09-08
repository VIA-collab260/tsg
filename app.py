import streamlit as st

st.set_page_config(
    page_title="Liquidador Tasas por Servicios Generales - Municipio de Moreno",
    layout="wide",
)

# Estilos CSS unificados para forzar tipografía Arial limpia, colores institucionales y consistencia visual total
st.markdown(
    """
    <style>
        /* Forzar fuente Arial corporativa y fondo claro en toda la app moderna */
        .stApp, html, body, [data-testid="stAppViewContainer"] {
            font-family: Arial, sans-serif !important;
            background-color: #f8fafc !important;
            color: #0f172a !important;
        }
        
        /* Unificar color y tipografía de todas las etiquetas, textos y párrafos nativos */
        label, p, span, div, [data-testid="stWidgetLabel"] p, .stMarkdown p {
            font-family: Arial, sans-serif !important;
            color: #1e293b !important;
        }
        
        /* Títulos limpios */
        h1, h2, h3, h4, h5, h6, [data-testid="stMarkdownContainer"] h1 {
            font-family: Arial, sans-serif !important;
            color: #1e3a8a !important;
        }
        
        /* Tarjetas de resultados perfectamente uniformes basados en tu diseño */
        .resultado-box {
            background-color: #ffffff !important;
            padding: 10px 14px;
            border-radius: 6px;
            border: 1px solid #cbd5e1 !important;
            margin-bottom: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
        }
        
        .resultado-label {
            font-family: Arial, sans-serif !important;
            color: #1e3a8a !important;
            font-weight: 600;
            font-size: 13px;
        }
        
        .resultado-valor {
            font-family: Arial, sans-serif !important;
            color: #0f172a !important;
            font-weight: bold;
            font-size: 13px;
        }
        
        /* Estilo personalizado para el botón de impresión */
        .stButton>button {
            background-color: #0284c7 !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 4px !important;
            border: none !important;
            padding: 10px 20px !important;
            width: 100% !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Encabezado institucional
st.markdown(
    """
    <div style="background-color: #0284c7; padding: 14px; border-radius: 6px; color: white; display: flex; align-items: center;">
        <span style="font-family: Arial, sans-serif; font-size: 16px; font-weight: bold; color: white !important;">Liquidador Tasas por Servicios Generales - Municipio de Moreno</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# Partida municipal en el medio
col_p1, col_p2, col_p3 = st.columns()
with col_p2:
    entry_partida = st.text_input("PARTIDA MUNICIPAL N°:")

st.markdown("---")

# Controles de entrada organizados uno al lado del otro (en 3 columnas)
col1, col2, col3 = st.columns(3)

with col1:
    var_estado = st.radio("Estado:", ["EDIFICADO", "BALDIO"])
    var_uso = st.radio("Uso:", ["RESIDENCIAL", "COMERCIAL", "INDUSTRIAL"])
    var_acceso = st.radio("Acceso Principal:", ["NO", "SI"])

with col2:
    var_zonif = st.selectbox("Zonificación:", ["A/B", "F", "OTRA"])
    var_tope = st.radio("Liberar Tope:", ["NO", "SI"])

with col3:
    st.markdown("**Descuentos:**")
    var_bc = st.radio("BC 10%:", ["NO", "SI"], horizontal=True)
    var_da = st.radio("DA 10%:", ["NO", "SI"], horizontal=True)
    var_be = st.radio("BE 5%:", ["NO", "SI"], horizontal=True)
    entry_edenor = st.text_input("EDENOR ($):", "0,00")

st.markdown("---")

# Superficies
col_sup1, col_sup2 = st.columns(2)
with col_sup1:
    entry_sup_terreno = st.text_input("Superficie de Terreno (m²):", "300,00")
with col_sup2:
    entry_sup_edificada = st.text_input("Superficie Edificada (m²):", "0,00")

# Valuaciones
col_val1, col_val2 = st.columns(2)
with col_val1:
    entry_va = st.text_input("Valuación ($):", "300000,00")
with col_val2:
    var_anio = st.selectbox(
        "Valuación año:", ["2023 o anterior", "2024", "2025", "2026"]
    )
# Lógica de cálculo y renderizado de resultados
try:
    va = float(entry_va.replace(".", "").replace(",", ".")) if entry_va else 0.0
    sup_terreno = float(entry_sup_terreno.replace(".", "").replace(",", ".")) if entry_sup_terreno else 0.0
    sup_edificada = float(entry_sup_edificada.replace(".", "").replace(",", ".")) if entry_sup_edificada else 0.0
    
    estado_sel = var_estado
    uso_sel = var_uso
    anio_sel = var_anio

    if anio_sel == "2023 o anterior": ca = 19.10
    elif anio_sel == "2024": ca = 2.76
    elif anio_sel == "2025": ca = 1.36
    else: ca = 1.00

    if uso_sel == "RESIDENCIAL": cu = 1.0
    elif uso_sel == "COMERCIAL": cu = 1.1
    else: cu = 1.25

    if estado_sel == "EDIFICADO": cb = 1.0
    else: cb = 1.6 if sup_terreno <= 500 else 1.7 if sup_terreno <= 5000 else 2.0

    if var_acceso == "SI":
        if uso_sel == "RESIDENCIAL" and estado_sel == "EDIFICADO": cap = 1.2
        elif estado_sel == "BALDIO": cap = 1.6
        else: cap = 1.5
    else:
        cap = 1.0  

    bi = round(va * ca * cu * cb * cap, 2)
    
    if bi <= 5730000:
        lim_inf, cfa_val, alic = 0.0, 107883.00, 0.0
    elif bi <= 6446250:
        lim_inf, cfa_val, alic = 5730000.0, 107883.00, 0.0150
    elif bi <= 7305750:
        lim_inf, cfa_val, alic = 6446250.0, 123095.84, 0.0152
    elif bi <= 8165250:
        lim_inf, cfa_val, alic = 7305750.0, 141843.90, 0.0154
    elif bi <= 12892500:
        lim_inf, cfa_val, alic = 8165250.0, 160838.66, 0.0156
    elif bi <= 21487500:
        lim_inf, cfa_val, alic = 12892500.0, 328337.79, 0.0160
    elif bi <= 30082500:
        lim_inf, cfa_val, alic = 21487500.0, 649028.37, 0.0164
    elif bi <= 38677500:
        lim_inf, cfa_val, alic = 30082500.0, 838975.84, 0.0169
    elif bi <= 47272500:
        lim_inf, cfa_val, alic = 38677500.0, 1096761.73, 0.0170
    elif bi <= 154447750:
        lim_inf, cfa_val, alic = 47272500.0, 163308.75, 0.0171
    elif bi <= 1000000000:
        lim_inf, cfa_val, alic = 154447750.0, 4201777.78, 0.0173
    else:
        lim_inf, cfa_val, alic = 1000000000.0, 25380696.47, 0.0183

    excedente = max(0.0, bi - lim_inf)
    tasa_anual = round(((excedente * alic) + cfa_val), 2)
    tasa_mensual = round(tasa_anual / 12, 2)
    
    tasa_proteccion = round(tasa_mensual * 0.095, 2)  
    tasa_salud = round(tasa_mensual * 0.105, 2)       
    
    monto_bc = round(tasa_mensual * 0.10, 2) if var_bc == "SI" else 0.0
    monto_da = round(tasa_mensual * 0.10, 2) if var_da == "SI" else 0.0
    monto_be = round(tasa_mensual * 0.05, 2) if var_be == "SI" else 0.0
    monto_edenor = float(entry_edenor.replace(".", "").replace(",", ".")) if entry_edenor else 0.0
    
    tasa_total = round((tasa_mensual + tasa_proteccion + tasa_salud) - monto_bc - monto_da - monto_be - monto_edenor, 2)
    
    if var_tope == "NO" and tasa_total < 4500.0:
        tasa_total = 8900.0 if estado_sel == "BALDIO" else 4500.0
        
    def fmt(val):
        return f"${val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    bi_str = fmt(bi)
    lim_str = fmt(lim_inf)
    cfa_str = fmt(cfa_val)
    tasa_anual_str = fmt(tasa_anual)
    alic_str = f"{alic * 100:.2f}%"
    tasa_mensual_str = fmt(tasa_mensual)
    bc_str = f"-{fmt(monto_bc)}" if monto_bc > 0 else f"-{fmt(0.0)}"
    da_str = f"-{fmt(monto_da)}" if monto_da > 0 else f"-{fmt(0.0)}"
    be_str = f"-{fmt(monto_be)}" if monto_be > 0 else f"-{fmt(0.0)}"
    edenor_str = f"-{fmt(monto_edenor)}" if monto_edenor > 0 else f"-{fmt(0.0)}"
    tasa_prot_str = fmt(tasa_proteccion)
    tasa_salud_str = fmt(tasa_salud)
    tasa_total_str = fmt(tasa_total)

    # =========================================================================
    # SECCIÓN DE RESULTADOS CON LAS ETIQUETAS REALES DE TU IMAGEN
    # =========================================================================
    st.markdown("---")
    
    # 1. Fila de Base Imponible y Coeficientes en horizontal
    c_bi, c_ca, c_cu, c_cb, c_cap = st.columns(5)
    with c_bi:
        st.markdown(f'<div class="resultado-box"><span class="resultado-label">Base imponible y Coeficientes BI:</span><span class="resultado-valor">{bi_str}</span></div>', unsafe_allow_html=True)
    with c_ca:
        st.markdown(f'<div class="resultado-box"><span class="resultado-label">CA:</span><span class="resultado-valor">{ca}</span></div>', unsafe_allow_html=True)
    with c_cu:
        st.markdown(f'<div class="resultado-box"><span class="resultado-label">CU:</span><span class="resultado-valor">{cu}</span></div>', unsafe_allow_html=True)
    with c_cb:
        st.markdown(f'<div class="resultado-box"><span class="resultado-label">CB:</span><span class="resultado-valor">{cb}</span></div>', unsafe_allow_html=True)
    with c_cap:
        st.markdown(f'<div class="resultado-box"><span class="resultado-label">CAP:</span><span class="resultado-valor">{cap}</span></div>', unsafe_allow_html=True)

    # Función adaptada para estructurar las filas según tu formato exacto
    def fila_item_tasas(descripcion, valor_texto, es_total=False):
        if es_total:
            st.markdown(
                f"""
                <div class="resultado-box" style="border: 2px solid #0f172a !important; margin-top: 15px; padding: 12px 14px;">
                    <span class="resultado-label" style="font-size: 15px; color: #1e3a8a; font-weight: bold;">{descripcion}</span>
                    <span class="resultado-valor" style="font-size: 16px; color: #0284c7; font-weight: bold;">{valor_texto}</span>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div class="resultado-box">
                    <span class="resultado-label" style="color: #1e3a8a;">{descripcion}</span>
                    <span class="resultado-valor">{valor_texto}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # 2. Bloque vertical de liquidación con tus nombres exactos de la imagen
    fila_item_tasas("Límite inferior:", lim_str)
    fila_item_tasas("Alícuota:", alic_str)
    fila_item_tasas("CFA:", cfa_str)
    fila_item_tasas("TSG Anual:", tasa_anual_str)
    fila_item_tasas("TSG Mensual:", tasa_mensual_str)
    fila_item_tasas("BC (Descuento):", bc_str)
    fila_item_tasas("DA (Descuento):", da_str)
    fila_item_tasas("BE (Descuento):", be_str)
    fila_item_tasas("EDENOR:", edenor_str)
    fila_item_tasas("Tasa de Protección:", tasa_prot_str)
    fila_item_tasas("Tasa de Salud:", tasa_salud_str)
    
    # 3. Fila destacada para el total a pagar
    fila_item_tasas("TSG Total:", tasa_total_str, es_total=True)

    # 4. Botón institucional para imprimir reporte
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🖨️ IMPRIMIR REPORTE"):
        st.info("Generando reporte de la partida municipal...")

except ValueError:
    st.error("Revise que los campos numéricos sean válidos.")
