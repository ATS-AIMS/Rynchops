"""
Python app to demo mT5/XLSum.
"""
import json
import streamlit as st
from rynchops import DemoModel, SPLIT_MODES
import pandas as pd


def init():
    """Loads the model from HF.
    """
    if "model" not in st.session_state:
        st.session_state.model = DemoModel()
    if "canned" not in st.session_state:
        with open("canned_text.json", "r", encoding="utf-8") as fp:
            st.session_state.canned = json.load(fp)["canned_text"]
    if "summa_mode" not in st.session_state:
        st.session_state.summa_mode = "Paragraph"


# layout ----------------
# on session start
st.set_page_config(
    "Arabic To English Abstractive Summarization Demo",
    page_icon=":eyes:",
    layout="wide",
)
with st.spinner("Loading Model..."):
    init()

# sidebar
input_mode = st.sidebar.radio("Input Mode", ["Canned Text", "Text Box"])

# title and desc
st.title("Arabic To English Summarization Demo")
st.markdown(
    "This app demonstrates cutting-edge NLP summarization and translation capabilities."
)

# input form area
st.header("Input Area")
input_form = st.empty()

# output area
col1, col2 = st.columns(2)
with col1:
    st.header("Full Input")
    full_input = st.empty()

with col2:
    st.header("Summarization")
    full_output = st.empty()

# about section
with st.expander("About the Model"):
    st.markdown(
        """This model is a combination of two models: mT5 and M2M100.

1. The model [mT5](https://arxiv.org/abs/2010.11934) was trained on the multilingual dataset [XLSum](https://aclanthology.org/2021.findings-acl.413/) by the [BUET CSE](https://cse.buet.ac.bd/research/index.php) NLP Group. The model can be found on the [:hugging_face: model repository](https://huggingface.co/csebuetnlp/mT5_multilingual_XLSum). It was intended to summarize news articles.
    
2. The model [Opus MT](https://github.com/Helsinki-NLP/Opus-MT) is the translation model. It is maintained by Helinski NLP.
    """
    )

# interactivity -----------------

# set the input form depending on the sidebar input mode
if input_mode == "Canned Text":
    with input_form.form("Input"):
        text_key = st.selectbox(
            "Select a canned input",
            options=[i for i, _ in enumerate(st.session_state.canned)],
            format_func=lambda i: st.session_state.canned[i]["Label"],
        )
        submitted = st.form_submit_button("Summarize!")
else:  # if input_mode == "Text Box":
    with input_form.form("Input"):
        text_area = st.text_area("Your Text")
        summa_mode = st.selectbox(label="Split On", options=SPLIT_MODES.keys())
        is_arabic = st.checkbox(label="Arabic Text?", value=True)
        submitted = st.form_submit_button("Summarize!")

# run the model on submit
if submitted:
    # collect the input fields
    if input_mode == "Canned Text":
        text_of_input = st.session_state.canned[text_key]["Full Text"]
        summa_mode = "Paragraph"
        is_arabic = st.session_state.canned[text_key]["do_translate"]
    else:  # if input_mode == "Text Box":
        text_of_input = text_area

    full_input.markdown(text_of_input)

    # pass input to model and print output
    with st.spinner("Summarizing..."):
        text_of_output = st.session_state.model.run(
            text_of_input, split_mode=summa_mode, do_translate=is_arabic
        )
        full_output.markdown("\n\n".join(text_of_output))
