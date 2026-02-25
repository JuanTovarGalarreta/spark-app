import streamlit as st
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

st.title("My PySpark App")

data = [("Alice", 25), ("Bob", 30)]
df = spark.createDataFrame(data, ["Name", "Age"])

st.write("Spark DataFrame:")
st.dataframe(df.toPandas())
