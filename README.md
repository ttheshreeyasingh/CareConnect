# CareConnect
> Voice Based Virtual Health Assistant

![Overview](./Docs/readme-util/demo.gif)


## Table of Contents
1. [Introduction](#introduction)
2. [Project Overview](#project-overview)
3. [Components](#components)
   - [Frontend](#frontend)
   - [Flask Application](#flask-application)
   - [Plivo API Integration](#plivo-api-integration)
4. [Installation](#installation)
   - [Frontend Setup](#frontend-setup)
   - [Flask Application Setup](#flask-application-setup)
   - [Ngrok Setup](#ngrok-setup)
5. [Usage](#usage)
6. [Demo](#demo)
7. [Design Overview](#design-overview)
   - [Call Flow](#call-flow)
   - [Symptom-to-Disease Model](#symptom-to-disease-model)
8. [Benefits](#benefits)
9. [Future Scope](#future-scope)

---

## 1. Introduction <a id="introduction"></a>
Welcome to CareConnect, an innovative healthcare assistant leveraging Plivo APIs to provide accessible healthcare advice through phone calls. This document provides comprehensive information about the project, its components, installation instructions, and usage guidelines.

---

## 2. Project Overview <a id="project-overview"></a>
CareConnect aims to make healthcare advice easily accessible by utilizing Plivo's Voice API. It enables users to seek medical advice through phone calls, offering a seamless and convenient experience.

---

## 3. Components <a id="components"></a>

### Frontend <a id="frontend"></a>
The frontend is responsible for providing the user interface. It allows users to initiate a call, input their number which is then used to initiate an outbound call to the user.

### Flask Application <a id="flask-application"></a>
The Flask application acts as the backend server. It handles the initiation of outbound calls, processes user input, interfaces with the Hugging Face API for symptom-to-disease prediction, and communicates with the Plivo API for voice interactions.

### Plivo API Integration <a id="plivo-api-integration"></a>
Plivo's Voice API is a crucial component of CareConnect. It facilitates voice interactions between users and the system, enabling seamless communication.

It takes the speech input from the user and converts it to text using the Speech-to-Text API. The text is then used to predict a diagnosis based on the symptoms provided by the user. The diagnosis is then converted to speech using the Text-to-Speech API and communicated to the user.

Also used is the Plivo Number API, which is used to purchase a Plivo number for the outbound call.


---

## 4. Installation <a id="installation"></a>

Install required dependencies using 
```
pip install -r requirements.txt
```
### Frontend Setup <a id="frontend-setup"></a>
1. Clone the repository: `git clone <repo-url>`
2. Navigate to the `frontend` directory using the following command:
```
cd CareConnect/src/frontend
```

3. Run the following command to start a local server:
```
python3 -m http.server
```

### Flask Application Setup <a id="flask-application-setup"></a>
1. Navigate to the `src` directory: 
```
cd CareConnect/src
```
2. Run the Flask application: `python main.py`.

### Ngrok Setup <a id="ngrok-setup"></a>
1. Download and install Ngrok from [https://ngrok.com/download](https://ngrok.com/download).
2. Open a terminal and run Ngrok: `
```
ngrok http 5000
```
3. Ngrok will provide a secure tunnel to the locally running Flask app. Use the generated URL in your Plivo application by pasting it in the .env file (which is created to store the auth details and huggingface token).

---

## 5. Usage <a id="usage"></a>
1. Access the frontend interface via `http://0.0.0.0:8000/index.html`.
2. Click on "Start Call" to initiate a call.
3. Follow the prompts to input your symptoms using voice.
4. Wait for the system to provide a diagnosis based on your symptoms.

---

## 6. Demo <a id="demo"></a>
A live demonstration of the project is available at [Demo Video Link](https://www.loom.com/share/bc4c3bad8b4b4083b1c960f718d36402?sid=54661ef6-4459-4caa-ab68-27d4d8e201ec).

---

## 7. Design Overview <a id="design-overview"></a>

### Call Flow <a id="call-flow"></a>
1. Outbound call is initiated when the user clicks "Start Call".
2. User provides symptom input via voice.
3. Symptom-to-Disease model predicts a diagnosis using the speech input.

### Symptom-to-Disease Model <a id="symptom-to-disease-model"></a>
- The model is based on a Transformer-based encoder-decoder architecture.
- Trained on a dataset of 100,000 symptom-disease pairs.
- [Link To Model](https://huggingface.co/abhirajeshbhai/symptom-2-disease-net)
---

## 8. Benefits <a id="benefits"></a>
- Quick and accessible healthcare advice.
- Efficient processing of speech input.
- Reliable diagnoses based on a comprehensive dataset.

---

## 9. Future Scope <a id="future-scope"></a>
- Integration with Plivo Messaging API for follow-up information.
- Implementation of Call Recording for reference.
- Call Forwarding to Specialist Doctors for advanced consultation.

---

