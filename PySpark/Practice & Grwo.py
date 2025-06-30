from pyspark.sql.functions import *

employees_df.withColumn('bonus',when(col('salary') >= 55000, col('salary') + 1000).otherwise(col('salary'))).withColumn('new_b',when(col('salary') <=52000 , lit('No_Bonus')).otherwise(col('salary'))).show()

#Same

from pyspark.sql.functions import col, lit, when

employees_df.withColumn(
    'bonus_status',
    when(col('salary') >= 55000, col('salary') + 1000)
    .when(col('salary') <= 52000, lit('No_Bonus'))
    .otherwise(col('salary'))
).show()

