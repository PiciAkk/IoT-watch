from flask import Flask, render_template, request
import requests
import json

url = "http://192.168.0.89:8080/jsonrpc"
headers = {
  'Content-Type': 'application/json'
}
app = Flask(__name__)
app.config["DEBUG"] = True

def callKodiAPI(method, params):
    payload = json.dumps({
        "id": 1,
        "jsonrpc": "2.0",
        "method": method,
        "params": params
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
def toggleLights():
    print("Toggling lights...")
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        requestForm = request.form.to_dict()
        try:
            requestForm['kodioff']
            callKodiAPI("System.Shutdown", {})
        except:
            pass
        try:
            requestForm['togglelights']
            toggleLights()
        except:
            pass
        try:
            requestForm['kodimute']
            callKodiAPI("Application.SetMute", {"mute": "toggle"})
        except:
            pass
        try:
            requestForm["voldown"]
            callKodiAPI("Application.SetVolume", {"volume": "decrement"})
        except:
            pass
        try:
            requestForm["uparrow"]
            callKodiAPI("Input.Up", {})
        except:
            pass
        try:
            requestForm["volup"]
            callKodiAPI("Application.SetVolume", {"volume": "increment"})
        except:
            pass
        try:
            requestForm["leftarrow"]
            callKodiAPI("Input.Left", {})
        except:
            pass
        try:
            requestForm["selectelement"]
            callKodiAPI("Input.Select", {})
        except:
            pass
        try:
            requestForm["rightarrow"]
            callKodiAPI("Input.Right", {})
        except:
            pass
        try:
            requestForm["backbtn"]
            callKodiAPI("Input.Back", {})
        except:
            pass
        try:
            requestForm["downarrow"]
            callKodiAPI("Input.Down", {})
        except:
            pass
        try:
            requestForm["homebtn"]
            callKodiAPI("Input.Home", {})
        except:
            pass
    return render_template('index.html')

app.run(host="0.0.0.0")
