import streamlit as st


st.header('Image Classification App')
st.subheader('This model was trained using a dataset')
st.code('''

# overwrite app.py

from PIL import Image
import streamlit as st
import numpy as np
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

st.title("Fruit Identification")
st.header("Supported fruits: lemon, apple, mandarin, orange")
st.text("Upload a clear image of a fruit")

fruit_data = pd.read_csv("fruit.csv", header=None, names=["fruit_label", "mass", "width", "height", "color_score", "fruit_name"])

uploaded_file = st.file_uploader("Enter image", type=["png", "jpeg", "jpg"])

def classify_fruit(image):
    # Function to classify the fruit based on the fruit data

    # Assuming you have a method to extract features from the image
    # Here we'll just use random values for demonstration
    mass = np.random.randint(50, 500)  # Random mass between 50 and 500 grams
    color_score = np.random.uniform(0, 1)  # Random color score between 0 and 1

    # Calculate the Euclidean distance between the features of the image and each fruit in the dataset
    fruit_data['distance'] = np.sqrt((fruit_data['mass'] - mass)**2 +
                                     (fruit_data['color_score'] - color_score)**2)

    # Find the closest fruit based on the calculated distance
    closest_fruit_index = fruit_data['distance'].idxmin()
    closest_fruit = fruit_data.loc[closest_fruit_index, 'fruit_name']

    return closest_fruit

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    predicted_fruit = classify_fruit(image)

    if predicted_fruit:
        st.write(f"The uploaded fruit is {predicted_fruit}.")
    else:
        st.write("Fruit classification failed.")

    # Create features (for demonstration purpose)
    X = fruit_data[['mass', 'color_score']]
    y = fruit_data['fruit_label']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"Model accuracy: {accuracy}")

    # Save the trained model as a .sav file
    joblib.dump(model, 'fruit_classifier.sav')

    st.write("Model saved as 'fruit_classifier.sav'")
''')
