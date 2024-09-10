from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from testpipeline.config.ConfigStore import *
from testpipeline.functions import *
from prophecy.utils import *
from testpipeline.graph import *

def pipeline(spark: SparkSession) -> None:
    df_TransposeAgg_1 = TransposeAgg_1(spark)
    df_Join_1 = Join_1(spark, df_TransposeAgg_1)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("testpipeline")\
                .getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/testpipeline")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/testpipeline", config = Config)(pipeline)

if __name__ == "__main__":
    main()
