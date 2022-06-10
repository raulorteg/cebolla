from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from settings import *


def generate_summary(period: str):

    # manage usser input exception
    if period.lower() not in VALID_PROCESSING_PERIODS:
        list_valid = ",".join(VALID_PROCESSING_PERIODS)
        raise Exception(
            f"Period selected not valid, try {list_valid}. Your input: ({period})"
        )

    # load the data
    data = pd.read_csv(
        DATA_LOG,
        names=[
            "Timestamp",
            "moistures1",
            "moistures2",
            "moistures3",
            "humidity",
            "temperature",
        ],
        dtype={
            "Timestamp": str,
            "moistures1": float,
            "moistures2": float,
            "moistures3": float,
            "humidity": float,
            "temperature": float,
        },
        parse_dates=["Timestamp"],
    )

    # select the subset of measures to be processed based on the
    # period ("week", "day", ...)
    if period.lower() == "day":
        data = data[data["Timestamp"] >= (datetime.now() - timedelta(days=1))]
        title = "last 24h"

    elif period.lower() == "week":
        data = data[data["Timestamp"] >= (datetime.now() - timedelta(days=7))]
        title = "last week"

    elif period.lower() == "month":
        data = data[data["Timestamp"] >= (datetime.now() - timedelta(days=30))]
        title = "last month"

    else:
        title = "historic"

    # generate the plots
    plt.close()
    plt.plot(data["Timestamp"], data["moistures1"], alpha=0.6, color="blue", label="s1")
    plt.plot(
        data["Timestamp"], data["moistures2"], alpha=0.6, color="green", label="s2"
    )
    plt.plot(
        data["Timestamp"], data["moistures3"], alpha=0.6, color="orange", label="s3"
    )
    plt.title(f"Moisture levels for period: {title}")
    plt.xlabel("Time")
    plt.ylabel("Analog moisture level")
    plt.legend()
    plt.savefig(f"{LOGGER_DIRECTORY}/moistures.png")

    plt.close()
    plt.plot(data["Timestamp"], data["humidity"])
    plt.title(f"Air humidity for period: {title}")
    plt.xlabel("Time")
    plt.ylabel("Air humidity (%)")
    plt.savefig(f"{LOGGER_DIRECTORY}/humidity.png")

    plt.close()
    plt.plot(data["Timestamp"], data["temperature"])
    plt.title(f"Temperatures for period: {title}")
    plt.xlabel("Time")
    plt.ylabel("Temperature (C)")
    plt.savefig(f"{LOGGER_DIRECTORY}/temperature.png")


if __name__ == "__main__":
    generate_summary("all")
