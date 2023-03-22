import paramiko
import re
def check_ethernet_interface(ip, port=22, username='p', password='p'):
    try:
        with paramiko.SSHClient() as client:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(ip, port, username, password)

            stdin, stdout, stderr = client.exec_command('interface ethernet monitor ether1 duration=1s')
            datos = stdout.read().decode('utf-8')
            #se utiliza expresiones regulares para ver el rate
            patron = r'rate:\s+([^\s]+)'
            resultado = re.search(patron, datos)
            if resultado:
                bits_por_segundo = resultado.group(1)
                # print(f"El rate se encuentra a: {bits_por_segundo}")
                return f"El rate se encuentra a: {bits_por_segundo}"
            else:
                print("No se encontró ninguna coincidencia.")

    except:
        return f"No se pudo conectar con {ip}"


#inicia un test de velocidad
def open_test(ip,port='22', username='p',password='p'):
    try:
        with paramiko.SSHClient() as client:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(ip, port, username, password)

            stdin, stdout, stderr = client.exec_command('tool bandwidth-test address=10.0.255.2 protocol=tcp user=p password=p direction=both duration=15s')
            datos = stdout.read().decode('utf-8')
            print(datos)

    except:
        return f'Hubo algun error con el test de velocidad'
#verifica la velocidad
def mirar_test(ip,port='22', username='tre',password='hhjj'):
    try:
        with paramiko.SSHClient() as client:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(ip, port, username, password)

            stdin, stdout, stderr = client.exec_command('interface monitor-traffic wlan1 duration=1s')
            datos = stdout.read().decode('utf-8')
            # print(datos)
            
            patron = r'rx-bits-per-second:\s+([^\s]+)'

            resultado = re.search(patron, datos)

            if resultado:
                bits_por_segundo = resultado.group(1)
                print(f"La velocidad seria de descarga seria de: {bits_por_segundo}")
                return f"La velocidad seria de descarga seria de: {bits_por_segundo}"
            else:
                print("No se encontró ninguna coincidencia.")

    except:
            print( f'Hubo algun error de lectura')
            return f'Hubo algun error de lectura'