import gradio as gr
import requests

def get_joke():
    url = "https://matchilling-chuck-norris-jokes-v1.p.rapidapi.com/jokes/random"

    headers = {
        "accept": "application/json",
        "X-RapidAPI-Key": "046a6483a3msh2a10c939f1c426ep1f953bjsn29b967f0e645",
        "X-RapidAPI-Host": "matchilling-chuck-norris-jokes-v1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()['value']

iface = gr.Interface(fn=get_joke, 
                     inputs=None, 
                     outputs="text",
                     title="Get Chuck Norris Jokes",
                     description="Click the button to get a random Chuck Norris joke!")

iface.launch()