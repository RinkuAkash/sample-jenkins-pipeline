import unittest
import pyspark
from main import create_data, filter_experience, avg_salary


class TestMainMethods(unittest.TestCase):

    def __init_(self):
        self.spark = pyspark.sql.SparkSession.builder.appName("testcases").getOrCreate()
        self.employees_data = create_data(self.spark)

    def test_filter_experience(self):
        self.assertEqual(3, avg_salary(self.employees_data))

    def test_avg_salary(self):
        selft.asserttEqual(2, avg_salary(self.employees_data).count())


if __name__ == "__main__":
    unittest.main()
