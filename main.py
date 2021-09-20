from pyspark.sql import SparkSession
from pyspark.sql import functions as F
import pyspark


def create_data(spark):

    columns = ["id", "gender",  "salary", "experience"]
    data =  [("1", "M", 52000, 14), ("2", "M", 40000, 9)
            , ("3", "F", 39000, 7), ("4", "F", 47000, 10)]

    rdd = spark.sparkContext.parallelize(data)
    return spark.createDataFrame(rdd).toDF(*columns)

def filter_experience(_df):
    return  _df.filter(F.col("experience")>=9).count()

def avg_salary(_df):
    _df = _df.groupBy("gender").avg("salary")
    _df = _df.withColumnRenamed("avg_salary", "avg(salary)")
    return _df


if __name__ == '__main__':
    spark = SparkSession.builder.appName('jenkinsPipeline').getOrCreate()
    employees_data = create_data(spark)
    print(filter_experience(employees_data))
    #print(avg_salary(employees_data).show())
