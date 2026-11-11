# Iris Flower Prediction App

A small interactive web app, built with [Streamlit](https://streamlit.io/), that predicts the species of an Iris flower from four measurements. It trains a Random Forest classifier on the classic Iris dataset from scikit-learn and updates the prediction live as you move the sliders.

## Features

- Sidebar sliders for the four flower measurements (sepal length/width, petal length/width)
- A table showing the values you entered
- The predicted species: *setosa*, *versicolor* or *virginica*
- How likely each species is, according to the model

## How it works

1. Your slider values are collected into a one-row pandas DataFrame.
2. The Iris dataset (150 samples, 3 species) is loaded with `sklearn.datasets.load_iris()`.
3. A `RandomForestClassifier` is trained on the full dataset.
4. The model predicts the species and the probability of each class for your input.

| Feature      | Slider range (cm) | Default |
|--------------|-------------------|---------|
| Sepal length | 4.3 – 7.9         | 5.4     |
| Sepal width  | 2.0 – 4.4         | 3.4     |
| Petal length | 1.0 – 6.9         | 1.3     |
| Petal width  | 0.1 – 2.5         | 0.2     |

The slider ranges match the minimum and maximum values found in the dataset.

## Requirements

- Python 3.8+
- streamlit
- scikit-learn
- pandas
- numpy

## Getting started

```bash
# 1. Create and activate a virtual environment (optional, but recommended)
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 2. Install the dependencies
pip install streamlit scikit-learn pandas numpy

# 3. Run the app
streamlit run iris-ml-app.py
```

Streamlit will open the app in your browser, usually at http://localhost:8501.

## Project structure

```
iris-flower-prediction/
├── iris-ml-app.py   # Streamlit app: UI, model training and prediction
└── README.md
```

## Notes

- The model is retrained each time the app reruns, which happens on every slider change. That takes very little time for a dataset this small. For larger models, cache the trained model with `@st.cache_resource`.
- No random seed is set, so the predicted probabilities can vary slightly between runs.

## Acknowledgements

- Iris dataset: R. A. Fisher (1936), available through scikit-learn.
- Built with Streamlit and scikit-learn.
