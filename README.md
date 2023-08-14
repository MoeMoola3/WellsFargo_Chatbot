# WellsFargo_Chatbot

The chatbot was built using data from the American multinational financial service Wells 
Fargo. The chatbot is named WALLY and is prompted to be clever, creative and friendly.

The first step in creating the chatbot was collecting the necessary data for fine tuning. Since 
I could not find a dataset online that fit the specific requirements, I performed web scraping 
to collect the data. Product descriptions were collected directly from the Wells Fargo 
website and customer testimonials were gathered from www.sitejabber.com.

The testimonials collected from sitejabber were varied which I broke into 3 different 
categories, “bad reviews”, “good reviews” and “mixed reviews”. Once collecting the data, I 
compiled them into an excel sheet.

Once the data was collected I used jupyter notebook to organize the data and convert it into 
json format. I then used openai data preparation tools to convert the json file into a jsonl
format as required by openai to perform the finetuning operation. The jsonl file was then 
used to train the davinci model. The davinci model was chosen because it is the most 
powerful and flexible model.

On completion of successfully creating a fine-tuned model. I then created a basic flask 
application and webhook to connect to Dialogflow. Dialogflow was used to create the 
conversational interface for the chatbot. The flask application was then hosted on replit and 
published.

### Steps to run the chatbot
The chatbot can be accessed via the link https://replit.com/@moemoola01. The project is 
called WFchatbot. The code to create the webhook can also be viewed here.
- Click into the WFchatbot tile
- At the top of the project make sure the repl is running
- You can now use the link to access the chatbot interface 
https://WFchatbot.moemoola01.repl.co

### Snapshots of the fine-tuning operation
<img src="https://github.com/MoeMoola3/WellsFargo_Chatbot/assets/73942516/1177565e-217a-4cc8-9ede-75878220d849"  width="850" height="600" />

### Snapshots of conversations with Wally

<img src="https://github.com/MoeMoola3/WellsFargo_Chatbot/assets/73942516/f87b3818-1ab7-4ecb-a293-33d0bb473c60"  width="850" height="500" />
<img src="https://github.com/MoeMoola3/WellsFargo_Chatbot/assets/73942516/cac0f7a2-aed7-420e-99d6-99d3dda66ca2"  width="850" height="500" />
<img src="https://github.com/MoeMoola3/WellsFargo_Chatbot/assets/73942516/2edb8421-f2e2-4d71-874f-e77d879fd900"  width="850" height="500" />
