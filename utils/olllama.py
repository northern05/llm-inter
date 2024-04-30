#ollama installation https://ollama.com/download/linux
#curl -fsSL https://ollama.com/install.sh | sh
#sudo ollama run llama3
import ollama
from werkzeug.exceptions import HTTPException

llama_model = 'llama3'
class LLMDriver:
    def __init__(self):
        self.general_prompt = general_prompt
        self.llm = ollama.Client(host="127.0.0.1:11434")
        self.llm.create(model=llama_model, modelfile=self.general_prompt)

    def generate_static_response(self, messages: list):
        try:
            response = self.llm.chat(model=llama_model, messages=messages)
            print(response['message']['content'])
        except ollama.ResponseError as e:
            raise HTTPException(description=str(e))
        return response['message']['content']


    def setup_general_prompt(self, new_general_prompt: str):
        self.general_prompt = new_general_prompt
        result = self.llm.create(model=llama_model, modelfile=self.general_prompt)
        return result

    def stream_response(self, messages: list):
        try:
            stream = self.llm.chat(
                model=llama_model,
                messages=messages,
                stream=True,
            )
            for chunk in stream:
                print(chunk['message']['content'], end='', flush=True)
        except ollama.ResponseError as e:
            raise HTTPException(description=str(e))
        return stream

general_prompt = """
FROM llama3
SYSTEM You are mario from super mario bros.
"""

if __name__ == '__main__':
    llm = LLMDriver()
    llm.stream_response([{'role': 'user', 'content': "I have tomatoes, basil and cheese at home. What can I cook for dinner?"}])
