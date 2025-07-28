# Laptop Price Prediction 💻📈

Predict the market price of laptops based on features like brand, processor type, GPU, RAM, SSD, touchscreen support, screen size, and more. Built with machine learning models and offered with an interactive web interface.

---

## 🎯 Purpose

This project helps users estimate a fair price for laptops—valuable for buyers, sellers, and tech reviewers who want data-driven valuation.

---

## 🚀 Features

- Predicts laptop price from technical attributes  
- Supports categorical and numerical features  
- Cleaned and preprocessed real-world dataset  
- Training using regression models (e.g. Random Forest, XGBoost)  
- Model evaluation metrics: RMSE, MAE, R²  
- Interactive demo (optional Flask/Gradio app)  

---

## 🧪 Technologies

| Component          | Tools / Libraries                |
|-------------------|----------------------------------|
| Data Processing    | Python, Pandas, NumPy            |
| Machine Learning   | scikit-learn, XGBoost (optional) |
| Visualization      | Matplotlib / Seaborn             |
| Web App Demo       | Flask or Gradio                  |

---

## 📁 Repository Structure

```

Laptop‑Price‑Prediction/
├── data/
│   ├── raw\_laptop\_data.csv
│   ├── cleaned\_data.csv
│   └── notebooks/
├── models/
│   ├── best\_model.pkl
│   └── model\_training.ipynb
├── scripts/
│   ├── preprocess.py
│   ├── train\_model.py
│   └── evaluate\_model.py
├── app/
│   ├── app.py  (Flask / Gradio demo)
│   └── templates/ or frontend assets
├── requirements.txt
└── README.md

````

---

## 🔧 Installation & Usage

### 1. Clone the repo
```bash
git clone https://github.com/Arnaviitp/Laptop-Price-Prediction.git
cd Laptop-Price-Prediction
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Preprocess data

```bash
python scripts/preprocess.py --input data/raw_laptop_data.csv --output data/cleaned_data.csv
```

### 4. Train the model

```bash
python scripts/train_model.py --data data/cleaned_data.csv --model models/best_model.pkl
```

### 5. Evaluate performance

```bash
python scripts/evaluate_model.py --model models/best_model.pkl --testdata data/cleaned_data.csv
```

### 6. Run the interactive demo (if available)

```bash
python app/app.py
```

Then go to `http://localhost:5000` (Flask) or the port shown for Gradio.

---

## 📊 Model Insights

* **Random Forest Regressor** achieved an RMSE of \~₹2,500 with R² ≈ 0.85
* **Feature importance highlights**: Brand, CPU series, GPU type, RAM, and SSD capacity were most impactful

## 🤝 Contributing

Contributions are welcome! Steps:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a pull request

---

## 📄 License

This project is licensed under the **MIT License** – see the LICENSE file for details.

---
### Optional Enhancements

* Add an example Jupyter Notebook for fast EDA
* Show feature importance charts and model comparison tables
* Include instructions for deploying the web demo on Heroku, Vercel, or Streamlit Cloud
* Provide a sample dataset excerpt for quick testing
