import streamlit as st
import ctransformers
from ctransformers import AutoModelForCausalLM

def init():
	ctransformers.Config(context_length=4096,max_new_tokens=6096)
	return AutoModelForCausalLM.from_pretrained("TheBloke/StableBeluga-7B-GGUF", model_file="stablebeluga-7b.Q4_K_S.gguf", model_type="llama", gpu_layers=0)

def ask(message):
    system_prompt = "### System:\nYou are StableBeluga, an AI that follows instructions extremely well. Help as much as you can. Remember, be safe, and don't do anything illegal.\n\n"
    prompt = f"{system_prompt}### User: {message}\n\n### Assistant:\n"
    return llm(prompt)

llm = init()
response = "Welcome"

if "messages" not in st.session_state:
    st.session_state.messages = []
    
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        response = ask(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
    
# Display assistant response in chat message container
with st.chat_message("assistant"):
    if response:
        st.markdown(response)
    
# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})