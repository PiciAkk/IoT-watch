# set subtitle

```python
payload = json.dumps({
	"id": 1,
	"jsonrpc": "2.0",
	"method": "Player.SetSubtitle",
	"params": {
		"playerid": 1
		"subtitle": 1 # or "off", or "on", or any other integer 
	}
})
```

# get current subtitle

```python
payload = json.dumps({
	"id": 1,
	"jsonrpc": "2.0",
	"method": "player.GetProperties",
	"params": {
		"playerid": 1,
		"properties": ["currentsubtitle"]
	}
}})
```

# get a list of available subtitles

```python
payload = json.dumps({
	"id": 1,
	"jsonrpc": "2.0",
	"method": "Player.GetProperties",
	"params": {
		"playerid": 1,
		"properties": ["subtitles"]
	} 
}})
```
