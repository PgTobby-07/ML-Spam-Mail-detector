HuggingFaceWebsite- https://huggingface.co/spaces/pgtobby1/SPamdetector    Please wait a bit for it to load

📩 SMS Spam Detector (Machine Learning)

📌 Overview
This project is a Machine Learning-based SMS Spam Detection system that classifies text messages as either Spam or Ham (Not Spam).

It uses:
- TF-IDF Vectorization to convert text into numerical features  
- Support Vector Machine (SVM) for classification  
- Gradio to create a simple and interactive web interface  

---

⚙️ How It Works

1. Input Message  
The user enters an SMS message into the interface.

2. Text Vectorization  
- The message is transformed using a TF-IDF Vectorizer  
- This converts text into numerical features based on word importance  

3. Prediction with SVM Model  
- The processed message is passed into a trained SVM model  
- The model predicts:
  1 → Spam  
  0 → Ham  

4. Output Display  
- Spam → SPAM (red)  
- Ham → HAM (blue)  

---

🧠 Machine Learning Components

🔹 TF-IDF Vectorizer (vectorizer.pkl)
- Converts text data into feature vectors  
- Captures importance of words in messages  
- Helps reduce noise from common words  

🔹 SVM Model (svm_model.pkl)
- A supervised learning algorithm used for classification  
- Effective for high-dimensional text data  
- Finds the optimal boundary between spam and non-spam messages  

---

📁 Project Structure

app.py  
svm_model.pkl  
vectorizer.pkl  
README.md  

---

🚀 Installation & Setup

1. Clone the repository
git clone https://github.com/your-username/sms-spam-detector.git  
cd sms-spam-detector  

2. Install dependencies
pip install gradio scikit-learn  

3. Run the application
python app.py  

---

🌐 Usage

1. Run the app  
2. Open the provided local URL in your browser  
3. Enter an SMS message  
4. View the prediction instantly  

---

💡 Example

Message: "Congratulations! You've won a free ticket!" → SPAM  
Message: "Hey, are we still meeting today?" → HAM  

---

🎯 Features

- Simple and clean UI using Gradio  
- Fast predictions  
- Lightweight and easy to deploy  
- Uses proven ML techniques for text classification  

---

📊 Future Improvements

- Add preprocessing (stopword removal, stemming, etc.)  
- Try deep learning models (LSTM, BERT)  
- Deploy online (Hugging Face / Streamlit Cloud)  
- Extend to email spam detection  

---

📜 License
This project is open-source and free to use.
