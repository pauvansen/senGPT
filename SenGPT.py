from langchain_core.prompts import PromptTemplate
import time
import langchain
from langchain_community.cache import SQLiteCache
from langchain_community.cache import InMemoryCache
from langchain_openai import OpenAI
import os


class SenGPTCache:
    def __init__(self) -> None:
        self.llm = None 
        self.cache = None 
        self.prompt_template = None
    
    def setup_model(self):
        self.llm = OpenAI(model_name = "gpt-3.5-turbo-instruct", api_key="Your OPENAI_API_KEY")

    def setup_in_memory_cache(self):
        self.cache = InMemoryCache()
        langchain.llm_cache = self.cache

    def setup_sqlite_cache(self):
        try:
            os.remove(".cache.db")
        except FileNotFoundError:
            pass
        self.cache = SQLiteCache(database_path = ".cache.db")
        langchain.llm_cache = self.cache

    def setup_prompt_template(self, template_string):
        self.prompt_template = PromptTemplate(template=template_string,input_variables=["question"])
    def predict(self, prompt):
        if self.llm is None:
            raise RuntimeError("Language model has not been set up. Please call setup_model() first")

        if self.cache is None:
            raise RuntimeError("Cache has not been set up. Please call setup_in_memory_cache or setup_sqlite_cache() first!")
        
        if self.prompt_template is None:
            raise RuntimeError("Prompt template has not been set up. Please call setup_prompt_template() first")
        

        start_time = time.time()
        formated_prompt = self.prompt_template.format(question=prompt)
        result = self.llm.invoke(formated_prompt)
        end_time = time.time()

        print (f"The predict function took {end_time - start_time:.2f} seconds ")
        return result