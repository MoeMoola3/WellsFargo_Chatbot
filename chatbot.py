# from flask import Flask, request
# import os
# import openai
# import sys
# from dotenv import load_dotenv

# app = Flask(__name__)

# load_dotenv()
# openai.api_key = os.getenv("API_KEY")

# @app.route('/')  # this is the home page route
# def hello_world(
# ):  # this is the home page function that generates the page code
#     return "Hello world!"

# @app.route('/webhook', methods=['POST'])
# async def webhook():
#     try:
#         req = request.get_json(silent=True, force=True)
#         fulfillmentText = 'you said'
#         query_result = req.get('queryResult')
#         query = query_result.get('queryText')

#         start_sequence = "\nWALLY->"
#         restart_sequence = "\nUser->"

#         if query_result.get('action') == 'input.unknown':

#             response = await openai.Completion.create(
#                 model="davinci:ft-personal-2023-02-16-14-08-08",
#                 prompt="The following is a conversation with an AI assistant. The assistant is Wally. Wally is helpful, creative, clever, and very friendly. \n\nWALLY-> Hello, I am your personal financial assistant. What can I help you with today?\nUser->"+query+"WALLY->",
#                 temperature=0.89,
#                 max_tokens=162,
#                 top_p=1,
#                 frequency_penalty=0,
#                 presence_penalty=0.6,
#                 stop=["\n"]
#             )

#         result = response.get('choices')[0].get('text')

#         return {
#             "fulfillmentText":
#             result,
#             "source":
#             "webhookdata"
#         }
#         return '200'
#     except Exception as e:
#         print('error',e)
#         exc_type, exc_obj, exc_tb = sys.exc_info()
#         fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#         print('oops',exc_type, fname, exc_tb.tb_lineno)
#         return '400'


# # if __name__ == '__main__':
# #     app.run(debug=True, port=os.getenv("PORT", default=5000))


# if __name__ == '__main__':
#     app.run(port=int(os.environ.get("PORT", 5000)))



from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)