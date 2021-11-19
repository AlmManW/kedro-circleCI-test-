import findspark
findspark.init()

from pyspark.sql.functions import lpad, collect_set, collect_list, year, month, dayofmonth, concat_ws, when, concat, count, max, lit, countDistinct, size, split, lower, col, substring, length, udf, format_string, date_format, to_utc_timestamp
import pyspark.sql.functions as f
from pyspark.sql.types import StringType, FloatType, ArrayType, IntegerType, DoubleType
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import HiveContext
import pyspark
 
spark = SparkSession.builder.config("spark.driver.memory", "6g").config("spark.hadoop.fs.s3a.access.key", "AKIAZUZ7CBT7A6MQZ6XD").config("spark.hadoop.fs.s3a.secret.key", "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").getOrCreate()
    #.config("spark.hadoop.fs.s3a.access.key", "some-value") \
    #.config("spark.hadoop.fs.s3a.secret.key", "some-value") \
    #.config("spark.hadoop.fs.s3a.endpoint", "s3.us-east-2.amazonaws.com") \
    #.config("spark.driver.memory", "8g") \
    #.config("spark.executor.memory", "8g") \
    #

def load_csv_data(sparkDF: pyspark.sql.dataframe.DataFrame) -> pyspark.sql.dataframe.DataFrame:
    """Preprocesses the data for companies.

    Args:
        companies: Raw data.
    Returns:
        Preprocessed data, with `company_rating` converted to a float and
        `iata_approved` converted to boolean.
    """
    print(type(sparkDF))
    sparkDF.show()
    sparkDF.printSchema()
    return sparkDF


