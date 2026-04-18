import gradio as gr
import pickle

# Load trained model
with open("svm_model.pkl", "rb") as f:
    svm_model = pickle.load(f)

# Load TF-IDF vectorizer
with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Prediction function
def predict_sms(message):
    message_vec = vectorizer.transform([message])
    prediction = svm_model.predict(message_vec)[0]

    if prediction == 1:
        return "<span style='color:red;font-weight:bold;'>SPAM</span>"
    else:
        return "<span style='color:blue;font-weight:bold;'>HAM</span>"

# Gradio interface
iface = gr.Interface(
    fn=predict_sms,
    inputs=gr.Textbox(
        label="Enter an SMS message",
        placeholder="Type your message here..."
    ),
    outputs=gr.HTML(label="Prediction"),
    title="SMS Spam Detector",
    description="This app uses an SVM model trained with TF-IDF features to detect spam messages."
)

iface.launch()
