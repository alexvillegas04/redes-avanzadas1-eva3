from flask import Flask
from flask import jsonify
from flask import request 
from flask import render_template 
from datetime import datetime
from ping3 import ping

sample = Flask (__name__)
SERVER_ADDRESS = '192.0.2.1'

@sample .route ("/")

def main():
	return render_template ("index.html")

consulta_historial = []
def check_server_status():
	response = ping(SERVER_ADDRESS)
	if response is not None:
		return "En linea"
	else:
		return "Fuera de linea"
def get_current_time():
	return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

@sample.route ('/monitoreo')

def monitoreo():
	status = check_server_status()
	last_check_time = get_current_time()

	consulta_historial.append({
		'fecha_hora': last_check_time,
		'estado': status
	})

	return jsonify({
		'estado': status,
		'ultima_comprobacion': last_check_time
	})

@sample.route('/historial')
def historial():
	return jsonify({
		'historial': consulta_historial
	})

if __name__ == "__main__":
	sample.run (host="0.0.0.0", port=1080)

