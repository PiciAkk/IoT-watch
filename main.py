from flask import Flask, render_template, request
import requests
import json
import broadlink

devices = broadlink.discover(timeout=5)
devices[0].auth()

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
    if devices[0].check_power() == True:
        devices[0].set_power(False)
    else:
        devices[0].set_power(True)
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        requestForm = request.form.to_dict()
        command = list(requestForm.keys())[0]
        if command == "kodioff":
            callKodiAPI("System.Shutdown", {})
        elif command == "togglelights":
            toggleLights()
        elif command == "kodimute":
            callKodiAPI("Application.SetMute", {"mute": "toggle"})
        elif command == "voldown":
            callKodiAPI("Application.SetVolume", {"volume": "decrement"})
        elif command == "uparrow":
            callKodiAPI("Input.Up", {})
        elif command == "volup":
            callKodiAPI("Application.SetVolume", {"volume": "increment"})
        elif command == "leftarrow":
            callKodiAPI("Input.Left", {})
        elif command == "selectelement":
            callKodiAPI("Input.Select", {})
        elif command == "rightarrow":
            callKodiAPI("Input.Right", {})
        elif command == "backbtn":
            callKodiAPI("Input.Back", {})
        elif command == "downarrow":
            callKodiAPI("Input.Down", {})
        elif command == "homebtn":
            callKodiAPI("Input.Home", {})
        elif command == "playpausebtn":
            callKodiAPI("Player.PlayPause", {"playerid": 1})
    return render_template('index.html')

app.run(host="0.0.0.0")
