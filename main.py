from src import beginner_problems, future_sales_prediction

def main():
    app_dict = {1:beginner_problems.number_guessing, 2:beginner_problems.calc_mean, 3:beginner_problems.calc_median, 4:beginner_problems.calc_mode}
    while True:
        user_input = int(input('Wybierz program:\n'))
        if user_input not in app_dict.keys():
            return
        app_dict[user_input]()

if __name__ == '__main__':
    main()
