# House Price Prediction System for Indian Metropolitan Cities

This repository hosts the code for a House Price Prediction system tailored for Indian metropolitan cities. The system utilizes various Machine Learning algorithms to predict house prices based on several key features.

## Algorithms Used
- **XGBoost**: A powerful gradient boosting algorithm known for its efficiency and effectiveness in regression tasks.
- **Linear Regression**: A fundamental regression technique used to model the relationship between dependent and independent variables.
- **GradientBoosterRegressor**: Another gradient boosting algorithm that combines the principles of gradient boosting with regression.


## Requirements

```text
asgiref==3.8.1
asttokens==2.4.1
beautifulsoup4==4.12.3
colorama==0.4.6
comm==0.2.2
debugpy==1.8.1
decorator==5.1.1
Django==5.0.6
django-bootstrap4==24.3
django-cors-headers==4.4.0
django-widget-tweaks==1.5.0
djangorestframework==3.15.2
executing==2.0.1
ipykernel==6.29.4
ipython==8.25.0
jedi==0.19.1
joblib==1.4.2
jupyter_client==8.6.2
jupyter_core==5.7.2
lightgbm==4.4.0
matplotlib-inline==0.1.7
nest-asyncio==1.6.0
numpy==2.0.0
packaging==24.1
pandas==2.2.2
parso==0.8.4
platformdirs==4.2.2
prompt_toolkit==3.0.47
psutil==6.0.0
pure-eval==0.2.2
Pygments==2.18.0
python-dateutil==2.9.0.post0
pytz==2024.1
pywin32==306
pyzmq==26.0.3
scikit-learn==1.5.0
scipy==1.14.0
six==1.16.0
SMTPEmail==0.4.2
soupsieve==2.5
sqlparse==0.5.0
stack-data==0.6.3
threadpoolctl==3.5.0
tornado==6.4.1
tqdm==4.66.4
traitlets==5.14.3
typing_extensions==4.12.2
tzdata==2024.1
wcwidth==0.2.13
xgboost==2.1.0
```

## Commands to run

1. Create Virtual Environment and select the Appropriate Python Interpreter
2. ```bash
   pip install -r requirements.txt
   ```
3. ```bash
   cd house_price_prediction
   ```
4.  ```bash
    Change the path of model as well as dataset to your custom absolute path in base/views.py
    ```

6. ```bash
   python manage.py makemigrations
   ```
7. ```bash
   python manage.py migrate
   ```
8. ```bash
   python manage.py runserver
   ```

