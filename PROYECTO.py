import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   


# =======================
# CONFIGURACIÓN GENERAL
# =======================
st.set_page_config(page_title="Programación de Turnos de Enfermería",
                   layout="wide",
                   page_icon="🩺")

# =======================
# LOGO EN LA BARRA LATERAL
# =======================
st.sidebar.image("logo.png", width=180)
st.sidebar.title("📌 Navegación")
menu = st.sidebar.radio(
    "Selecciona una sección:",
    ["🏠 Dashboard",
     "📘 Explicación del documento y notación",
     "📊 Cargar modelo y dashboard",
     "🧮 Calculadora interactiva"]
)
if menu == "🏠 Dashboard":

    st.title("🩺 Sistema de Programación de Turnos de Enfermería")
    st.subheader("Realizado por **Paula Betina Reyes** 👋")

    # -----------------------------------------
    # 1. OBJETIVO DEL TRABAJO
    # -----------------------------------------
    st.header("🎯 Objetivo del trabajo")
    st.write("""
    Este proyecto implementa un **modelo de programación matemática** basado en el artículo 
    *A mathematical programming model for scheduling of nurses labor shifts*.  
    Su objetivo es:

    **✔ Minimizar el tiempo de inactividad de las enfermeras durante una semana**,  
    cumpliendo todas las restricciones reales del sistema hospitalario.

    El sistema está diseñado para **validar, analizar y explicar** la factibilidad del modelo de turnos.
    """)

    # -----------------------------------------
    # 2. OBJETIVO DEL USUARIO
    # -----------------------------------------
    st.header("👤 Objetivo del usuario")
    st.write("""
    Esta herramienta permite al usuario:

    - Cargar una matriz `Xij` generada en MATLAB.  
    - Verificar si la asignación de turnos es **factible**.  
    - Analizar gráficas explicadas paso a paso.  
    - Entender las restricciones del modelo.  
    - Usar una calculadora interactiva para probar escenarios.  
    """)

    # -----------------------------------------
    # 3. ¿QUÉ DEBE HACER EL USUARIO? (PASOS)
    # -----------------------------------------
    st.header("🧭 Pasos que debe seguir el usuario")

    st.write("""
    1️⃣ **Leer brevemente los conceptos básicos** (variables, restricciones, parámetros).  
    2️⃣ Ir a la sección **Explicación del documento** si quiere el detalle completo.  
    3️⃣ Dirigirse a **Cargar modelo y dashboard**.  
    4️⃣ Subir el archivo Excel generado por MATLAB.  
    5️⃣ Observar si el modelo es factible o no.  
    6️⃣ Analizar las gráficas explicadas.  
    7️⃣ Usar la **Calculadora interactiva** para probar otros escenarios.  
    """)
    st.subheader("📄 PDF del documento original")
    pdf_url = "https://drive.google.com/file/d/1Rd9sPU9I0pNGOMvJ3tocUnpNaPz6Zz7T/view?usp=sharing"

    st.markdown(
        f"""
        <a href="{pdf_url}" target="_blank">
            <button style="background-color:#4CAF50;color:white;padding:10px 15px;
            border:none;border-radius:6px;font-size:16px;cursor:pointer;">
                📘 Abrir PDF en nueva pestaña
                </button>
        </a>
        """,
        unsafe_allow_html=True
      )  
    # -----------------------------------------
    # 4. ¿QUÉ HACE ESTA PÁGINA WEB?
    # -----------------------------------------
    st.header("💡 ¿Qué hace esta página web?")

    st.write("""
    Esta aplicación funciona como una **plataforma interactiva** que toma la matriz binaria de turnos 
    y permite:

    - Validar automáticamente si cumple las restricciones reales.  
    - Mostrar gráficas interpretadas para usuarios no expertos.  
    - Explicar cada aspecto del modelo matemático.  
    - Mostrar el PDF original por si el usuario desea profundizar.  
    - Ser utilizada como material académico y herramienta de aprendizaje.  
    """)

    # -----------------------------------------
    # 5. CONCEPTOS NECESARIOS PARA ENTENDER EL MODELO
    # -----------------------------------------
    
    st.header("📚 Conceptos que el usuario debe conocer")
    
    with st.expander("📘 ¿Qué es la Programación Lineal?"):
        st.write("""
        La **programación lineal** es una técnica matemática usada para encontrar la mejor manera 
        de asignar recursos cuando existen **restricciones**.

        En este sistema de turnos de enfermería, la programación lineal permite:

        - Asignar turnos cumpliendo límites de horas.
        - Mantener el descanso adecuado entre turnos.
        - Garantizar mínimos y máximos de enfermeras por turno.
        - Reducir el tiempo de inactividad del personal.
        - Crear esquemas de trabajo justos y eficientes.

        En este modelo, definimos:

        **🔹 Variables (Xᵢⱼ)** → indican si la enfermera *i* trabaja el turno *j*.  
        **🔹 Función objetivo:** minimizar el tiempo inactivo.  
        **🔹 Restricciones:** horas máximas, descansos y límites por turno.

        Así, la programación lineal ayuda a tomar decisiones óptimas dentro de un hospital. 
        """)
        st.image("PROGRAMACION LINEAL.JPG", use_container_width=True)

    with st.expander("🧩 Elementos principales de la Programación Lineal"):
        st.write("""
        Existen diferentes tipos de modelos, pero nuestro proyecto utiliza el más especializado:

        ### **🔹 Programación Entera Binaria**
        Variables solo pueden ser **0 o 1**:  
        - 1 → enfermera asignada  
        - 0 → no asignada

        Otros tipos incluyen:
        - **Programación Lineal (PL):** variables reales.
        - **Programación Entera:** variables enteras o binarias.
        - **Programación Mixta:** combina reales con enteras.
        - **Programación por Metas:** maneja múltiples objetivos. 
        """)
        st.image("ELEMENTOS PRINICPALES DE PROGRAMCION LINEAL.PNG", use_container_width=True)
        st.write("""
        Un modelo de programación lineal está compuesto por:

        ### **1️⃣ Variables de decisión**
        Lo que queremos encontrar.  
        En este proyecto → asignaciones enfermera–turno (**Xᵢⱼ**).

        ### **2️⃣ Función objetivo**
        Lo que se desea optimizar.  
        Aquí → **minimizar el tiempo total de inactividad**.

        ### **3️⃣ Restricciones**
        Límites que deben cumplirse:
        - Máximo de horas por semana  
        - Descanso mínimo entre turnos  
        - Mínimo y máximo de enfermeras por turno  
        """)

    with st.expander("⚙️ Etapas de un modelo de Programación Lineal"):
        st.write("""
        Estas etapas explican cómo se formula y resuelve un modelo:
        1. Plantear variables  
        2. Definir restricciones  
        3. Construir función objetivo  
        """)
        st.image("ETAPAS DE PROGRMACION LINEAL.PNG", use_container_width=True)

    with st.expander("🌟 Beneficios de la Programación Lineal"):
        st.write("Permite optimizar recursos, reducir costos y mejorar decisiones.")
        st.image("BENEFICIOS.JPG", use_container_width=True)

