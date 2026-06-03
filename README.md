# NutriScan: Offline Scanner
# Application Description 

NutriScan: Offline Scanner is a Python application designed to help users track daily food intake and monitor nutritional values in one system. It provides details on calories, protein, carbohydrates, and fat, with features like meal logging, food database, BMI calculator, and camera scanner.

The application allows users to:
- View a food database containing common food items and their nutritional values.
- Analyze food to display calories, protein, carbohydrates, and fat content.
- Log meals to keep track of daily food consumption.
- View meal history for better eating pattern awareness.
- Calculate BMI (Body Mass Index) based on height and weight input • Use a camera scanner module for food input simulation.
- Save meal records into a file for future reference.

## OOP Concepts Used
This project demonstrate core Object-Oriented Programming(OOP) concepts.

- Class: The User class is used to define the structure and behavior of a user within the NutriScan system.
-	Object: A user object is created from the User class to store and manage user information and meal records.
-	Attributes: The User class contains attributes such as name, age, goal, and meal_log to store user data.
-	Methods: The log_meal() and show_meals() methods perform actions related to meal management and user interaction.
-	Encapsulation: User data and related functionalities are grouped within the User class, improving code organization and maintainability.
-	Modularity: The application is divided into separate components such as Food Analysis, BMI Calculator, Meal Storage, Food Database, and Camera Scanner, making the system easier to develop, maintain, and expand.

# Technologies Used
-	Python ( main programming language)
-	OpenCV (camera scanner feature )
-	JSON (data storage format)
-	File Handling ( saving and exporting data)


## Project Structure

```text
Nutriscan/
│
├── data
│   └── food.py
│
├── interfaces
│   └── nutrition_service.py
│
├── models
│   ├── meal.py
│   └── user.py
│
├── services
│   ├── bmi_service.py
│   ├── camera_service.py
│   ├── meal_service.py
│   ├── nutrition_service_impl.py
│   └── storage_service.py
│
├── tests
│   └── test_nutriscan.py
│
├── ui
│   └── main_menu.py
│
├── main.py
├── meal_log.json
└── README.md
```
# How to Run
1.	Requirements Python 3.x
2.	Clone this repository:
 ``` bash  
  git clone https://github.com/nerielannegonzales-gif/Nutriscan
 ``` 

# Navigate to the project folder:
``` bash
cd NutriScan
 ``` 

# Run the Application:
``` bash
python main.py
```


# Running Tests
``` bash
pytest tests
```


# Author 


Developed as a school project by:

•	Neriel Ann Gonzales(GitHub Profile of Gonzales)
(https://github.com/nerielannegonzales-gif)

•	Cathilyn Escullar (GitHub Profile of Escullar)
(https://github.com/cathilynescullar-cmyk)

•	Angel G. Listana (GitHub Profile of Listana)
(https://https://github.com/angellistana617-sudo)

In Partial Fulfillment of the Requirements for the Subject CC103 Computer Programming 2 under the Course of Bachelor of Science in Information Technology at Sorsogon State University - Bulan Campus. With the supervision of our Professor John Mark Gabrentina.
