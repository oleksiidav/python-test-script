# Databricks notebook source

# COMMAND ----------
import pyspark.sql.functions as f

df = spark.createDataFrame([
    (1,2)
], ['test_1', 'test_2'])
