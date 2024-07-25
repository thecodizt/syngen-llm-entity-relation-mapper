import streamlit as st
import pandas as pd

from input import load_data
from evaluate import evaulate_model
from postprocess import make_many_many, make_one_one

def llm_relation():
    st.title("LLM Based Entity Relation Mapping")
    
    st.subheader("Model")
    model = st.selectbox(label="Choose the LLM to be used", options=["mistral", "vicuna"])
    
    st.subheader("Relation Context")
    context = st.text_input(label="Enter the base context for linking items")
    
    rel_types = ["One to One", "Many to Many"]
    threshold = 0
    st.subheader("Relation Type")
    rel_type = st.selectbox("Type of relation mapping", options=rel_types)
    
    if rel_type == rel_types[1]:
        threshold = st.slider(label="Threshold for likelihood probability", max_value=1.0, min_value=0.0, step=0.1)
    
    st.subheader("Table 1")
    dataset_1 = load_data("t1")
    
    if dataset_1 is not None and len(dataset_1) > 0:
        st.subheader("Table 2")
        dataset_2 = load_data("t2")
        
        st.header("Generated Pairing")
        
        if dataset_2 is not None and len(dataset_2) > 0:
            relation = evaulate_model(dataset_1=dataset_1,dataset_2=dataset_2, model=model, context=context)
            
            if relation is not None:
                
                st.subheader("Final Results")
                if rel_type == rel_types[0]:
                    one_one = make_one_one(relation)
                    st.dataframe(one_one)
                    
                    file = one_one.to_csv(index=False)
                    st.download_button(label="Download CSV", data=file,file_name="relations.csv" )
                    
                if rel_type == rel_types[1]:
                    many_many = make_many_many(relation, threshold)
                    st.dataframe(many_many)
                    
                    file = many_many.to_csv(index=False)
                    st.download_button(label="Download CSV", data=file,file_name="relations.csv")
            
if __name__ == "__main__":
    llm_relation()
                