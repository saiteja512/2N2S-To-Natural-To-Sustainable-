# Smart Rainwater Harvesting Management System

A predictive web dashboard that provides real-time monitoring and forecasting for rainwater harvesting tanks to promote efficient water conservation.

## 🌦️ Overview
This project is an end-to-end data science application that solves the problem of inefficient rainwater management. Many current systems lack the real-time data and predictive insights needed to prevent overflow or unnecessary use of municipal water.

This application provides a solution by:
- Training a machine learning model on historical data to predict the next day's water level.
- Serving this model via a Python/Flask backend API.
- Displaying the data on a real-time, user-friendly web dashboard that provides actionable recommendations.

## ✨ Key Features
- **Real-Time Tank Monitoring**: A dynamic gauge visualizes the current water level in the tank.
- **Predictive Forecasting**: Uses a machine learning model to predict the water level for the next day based on current levels, usage, and rainfall forecasts.
- **Actionable Alerts**: The system provides clear messages, such as *"System Normal"* or *"Motor On Recommended"*, to help users make smart decisions.
- **Client-Server Architecture**: A robust backend built with Flask serves predictions to a sleek, modern frontend built with HTML, Tailwind CSS, and Chart.js.

## 🛠️ Technology Stack

| Component        | Technologies Used                                |
|------------------|--------------------------------------------------|
| Backend & API    | Python, Flask, Flask-CORS                        |
| Machine Learning | Scikit-learn (Linear Regression), Pandas, NumPy, Joblib |
| Frontend         | HTML, Tailwind CSS, JavaScript, Chart.js         |

## ⚙️ Setup and Installation

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rainwater-harvesting-system.git
cd rainwater-harvesting-system
```

### 2. Create and Activate a Virtual Environment
It's recommended to use a virtual environment to manage project dependencies.

**Windows:**
```bash
python -m venv venv
.env\Scriptsctivate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all the required Python libraries from the requirements.txt file.
```bash
pip install flask flask-cors scikit-learn pandas joblib numpy
```

### 4. (Optional) Train the Model
The repository already includes a pre-trained model (`rainwater_model.pkl`). However, if you modify the `rainwater_data.csv` or want to retrain the model, run the following command:
```bash
python model_trainer.py
```
This will create/overwrite the `rainwater_model.pkl` file.

### 5. Run the Application
Start the Flask backend server.
```bash
python app.py
```
You should see output in your terminal indicating that the model has been loaded and the server is running on [http://127.0.0.1:5000](http://127.0.0.1:5000).

### 6. View the Dashboard
Open your web browser and navigate to:
```
http://127.0.0.1:5000
```
You should see the live dashboard!

## 📁 Project Structure
```
├── app.py                  # The Flask backend server
├── model_trainer.py        # Script to train the ML model
├── rainwater_model.pkl     # The pre-trained machine learning model
├── rainwater_data.csv      # The dataset used for training
├── templates/
│   └── index.html          # The frontend HTML dashboard
└── README.md               # You are here!
```

## 👨‍💻 Contributors
- Saiteja Mareda  
- Tanvi  
- Sathwik Vanam  
- Noor Mohammad  
