# Databricks notebook source
# MAGIC %md
# MAGIC ## Change the column names from CamelCase to snake_case for all tables

# COMMAND ----------

# load packages for name convention change
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace

# COMMAND ----------

# get all the table names
table_name = []

for i in dbutils.fs.ls('mnt/silver/SalesLT/'):
  table_name.append(i.name.split('/')[0])

# COMMAND ----------

# loop to change the column names in each table
for each_table in table_name:
    path = '/mnt/silver/SalesLT/' + each_table
    df = spark.read.format('delta').load(path)

    # Get the list of column names
    column_names = df.columns

    for old_col_name in column_names:
        # Convert column name from ColumnName to Column_Name format
        new_col_name = "".join(["_" + char if char.isupper() and not old_col_name[i - 1].isupper() else char for i, char in enumerate(old_col_name)]).lstrip("_")
      
        # Change the column name using withColumnRenamed and regexp_replace
        df = df.withColumnRenamed(old_col_name, new_col_name.lower())

    output_path = '/mnt/gold/SalesLT/' + each_table +'/'
    df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

# show the last table in the loop transformation
display(df)