# =======================
# 1. DASHBOARD
# =======================

    st.header("📚 Conceptos básicos para evaluar la factibilidad del modelo de turnos de acuerdo con los conceptos vistos anteriormente.")
    with st.expander("🔢 ¿Qué es una variable de decisión?"):
        st.write("""
        Es una variable que el modelo decide.  
        En este caso, **Xij = 1 si la enfermera i trabaja el turno j**.
        """)

    with st.expander("⚙️ ¿Qué son los parámetros?"):
        st.write("""
        Son datos fijos del problema:  
        - Horas máximas semanales (WH)  
        - Mínimo y máximo de enfermeras por turno  
        - Cantidad de turnos (21 por semana)
        """)

    with st.expander("🎯 ¿Qué es la función objetivo?"):
        st.write("""
        Es lo que buscamos optimizar. El modelo propone **minimizar el tiempo ocioso total**.
        """)

    with st.expander("📏 ¿Qué son las restricciones?"):
        st.write("""
        Son reglas que NO se pueden violar:
        - No superar 40h semanales  
        - Tener descanso (3 turnos ventana)  
        - Cumplir mínimos y máximos por turno  
        """)

    # -----------------------------------------
    # 6. MENSAJE FINAL
    # -----------------------------------------
    st.success("""
    ✔ Con esta información el usuario está preparado para entender el modelo  
    ✔ Puede navegar por las demás secciones para usar el sistema correctamente  
    """)

