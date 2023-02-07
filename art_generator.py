import streamlit as st
import openai
from base64 import b64decode

openai.api_key = st.secrets['OPENAI_API_KEY']

st.title('DALL-E art generator')

def convert_to_image(img_data):
    return b64decode(img_data["b64_json"])

def generate_art(description):
    """ A function making a call to DALL-E with passed description
    and updating image URL """
    response = openai.Image.create(
    prompt=PROMPT,
    n=1,
    size="1024x1024",
    response_format="b64_json",
    )
    return convert_to_image(response["data"][0])



PROJECT = st.text_input("Enter a name for your art project")
PROMPT = st.text_area("Describe the creating that you want DALL-E to create for you. \
                      A more detailed request can improve the result.")

if st.button("Submit"):
    st.header(PROJECT)
    generated_img = generate_art(PROMPT)
    st.image(generated_img, output_format="PNG")
else:
    pass




