# **Gold Price Prediction AI-Powered Web Application**

## **Overview**
The project involves creating a web application using machine learning to predict gold prices based on historical data. It leverages the Flask framework and is containerized using Docker for easy deployment.

## **Key Features**
- **AI Model**: Trains a model using historical data to predict gold prices.
- **Real-Time Predictions**: Provides predictions on future gold price trends.
- **Web Interface**: Built using Flask for easy interaction.
- **Dockerized**: Easy deployment through Docker.

## **Technologies**
- **Python**
- **Flask**
- **scikit-learn**
- **pandas**
- **numpy**
- **Plotly**
- **Docker**

## **Usage**

### **Running Locally**

1. Clone the repository:
   ```bash
   git clone https://github.com/zaed-nusirat0/Gold-Price-Predictor-AI-Powered-Web-App.git
Navigate to the project directory and install dependencies:

bash
cd Gold-Price-Predictor-AI-Powered-Web-App
pip install -r requirements.txt
Run the application:

bash
python app.py
The app runs on http://127.0.0.1:5000/.

Running with Docker
Build Docker image:

bash
docker build -t gold_price_prediction .
Run Docker container:

bash
docker run -d -p 8000:8000 --name price_prediction gold_price_prediction
The app will be accessible at http://127.0.0.1:8000/.

Contributing
Fork the repository, create a branch, make changes, and submit a pull request.

Docker Image Usage
Pull Image:

bash

docker pull zaidtech/gold_price_prediction:latest
Run Container:

bash

docker run -d -p 8000:8000 --name price_prediction zaidtech/gold_price_prediction:latest
Project Structure
app.py: Main application.
Dockerfile: Docker configuration.
requirements.txt: Dependencies.
model.pkl: Pre-trained model.
data/: Dataset directory.
Important Notes
Predictions are based on historical data and may not reflect sudden market changes.
For production, use a more robust server like Gunicorn.
Bash Scripts
build_image.sh: Builds the Docker image.
run_container.sh: Runs the Docker container.
start_local.sh: Runs the app locally without Docker.
Docker Hub Push
Log in, tag, and push the image to Docker Hub:

bash
docker login
docker tag gold_price_prediction:latest zaidtech/gold_price_prediction:tagname
docker push zaidtech/gold_price_prediction:tagname
csharp
