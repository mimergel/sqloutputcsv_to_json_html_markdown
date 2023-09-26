# Convert CSV to JSON, HTML or MARKDOWN Table
This is a Python script to use in an Azure Function.
It will converts CSV input to JSON, HTML or MARKDOWN table output. 

# Install dependencies
Before you can get started, you should install Node.js which includes npm. This is how you will obtain the Azure Functions Core Tools. If you prefer not to install Node.js, see the other installation options in our Core Tools reference.
Run the following command to install the Core Tools package:

`npm install -g azure-functions-core-tools@4 --unsafe-perm true`

# Create an Azure Functions project
In the terminal window or from a command prompt, navigate to a new empty folder [your_function_name] for your project, and run the following command:

`func init`

You will also be prompted to choose a runtime for the project. Select .
Create a function
To create a function, run the following command:

`func new`

This will prompt you to choose a template for your function. We recommend HTTP trigger for getting started.

# Download this repo into the current folder
`git clone https://github.com/mimergel/sqloutputcsv_to_json_html_markdown.git`

# Run your function project locally
Run the following command to start your function app:

`func start`

The runtime will output a URL for any HTTP functions, which can be copied and run in your browser's address bar.
To stop debugging, use Ctrl-C in the terminal.

# Test the function
In a separate terminal run the following. Use your_function_name.

```
csv_data='CARRNAME,ECONOMY_OCCUPATION,BUSINESS_OCCUPATION,FIRST_OCCUPATION
"Alitalia",822,75,47
"American Airlines",694,59,40
"Singapore Airlines",976,69,49
"Lufthansa",5586,450,318
"Qantas Airways",315,27,20
"United Airlines",1861,136,86'

echo "$csv_data" | curl -X POST http://localhost:7071/api/[your_function_name]?response_type=markdown -H "Content-Type: text/csv" --data-binary @-
```



# Deploy your code to Azure
To publish your Functions project into Azure, enter the following command:

`func azure functionapp publish [your_function_name]`

You may be prompted to sign into Azure. Follow the onscreen instructions.