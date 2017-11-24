#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import csv
from io import StringIO
from functools import reduce
from operator import add
from httplib2 import Http
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from apiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
CLIENT_SECRETS_PATH = './config/client_secrets.json'
VIEW_ID = '130571540'
DIMENSIONS = ['ga:userBucket', 'ga:pageTitle']
METRICS = ['ga:pageViews']
ORDER_BYS = ['ga:userBucket']


def initialize_analyticsreporting():
    """Initializes the analyticsreporting service object.

    Returns:
      analytics an authorized analyticsreporting service object.
    """
    # Parse command-line arguments.
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[tools.argparser])
    flags = parser.parse_args([])

    # Set up a Flow object to be used if we need to authenticate.
    flow = client.flow_from_clientsecrets(
        CLIENT_SECRETS_PATH, scope=SCOPES,
        message=tools.message_if_missing(CLIENT_SECRETS_PATH))

    # Prepare credentials, and authorize HTTP object with them.
    # If the credentials don't exist or are invalid run through the native client
    # flow. The Storage object will ensure that if successful the good
    # credentials will get written back to a file.
    storage = file.Storage('./config/analyticsreporting.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(flow, storage, flags)
    http = credentials.authorize(http=Http())

    # Build the service object.
    analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)

    return analytics

def get_report(analytics, page_token=None):
    # Use the Analytics Service Object to query the Analytics Reporting API V4.
    body = {
        'reportRequests': [
            {
                'viewId': VIEW_ID,
                'dateRanges': [{'startDate': '31daysAgo', 'endDate': 'today'}],
                'dimensions': [{'name': d} for d in DIMENSIONS],
                'metrics': [{'expression': m} for m in METRICS],
                'orderBys': [{'fieldName': f} for f in ORDER_BYS],
                'pageToken': page_token
            }
        ]
    }

    return analytics.reports().batchGet(body=body).execute()

def get_reports(analytics):
    page_token = None
    while page_token != -1:
        response = get_report(analytics, page_token)
        report = response['reports'][0]
        page_token = report.get('nextPageToken', -1)
        yield report

def convert(report):
    """Convert Google Analytics Report to 2D Array

    Returns:
      M 2D Array
    """
    M = []
    for row in report['data']['rows']:
        dimensions = row['dimensions']
        metrics = row['metrics'][0]['values']
        M.append(dimensions + metrics)
    return M

def main():
    analytics = initialize_analyticsreporting()
    M = [*reduce(add, [convert(report) for report in get_reports(analytics)])]

    csv_io = StringIO(newline='')
    w = csv.writer(csv_io, quoting=csv.QUOTE_ALL)
    w.writerow(DIMENSIONS + METRICS)
    for row in M:
        w.writerow(row)

    print(csv_io.getvalue())


if __name__ == '__main__':
  main()
