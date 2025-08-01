# Fire Classification Project

## Welcome to the Fire Classification Project! 🔥

This project is all about using smart tech to detect and classify wildfires quickly and accurately. By analyzing data, we aim to help firefighters, communities, and environmentalists tackle fires early to save forests, homes, and lives.

---

## What’s This Project About?

Wildfires are a big problem, causing damage to nature and communities. Our goal is to build a tool that spots fires early and predicts how severe they might be. We use data and machine learning to make this happen, making it easier for people to act fast and stay safe.

---

## How It Works

Here’s the step-by-step process we followed to build this project:

1. *Gathering Data*: We collected data about fires, like satellite images, weather conditions, and past fire records, to understand what causes and spreads them.
2. *Exploring the Data*: We dug into the data to spot patterns, like which areas are more likely to catch fire or what weather makes fires worse.
3. *Balancing the Data*: Some fire events were rare in our data, so we used a tool called SMOTE to make sure our model didn’t ignore them.
4. *Scaling the Data*: We adjusted the data to make it easier for our model to process, ensuring everything was on the same level.
5. *Building the Model*: We used a smart algorithm called Random Forest to classify fires (e.g., small vs. dangerous) based on the data.
6. *Checking Results*: We used a confusion matrix to see how well our model did at predicting fires correctly.

---

## What We Found

Our model worked great! The Random Forest algorithm accurately classified fires, and the confusion matrix showed it was reliable. This means it can help predict fires and guide efforts to stop them before they spread.

---

## What’s Next? (Future Scope)

We’re excited about making this project even better! Here are two big ideas for the future:

1. *Live Sensors and Smarter AI*  
   - *Plan*: Add live data from drones, satellites, and sensors, and use cooler AI (like deep learning) to spot fires faster and more accurately.  
   - *Why It’s Awesome*: This will help firefighters catch fires early, saving forests, homes, and lives by acting quickly.

2. *Easy Alert App or Website*  
   - *Plan*: Build a simple app or website to show fire risks and send real-time warnings to people.  
   - *Why It’s Awesome*: It keeps communities, leaders, and emergency teams in the know, helping them plan, stay safe, and fight fires smarter.

---

## How to Use This Project

1. *Get the Code*: Clone this repository to your computer.
2. *Install Tools*: You’ll need Python and libraries like pandas, scikit-learn, and imbalanced-learn (for SMOTE). Check requirements.txt for the full list.
3. *Run the Code*: Open the Jupyter notebook or Python script in the repo and follow the steps to process data and train the model.
4. *Check the Results*: Look at the confusion matrix and other metrics to see how the model performs.
5. *Explore the Data*: Feel free to add your own data or tweak the model to make it even better!

---

## Tools We Used

- *Python*: For coding the project.
- *Pandas & NumPy*: For handling and exploring data.
- *Scikit-learn*: For building the Random Forest model and confusion matrix.
- *SMOTE*: To balance the data.
- *Matplotlib/Seaborn*: For visualizing patterns in the data.

---

Thanks for checking out the Fire Classification Project! Let’s keep our forests and communities safe.

---

I am adding the link in the readme file since my Model - best_fire_detection_model.pkl file is **638.1 MB**. Any file larger than 25 MB is not accepted in the Github without LFS.

Link for the Model:
https://drive.google.com/file/d/1Uz2n5EUD0uOoxmXihF5CWSPqp0cIWIEJ/view?usp=sharing