# =======================
# 2. EXPLICACIÓN DEL MODELO (VERSIÓN SENCILLA Y CLARA)
# =======================
if menu == "📘 Explicación del documento y notación":

    st.title("📘 Explicación del documento y notación (clara y numerada)")

    st.write("""
    Esta sección explica de forma simple cómo funciona el **modelo matemático** 
    que se utiliza para programar turnos de enfermería. 
    La idea es que cualquier persona, incluso sin conocimientos técnicos, 
    pueda entender qué hace el modelo y por qué funciona.
    """)

    # ---------------------------------------------------------
    # 1. PARÁMETROS
    # ---------------------------------------------------------
    st.subheader("1️⃣ Parámetros del modelo (datos que de acuerdo el documento que hemos descargado en PDF)")

    st.write("""
    Los parámetros son valores fijos que el sistema necesita para funcionar:

    - **TN** → Total de enfermeras disponibles.  
    - **21 turnos semanales** → 3 turnos por día × 7 días.  
    - **WH = 40 horas** → horas máximas que una enfermera puede trabajar por semana.  
    - **h = 8 horas** → duración de cada turno.  
    - **Nj(min)** → mínimo de enfermeras que deben estar en el turno j.  
    - **Nj(max)** → máximo permitido en el turno j.
    
    Estos valores NO los calcula el modelo, los recibe como entrada.
    """)

    # ---------------------------------------------------------
    # 2. VARIABLES
    # ---------------------------------------------------------
    st.subheader("2️⃣ Variables de decisón del modelo")

    st.write("""
    Las variables representan decisiones. Aquí la pregunta es:

    **¿La enfermera i trabaja el turno j?**

    Para eso se usa una variable binaria:

    """)

    st.latex(r"X_{ij} = \begin{cases} 1 & \text{si la enfermera i trabaja el turno j}\\ 0 & \text{si no trabaja}\end{cases}")

    st.write("""
    Como hay **TN enfermeras** y **21 turnos**, el total de variables es:
    """)

    st.latex(r"\text{Variables totales} = TN \times 21")

    st.info("""
    EJEMPLO: si TN = 100 ⇒ 100×21 = 2100 variables ✔️ (supera las 2000)
    """)

    # Tabla
    st.subheader("📌 ¿Cómo crece el número de variables?")
    data = {
        "Enfermeras (i)": [50, 100, 150, 200, 100],
        "Turnos (j)": [21, 21, 21, 21, 40],
        "Variables i×j": [1050, 2100, 3150, 4200, 4000]
    }
    st.table(pd.DataFrame(data))

    st.info("""
    EN ESTE CASO, Variables = 100 × 21 = 2100 ✔️
    """)
    # ---------------------------------------------------------
    # 3. FUNCIÓN OBJETIVO
    # ---------------------------------------------------------
    st.subheader("3️⃣ Función Objetivo (¿qué quiere lograr el modelo?)")

    st.write("""
    El objetivo del modelo es:

    ### 👉 **Minimizar el tiempo de inactividad de las enfermeras**  
    (es decir, aprovechar mejor su tiempo sin pasarse del límite de horas).

    Cada turno vale 8 horas.  
    Si una enfermera trabaja pocos turnos → tiene tiempo inactivo.

    La función objetivo matemática es:
    """)

    st.latex(r"Min \left[ WH \cdot TN - 8\sum_{i=1}^{TN}\sum_{j=1}^{21}X_{ij} \right]")

    st.write("""
    Explicación simple:
    - **WH × TN** = horas que el hospital podría usar si TODAS las enfermeras trabajaran 40 h.  
    - **8 × sum(Xij)** = horas realmente programadas en turnos.
    
    Restar ambos valores permite medir cuántas horas NO se están aprovechando.
    """)

    # ---------------------------------------------------------
    # 4. RESTRICCIONES
    # ---------------------------------------------------------
    st.subheader("4️⃣ Restricciones (reglas que el modelo debe cumplir)")

    # R1
    st.markdown("### ✔️ R1 — Límite de horas por enfermera")
    st.latex(r"8\sum_{j=1}^{21} X_{ij} \le 40")
    st.write("""
    Cada enfermera puede trabajar **máximo 40 h** por semana  
    → como cada turno dura 8 h, no puede tener más de 5 turnos.
    """)

    # R2
    st.markdown("### ✔️ R2 — Descanso mínimo entre turnos")
    st.latex(r"X_{i,k}+X_{i,k+1}+X_{i,k+2} \le 1")
    st.write("""
    Esta regla asegura descanso.  
    Una enfermera no puede trabajar tres turnos seguidos.
    """)

    # R3
    st.markdown("### ✔️ R3 — Mínimo por turno")
    st.latex(r"\sum_i X_{ij} \ge Nj(min)")
    st.write("""
    Evita que un turno quede con pocas enfermeras → **garantiza seguridad**.
    """)

    # R4
    st.markdown("### ✔️ R4 — Máximo por turno")
    st.latex(r"\sum_i X_{ij} \le Nj(max)")
    st.write("""
    Controla el número de enfermeras para evitar **sobrecostos**.
    """)

    # R5
    st.markdown("### ✔️ R5 — Naturaleza binaria")
    st.latex(r"X_{ij} \in \{0,1\}")
    st.write("""
    Las decisiones son sí (1) o no (0).  
    No existen medias: no se puede trabajar “medio turno”.
    """)

    # ---------------------------------------------------------
    # PDF original
    # ---------------------------------------------------------
    st.subheader("📄 PDF del documento original")
    pdf_url = "https://drive.google.com/file/d/1Rd9sPU9I0pNGOMvJ3tocUnpNaPz6Zz7T/view?usp=sharing"

    st.markdown(
        f"""
        <a href="{pdf_url}" target="_blank">
            <button style="background-color:#4CAF50;color:white;padding:10px 15px;
            border:none;border-radius:6px;font-size:16px;cursor:pointer;">
                📘 Abrir PDF en nueva pestaña
                </button>
        </a>
        """,
        unsafe_allow_html=True
    )  

