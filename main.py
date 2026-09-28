import dieting
import workout_plan
import achievement 
import history
import datetime

def display_menu():
    print("\n" + "="*30)
    print(" FITNESS & CALORIE TRACKER ")
    print("="*30)
    print("1. Log your Meal.")
    print("2. Log your Workout.")
    print("3. Your Daily Dashboard.")
    print("4. Set Target Achievements.")
    print("5. View Your Progress.")
    print("6. Save Day in History.")
    print("7. View History.")
    print("8. Exit.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            dieting.log_meal()
            
        elif choice == '2':
            workout_plan.log_workout()
            
        elif choice == '3':
            print("\n=== Daily Dashboard ===")
            dieting.view_nutrition_summary()
            burned = workout_plan.get_total_calories_out()
            print(f"Calories Burned: {burned}")
            
        elif choice == '4':
            achievement.set_goals()
            
        elif choice == '5':
            current_cals = dieting.get_total_calories_in()
            achievement.check_progress(current_cals)
            
        elif choice == '6':
            date_today = str(datetime.date.today())
            cals_in = dieting.get_total_calories_in()
            cals_out = workout_plan.get_total_calories_out()
            history.save_summary(date_today, cals_in, cals_out)
            
        elif choice == '7':
            history.view_history()
            
        elif choice == '8':
            print("Exiting Tracker. Have a healthy day!")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()