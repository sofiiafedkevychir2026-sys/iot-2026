class Pool:

    def __init__(self, address= "вул.Центральна, 31", volume=70000, max_visitors = 70, working_hours = "08:00 - 19:00", price = 150):
        self.__address = address
        self.__volume = volume
        self.__max_visitors = max_visitors

        self.working_hours = working_hours
        self.price = price

    def __del__(self):
        print(f"Басейн за адресою '{self.__address}' видалено з пам'яті.")


    def get_address(self):
        return self.__address

    def get_volume(self):
        return self.__volume

    def get_max_visitors(self):
        return self.__max_visitors



    def __str__(self):
        return (f"\nАдреса: {self.__address}, "
                f"\nОб'єм води: {self.__volume} л, "
                f"\nМакс. відвідувачів: {self.__max_visitors}, "
                f"\nРобочі години: {self.working_hours}, "
                f"\nЦіна: {self.price} грн"
                f"\n \n")


    def __repr__(self):
        return (f"SwimmingPool('{self.__address}', {self.__volume}, {self.__max_visitors}, "
                f"'{self.working_hours}', {self.price})")


def main():

    pool1 = Pool()
    pool2 = Pool("вул.Вулиця, 1", 50000, 48)
    pool3 = Pool("вул.Під Голоском, 24", 60000, 55, "7:00 - 20:00", 200)


    print(f"Басейн 1: {pool1}"
          f"Басейн 2: {pool2}"
          f"Басейн 3: {pool3}")


if __name__ == "__main__":
    main()


