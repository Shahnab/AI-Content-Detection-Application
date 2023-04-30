import streamlit as st
import streamlit.components.v1 as components

st. set_page_config(layout="wide")

col1, mid, col2= st.columns([1,1,20])
with col1:
    st.image("https://contentatscale.ai/ai-content-detector/assets/images/seo-content.png", width=70)
with col2:
    st.markdown("# AI Content Detection Tool")

tab1, tab2 = st.tabs(["Interface", "About the App"])

with tab1:
# 	st.markdown("AI Content Detection Tool")
	st.components.v1.iframe("https://shad0ws-ai-content-perplexityscorer.hf.space", width=1100, height=650, scrolling=True)

with tab2:
# 	st.markdown("AI Content Detection Tool")
	st.markdown("##### “AI content detectors work by analyzing the text and using a variety of metrics to determine whether it was written by a human or a machine")
	st.markdown("##### One of the key metrics is perplexity, which is a measure of how well a language model can predict the next word in a given sentence")
	st.subheader("How does this tool work")
	st.markdown("##### When a text is fed through an AI content detector, the tool analyzes the perplexity score to determine whether it was likely written by a human or generated by an AI language model")
	st.subheader("Demo video")
	st.video('https://youtu.be/IvdYNZKjc1c')
