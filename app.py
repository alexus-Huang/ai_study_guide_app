from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
print("API KEY:", os.getenv("GEMINI_API_KEY"))
app = Flask(__name__)


genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/",methods = ["POST","GET"])
def main():
    text_output = ""
    user_input_display = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        user_input_display = user_input
        prompt = (
            "You are a helpful AI assistant. "
            "If the user provides a statement, summarize it. "
            "If the user asks a question or gives an instruction, fulfill it naturally.\n\n"
            f"User Input: {user_input}"
        )
        
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(user_input)
        text_output = response.text
        
    return render_template("index.html",output = text_output,user_input = user_input_display)
if __name__ == "__main__":
    app.run(debug=True) 