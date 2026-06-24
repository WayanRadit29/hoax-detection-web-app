# Hoax Detection Web App

A web-based hoax detection system with text prediction, information filtering, and a lightweight AI module.

## Description

Hoax Detection Web App is a simple web application developed as a final project for the Software Development and Design Concept course.

The system allows users to:

* Input text information or news content
* Predict whether the content is classified as **Hoax** or **Tidak Hoax**
* Browse information stored in the database
* Filter information by date, source, topic, and label

The primary focus of this project is software engineering implementation, including frontend development, backend integration, database management, system design, and deployment.

---

## Features

### 1. Hoax Prediction

Users can enter text through a web form and receive a prediction result:

* Hoax
* Tidak Hoax

The prediction is generated using a lightweight rule-based AI module.

### 2. Information Database

The application stores information and news records inside a SQLite database.

Each record contains:

* Title
* Content
* Source
* Topic
* Publication Date
* Label

### 3. Information Filtering

Users can filter information based on:

* Date range
* Source
* Topic
* Label (Hoax / Tidak Hoax)

---

## Technology Stack

### Frontend

* HTML5
* Tailwind CSS
* JavaScript

### Backend

* Python
* Flask

### Database

* SQLite

### AI Module

* Rule-Based Text Classification

---

## Project Structure

```text
hoax-detection-web-app/
│
├── app.py
├── prediction.py
├── database.db
├── import_dataset.py
├── merge_datasets.py
├── preprocess_hoax_data.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── final_dataset.csv
│   ├── hoax_data_final.csv
│   ├── non_hoax_data.csv
│   └── Meta Data.xlsx
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── index.html
│   ├── prediction.html
│   ├── information.html
│   └── article.html
│
└── __pycache__/
```

---

## Dataset

The project uses a combination of:

### Hoax Dataset

Based on data collected from TurnBackHoax and processed into:

```text
data/hoax_data_final.csv
```

### Non-Hoax Dataset

Manually curated informational data from official-style sources such as:

* BMKG
* Kementerian Kesehatan
* Bank Indonesia
* Kominfo
* Government Websites
* Academic Portals

Stored in:

```text
data/non_hoax_data.csv
```

### Final Dataset

Merged dataset used by the application:

```text
data/final_dataset.csv
```

Dataset schema:

```text
title
content
source
topic
publication_date
label
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/WayanRadit29/hoax-detection-web-app.git

cd hoax-detection-web-app
```

Create virtual environment:

```bash
python -m venv softeng
```

Activate virtual environment:

### Windows PowerShell

```powershell
.\softeng\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Run Flask server:

```bash
python app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Application Pages

### Home Page

Route:

```text
/
```

Displays project overview and navigation.

### Prediction Page

Route:

```text
/prediction
```

Allows users to input text and receive prediction results.

### Information Page

Route:

```text
/information
```

Displays stored information records and filtering features.

### Article Page

Route:

```text
/article/<id>
```

Displays detailed information for a selected article.

---

## Database

Database engine:

```text
SQLite
```

Database file:

```text
database.db
```

Main table fields:

```text
id
title
content
source
topic
publication_date
label
```

---

## AI Prediction Module

The application uses a lightweight rule-based classifier.

The model analyzes:

* Hoax-related phrases
* Clickbait indicators
* Suspicious wording patterns
* Trusted source signals

Output:

```text
Hoax
```

or

```text
Tidak Hoax
```

---

## Team Members

| Name                | Role                                                |
| ------------------- | --------------------------------------------------- |
| Wayan | Backend Developer, Database Integration, Deployment |
| Berliana            | Frontend Developer                                  |
| Nabil               | AI Engineer                                         |

---

## Course Information

Course:

```text
Konsep Pengembangan dan Perancangan Perangkat Lunak
```

Project Type:

```text
Final Project
```

Academic Year:

```text
2025/2026
```

---

## License

This project was developed for educational purposes as a university final project.
