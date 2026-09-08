import streamlit as st

st.set_page_config(
    page_title="Liquidador Tasas por Servicios Generales - Municipio de Moreno",
    layout="wide",
)

# Estilos CSS optimizados para visualización compacta y reglas de impresión en una hoja A4
st.markdown(
    """
    <style>
        /* Forzar fuente Arial corporativa y fondo claro en toda la app */
        .stApp, html, body, [data-testid="stAppViewContainer"] {
            font-family: Arial, sans-serif !important;
            background-color: #f8fafc !important;
            color: #0f172a !important;
        }
        
        /* Unificar color y tipografía de todas las etiquetas nativas */
        label, p, span, div, [data-testid="stWidgetLabel"] p, .stMarkdown p {
            font-family: Arial, sans-serif !important;
            color: #1e293b !important;
        }
        
        /* Reducir márgenes de los controles de selección de Streamlit para que entren en horizontal */
        [data-testid="stWidgetLabel"] {
            margin-bottom: 2px !important;
            padding-bottom: 0px !important;
        }
        
        div.row-widget.stRadio > div {
            flex-direction: row !important;
            gap: 10px !important;
        }
        
        /* Tarjetas de resultados compactas para maximizar espacio */
        .resultado-box {
            background-color: #ffffff !important;
            padding: 6px 10px;
            border-radius: 4px;
            border: 1px solid #cbd5e1 !important;
            margin-bottom: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 1px 2px rgba(0,0,0,0.04);
        }
        
        .resultado-label {
            font-family: Arial, sans-serif !important;
            color: #1e3a8a !important;
            font-weight: 600;
            font-size: 12px;
        }
        
        .resultado-valor {
            font-family: Arial, sans-serif !important;
            color: #0f172a !important;
            font-weight: bold;
            font-size: 12px;
        }
        
        /* Estilo personalizado para el botón de impresión */
        .stButton>button {
            background-color: #0284c7 !important;
            color: white !important;
            font-weight: bold !important;
            border-radius: 4px !important;
            border: none !important;
            padding: 8px 16px !important;
            width: 100% !important;
        }

        /* REGLAS ESTRICTAS DE IMPRESIÓN PARA HOJA A4 */
        @media print {
            body, .stApp, [data-testid="stAppViewContainer"] {
                background-color: #ffffff !important;
                color: #000000 !important;
                font-size: 10pt !important;
            }
            /* Ocultar barra lateral, botones superiores y de desarrollo de Streamlit */
            header, [data-testid="stSidebar"], [data-testid="stHeader"], .stDeployButton, [data-testid="stDecoration"] {
                display: none !important;
            }
            /* Ocultar el propio botón de impresión al mandar a imprimir */
            .stButton {
                display: none !important;
            }
            /* Quitar el scroll dinámico de la página web */
            [data-testid="stAppViewContainer"] {
                overflow: visible !important;
                position: static !important;
            }
            /* Ajustar contenedores al ancho de la hoja A4 sin márgenes web */
            .block-container {
                padding-top: 0 !important;
                padding-bottom: 0 !important;
                max-width: 100% !important;
            }
            .resultado-box {
                border: 1px solid #000000 !important;
                page-break-inside: avoid !important;
            }
        </div>
    </style>
    """,
    unsafe_allow_html=True,
)

