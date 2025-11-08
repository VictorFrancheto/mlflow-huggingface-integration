from mlflow import log_metric, start_run
from random import choice

metrics_names = ["cpu", "ram", "disk"]
percentages = [i for i in range(0, 100)]

with start_run():
    for i in range(40):
        log_metric(choice(metrics_names), choice(percentages))
