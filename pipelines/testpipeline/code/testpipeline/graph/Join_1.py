from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from testpipeline.config.ConfigStore import *
from testpipeline.functions import *

def Join_1(spark: SparkSession, in0: DataFrame, in1: DataFrame, *inDFs: DataFrame) -> DataFrame:
    pass
