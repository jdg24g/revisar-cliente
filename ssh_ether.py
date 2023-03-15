import paramiko
def check_ethernet_interface(ip, port=22, username='tre', password='hhjj'):
    try:
        with paramiko.SSHClient() as client:
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.load_system_host_keys()
            client.connect(ip, port, username, password)

            stdin, stdout, stderr = client.exec_command('interface ethernet monitor ether1 duration=1s')
            datos = stdout.read().decode('utf-8')
            # print(len(datos), datos)

            if datos.find("rate: 100Mbps") != -1:
                return datos[129:142]
            elif datos.find("rate: 10Mbps") != -1:
                return datos[129:141]
            else:
                return datos[129:142]

    except:
        return f"No se pudo conectar con {ip}"


#inicia un test de velocidad
def open_test(ip,port='22', username='tre',password='hhjj'):
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
            print(datos)
    except:
            print( f'Hubo algun error de lectura')
            return f'Hubo algun error de lectura'