# =======================
# 3. CARGAR MODELO Y DASHBOARD — VERSIÓN MEJORADA
# =======================
if menu == "📊 Cargar modelo y dashboard":

    st.title("📊 Análisis de factibilidad del modelo de turnos de enfermería")

    st.write("""
    En esta sección puedes subir el archivo **Xij_SoloTabla.xlsx**, el cual contiene la matriz de 
    decisiones del modelo:

    - **Filas = enfermeras (i)**  
    - **Columnas = turnos (j)**  
    - Cada celda vale **1 si la enfermera trabaja ese turno**, o **0 si no trabaja**  

    """)
    
    uploaded_file = st.file_uploader("📤 Sube el archivo Xij_SoloTabla.xlsx", type=["xlsx"])

    if uploaded_file:

        # ========================
        # 1. Cargar matriz
        # ========================
        X = pd.read_excel(uploaded_file, header=None)
        st.write("### 📋 Matriz cargada (Xij):")
        st.dataframe(X)

        nurses = X.shape[0]     # número de enfermeras
        shifts = X.shape[1]     # número de turnos
        WH = 40                  # máximo permitido por enfermera
        hours = X.sum(axis=1) * 8   # horas por enfermera

        # ========================
        # 2. Evaluar factibilidad
        # ========================
        feasible_hours = (hours <= WH).all()

        st.subheader("📌 Resultado global del modelo")

        if feasible_hours:
            st.success("✔️ El modelo es **FACTIBLE**: todas las enfermeras cumplen el máximo permitido de 40 horas.")
        else:
            st.error("❌ El modelo **NO es factible**: una o más enfermeras exceden las 40 horas permitidas.")

            st.warning(f"👉 Número de enfermeras que exceden el límite: {(hours > WH).sum()}")

        # ========================
        # 3. GRÁFICA 1 — Horas por enfermera
        # ========================
        st.subheader("📈 Gráfica 1: Horas trabajadas por cada enfermera")

        fig, ax = plt.subplots()
        ax.bar(np.arange(nurses) + 1, hours)
        ax.axhline(40, linestyle="--", color="red", label="Máximo permitido (40 h)")
        ax.set_xlabel("Enfermera")
        ax.set_ylabel("Horas trabajadas")
        ax.set_title("Horas asignadas por enfermera")
        ax.legend()

        st.pyplot(fig)

        st.write("""
        ### 📝 Interpretación de la gráfica:
        - Cada barra representa las **horas totales asignadas** a una enfermera.  
        - La línea roja marca el **límite máximo permitido de 40 horas**.  
        - Si alguna barra **sobrepasa la línea roja**, entonces el modelo **no es factible**  
          porque **viola la restricción R1 (límite de horas)**.
        """)

        # ========================
        # 4. GRÁFICA 2 — Carga por día (7 días)
        # ========================
        st.subheader("📆 Gráfica 2: Carga semanal agrupada por día")

        totals = []
        for d in range(7):
            start = d * 3
            end = start + 3
            totals.append(X.iloc[:, start:end].sum().sum())

        fig2, ax2 = plt.subplots()
        ax2.plot(range(1, 8), totals, marker="o")
        ax2.set_xlabel("Día de la semana")
        ax2.set_ylabel("Total de asignaciones (turnos trabajados)")
        ax2.set_title("Carga total de trabajo por día")

        st.pyplot(fig2)

        st.write("""
        ### 📝 Interpretación de la gráfica:
        - Cada punto representa el total de enfermeras que trabajaron en los tres turnos del día.  
        - Permite ver **cuáles días están más cargados** y detectar posibles **desbalanceos**.  
        - Si un día tiene una carga muy baja o muy alta, puede indicar que se violan:  
          - **R3** → mínimo por turno  
          - **R4** → máximo por turno  
        """)


        # ========================
        # 6. NUEVA GRÁFICA  — Turnos por turno (21 turnos)
        # ========================
        st.subheader("📊 Gráfica 3: Enfermeras asignadas por turno individual (21 turnos)")

        nurses_per_shift = X.sum(axis=0)

        fig4, ax4 = plt.subplots(figsize=(10, 4))
        ax4.bar(np.arange(1, shifts + 1), nurses_per_shift)
        ax4.set_xlabel("Turno (j)")
        ax4.set_ylabel("Enfermeras asignadas")
        ax4.set_title("Número de enfermeras por turno")

        st.pyplot(fig4)

        st.write("""
        ### 📝 Interpretación:
        - Se observa cómo están cubiertos los **21 turnos de la semana**.  
        - Turnos con muy pocas o muchas asignaciones pueden violar:  
            - **R3 (mínimo por turno)**  
            - **R4 (máximo por turno)**  
        - Esta gráfica ayuda a evaluar si la cobertura por turno es equilibrada.
        """)

