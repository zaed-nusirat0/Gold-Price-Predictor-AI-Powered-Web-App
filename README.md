# **Gold Price Prediction AI-Powered Web Application**

## **Project Overview**

The **Gold Price Prediction AI-Powered Web Application** is an innovative tool designed to predict future gold prices using machine learning algorithms. This project utilizes various data science techniques and models to analyze historical gold price data and predict the future trend of gold prices. The application is powered by a Flask web framework, allowing users to interact with the prediction model through a simple, easy-to-use interface.

### **Features**

- **AI Model**: Trains a machine learning model using historical gold price data.
- **Real-Time Predictions**: Provides users with real-time gold price predictions based on the trained model.
- **Web Interface**: A user-friendly interface powered by Flask for seamless interaction with the prediction model.
- **Dockerized**: The application is containerized using Docker, making it easy to deploy and use on any machine.

---

## **Technologies Used**

- **Python**: The main programming language for building the application and machine learning model.
- **Flask**: A micro web framework for building the web application.
- **scikit-learn**: Used for building the machine learning model for gold price prediction.
- **pandas & numpy**: For data manipulation and preprocessing.
- **Plotly** & **Matplotlib**: For data visualization.
- **Docker**: To containerize the application for easy deployment.

---

## **How to Use the Application**

### **Running Locally**

1. **Clone the Repository**:

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/zaed-nusirat0/Gold-Price-Predictor-AI-Powered-Web-App.git
Install Dependencies:

Navigate to the project directory and install the required dependencies by running:

bash
نسخ الكود
cd Gold-Price-Predictor-AI-Powered-Web-App
pip install -r requirements.txt
Run the Application:

Start the Flask application locally by running:

bash
نسخ الكود
python app.py
By default, the application will be running on http://127.0.0.1:5000/. You can access the web application through your browser.

Running the Application with Docker
If you prefer to run the application inside a Docker container, follow these steps:

Build the Docker Image:

First, build the Docker image using the following command:

bash
نسخ الكود
docker build -t gold_price_prediction .
Run the Docker Container:

After building the image, you can run the container with the following command:

bash
نسخ الكود
docker run -d -p 8000:8000 --name price_prediction gold_price_prediction
The application will be accessible at http://127.0.0.1:8000/ from your browser.

Predicting Gold Prices
Once the application is running, you can input the relevant historical data into the web form and get predictions on the future gold price trend. The machine learning model used in this application analyzes past price movements and generates predictions based on that data.

How to Contribute
We welcome contributions to the project! To contribute:

Fork the repository.
Create a new branch for your feature or fix.
Make the necessary changes and commit them.
Push your changes and create a pull request.
Docker Image Usage
This project is also available as a Docker image, making it easy to deploy and run on any machine with Docker installed. To use the pre-built image, follow these steps:

Step 1: Pull the Docker Image
You can pull the latest image from Docker Hub using:

bash
نسخ الكود
docker pull zaidtech/gold_price_prediction:latest
Step 2: Run the Docker Container
Once the image is pulled, run the container using:

bash
نسخ الكود
docker run -d -p 8000:8000 --name price_prediction zaidtech/gold_price_prediction:latest
This will launch the application, and you can access it at http://127.0.0.1:8000/.

Project Structure
Here’s an overview of the main files and directories in this project:

bash
نسخ الكود
Gold-Price-Predictor-AI-Powered-Web-App/
│
├── app.py                  # Main Flask application
├── Dockerfile              # Docker configuration file
├── requirements.txt        # Python dependencies
├── model.pkl               # Saved machine learning model
├── data/                   # Directory containing datasets
│   └── gold_price_data.csv # Historical gold price data
└── README.md               # Project documentation
Important Notes
The model is trained on historical gold price data, so the predictions are based on past trends and may not always reflect sudden market changes.
For production use, consider deploying the app using a more robust WSGI server like Gunicorn or uWSGI instead of Flask's built-in development server.
The model.pkl file is a pre-trained model used for prediction. If you want to retrain the model, you can follow the steps in the Python scripts inside the repository to retrain it with new data.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Conclusion
The Gold Price Prediction AI-Powered Web Application provides a simple yet effective solution for predicting future gold prices. By combining machine learning with web technologies, the app offers real-time predictions based on historical data. The Dockerization of the project ensures easy deployment and usage across various environments.

Bash Scripts for Docker Build and Run
build_image.sh
bash
نسخ الكود
#!/bin/bash

# This script builds the Docker image

echo "Building Docker image..."
docker build -t gold_price_prediction .
echo "Docker image built successfully."
run_container.sh
bash
نسخ الكود
#!/bin/bash

# This script runs the Docker container

echo "Running Docker container..."
docker run -d -p 8000:8000 --name price_prediction gold_price_prediction
echo "Docker container is running at http://127.0.0.1:8000/"
start_local.sh
bash
نسخ الكود
#!/bin/bash

# This script runs the app locally without Docker

echo "Starting the Flask app locally..."
python app.py
echo "App is running at http://127.0.0.1:5000/"
Requirements.txt
makefile
نسخ الكود
Flask==2.3.2
pandas==2.1.1
numpy==1.24.4
scikit-learn==1.3.1
plotly==5.16.1
seaborn==0.12.2
matplotlib==3.8.0
Dockerfile
dockerfile
نسخ الكود
# Use the latest Python image
FROM python:latest

# Set the working directory in the container
WORKDIR /app

# Copy all the files into the container
COPY . /app/

# Install the dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port 8000 for the application
EXPOSE 8000

# Run the application
CMD ["python", "app.py", "--host", "0.0.0.0", "--port", "8000"]
Pushing Docker Image to Docker Hub
To push the Docker image to Docker Hub, make sure you're logged in with:

bash
نسخ الكود
docker login
Then, tag the image:

bash
نسخ الكود
docker tag gold_price_prediction:latest zaidtech/gold_price_prediction:tagname
And finally, push the image:

bash
نسخ الكود
docker push zaidtech/gold_price_prediction:tagname

