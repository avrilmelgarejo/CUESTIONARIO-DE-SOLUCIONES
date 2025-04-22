import streamlit as st

st.set_page_config(page_title="Preguntas sobre Disoluciones", layout="centered")
st.title("📘 Disoluciones: Preguntas y Respuestas")

st.write("Haz clic en cada pregunta para ver su respuesta.")

qa = {
    "1. ¿Qué es una solución (o disolución)?":
        "Es una mezcla homogénea de dos o más sustancias en una sola fase. El soluto se disuelve en el solvente formando una sola fase visible.",
    
    "2. ¿Qué significa que los componentes de una disolución pierden sus características individuales?":
        "Significa que una vez mezclados, ya no se pueden distinguir ni separar por medios físicos simples. Actúan como una única sustancia.",
    
    "3. ¿Qué es solución acuosa?":
        "Es una disolución donde el solvente es agua. Por ejemplo, la sal disuelta en agua forma una solución acuosa.",
    
    "4. ¿Es falso o verdadero que las mezclas de gases, tales como la atmósfera, a veces también se consideran como soluciones?":
        "✅ Verdadero. Las mezclas de gases como el aire son soluciones homogéneas de diferentes gases.",
    
    "5. ¿Qué les sucede a las sales, los ácidos y las bases cuando se disuelven en el agua?":
        "Se disocian en iones. Por ejemplo, la sal (NaCl) se separa en iones Na⁺ y Cl⁻ en el agua.",
    
    "6. Da 3 características de las soluciones (o disoluciones).":
        "- Son homogéneas.\n- Sus componentes no se pueden separar mecánicamente.\n- El soluto se encuentra en menor proporción que el solvente.",
    
    "7. ¿Qué es soluto y cuáles son sus características?":
        "El soluto es la sustancia que se disuelve. Se encuentra en menor cantidad y puede ser sólido, líquido o gas.",
    
    "8. ¿Qué es solvente y cuáles son sus características?":
        "El solvente es la sustancia que disuelve al soluto. Se encuentra en mayor proporción. El agua es el solvente más común.",
    
    "9. ¿Cómo se explica el carácter homogéneo de las soluciones y la imposibilidad de separar sus componentes por medios mecánicos?":
        "Porque sus partículas están distribuidas uniformemente a nivel molecular, y no se pueden filtrar ni separar fácilmente.",
    
    "10. En base a su concentración, ¿cómo se clasifican las disoluciones?":
        "- Diluidas: baja cantidad de soluto\n- Concentradas: alta cantidad de soluto\n- Saturadas: no disuelven más soluto\n- Sobresaturadas: contienen más soluto del que normalmente se disolvería",
    
    "11. Si sabemos que cuando diluimos 36 gramos de sal de mesa en 100 gramos de agua a 20°C, la solución queda saturada, ¿qué pasaría si intentamos disolver 38 gramos de sal en 100 gramos de agua?":
        "Quedarán 2 gramos sin disolverse. La solución estará saturada y el exceso de sal precipitará al fondo."
}

for pregunta, respuesta in qa.items():
    with st.expander(pregunta):
        st.markdown(respuesta)
