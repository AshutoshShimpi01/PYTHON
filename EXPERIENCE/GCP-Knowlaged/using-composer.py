Great! Let's walk through **both** examples to give you practical knowledge on:

1. ✅ **Running a PySpark ETL Job on Dataproc**
2. ✅ **Orchestrating it with Cloud Composer (Airflow)**

---

## 💡 1. PySpark ETL Job on Dataproc

### 📂 Example Scenario

* Input: `gs://your-bucket/input/employees.csv`
* Output: Transformed data → `gs://your-bucket/output/employees_cleaned/`

### 📜 PySpark Script: `employee_etl.py`

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("EmployeeETL").getOrCreate()

# Read input CSV from Cloud Storage
df = spark.read.option("header", "true").csv("gs://your-bucket/input/employees.csv")

# Transformation: Filter out rows with null salary and cast salary to float
df_cleaned = df.filter(col("salary").isNotNull()) \
               .withColumn("salary", col("salary").cast("float"))

# Save output back to Cloud Storage in Parquet format
df_cleaned.write.mode("overwrite").parquet("gs://your-bucket/output/employees_cleaned/")

spark.stop()
```

---

### 🔧 Submit the Job to Dataproc

```bash
gcloud dataproc jobs submit pyspark gs://your-bucket/scripts/employee_etl.py \
    --cluster=my-dataproc-cluster \
    --region=us-central1
```

Make sure your PySpark file is uploaded to a GCS bucket like:

```bash
gsutil cp employee_etl.py gs://your-bucket/scripts/
```

---

## ⏰ 2. Orchestrate with Cloud Composer (Airflow)

### ✈️ Airflow DAG to Run Dataproc Job

Create a file `dataproc_etl_dag.py` and place it in Composer’s `/dags` folder.

```python
from airflow import models
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from datetime import datetime, timedelta

# DAG default arguments
default_args = {
    'start_date': datetime(2025, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Dataproc job config
PYSPARK_JOB = {
    "reference": {"project_id": "your-project-id"},
    "placement": {"cluster_name": "my-dataproc-cluster"},
    "pyspark_job": {"main_python_file_uri": "gs://your-bucket/scripts/employee_etl.py"},
}

with models.DAG(
    "employee_etl_pipeline",
    default_args=default_args,
    schedule_interval=None,  # Set your cron if needed
    catchup=False,
) as dag:

    run_etl = DataprocSubmitJobOperator(
        task_id="submit_pyspark_etl",
        job=PYSPARK_JOB,
        region="us-central1",
        project_id="your-project-id",
    )

    run_etl
```

---

## ✅ What You Need to Set Up

### GCP Requirements:

* Create a **Dataproc Cluster**
* Enable APIs: `Dataproc`, `Composer`, `Storage`, `Compute Engine`
* Create a **Cloud Composer Environment**
* Upload the **PySpark script** to GCS
* Upload the **Airflow DAG** to Composer’s `/dags` bucket

---

Would you like:

* A version of this that includes **BigQuery as the destination**?
* Steps to schedule this pipeline daily or based on triggers?
* Or help creating the GCS bucket structure?

Let me know!
