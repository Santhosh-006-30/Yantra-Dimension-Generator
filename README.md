# 🕉️ Yantra Dimension Generator

This project generates **astronomical yantra dimensions** (Samrat Yantra, Rama Yantra, Digamsa Yantra, etc.) based on a given **latitude and longitude**.

## 🚀 Features
- Input latitude & longitude
- Calculates dimensions of traditional Indian astronomical instruments
- Clean UI using **Tailwind CSS**
- Flask backend for computation

## 📂 Project Structure
yantra-dimension-generator/
│── app.py                 # Flask backend
│── requirements.txt       # Dependencies
│── README.md              # Project details
│── templates/
│   └── index.html         # Frontend UI
│── static/
│   └── (optional assets)  # Tailwind (if not using CDN)

1. Clone the repo:
   ```bash
   git clone https://github.com/Santhosh-006-30/yantra-dimension-generator.git
   cd yantra-dimension-generator

2. Create virtual environment & install dependencies:
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)
pip install -r requirements.txt

3. Run the app:
python app.py

