# UAM_julio2019

Seleccionar y copiar el siguiente texto:

[{
	"id": "a9ba2a0f.7097e8",
	"type": "tab",
	"label": "Flow 3",
	"disabled": false,
	"info": ""
}, {
	"id": "4aba9546.10634c",
	"type": "inject",
	"z": "a9ba2a0f.7097e8",
	"name": "",
	"topic": "",
	"payload": "",
	"payloadType": "date",
	"repeat": "60",
	"crontab": "",
	"once": false,
	"onceDelay": 0.1,
	"x": 151.5,
	"y": 215,
	"wires": [
		["37a64daa.156092"]
	]
}, {
	"id": "37a64daa.156092",
	"type": "weather",
	"z": "a9ba2a0f.7097e8",
	"name": "",
	"longitude": "2",
	"latitude": "40",
	"x": 356.5,
	"y": 214,
	"wires": [
		["9fabd051.68cbc"]
	]
}, {
	"id": "a33879bc.a60728",
	"type": "debug",
	"z": "a9ba2a0f.7097e8",
	"name": "",
	"active": false,
	"tosidebar": true,
	"console": false,
	"tostatus": false,
	"complete": "false",
	"x": 751.5,
	"y": 214,
	"wires": []
}, {
	"id": "9fabd051.68cbc",
	"type": "change",
	"z": "a9ba2a0f.7097e8",
	"name": "",
	"rules": [{
		"t": "set",
		"p": "wdir",
		"pt": "flow",
		"to": "payload.current.wind.direction.value",
		"tot": "msg"
	}, {
		"t": "set",
		"p": "wspeed",
		"pt": "flow",
		"to": "payload.current.wind.speed.value",
		"tot": "msg"
	}],
	"action": "",
	"property": "",
	"from": "",
	"to": "",
	"reg": false,
	"x": 551.5,
	"y": 214,
	"wires": [
		["a33879bc.a60728"]
	]
}, {
	"id": "5fb21f6e.d2de7",
	"type": "function",
	"z": "a9ba2a0f.7097e8",
	"name": "Generate payload",
	"func": "seed1 = Math.random() -0.5;\nseed2 = Math.random() -0.5;\nseed3 = Math.random() -0.5;\nseed4 = Math.random() -0.5;\n\nWindSpeed = parseInt(flow.get('wspeed'));\n\nWindDirection = parseInt(flow.get('wdir'));\n\nTurbineSpeed = (1.5*WindSpeed) + (seed1);\n\nPower = (TurbineSpeed*15) + (seed2*4);\n\nVibrationX = (seed3/20 + Math.abs(Math.abs(WindDirection-180) -180)/100 + WindSpeed/100)/10;\n\nVibrationY = (seed4/20 + Math.abs(Math.abs(WindDirection-180) -180)/100 + WindSpeed/100)/10;\n\nmsg.payload = {\"WindSpeed\": WindSpeed,\"WindDirection\": WindDirection, \"TurbineSpeed\":TurbineSpeed,\"Power\":Power,\"VibrationX\":VibrationX,\"VibrationY\":VibrationY};\n\n\nreturn msg;",
	"outputs": 1,
	"noerr": 0,
	"x": 421.5,
	"y": 335,
	"wires": [
		["3cfc9abd.6fa606", "398c8f3c.65ab2"]
	]
}, {
	"id": "a9397809.ba1cf8",
	"type": "inject",
	"z": "a9ba2a0f.7097e8",
	"name": "",
	"topic": "",
	"payload": "",
	"payloadType": "date",
	"repeat": "10",
	"crontab": "",
	"once": false,
	"onceDelay": 0.1,
	"x": 155,
	"y": 336,
	"wires": [
		["5fb21f6e.d2de7"]
	]
}, {
	"id": "3cfc9abd.6fa606",
	"type": "debug",
	"z": "a9ba2a0f.7097e8",
	"name": "",
	"active": true,
	"tosidebar": true,
	"console": false,
	"tostatus": false,
	"complete": "false",
	"x": 650,
	"y": 410,
	"wires": []
}, {
	"id": "398c8f3c.65ab2",
	"type": "wiotp out",
	"z": "a9ba2a0f.7097e8",
	"authType": "d",
	"qs": "false",
	"qsDeviceId": "",
	"deviceKey": "",
	"deviceType": "",
	"deviceId": "",
	"event": "event",
	"format": "json",
	"qos": "",
	"name": "",
	"x": 673.5,
	"y": 334,
	"wires": []
}]
