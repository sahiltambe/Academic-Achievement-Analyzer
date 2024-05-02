# Academic Achievement Analyzer - Sahil Tambe

The Academic Achievement Analyzer is a project designed to analyze and track academic performance metrics for students.

## Overview

The Academic Achievement Analyzer provides insights into student performance based on various parameters such as grades, attendance, participation, and more. It aims to help educators, administrators, and parents gain a deeper understanding of student progress and identify areas for improvement.

## Features

- **Performance Metrics**: Analyze grades, attendance records, and participation levels.
- **Visualization**: Visualize student performance data through charts and graphs for better comprehension.
- **Trend Analysis**: Identify trends and patterns in student academic performance over time.
- **Customization**: Customize parameters and filters to tailor analysis based on specific needs.
- **Alerts**: Receive alerts for noteworthy changes or anomalies in student performance.

## Usage

1. **Data Collection**: Gather student performance data from various sources such as gradebooks, attendance records, and assessment results.
2. **Data Processing**: Clean and preprocess the data to ensure accuracy and consistency.
3. **Analysis**: Utilize the Academic Achievement Analyzer to analyze and interpret student performance metrics.
4. **Actionable Insights**: Use the insights gained to implement targeted interventions and support strategies for students.

## Getting Started
To run the Academic Achievement Analyzer locally:
1. **Clone the Repository**: Clone this GitHub repository to your local machine.

2. **Install Dependencies**: Install the required dependencies for the demo by running the appropriate package manager command (e.g., `npm install`, `pip install -r requirements.txt`).
3. **Run the Flask application using the provided command**
3. **Access the application through your web browser**

## Dependencies

- **Python 3.x**
- **Flask**
- **Pandas**
- **Scikit-learn**
- **Other necessary libraries (specified in requirements.txt)**



# Project Documentation
## AWS Deployment Link :

**AWS Elastic Beanstalk link** : [http://academicachievementanalyzersahiltambe-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/](http://academicachievementanalyzersahiltambe-env.eba-7zp3wapg.ap-south-1.elasticbeanstalk.com/)

# Screenshot of UI

![HomepageUI](./Screenshots/1.jpg)
![ResultPage](./Screenshots/ProjectUI.jpg)

# Approach for the project 

1. **Data Ingestion** : 
    * In Data Ingestion phase the data is first read as csv/fetch from the database(MySQL).
    * Then the data is split into training and testing and saved as csv file.

2. **Data Transformation** : 
    * In this phase a ColumnTransformer Pipeline is created.
    * for Numeric Variables first SimpleImputer is applied with strategy median , then Standard Scaling is performed on numeric data.
    * for Categorical Variables SimpleImputer is applied with most frequent strategy, then ordinal encoding performed , after this data is scaled with Standard Scaler.
    * This preprocessor is saved as pickle file.

3. **Model Training** : 
    * In this phase base model is tested . The best model found was Linear regressor.
    * After this hyperparameter tuning is performed on Linear Regression.
    * This model is saved as pickle file.

4. **Prediction Pipeline** : 
    * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python.

5. **Flask App creation** : 
    * Flask app is created with User Interface to predict the gemstone prices inside a Web Application.


## Contributors & Contributing
**Sahil Tambe**
Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.


## Contact

For questions or inquiries about the project, feel free to contact the project maintainers at [sahiltambe1996@gmail.com](mailto:sahiltambe1996@gmail.com).