import random


def get_1d20_dice_roll() -> int:
    roll = random.randint(1, 20)
    return roll


class TavernCalculator:
    """
    Calculates the chance of selling a specialty ale at the player-owned tavern
    r = 1d20 - DC
    *r >= DC
    c = cost - base ale price
    *c >= base ale price

    r + (100 - (10 * c)) = chance of success

    Example:
    DC = 10
    r = 9
    cost = 12
    base ale price = 6
    c = 6
    9 + (100 - (10 * 6)) = 49% chance of success
    """
    dc = 10
    base_ale_price = 6  # cp

    def get_chance_of_success(self):
        cost = self.get_specialty_ale_cost()
        dc_roll = get_1d20_dice_roll()
        if self.is_dc_check_successful(dc_roll):
            return self.get_total_success_rate(cost, dc_roll)
        else:
            print(f"Failed DC check with a roll of {dc_roll}")
            return 0

    def is_dc_check_successful(self, roll: int) -> bool:
        if roll < self.dc:
            return False
        return True

    def get_specialty_ale_cost(self) -> int:
        try:
            cost = int(input("What is the cost of the specialty ale? "))
        except ValueError:
            print("Please enter a valid number.")
            return self.get_specialty_ale_cost()

        return cost

    def get_total_success_rate(self, cost: int, dc_roll: int):
        base_success_percent = self.get_base_success_percent(cost)
        print(f"DC roll was a {dc_roll}")
        return base_success_percent + (dc_roll - self.dc)

    def get_base_success_percent(self, cost: int) -> int:
        base_percentage = 10 * (cost - self.base_ale_price)
        return 100 - base_percentage

    # def get_success_bonus(self, roll: int, cost: int) -> int:
    #     bonus = (roll - self.dc) + (cost - self.base_ale_price)
    #     return bonus


if __name__ == '__main__':
    def play():
        tavern_calculator = TavernCalculator()
        chance_of_success = tavern_calculator.get_chance_of_success()
        print(f"The chance of someone buying a specialty ale is {chance_of_success}%.")
        choice = input("Calculate again? (yes/no) ")
        if choice[0] == 'y':
            play()

    play()
