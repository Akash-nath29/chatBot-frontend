from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Load the H5 model
model = tf.keras.models.load_model('my_model.h5')
# Set the tokenizer (you should adapt this to your specific tokenization process)
tokenizer = Tokenizer()
# Load or generate your tokenizer with your specific vocabulary

@app.route('/')
def index():
    return render_template('chat.html') #return render_template('index.html', response=None)

@app.route('/ask', methods=['GET', 'POST'])
def ask():
    user_message = request.form.get('user_message')

    # Tokenize the user message (adapt this to your tokenizer)
    user_message = [user_message]
    user_message = tokenizer.texts_to_sequences(user_message)
    user_message = pad_sequences(user_message, padding='post', maxlen=18)

    # Make a prediction using the loaded model
    response = model.predict(user_message)

    # Convert the model's response back to text (adapt this to your specific dataset)
    response = "This is a placeholder response."
    print(jsonify({'response': response}))
    return jsonify({'response': response}) #return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)