# SCT_ML_01
 # 🏠 House Price Prediction using Linear Regression

This project is a **Machine Learning-based web app** that predicts house prices using a **Linear Regression model**. The user can input features like the total living area, number of bedrooms, and bathrooms, and instantly receive a predicted sale price through an interactive **Streamlit interface**.

---

## 📌 What Does This Model Do?

This ML model was trained using a dataset of real estate listings and applies **Linear Regression** to estimate house prices based on:

- `GrLivArea` – Above-ground living area (in square feet)
- `BedroomAbvGr` – Number of bedrooms above ground
- `FullBath` – Number of full bathrooms

Once trained, the model is saved as `model.pkl` and used within the app to provide predictions in real-time.

---

## 👤 Who Is This For?

- 🧪 Students learning ML & Streamlit
- 💼 Developers showcasing ML in a web app
- 🏡 Anyone interested in how house pricing prediction works

---

## 💡 How to Use This Project Locally

### 1️⃣ Step-by-Step Setup Instructions

#### ✅ Step 1: Clone the repository
```bash
git clone https://github.com/Anindya-Dev/SCT_ML_01.git
cd SCT_ML_01
#Installs all the required libraries.
pip install -r requirements.txt
#Run the app on a localhost server.
streamlit run app.py

Hosted on streamlit - https://sctml01-hhtkvabx5gprgecdqgtojs.streamlit.app/
