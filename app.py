from flask import Flask, request, jsonify,render_template
import openai
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Chave da API
openai.api_key = ""


@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')  
    if not user_input:
        return jsonify({'error': 'Nenhum input fornecido'}), 400

    try:
        response =  openai.ChatCompletion.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "user", "content": user_input}  
            ]
        )
        
        bot_reply = response['choices'][0]['message']['content']
        
        return jsonify({"bot_reply": bot_reply})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
