SMS Spam Detection and Model Comparison

   An end to end machine learning project designed to classify SMS messages as either "spam" or "ham" (legitimate). Using Jupyter Notebook, we provide a deep dive into the performance differences between standard non-ensemble algorithms and advanced ensemble techniques.

1.  Project Overview

 SMS spam is a classic Natural Language Processing (NLP) problem. This project takes a raw dataset of text messages and applies preprocessing and machine learning techniques to build robust classifiers. A core focus of this project is comparing the predictive power of single, non-ensemble models against the combined strength of ensemble methods, followed by model interpretability using SHAP values.

2.  Models Explored

This project explicitly trains and evaluates two categories of machine learning models to highlight their comparative strengths:

A. **Non-Ensemble Models**: These models serve as our baseline and provide fast, interpretable classification:

i. **Decision Tree Classifier**: A simple, rule-based model that splits data based on feature thresholds.

ii. **Multinomial Naive Bayes**: A probabilistic classic for text classification, highly effective with word frequency data.

iii. **Support Vector Machine (LinearSVC)**: A powerful linear model that finds the optimal hyperplane to separate spam from ham.

B. **Ensemble Models**: We applied hyperparameter tuning (GridSearchCV) to optimize their performance:

i. **Random Forest**: An ensemble of decision trees trained on random subsets of data and features, reducing overfitting.

ii. **Bagging Classifier**: Utilizes a base estimator (Decision Trees) and trains them on varied subsets of the dataset to improve stability and accuracy.

iii. **AdaBoost Classifier**: A boosting technique that sequentially trains models, giving more weight to previously misclassified messages to improve overall recall.

3.  Key Pipeline Features

A. Text Preprocessing: Utilizes TfidfVectorizer to convert raw text messages into a numerical format while filtering out English stop words.

B. Class Balancing: Applies Synthetic Minority Over-sampling Technique (SMOTE) to handle the inherent imbalance between spam and ham messages in the training data.

C. Model Interpretability: Extracts and visualizes the top 10 most important features (words) for each ensemble model. Uses SHAP (SHapley Additive exPlanations) to explain the output of the Random Forest model.

D. Data Clustering: Employs TruncatedSVD for dimensionality reduction and scipy's hierarchical clustering to generate a dendrogram, visualizing the natural groupings of the text data.

4.  Results Summary

The models were evaluated using Accuracy, Precision, Recall, and F1 Score:

A. Non-Ensemble Performance: The Linear SVC achieved exceptional baseline performance, frequently reaching 99% accuracy with perfect precision, demonstrating that simple linear boundaries work well for this specific TF-IDF feature space.

B. Ensemble Performance: Post-hyperparameter tuning, models like AdaBoost and Random Forest showed strong, balanced F1 scores on the SMOTE-adjusted data, proving highly effective at identifying spam without falsely flagging legitimate messages.

5.  Built With

A. Python 3

B. Pandas and NumPy: Data manipulation and analysis.

C. Scikit-Learn: Machine learning algorithms, TF-IDF vectorization, and evaluation metrics.

D. Imbalanced-Learn: SMOTE for handling dataset class imbalance.

E. SHAP: Game-theoretic approach to explain model predictions.

F. SciPy and Matplotlib: Hierarchical clustering and visualization.

6.  Installation and Usage

7.  Install required dependencies:
    pip install pandas numpy scikit-learn imbalanced-learn shap scipy matplotlib

8.  Run the Notebook:
    Launch Jupyter Notebook and open spam-detection-ml.ipynb.
    Note: Ensure your dataset is encoded in latin-1 as expected by the pandas read function.

9. **Dataset** : 
The notebook expects a dataset named **spam.csv** with at least two columns:
A. Category (or label): Containing the string **'ham' **or **'spam'.**

B. Message (or text): The raw text of the SMS message.
