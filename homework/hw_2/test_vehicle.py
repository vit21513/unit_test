import unittest
from vehicle import Vehicle, Car, Motorcycle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        self.mycar = Car("Lada", "Calina", 2011)
        self.moto = Motorcycle("Honda", "CX1", 2017)

    # Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя оператор instanceof).
    def test_class_instanceof(self):
        self.assertIsInstance(self.mycar, cls=Vehicle, msg="классы разные")

    # Проверить, что объект Car создается с 4-мя колесами.
    def test_quantity_wheels_car(self):
        self.assertEqual(self.mycar.get_numwheels, 4)

    # Проверить, что объект Motorcycle создается с 2-мя колесами.
    def test_quantity_wheels_moto(self):
        self.assertEqual(self.moto.get_numwheels, 2)

    # Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
    def test_speed_test_car(self):
        self.mycar.testDrive()
        self.assertEqual(self.mycar.get_speed, 60)

    # Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
    def test_speed_test_moto(self):
        self.moto.testDrive()
        self.assertEqual(self.moto.get_speed, 75)

    # Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) машина останавливается (speed = 0).
    def test_parking_car(self):
        self.mycar.testDrive()
        self.mycar.park()
        self.assertEqual(self.mycar.get_speed, 0)

        # Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта) мотоцикл останавливается (speed = 0).

    def test_parking_moto(self):
        self.moto.testDrive()
        self.moto.park()
        self.assertEqual(self.moto.get_speed, 0)
