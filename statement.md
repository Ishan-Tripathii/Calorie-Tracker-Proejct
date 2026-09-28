Problem Statement

With our busy lifestyles, it can be daunting to keep a healthy lifestyle if you don't keep track of what you eat and how much activity you get each day. It can be a challenge finding an app that is relatively simple, does not require much configuration or the internet. It can be difficult to find a simple and flexible app that allows you to track your calorie intake, track your fitness measurements, set weight loss goals, and save your progress over time without any bells and whistles.

Scope of the Project

The goal of this project is to create a CLI Fitness and calorie tracker using Python.

- In-Scope:

The system will log every meal entered, including all nutritional values (calories, proteins, carbs, fats). It will track each workout entered (type, duration and intensity) and automatically compute the number of calories used. It will give a comprehensive summary of everything logged. 

Users will be able to set weight and health goals. 

The system will track and store local history of fitness summaries via CSV files.

- Out-of-Scope:

There will not be a graphical user interface (GUI), and a web or mobile application will not be part of the scope. There will not be any integration with fitness gadgets like smart watches. There will not be support for multiple online users nor a use of database.

Target Users

- Fitness Novices: The right tool for someone looking for a text-based method to track caloric intake and calories burned over the course of a day.

- Students & Developers: Python learners or those who want to participate in small projects. The system is neatly organized script that uses file input/output, dictionaries, and loops, and imports.

- CLI fans: Users who dislike software that has a graphical user interface and prefer terminal commands.

High-Level Features

23. Modular design: The 5 modules (diet.py, workout.py, goals.py, history_logger.py, and main.py) will be separated into separate files to make sure each one has a specific role.

2. Full Meal Logging: For each day, the system will log every meal and sum up the number of calories, protein, carbohydrates, and fats.

3. Workout Power Calculation: It will compute the calories burned, using your time and intensity of workout (low, medium, high).

4. Tracking Progress to Your Goals: A comparison of calorie intake versus goals will be shown, and users will be notified if their intake exceeds their predetermined goals.

5. History Logs: Summaries will be saved with the date in a CSV file (fitness_history.csv) so users can keep track of progress.
