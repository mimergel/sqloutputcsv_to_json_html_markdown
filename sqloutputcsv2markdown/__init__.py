import csv
import json
import logging
import pandas as pd

import azure.functions as func

from io import StringIO

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Get the CSV data from the request body
        csv_data = req.get_body().decode()

        # Check if the request wants JSON, HTML, or Markdown response
        response_type = req.params.get('response_type')

        # Convert the CSV data into a pandas DataFrame
        df = pd.read_csv(StringIO(csv_data))
        df = df.applymap(str)  # Convert all values to strings

        # Convert the DataFrame into the desired format
        if response_type == 'html':
            # Convert the DataFrame into an HTML table
            output_data = df.to_html(index=False)
            mimetype = 'text/html'
        elif response_type == 'markdown':
            # Convert the DataFrame into a markdown table
            output_data = df.to_markdown(index=False)
            mimetype = 'text/markdown'
        else:
            # Convert the CSV data into JSON
            output_data = df.to_json(orient='records')
            mimetype = 'application/json'

        # Return the output data
        return func.HttpResponse(output_data, status_code=200, mimetype=mimetype)
    except Exception as e:
        return func.HttpResponse(
            "An error occurred: %s" % str(e),
            status_code=500
        )

