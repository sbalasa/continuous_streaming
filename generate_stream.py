#!/usr/bin/env python3
"""
Main runner to Stream Continous Data.

Author: Santhosh Balasa
Email: santhosh.kbr@gmail.com
Date: 26/May/2021
"""

import time
import click
import sched
import feedparser


from pprint import pprint


# Global
STREAM_URL = "http://feedparser.org/docs/examples/atom10.xml"


def generate_random_data(interval, scheduler):
    """
    Function to generate the random data.

    Args:
        interval (int): Time interval to stream the data
        scheduler (sched.scheduler): scheduler object
    """
    pprint(feedparser.parse(STREAM_URL))
    scheduler.enter(60 * interval, 1, generate_random_data, (interval, scheduler))


@click.command()
@click.option(
    "--interval",
    required=True,
    help="Pass the time interval in minutes to stream the data",
)
def main(interval):
    """
    CST: Continous Streaming Tool
        This tool is live stream data continously based on the time interval.
    Args:
        interval (str): Time interval to generate the stream.
    """
    interval = int(interval)
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(60 * interval, 1, generate_random_data, (interval, scheduler))
    scheduler.run()


if __name__ == "__main__":
    main()
