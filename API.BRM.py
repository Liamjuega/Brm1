import requests
import json
import PyPDF2

def extraer_texto_pdf(pdf_path):
    with open(pdf_path, "rb") as archivo:
        lector_pdf = PyPDF2.PdfReader(archivo)
        texto = ""
        for pagina in lector_pdf.pages:
            texto += pagina.extract_text()
    return texto

# pathPDF
pdf_path = input("Path: ")
texto_pdf = extraer_texto_pdf(pdf_path)
print(texto_pdf)  # printPDF

api_key = "AKIAUN7I4AARHAOOPOFW"

prompt = input("Tu Prompt: ")
headers = {
    "Autorization": f"Bearer {api_key}",
    "Content-Type": "aplicattion/json",
}
data = {
    "model": "anthropic.claude-3-5-haiku-20241022-v1:0",
    "messages": 
    {
        {
            "role":"user",
            "content":prompt
        }
    }
}

url = "https://us-east-1.console.aws.amazon.com/bedrock/home?region=us-east-1#/text-generation-playground?modelId=anthropic.claude-3-5-haiku-20241022-v1%3A0&provisionedModelArn=arn%3Aaws%3Abedrock%3Aus-east-1%3A304894181410%3Ainference-profile%2Fus.anthropic.claude-3-5-haiku-20241022-v1%3A0&modelOptionValue=arn%3Aaws%3Abedrock%3Aus-east-1%3A304894181410%3Ainference-profile%2Fus.anthropic.claude-3-5-haiku-20241022-v1%3A0&modelOptionName=US+Anthropic+Claude+3.5+Haiku"

response = requests.post(url, headers=headers, json=data)

answer = response.json()['choices'][0]['message']['content']

print("\n", answer, "\n")