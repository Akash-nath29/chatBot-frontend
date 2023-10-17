import tensorflow as tf

# Load the model from the .h5 file
model = tf.keras.models.load_model('model.h5')
def predict():
    data = request.get_json()
    # You can use the 'model' to make predictions here.
    prediction = model.predict(data)
    return jsonify({'prediction': prediction.tolist()})
