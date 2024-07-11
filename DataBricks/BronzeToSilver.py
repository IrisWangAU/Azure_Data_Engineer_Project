# Databricks notebook source
# MAGIC %md
# MAGIC ## Convert Date Format to YYYY-MM-DD for all tables

# COMMAND ----------

table_name = []

for i in dbutils.fs.ls('mnt/bronze/SalesLT/'):
  table_name.append(i.name.split('/')[0])

table_name

# COMMAND ----------

# import pacakges for time format
from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

# loop to change the format for each table
for each_table in table_name:
  path = '/mnt/bronze/SalesLT/' + each_table + '/' + each_table + '.parquet'
  df = spark.read.format('parquet').load(path)
  column = df.columns

  for col in column:
    if "Date" in col or "date" in col:
      df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))
  # save the modified tables as delta format in silver container    
  output_path = '/mnt/silver/SalesLT/' + each_table +'/'
  df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

# display the last df in the loop transformation
display(df)
