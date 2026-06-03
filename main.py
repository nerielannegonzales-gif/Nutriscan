from models.user import User
from services.nutrition_service_impl import NutritionServiceImpl
from services.bmi_service import BMIService
from services.storage_service import StorageService
from ui.main_menu import MainMenu

nutrition = NutritionServiceImpl()
bmi = BMIService()
storage = StorageService()
menu = MainMenu()

print("=" * 40)
print("NUTRISCAN")
print("Offline Food Scanner Application")
print("=" * 40)

name = input("Enter your name: ")
age = input("Enter your age: ")
goal = input("Enter your health goal: ")

user = User(name, age, goal)

while True:
    menu.show()

    choice = input("Choice: ")

    if choice == "1":
        nutrition.display_foods()

    elif choice == "2":
        food = input("Food name: ")
        nutrition.analyze_food(food)

    elif choice == "3":
        food = input("Food to log: ")
        user.log_meal(food)
        print("Meal logged.")

    elif choice == "4":
        user.show_meals()

    elif choice == "5":
        bmi.calculate_bmi()

    elif choice == "6":
        storage.save_meals(user)

    elif choice == "7":
        print("Camera scanner coming soon.")

    elif choice == "8":
        print("Thank you for using NutriScan!")
        break

    else:
        print("Invalid choice.")
