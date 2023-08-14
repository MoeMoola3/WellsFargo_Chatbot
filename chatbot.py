from flask import Flask, request, render_template
import os
import openai
import sys

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/')  # this is the home page route
# def hello_world(
# ):  # this is the home page function that generates the page code
#   return "Hello world!"
def index():
  return render_template('index.html')


@app.route('/webhook', methods=['POST'])
async def webhook():
  try:
    req = request.get_json(silent=True, force=True)
    fulfillmentText = 'you said'
    query_result = req.get('queryResult')
    query = query_result.get('queryText')

    start_sequence = "\nWALLY->"
    restart_sequence = "\nUser->"

    if query_result.get('action') == 'input.unknown':
      response = None
      response = openai.Completion.create(
        model="davinci:ft-personal-2023-02-16-14-08-08",
        prompt=
        "The following is a conversation with a digital marketing solution chatbot for Wells Fargo. The chatbot is called Wally. Wally is helpful, creative, clever, and very friendly.\n\nWALLY-> Hello, I am your personal digital marketing solution for Wells Fargo. What can I help you with today?\nUser->"
        + query + "WALLY->",
        temperature=0.89,
        max_tokens=162,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"])

    # result = response.get('choices')[0].get('text')
    result = response.get('choices')[0].get('text').replace(
      restart_sequence, '')

    return {"fulfillmentText": result, "source": "webhookdata"}
    return '200'
  except Exception as e:
    print('error', e)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print('oops', exc_type, fname, exc_tb.tb_lineno)
    return '400'


app.run(host='0.0.0.0', port=81)
