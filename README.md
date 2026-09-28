# Fitness-and-Calorie-Tracker-Project

Fitness and Calorie Tracker Project for VITyarthi:

This modular Python Command Line Interface (CLI) program enables users to successfully maintain their health goals. By enabling the user to track nutritional data, exercise, calorie deficits/surpluses, weight loss targets, and the continuity of historical fitness data in CSV format.

Created by: Ishan Tripathi

Registration Number: 26BCY10146

Overview of the Project

Fitness and Calorie Tracker is an intuitive command-line tool for everyday health and fitness tracking. It combines meal logging with exercise logs to provide a target-driven nutrition, macro, and calorie computation with real time feedback on current progress, along with storing historical summaries for long-term tracking. We use Python libraries and a modular design, which isolates business logic for diet tracking, workout logging, target goals, and database handling to keep a persistent history into different Python modules.

Features

* Meal and Nutrition Tracking (dieting.py):

* Enables food entry with the macro specific values: Calories, Protein (grams), Carbohydrates (grams) and Fats (grams).

* Provides calorie amount and macro summaries for that day.

* Workout Logging (workout_plan.py):

* Monitors actual (timed) workout sessions by activity, total time (minutes) and medium or high intensity.

* Automatically calculates how many calories you've burned according to your intensity multipliers.

* Daily Dashboard (main.py):

* Provides a summarized view of total calories consumed, macro ratios, and total calories burned.

* Goal and Target Management (achievement.py):

* Allows customisability of daily calorie intake target and target weight goals (kg).

* Provides sprint checks to display percentage, remaining calories, and limit warnings.

* Persistent Historical Logging (history.py):

* Exports and appends the following fitness data to a local file (fitness_history.csv): date, calories in, calories out.

* Enables view stored historical progression entirely from command-line interface.

Technologies / Tools Used

* Programming Language: Python 3.x

* Standard Libraries:

* csv (data storage or for input/output to a file)

* datetime (for fetching system date timestamps)

• Version Control and Repository: Git / GitHub

How to Run the project after clonging Now when you get the whole project in local you have to run the project by executing the script. Steps to run the project: 1. Install the requirements 2. 

Run The script to run the project 3. 

Data Preparation is done then all the reports.

# Prerequisites

Please ensure that Python is installed in your environment (Python version 3.6 or above).

# Installation and Execution

1. Clone the Repository:

``bash

git clone https://github.com/Ishan-Tripathii/Calorie-Tracker-Proejct

cd Calorie-Tracker-Proejct

`

2. Verify Project Structure:

Save all.py files to the working directory:

`

main.py

dieting.py

workout_plan.py

achievement.py

history.py

`

3. Run the Application:

Execute the entry point file:

`bash

python main.py

``

Instructions for Testing

The following sequence must be used to test and verify all the features of the application once main.py has been run:

1. Option 4: Set Target Goals

* Input 2000 as the goal and 70.0 as the weight. Confirm the success message.

2. Option 1: Log a Meal

* Provide food name Oatmeal and specify number of calories (300), number of protein (10g), the amount of carbs (50 g), and fats (5 g).

3. Option 2: Log a Workout

* Put exercise (Running). Time (30 minutes). Put the intensity of exercise (high). Check the number of kcal burnt (360 kcal).

4. Option 3: View Daily Dashboard

*Ensure that the calories entered and the calories burned are correct.

5. Option 5: View Goal Progress

• Review current progress % and remaining allowable calories.

6. Option 6: Save Day to History Log

* Save session. Make sure that fitness_history.csv has been refreshed in your folder location.

7. Option 7: View History Log

* Check the date of today, and the stored values are read properly from the CSV file.
8. Option 8: Exit

* Confirm program exit.
