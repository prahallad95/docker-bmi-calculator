# BMI Calculator using Flask & Docker

## Overview

This is a simple **BMI (Body Mass Index) Calculator** built with **Python Flask** and containerized using **Docker**. Users can enter their weight and height through a web interface, and the application calculates and displays their BMI.

---

## Features

* Simple and responsive web interface
* Calculates BMI based on user input
* Built with Python Flask
* Dockerized for easy deployment
* Beginner-friendly project

---

## Technologies Used

* Python 3
* Flask
* HTML
* Docker

---

## Project Structure

```text
bmi-calculator/
│── app.py
│── requirements.txt
│── Dockerfile
│── README.md
└── templates/
    └── index.html
```

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/bmi-calculator.git
cd bmi-calculator
```

---

## Run Locally

Install the required package:

```bash
pip install -r requirements.txt
```

Start the Flask application:

```bash
python app.py
```

Open your browser and visit:

```
http://localhost:5000
```

---

## Run Using Docker

### Build the Docker Image

```bash
docker build -t bmi-calculator .
```

### Run the Docker Container

```bash
docker run -d -p 5000:5000 --name bmi-app bmi-calculator
```

Open your browser:

```
http://localhost:5000
```

---

## Example

**Input**

* Weight: **70 kg**
* Height: **1.75 m**

**Output**

```
Your BMI is: 22.86
```

---

## BMI Formula

```
BMI = Weight (kg) / Height² (m²)
```

---

## Docker Commands

### List Running Containers

```bash
docker ps
```

### Stop the Container

```bash
docker stop bmi-app
```

### Start the Container

```bash
docker start bmi-app
```

### Remove the Container

```bash
docker rm -f bmi-app
```

### Remove the Docker Image

```bash
docker rmi bmi-calculator
```

---

## Future Improvements

* Add BMI categories (Underweight, Normal, Overweight, Obese)
* Improve the UI using Bootstrap
* Add input validation
* Deploy on a cloud platform (AWS, Azure, or Render)
* Add unit tests

---

## License

This project is intended for learning and educational purposes.

