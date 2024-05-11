# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 01:19:12 2024

@author: marpi
"""

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

import warnings
from langchain._api import LangChainDeprecationWarning
warnings.simplefilter("ignore", category=LangChainDeprecationWarning)


llm=CTransformers(model='C:\\Users\\marpi\\Downloads\\AINEW\\Models\\llama-2-7b-chat.bin',
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature':0.01})

print("done")

