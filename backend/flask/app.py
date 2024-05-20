from flask import Flask, request, jsonify
# from pyspark.sql import SparkSession

app = Flask(__name__)

# # Initialize SparkSession
# spark = (SparkSession.builder
#          .appName('pyspark-app')
#          .master('local[*]')
#          .getOrCreate())


# @app.route(rule='/spark-job', methods=['POST'])
# def run_spark_job():
#
#     # Read the JSON file into a DataFrame
#     df = spark.read.json("students.json")
#
#     # Show the contents of the DataFrame
#     print(df.show())
#
#     # Print the schema of the DataFrame
#     print(df.printSchema())
#
#     # Perform some transformations or actions
#     df_result = df.groupBy("gender").count()
#
#     # Collect the results
#     print(df_result.collect())


@app.route('/')
def home():
    return "Hello Flask and Docker!"


@app.route('/cache-me')
def cache():
    return "nginx will cache this response"


@app.route('/info')
def info():
    resp = {
        'connecting_ip': request.headers['X-Real-IP'],
        'proxy_ip': request.headers['X-Forwarded-For'],
        'host': request.headers['Host'],
        'user-agent': request.headers['User-Agent']
    }

    return jsonify(resp)


@app.route('/flask-health-check')
def flask_health_check():
    return "success"
