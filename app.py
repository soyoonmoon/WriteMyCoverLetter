from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try: 
        description = request.json['description']
        wordLimit = int(request.json['wordLimit'])
        tokensLimit = wordLimit * 5

        response = openai.Completion.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "user", "content": description}
            ],
            max_tokens = tokensLimit
        )

    # debugging purpose
    # chatGPT_response = response.choices[0].text.strip()
    # print(f"ChatGPT response: {chatGPT_response}")
    # print(response.choices[0].message.content)
        return jsonify(response.choices[0].message.content)
    except Exception as e:
        print("Error occurred:", e)
        # return jsonify({"error": str(e)}), 500
        return jsonify({"error": "OpenAI API Error: " + str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
