# 📧 Spam Detection Model

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-orange.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Tests](https://img.shields.io/badge/Tests-7%20passed-brightgreen.svg)

A machine learning project that classifies SMS messages as **spam** or **ham** using Natural Language Processing (NLP) and scikit-learn. Built with a clean, production-ready structure including a REST API for real-time predictions.

---

## 🚀 Demo

```python
from src.models.predict import predict_message

predict_message("FREE prize! Click now to win cash!")  # → SPAM
predict_message("Hey, are you coming to class today?") # → HAM
```

---

## 📊 Model Performance

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---|---|---|---|
| Naive Bayes | 97.85% | 97.20% | 96.80% | 97.00% |
| **Logistic Regression** | **98.20%** | **97.50%** | **97.10%** | **97.30%** |
| Random Forest | 97.50% | 96.90% | 96.40% | 96.60% |

> ✅ **Best Model: Logistic Regression** with 98.20% accuracy

---

## 🗂️ Project Structure

```
spam-detection/
│
├── data/
│   ├── raw/                    # Original dataset (not tracked by git)
│   └── processed/              # Train, validation, test splits
│       ├── train.csv
│       ├── val.csv
│       └── test.csv
│
├── notebooks/                  # Jupyter notebooks for exploration
│   ├── 01_eda.ipynb            # Exploratory Data Analysis
│   ├── 02_preprocessing.ipynb  # Text cleaning & preparation
│   ├── 03_feature_engineering.ipynb  # TF-IDF feature extraction
│   ├── 04_model_training.ipynb # Model training & comparison
│   └── 05_evaluation.ipynb     # Metrics & result analysis
│
├── src/                        # Production-ready source code
│   ├── data/
│   │   ├── make_dataset.py     # Dataset creation & splitting
│   │   └── preprocess.py       # Text cleaning functions
│   ├── features/
│   │   └── build_features.py   # TF-IDF vectorization
│   ├── models/
│   │   ├── train.py            # Model training
│   │   ├── predict.py          # Prediction functions
│   │   └── evaluate.py         # Evaluation metrics
│   └── utils/
│       ├── helpers.py          # Utility functions
│       └── logger.py           # Logging configuration
│
├── models/                     # Saved model artifacts
│   ├── spam_classifier.pkl
│   └── tfidf_vectorizer.pkl
│
├── api/
│   └── app.py                  # FastAPI REST API
│
├── tests/                      # Unit tests
│   ├── test_preprocess.py
│   └── test_model.py
│
├── reports/
│   └── figures/                # Generated visualizations
│       ├── confusion_matrix.png
│       └── roc_curve.png
│
├── .gitignore
├── requirements.txt
├── config.yaml
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/rahat-ai-dev/spam-detection-model.git
cd spam-detection-model
```

### 2. Create a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the dataset

Download the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) from Kaggle and place it in:

```
data/raw/spam.csv
```

---

## 🔄 How to Run

### Run the notebooks (in order)

```bash
jupyter notebook
```

Open and run each notebook in order:
1. `01_eda.ipynb`
2. `02_preprocessing.ipynb`
3. `03_feature_engineering.ipynb`
4. `04_model_training.ipynb`
5. `05_evaluation.ipynb`

### Run the API

```bash
uvicorn api.app:app --reload
```

API will be available at: `http://127.0.0.1:8000`

Interactive docs at: `http://127.0.0.1:8000/docs`

### Run the tests

```bash
pytest tests/ -v
```

---

## 🌐 API Usage

### Check if API is running

```bash
GET http://127.0.0.1:8000/
```

```json
{
  "message": "Spam Detection API is running!"
}
```

### Predict a message

```bash
POST http://127.0.0.1:8000/predict
```

**Request:**
```json
{
  "text": "FREE prize! Click now to win cash!"
}
```

**Response:**
```json
{
  "text": "FREE prize! Click now to win cash!",
  "prediction": "SPAM",
  "is_spam": true
}
```

---

## 🧪 Test Results

```
tests/test_model.py::test_spam_prediction       PASSED
tests/test_model.py::test_ham_prediction        PASSED
tests/test_model.py::test_model_loads           PASSED
tests/test_preprocess.py::test_lowercase        PASSED
tests/test_preprocess.py::test_removes_punctuation  PASSED
tests/test_preprocess.py::test_removes_stopwords    PASSED
tests/test_preprocess.py::test_empty_string     PASSED

7 passed in 1.21s
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.8+ | Core language |
| pandas & numpy | Data manipulation |
| NLTK | Text preprocessing |
| scikit-learn | ML models & TF-IDF |
| FastAPI | REST API |
| uvicorn | ASGI server |
| pytest | Unit testing |
| matplotlib & seaborn | Visualizations |
| Jupyter | Notebooks |

---

## 📈 How It Works

```
Raw SMS Text
     ↓
Text Cleaning (lowercase, remove punctuation, stopwords, stemming)
     ↓
TF-IDF Vectorization (3000 features)
     ↓
Logistic Regression Classifier
     ↓
SPAM or HAM
```

---

## 📁 Dataset

- **Name:** SMS Spam Collection Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- **Size:** 5,572 SMS messages
- **Labels:** spam (747) / ham (4,825)

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Rahat**
- GitHub: [@rahat-ai-dev](https://github.com/rahat-ai-dev)

---

⭐ If you found this project helpful, please give it a star!