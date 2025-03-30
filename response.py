from openai import OpenAI
import json
import boto3

aws_client = boto3.client("secretsmanager", region_name="us-east-1")
response = aws_client.get_secret_value(SecretId="openai_llm_key")
secret = json.loads(response["SecretString"])
client = OpenAI(api_key=secret["OPENAI_KEY"])



def get_gpt4omini(prompt):
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages= [
      {"role": "system", "content": "You are a helpful therapist who believes in Jesus."},
      {"role": "user", "content": prompt}
    ]
  )
  gpt_res = completion.choices[0].message.content
  return gpt_res

def get_summary(conversation_history):
  summary_prompt = open("summary_prompt.txt", "r").read()
  summary_prompt = summary_prompt.format(conversation= conversation_history)
  summary = get_gpt4omini(summary_prompt)
  return summary

def get_ai_response(query, summary):
  ai_prompt = open("christ_prompt.txt", "r").read()
  ai_prompt = ai_prompt.format(query=query, conversation_summary=summary)
  return get_gpt4omini(ai_prompt)

def get_christ_res(query, conversation_history):
  predefined_questions = json.load(open("predefined_questions.json", "r"))
  if query in predefined_questions:
    response = predefined_questions[query]
    return response
  summary = get_summary(conversation_history)
  ai_response = get_ai_response(query, summary)
  return ai_response