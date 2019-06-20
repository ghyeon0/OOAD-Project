from Food import Food
import csv


class FoodManagement:
    def __init__(self):
        self.foods = []
        self.get_food_data()

    def get_food_data(self):
        food_file = open("./data/foods.csv")
        food_reader = csv.reader(food_file)

        for food in list(food_reader)[1:]:
            self.foods.append(Food(food[0], food[1], int(food[2])))

        food_file.close()

    def add_new_food(self, name, type, charge):
        self.foods.append(Food(name, type, charge))

    def remove_food(self, name):
        for food in self.foods:
            if food.get_name() == name:
                self.foods.remove(food)
                break

    def get_foods(self):
        return self.foods

    def shutdown(self):
        food_file = open("./data/foods.csv", "w", newline='')
        food_writer = csv.writer(food_file)
        food_writer.writerow(["name", "type", "charge"])
        for food in self.foods:
            food_writer.writerow([food.get_name(), food.get_type(), str(food.get_charge())])

        food_file.close()

