# Airline Passenger Satisfaction

This project aims to analyze and visualize airline passenger satisfaction data to gain insights into factors affecting passenger experiences.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7+
- `pip` (Python package installer)

## Setup

Follow these steps to set up and run the project properly:

1. **Create a virtual environment**

   It's recommended to create a virtual environment to manage dependencies. You can create a virtual environment using the following command:

   python -m venv venv

2. **Activate a virtual environment**

- on windows : .\venv\Scripts\activate
- on mac or linux : source venv/bin/activate
3. **Install the required packages using the requirements.txt file:**
   pip install -r requirements.txt
4. **Set the "PYTHONPATH" environment variable to the project's root directory. This ensures that the modules can be imported correctly.**
- on windows : set PYTHONPATH=...(project parent paths in your local)\Airline_Passenger_Satisfaction
- on mac or linux : export PYTHONPATH=...(project parent paths in your local)/Airline_Passenger_Satisfaction

# open folder in vscode
```

Visual Studio Code setup:

```
# Install vscode extensions: Pyton (microsoft), Pylance (microsoft), Black Formatter (microsoft), isort(microsoft)

# for data visualization
python -m cli visualize -v
# for classification
python -m cli clissify --c