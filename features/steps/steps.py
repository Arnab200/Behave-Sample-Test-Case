from behave import *
import os
import requests
import time

answer = []

@given('The flask server is running')
def step_impl(context):
    """ Running the python file restAPI.py"""
    # os.system('python3.6 /home/arnab/PythonProjects/restAPI/restAPI.py')
    print('Server up and running')

@when('I send a post request to the server url')
def step_impl(context):
    """prepare a post request to send it to the server url for getting out the output"""
    url = 'http://localhost:5000/messagereader'
    data = "name"
    response = requests.post(url=url, data=data)
    answer.append(response)
    print('Sent name request to the server')

@then('I should get back my name back in the response')
def step_impl(context):
    print(answer)
