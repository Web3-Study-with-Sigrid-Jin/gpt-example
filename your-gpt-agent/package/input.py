import streamlit

def get_text():
    input_text = streamlit.text_input("Type in your prompt below", key="input")
    return input_text