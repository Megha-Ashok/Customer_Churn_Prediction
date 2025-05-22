# Customer Churn Prediction Application

## 📊 Project Overview / Purpose

This Customer Churn Prediction system helps businesses identify which customers are likely to stop using their services. By leveraging machine learning and deep learning models, the application predicts customer churn based on historical customer data, allowing companies to proactively retain valuable customers and reduce revenue loss.

With data-driven insights, businesses can tailor marketing campaigns, improve customer engagement, and increase customer lifetime value — turning churn risk into retention opportunity.

---

## Why Customer Churn Prediction?

Customer churn is a critical challenge for subscription-based and service companies. Losing customers without understanding why leads to wasted acquisition costs and lost revenue. This project:

- Predicts customer churn with high accuracy.
- Identifies risk factors impacting customer retention.
- Helps businesses make informed decisions on customer retention strategies.
- Saves costs by targeting customers most likely to churn.
- Improves overall customer satisfaction and loyalty.

---

## Key Features & Services

1. **Data Preprocessing**  
   Cleans and prepares customer data by handling duplicates, encoding categorical variables, and scaling features.

2. **Feature Engineering**  
   Includes important customer attributes such as geography, gender, age, balance, tenure, credit card status, and more.

3. **Deep Learning Model**  
   Utilizes a simple feed-forward neural network built with TensorFlow/Keras to predict churn.

4. **Model Evaluation**  
   Evaluates prediction accuracy on a test set and visualizes training/validation loss and accuracy over epochs.

5. **Flask Web App Integration**  
   Provides a user-friendly interface to input customer details and get real-time churn predictions.

---

## 🚀 How It Works

1. Upload customer data (or input manually via UI).  
2. The system preprocesses the inputs (encoding, scaling).  
3. The trained neural network model predicts churn probability.  
4. Results are displayed as **likely to churn** or **likely to stay** with probability scores.  
5. Businesses use insights to implement retention strategies.

---

## Input Features

| Feature           | Description                          |
|-------------------|------------------------------------|
| CreditScore       | Customer credit score               |
| Geography         | Customer location (France, Germany, Spain) |
| Gender            | Customer gender                    |
| Age               | Customer age                       |
| Tenure            | Years with the company             |
| Balance           | Account balance                   |
| NumOfProducts     | Number of products held            |
| HasCreditCard     | Whether customer has a credit card |
| IsActiveMember    | Customer activity status            |
| EstimatedSalary   | Estimated yearly salary             |

---

## Model Architecture

- Input Layer: 11 features  
- Hidden Layer: Dense layer with 3 neurons, sigmoid activation  
- Output Layer: Single neuron, sigmoid activation (binary classification)  
- Loss Function: Binary Cross-Entropy  
- Optimizer: Adam  
- Epochs: 10  

---

## Demo Screenshots

<!-- Replace with your own screenshots -->
<p align="center">
  <img src="images/churn_form.png" alt="Input Form" width="600" />
</p>
<p align="center">
  <img src="images/churn_result.png" alt="Prediction Result" width="600" />
</p>

---

## 🛠️ How to Run Locally

### Prerequisites

- Python 3.7+  
- TensorFlow  
- Flask  
- scikit-learn  
- pandas, numpy  

### Steps

1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/customer-churn-prediction.git
   cd customer-churn-prediction
