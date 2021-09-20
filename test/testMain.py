import unittest
import pyspark
from main import create_data, filter_experience, avg_salary


class TestMainMethods(unittest.TestCase):

    def setUp(self):
        self.spark = pyspark.sql.SparkSession.builder.appName("testcases").getOrCreate()
        self.employees_data = create_data(self.spark)

    def test_filter_experience(self):
        self.assertEqual(3, filter_experience(self.employees_data).select("experience").count())

    def test_avg_salary(self):
        self.assertEqual(2, avg_salary(self.employees_data).select("avg(salary)").count())


if __name__ == "__main__":
    unittest.main()
