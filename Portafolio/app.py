import streamlit as st

st.sidebar.title("Menu de navegacion")
options = ["Sobre mi", "Proyectos", "Contacto", "Habilidades"]
choice = st.sidebar.selectbox("Ir a", options)

if choice=="Sobre mi":
    col1, col2 = st.columns(2)
    with col1:
        st.title("Este es mi protafolio")
        st.write("Soy tal persona ...")

    with col2:
        st.image("img/perfil.jpg")
elif choice=="Proyectos":
    
    st.title("Proyectos")
    proyecto1 = "img/proyecto1.png"
    proyecto2 = "img/proyecto2.png"
    proyecto3 = "img/proyecto3.jpg"
    proyecto4 = "img/proyecto4.png"

    if st.button("Proyecto 1"):
        st.image(proyecto1, caption="Proyecto 1", use_column_width=True)

    if st.button("Proyecto 2"):
        st.image(proyecto2, caption="Proyecto 2", use_column_width=True)

    if st.button("Proyecto 3"):
        st.image(proyecto3, caption="Proyecto 3", use_column_width=True)
    
    if st.button("Proyecto 4"):
        st.image(proyecto4, caption="Proyecto 4", use_column_width=True)
    
    
elif choice=="Contacto":
    st.header("Este es mi contacto")
    
    nombre = st.text_input("Ingresa tu nombre")
    e_mail = st.text_input("Ingresa tu e-mail")
    mensaje = st.text_area("Ingresa tu mensaje")

    if st.button("Enviar"):
        if nombre and e_mail and mensaje:
            st.success("Mensaje enviado")
        else:
            st.warning("Por favor termine de llenar")
elif choice=="Habilidades":
    st.header("Habilidades")

    skills = {"Python": 0.8, "JavaScript": 0.7, "HTML/CSS": 0.6, "SQL": 0.5}

    for skill, value in skills.items():
        st.write(skill)
        st.progress(value)