# =======================
# 4. CALCULADORA INTERACTIVA
# =======================
if menu == "🧮 Calculadora interactiva":

    st.title("🧮 Calculadora de factibilidad")

    st.write("""
    Esta herramienta te permite evaluar si una enfermera puede cubrir cierta cantidad 
    de turnos sin superar el límite de **40 horas semanales**.
    """)

    # -------------------------
    # Entradas del usuario
    # -------------------------
    nurse_name = st.text_input("Nombre de la enfermera", "Enfermera 1")

    shifts_worked = st.number_input(
        "¿Cuántos turnos trabajará esta semana?",
        min_value=0,
        max_value=21,
        value=10
    )

    st.write("Cada turno equivale a **8 horas**.")

    # -------------------------
    # BOTÓN PARA CALCULAR
    # -------------------------
    if st.button("Calcular factibilidad"):

        hours = shifts_worked * 8

        # ===============================
        # Resultado textual
        # ===============================
        st.subheader("📌 Resultado del análisis")

        if hours <= 40:
            st.success(f"✔️ {nurse_name} trabajará **{hours} horas**, lo cual es **FACTIBLE** (≤ 40).")
            no_factible = False
        else:
            extra = hours - 40
            st.error(f"❌ {nurse_name} trabajará **{hours} horas**, lo cual NO es factible.")
            st.warning(f"Se excede el límite en **{extra} horas**.")
            no_factible = True

        # ===============================
        # Gráfica de comparación
        # ===============================
        st.subheader("📊 Gráfica: Horas asignadas vs límite permitido")

        fig, ax = plt.subplots(figsize=(5, 3))

        ax.bar(["Horas asignadas"], [hours], color="steelblue")
        ax.axhline(40, color="red", linestyle="--", label="Límite permitido (40 h)")

        ax.set_ylabel("Horas")
        ax.set_title(f"Horas trabajadas por {nurse_name}")
        ax.legend()

        st.pyplot(fig)

        st.write("""
        ### 📝 Interpretación:
        - La barra azul muestra las **horas totales** según los turnos asignados.  
        - Si sobrepasa la línea roja, el plan **no es factible**.  
        """)

        # ======================================================
        # 🔥 NUEVA SECCIÓN: Cuando NO es factible → segunda persona
        # ======================================================
        if no_factible:
            st.markdown("---")
            st.subheader("🧩 Reasignación necesaria")

            st.write("""
            Como esta enfermera **no puede cubrir todos los turnos**, 
            otra persona deberá asumir parte de la carga.
            """)

            second_turns = st.number_input(
                "¿Cuántos turnos cubrirá la otra persona?",
                min_value=0,
                max_value=21,
                value=5,
                key="segunda_persona"
            )

            second_hours = second_turns * 8

            # Resultado
            if second_hours <= 40:
                st.success(f"✔️ La segunda persona trabajará **{second_hours} horas**, lo cual es FACTIBLE.")
            else:
                extra2 = second_hours - 40
                st.error(f"❌ La segunda persona trabajará **{second_hours} horas**, NO es factible.")
                st.warning(f"Se excede el límite en **{extra2} horas**.")

            # Gráfica
            st.subheader("📊 Gráfica: Segunda persona")

            fig2, ax2 = plt.subplots(figsize=(5, 3))

            ax2.bar(["Horas asignadas"], [second_hours], color="orange")
            ax2.axhline(40, color="red", linestyle="--", label="Límite permitido (40 h)")

            ax2.set_ylabel("Horas")
            ax2.set_title("Horas trabajadas por la segunda persona")
            ax2.legend()

            st.pyplot(fig2)

            st.write("""
            ### 📝 Interpretación:
            - Esta gráfica muestra si la **segunda persona** puede asumir los turnos restantes.  
            - Permite validar rápidamente si la redistribución es viable.  
            """)



