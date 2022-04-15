"""
@author: KartikeyaSharma
"""


import streamlit as st
import keras
import numpy as np
# import matplotlib.pyplot as plt

if "button_clicked" not in st.session_state:    
    st.session_state.button_clicked = False
    

def generate_images_from_pretrained_model(model):
    test_input = np.random.normal(0, 1, (1, 100))

    gen_image = (model.predict(test_input))
    return gen_image


def yes_button_click():
    st.write("Yay! The Generator is Happy 😊")

def no_button_click():
    st.write("Uh-oh The Generator is Sad 😔")


def main():
    
    st.markdown("<h5 style='text-align: left; color: Pink;'>Author: Kartikeya Sharma</h5>",
    unsafe_allow_html=True)
    st.write("[GitHub Repository](https://github.com/Kartikeya2710/Machine-Learning/tree/main/GANs)")
    st.markdown("<h2 style='text-align: center; color: White;'>Generate Hand-Written Digits using GANs</h2>",
    unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: White;'>Hit Create to generate Hand-Written Digits!</h5>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        st.write('')

    with col2:
        pretrained_model = keras.models.load_model("Saved Model")
        cen_button = st.button("Create")

        
    with col3:
        st.write("")


    col1, col2, col3 = st.columns([1, 1.8, 1])

    with col2: 
        if (cen_button or st.session_state.button_clicked):
            st.session_state.button_clicked = True
            gen_image = generate_images_from_pretrained_model(pretrained_model)
                
            
            st.image(gen_image.reshape((28, 28, 1)), clamp=True, channels='RGB', use_column_width=True)
            st.success('Does this look Hand-Written?')

            yes_button =  st.button("Looks Real")
            no_button = st.button("Not Quite")
            if yes_button:
                yes_button_click()

            elif no_button:
                no_button_click()

main()