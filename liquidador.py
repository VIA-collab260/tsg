import tkinter as tk
from tkinter import messagebox, ttk

def calcular_liquidador():
    try:
        va = float(entry_va.get().replace(",", ".")) if entry_va.get() else 0.0
        sup_terreno = float(entry_sup_terreno.get().replace(",", ".")) if entry_sup_terreno.get() else 0.0
        sup_edificada = float(entry_sup_edificada.get().replace(",", ".")) if entry_sup_edificada.get() else 0.0
        
        estado_sel = var_estado.get()
        uso_sel = var_uso.get()
        anio_sel = var_anio.get()

        if anio_sel == "2023 o anterior": ca = 19.10
        elif anio_sel == "2024": ca = 2.76
        elif anio_sel == "2025": ca = 1.36
        else: ca = 1.00

        if uso_sel == "RESIDENCIAL": cu = 1.0
        elif uso_sel == "COMERCIAL": cu = 1.1
        else: cu = 1.25

        if estado_sel == "EDIFICADO": cb = 1.0
        else: cb = 1.6 if sup_terreno <= 500 else 1.7 if sup_terreno <= 5000 else 2.0

        if var_acceso.get() == "SI":
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
        
        monto_bc = round(tasa_mensual * 0.10, 2) if var_bc.get() == "SI" else 0.0
        monto_da = round(tasa_mensual * 0.10, 2) if var_da.get() == "SI" else 0.0
        monto_be = round(tasa_mensual * 0.05, 2) if var_be.get() == "SI" else 0.0
        monto_edenor = float(entry_edenor.get().replace(",", ".")) if entry_edenor.get() else 0.0
        
        tasa_total = round((tasa_mensual + tasa_proteccion + tasa_salud) - monto_bc - monto_da - monto_be - monto_edenor, 2)
        
        if var_tope.get() == "NO" and tasa_total < 4500.0:
            tasa_total = 8900.0 if estado_sel == "BALDIO" else 4500.0
            
        bi_str = f"${bi:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_bi_val.config(text=bi_str)
        lbl_ca_val.config(text=str(ca))
        lbl_cu_val.config(text=str(cu))
        lbl_cb_val.config(text=str(cb))
        lbl_cap_val.config(text=str(cap))
        
        lim_str = f"${lim_inf:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        cfa_str = f"${cfa_val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        tasa_anual_str = f"${tasa_anual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        alic_str = f"{alic * 100:.2f}%"
        
        lbl_lim_val.config(text=lim_str)
        lbl_alic_val.config(text=alic_str)
        lbl_cfa_val.config(text=cfa_str)
        lbl_tsg_anual_val.config(text=tasa_anual_str)
        
        tasa_mensual_str = f"${tasa_mensual:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_tasa_servicios_val.config(text=tasa_mensual_str)
        
        bc_str = f"-${monto_bc:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_bc_val.config(text=bc_str)
        
        da_str = f"-${monto_da:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_da_val.config(text=da_str)
        
        be_str = f"-${monto_be:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_be_val.config(text=be_str)
        
        edenor_str = f"-${monto_edenor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_edenor_val.config(text=edenor_str)
        
        tasa_prot_str = f"${tasa_proteccion:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_tasa_proteccion_val.config(text=tasa_prot_str)
        
        tasa_salud_str = f"${tasa_salud:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_tasa_salud_val.config(text=tasa_salud_str)
        
        tasa_total_str = f"${tasa_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        lbl_tTotal_val.config(text=tasa_total_str)
        
    except ValueError:
        messagebox.showerror("Error", "Revise que los campos numéricos sean válidos.")

root = tk.Tk()
root.title("Liquidador Tasas por Servicios Generales - Municipio de Moreno")
root.geometry("820x1050")
root.configure(bg="#e0f2fe")  # Fondo azul claro institucional

main_canvas = tk.Canvas(root, bg="#e0f2fe", highlightthickness=0)
scrollbar = ttk.Scrollbar(root, orient="vertical", command=main_canvas.yview)
scrollable_frame = tk.Frame(main_canvas, bg="#e0f2fe")

scrollable_frame.bind(
    "<Configure>",
    lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all"))
)

main_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
main_canvas.configure(yscrollcommand=scrollbar.set)

main_canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Encabezado con color azul claro institucional y logotipo simulado
f_header = tk.Frame(scrollable_frame, bg="#0284c7", pady=10)
f_header.pack(fill=tk.X, padx=15, pady=(15, 0))

lbl_encabezado = tk.Label(f_header, text="Liquidador Tasas por Servicios Generales", font=("Arial", 13, "bold"), bg="#0284c7", fg="white")
lbl_encabezado.pack(side=tk.LEFT, padx=5)

# Partida municipal en el medio
f_partida = tk.Frame(scrollable_frame, bg="#e0f2fe")
f_partida.pack(anchor="center", pady=(10, 6))
tk.Label(f_partida, text="PARTIDA MUNICIPAL N°:", font=("Arial", 9, "bold"), bg="#e0f2fe", fg="#0369a1").pack(side=tk.LEFT)
entry_partida = tk.Entry(f_partida, width=25, bg="#ffffff", relief="solid", bd=1)
entry_partida.pack(side=tk.LEFT, padx=5)

frame_form = tk.Frame(scrollable_frame, bg="#ffffff", bd=1, relief="solid", padx=12, pady=12)
frame_form.pack(fill=tk.X, padx=15, pady=2)

f_top = tk.Frame(frame_form, bg="#ffffff")
f_top.pack(fill=tk.X, pady=2)

f_estado = tk.Frame(f_top, bg="#ffffff")
f_estado.pack(side=tk.LEFT, padx=4)
tk.Label(f_estado, text="Estado:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
var_estado = tk.StringVar(value="EDIFICADO")
f_est_btns = tk.Frame(f_estado, bg="#ffffff")
f_est_btns.pack(anchor="w")
tk.Radiobutton(f_est_btns, text="EDIFICADO", variable=var_estado, value="EDIFICADO", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)
tk.Radiobutton(f_est_btns, text="BALDIO", variable=var_estado, value="BALDIO", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)

f_uso = tk.Frame(f_top, bg="#ffffff")
f_uso.pack(side=tk.LEFT, padx=15)
tk.Label(f_uso, text="Uso:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
var_uso = tk.StringVar(value="RESIDENCIAL")
f_uso_btns = tk.Frame(f_uso, bg="#ffffff")
f_uso_btns.pack(anchor="w")
tk.Radiobutton(f_uso_btns, text="RESIDENCIAL", variable=var_uso, value="RESIDENCIAL", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)
tk.Radiobutton(f_uso_btns, text="COMERCIAL", variable=var_uso, value="COMERCIAL", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)
tk.Radiobutton(f_uso_btns, text="INDUSTRIAL", variable=var_uso, value="INDUSTRIAL", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)

f_acc = tk.Frame(f_top, bg="#ffffff")
f_acc.pack(side=tk.LEFT, padx=15)
tk.Label(f_acc, text="Acceso Principal:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
var_acceso = tk.StringVar(value="NO")
f_acc_btns = tk.Frame(f_acc, bg="#ffffff")
f_acc_btns.pack(anchor="w")
tk.Radiobutton(f_acc_btns, text="NO", variable=var_acceso, value="NO", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)
tk.Radiobutton(f_acc_btns, text="SI", variable=var_acceso, value="SI", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)

# Descuentos y Edenor en la misma fila
tk.Label(frame_form, text="DESCUENTOS Y EDENOR:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w", padx=4, pady=(8, 2))
f_desc_row = tk.Frame(frame_form, bg="#ffffff")
f_desc_row.pack(fill=tk.X, padx=4, pady=2)

var_bc, var_da, var_be = tk.StringVar(value="NO"), tk.StringVar(value="NO"), tk.StringVar(value="NO")
for title, var in [("BC 10%:", var_bc), ("DA 10%:", var_da), ("BE 5%:", var_be)]:
    sub = tk.Frame(f_desc_row, bg="#ffffff")
    sub.pack(side=tk.LEFT, padx=6)
    tk.Label(sub, text=title, font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
    btns = tk.Frame(sub, bg="#ffffff")
    btns.pack(anchor="w")
    tk.Radiobutton(btns, text="NO", variable=var, value="NO", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)
    tk.Radiobutton(btns, text="SI", variable=var, value="SI", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)

f_edenor_inline = tk.Frame(f_desc_row, bg="#ffffff")
f_edenor_inline.pack(side=tk.LEFT, padx=15)
tk.Label(f_edenor_inline, text="EDENOR ($):", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
entry_edenor = tk.Entry(f_edenor_inline, width=15, bg="#f8fafc", relief="solid", bd=1)
entry_edenor.insert(0, "0,00")
entry_edenor.pack(anchor="w", pady=2)
entry_edenor.bind("<KeyRelease>", lambda e: calcular_liquidador())

f_mid2 = tk.Frame(frame_form, bg="#ffffff")
f_mid2.pack(fill=tk.X, padx=4, pady=6)

f_zon = tk.Frame(f_mid2, bg="#ffffff")
f_zon.pack(side=tk.LEFT)
tk.Label(f_zon, text="ZONIFICACION:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
var_zonif = tk.StringVar(value="A/B")
f_zon_btns = tk.Frame(f_zon, bg="#ffffff")
f_zon_btns.pack(anchor="w")
tk.Radiobutton(f_zon_btns, text="A/B", variable=var_zonif, value="A/B", bg="#ffffff", selectcolor="#ffffff").pack(side=tk.LEFT)
tk.Radiobutton(f_zon_btns, text="F", variable=var_zonif, value="F", bg="#ffffff", selectcolor="#ffffff").pack(side=tk.LEFT)
tk.Radiobutton(f_zon_btns, text="OTRA", variable=var_zonif, value="OTRA", bg="#ffffff", selectcolor="#ffffff").pack(side=tk.LEFT)

f_topes = tk.Frame(f_mid2, bg="#ffffff")
f_topes.pack(side=tk.LEFT, padx=30)
tk.Label(f_topes, text="LIBERAR TOPE:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
var_tope = tk.StringVar(value="NO")
f_tope_btns = tk.Frame(f_topes, bg="#ffffff")
f_tope_btns.pack(anchor="w")
tk.Radiobutton(f_tope_btns, text="NO", variable=var_tope, value="NO", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)
tk.Radiobutton(f_tope_btns, text="SI", variable=var_tope, value="SI", bg="#ffffff", selectcolor="#ffffff", command=calcular_liquidador).pack(side=tk.LEFT)

tk.Label(frame_form, text="SUPERFICIE DE TERRENO (m²):", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w", padx=4, pady=(8, 2))
entry_sup_terreno = tk.Entry(frame_form, width=72, bg="#f8fafc", relief="solid", bd=1)
entry_sup_terreno.insert(0, "300,00")
entry_sup_terreno.pack(anchor="w", padx=4, pady=2)
entry_sup_terreno.bind("<KeyRelease>", lambda e: calcular_liquidador())

tk.Label(frame_form, text="SUPERFICIE EDIFICADA (m²):", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w", padx=4, pady=(8, 2))
entry_sup_edificada = tk.Entry(frame_form, width=72, bg="#f8fafc", relief="solid", bd=1)
entry_sup_edificada.insert(0, "0,00")
entry_sup_edificada.pack(anchor="w", padx=4, pady=2)
entry_sup_edificada.bind("<KeyRelease>", lambda e: calcular_liquidador())

f_val_anio_row = tk.Frame(frame_form, bg="#ffffff")
f_val_anio_row.pack(fill=tk.X, padx=4, pady=(8, 2))

f_va_col = tk.Frame(f_val_anio_row, bg="#ffffff")
f_va_col.pack(side=tk.LEFT, fill=tk.X, expand=True)
tk.Label(f_va_col, text="VALUACION ($):", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
entry_va = tk.Entry(f_va_col, width=40, bg="#f8fafc", relief="solid", bd=1)
entry_va.insert(0, "300000,00")
entry_va.pack(anchor="w", pady=2)
entry_va.bind("<KeyRelease>", lambda e: calcular_liquidador())

f_anio_col = tk.Frame(f_val_anio_row, bg="#ffffff")
f_anio_col.pack(side=tk.LEFT, padx=15)
tk.Label(f_anio_col, text="VALUACION año:", font=("Arial", 9, "bold"), bg="#ffffff", fg="#334155").pack(anchor="w")
var_anio = tk.StringVar(value="2026")
combo_anio = ttk.Combobox(f_anio_col, textvariable=var_anio, values=["2023 o anterior", "2024", "2025", "2026"], state="readonly", width=25)
combo_anio.pack(anchor="w", pady=2)
combo_anio.bind("<<ComboboxSelected>>", lambda e: calcular_liquidador())

# Sección inferior organizada con etiquetas y recuadros individuales al lado para cada valor
def crear_fila_resultado(parent, texto_izq):
    f = tk.Frame(parent, bg="#e0f2fe")
    f.pack(fill=tk.X, padx=15, pady=3)
    lbl = tk.Label(f, text=texto_izq, font=("Arial", 9, "bold"), bg="#e0f2fe", fg="#0369a1", anchor="w", width=38)
    lbl.pack(side=tk.LEFT)
    lbl_val = tk.Label(f, text="", font=("Arial", 9, "bold"), bg="#ffffff", fg="#1e293b", relief="solid", bd=1, width=25, anchor="w", padx=5)
    lbl_val.pack(side=tk.LEFT)
    return lbl_val

def crear_fila_coeficientes(parent):
    f = tk.Frame(parent, bg="#e0f2fe")
    f.pack(fill=tk.X, padx=15, pady=3)
    lbl = tk.Label(f, text="Base imponible y Coeficientes:", font=("Arial", 9, "bold"), bg="#e0f2fe", fg="#0369a1", anchor="w", width=24)
    lbl.pack(side=tk.LEFT)
    
    sub = tk.Frame(f, bg="#e0f2fe")
    sub.pack(side=tk.LEFT)
    
    for label_txt, attr_name in [("BI:", "lbl_bi_val"), ("CA:", "lbl_ca_val"), ("CU:", "lbl_cu_val"), ("CB:", "lbl_cb_val"), ("CAP:", "lbl_cap_val")]:
        tk.Label(sub, text=label_txt, font=("Arial", 8, "bold"), bg="#e0f2fe", fg="#0369a1").pack(side=tk.LEFT, padx=(4, 1))
        lbl_v = tk.Label(sub, text="", font=("Arial", 8), bg="#ffffff", fg="#1e293b", relief="solid", bd=1, width=10, anchor="w", padx=2)
        lbl_v.pack(side=tk.LEFT, padx=(0, 4))
        globals()[attr_name] = lbl_v

lbl_bi_val = None
lbl_ca_val = None
lbl_cu_val = None
lbl_cb_val = None
lbl_cap_val = None
crear_fila_coeficientes(scrollable_frame)

lbl_lim_val = crear_fila_resultado(scrollable_frame, "Límite inferior:")
lbl_alic_val = crear_fila_resultado(scrollable_frame, "Alícuota:")
lbl_cfa_val = crear_fila_resultado(scrollable_frame, "CFA:")
lbl_tsg_anual_val = crear_fila_resultado(scrollable_frame, "TSG Anual:")
lbl_tasa_servicios_val = crear_fila_resultado(scrollable_frame, "TSG Mensual:")
lbl_bc_val = crear_fila_resultado(scrollable_frame, "BC (Descuento):")
lbl_da_val = crear_fila_resultado(scrollable_frame, "DA (Descuento):")
lbl_be_val = crear_fila_resultado(scrollable_frame, "BE (Descuento):")
lbl_edenor_val = crear_fila_resultado(scrollable_frame, "EDENOR:")
lbl_tasa_proteccion_val = crear_fila_resultado(scrollable_frame, "Tasa de Protección:")
lbl_tasa_salud_val = crear_fila_resultado(scrollable_frame, "Tasa de Salud:")

# TCG Total con mini recuadro e identificación TSG por Servicios Generales solicitada
f_total = tk.Frame(scrollable_frame, bg="#e0f2fe")
f_total.pack(fill=tk.X, padx=15, pady=(8, 15))
tk.Label(f_total, text="TSG Total:", font=("Arial", 10, "bold"), bg="#e0f2fe", fg="#0284c7", width=34, anchor="w").pack(side=tk.LEFT)
lbl_tTotal_val = tk.Label(f_total, text="", font=("Arial", 11, "bold"), bg="#ffffff", fg="#0284c7", relief="solid", bd=1, width=22, anchor="w", padx=5)
lbl_tTotal_val.pack(side=tk.LEFT)

btn_imprimir = tk.Button(scrollable_frame, text="🖨️ IMPRIMIR REPORTE", font=("Arial", 9, "bold"), bg="#0284c7", fg="white", relief="solid", bd=1, padx=10, pady=5)
btn_imprimir.pack(anchor="w", padx=15, pady=(5, 20))

calcular_liquidador()

root.mainloop()