# Encabezado institucional
st.markdown(
    """
    <div style="background-color: #0284c7; padding: 12px; border-radius: 6px; color: white; display: flex; align-items: center;">
        <span style="font-family: Arial, sans-serif; font-size: 15px; font-weight: bold; color: white !important;">Liquidador Tasas por Servicios Generales - Municipio de Moreno</span>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# Partida municipal centrada
col_p1, col_p2, col_p3 = st.columns(3)
with col_p2:
    entry_partida = st.text_input("PARTIDA MUNICIPAL N°:")

st.markdown("---")

# Controles organizados estrictamente uno al lado del otro de izquierda a derecha (Fila 1)
col_form1, col_form2, col_form3 = st.columns(3)
with col_form1:
    var_estado = st.radio("Estado:", ["EDIFICADO", "BALDIO"])
with col_form2:
    var_uso = st.radio("Uso:", ["RESIDENCIAL", "COMERCIAL", "INDUSTRIAL"])
with col_form3:
    var_acceso = st.radio("Acceso Principal:", ["NO", "SI"])

# Fila 2 de controles horizontales
col_form4, col_form5, col_form6 = st.columns(3)
with col_form4:
    var_zonif = st.selectbox("Zonificación:", ["A/B", "F", "OTRA"])
with col_form5:
    var_tope = st.radio("Liberar Tope:", ["NO", "SI"])
with col_form6:
    entry_edenor = st.text_input("EDENOR ($):", "0,00")

# Fila 3 de descuentos horizontales
st.markdown("**Descuentos:**")
col_desc1, col_desc2, col_desc3 = st.columns(3)
with col_desc1:
    var_bc = st.radio("BC 10%:", ["NO", "SI"], horizontal=True)
with col_desc2:
    var_da = st.radio("DA 10%:", ["NO", "SI"], horizontal=True)
with col_desc3:
    var_be = st.radio("BE 5%:", ["NO", "SI"], horizontal=True)

st.markdown("---")

# Superficies y Valuaciones en formato compacto horizontal
col_sup1, col_sup2, col_val1, col_val2 = st.columns(4)
with col_sup1:
    entry_sup_terreno = st.text_input("Superficie de Terreno (m²):", "300,00")
with col_sup2:
    entry_sup_edificada = st.text_input("Superficie Edificada (m²):", "0,00")
with col_val1:
    entry_va = st.text_input("Valuación ($):", "300000,00")
with col_val2:
    var_anio = st.selectbox("Valuación año:", ["2023 o anterior", "2024", "2025", "2026"])

# Lógica de cálculo y renderizado en formato horizontal compacto para hoja A4
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

    st.markdown("---")
    
    # 1. COEFICIENTES (Fila horizontal existente)
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

    # Función auxiliar para renderizar cajas limpias dentro de las columnas horizontales
    def caja_horizontal(descripcion, valor_texto, columna_destino):
        with columna_destino:
            st.markdown(
                f"""
                <div class="resultado-box">
                    <span class="resultado-label">{descripcion}</span>
                    <span class="resultado-valor">{valor_texto}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    # NUEVO: Distribución horizontal de importes en 3 columnas anchas (Izquierda a Derecha)
    c_res1, c_res2, c_res3 = st.columns(3)
    
    # Fila 1 Horizontal: Límite inferior, Alícuota y CFA alineados uno al lado del otro
    caja_horizontal("Límite inferior:", lim_str, c_res1)
    caja_horizontal("Alícuota:", alic_str, c_res2)
    caja_horizontal("CFA:", cfa_str, c_res3)
    
    # Fila 2 Horizontal: Tasas calculadas bases
    caja_horizontal("TSG Anual:", tasa_anual_str, c_res1)
    caja_horizontal("TSG Mensual:", tasa_mensual_str, c_res2)
    caja_horizontal("Tasa de Protección:", tasa_prot_str, c_res3)
    
    # Fila 3 Horizontal: Impuestos adicionales y deducciones básicas
    caja_horizontal("Tasa de Salud:", tasa_salud_str, c_res1)
    caja_horizontal("EDENOR:", edenor_str, c_res2)
    caja_horizontal("BC (Descuento):", bc_str, c_res3)
    
    # Fila 4 Horizontal: Descuentos restantes distribuidos uniformemente
    caja_horizontal("DA (Descuento):", da_str, c_res1)
    caja_horizontal("BE (Descuento):", be_str, c_res2)

    # 3. Cuadro destacado final para el TSG Total posicionado abajo abarcando el ancho completo
    st.markdown(
        f"""
        <div class="resultado-box" style="border: 2px solid #0f172a !important; margin-top: 10px; padding: 10px 14px;">
            <span class="resultado-label" style="font-size: 14px; color: #1e3a8a; font-weight: bold;">TSG Total:</span>
            <span class="resultado-valor" style="font-size: 15px; color: #0284c7; font-weight: bold;">{tasa_total_str}</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    # 4. Botón institucional para imprimir reporte (Abre el diálogo nativo de impresión del sistema)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🖨️ IMPRIMIR REPORTE EN HOJA A4"):
        st.markdown("""<script>window.print();</script>""", unsafe_allow_html=True)
        st.success("Abriendo ventana de impresión... Seleccione guardar como PDF o su impresora física.")

except ValueError:
    st.error("Revise que los campos numéricos sean válidos.")
