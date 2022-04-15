"""
@author: KartikeyaSharma
"""


import streamlit as st
import keras
import numpy as np
# import matplotlib.pyplot as plt

def generate_images_from_pretrained_model(model):
    test_input = np.random.normal(0, 1, (1, 100))

    gen_image = (model.predict(test_input))
    return gen_image

def main():
    
    st.markdown("<text style='text-align: left; color: Red;'>Author: Kartikeya Sharma</text>",
    unsafe_allow_html=True)
    st.write("GitHub Repository: [link]()")
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
        if cen_button: #making and printing our prediction
            gen_image = generate_images_from_pretrained_model(pretrained_model)
            st.image(gen_image.reshape((28, 28, 1)), clamp=True, channels='RGB', use_column_width=True)
            st.success('The GAN generated this image. Does this look human-like?')

if __name__ == '__main__':
    main()