from librouteros import *
import json
from ssh_ether import check_ethernet_interface
# ip = '192.168.31.138'

def check_cliente(ip):
    try:
        ether = check_ethernet_interface(ip)
        ether_result = ether
    except:
        ether_result = ether
    try:
        api = connect(
        username='tre',
        password='hhjj',
        host=ip)
        #------------------------------------------------------------------
        wireless_information = api.path('interface/wireless')
        wireless_information = tuple(wireless_information)[0]
        mac_address = wireless_information['mac-address']
        ssid = wireless_information['ssid']
        radio_name = wireless_information['radio-name']
        #------------------------------------------------------------------
        registration_table = api.path('interface/wireless/registration-table')
        registration_table = tuple(registration_table)[0]
        distance = registration_table['distance']
        tx_signal01 = registration_table['signal-strength']
        rx_signal01 = registration_table['tx-signal-strength']
        tx_ccq = registration_table['rx-ccq']
        rx_ccq = registration_table['tx-ccq']
        os_version = registration_table['routeros-version']
        #------------------------------------------------------------------
        dhcp = api.path('ip/dhcp-server/lease')
        dhcp = tuple(dhcp)
        #------------------------------------------------------------------
        #------------------------------------------------------------------
        resultadoa = f'El mac del equipo  de {radio_name}\nseria {mac_address}.\nConectado por {ssid} con señal de {rx_signal01}/{tx_signal01} a {distance}km\nCCQ de {rx_ccq}/{tx_ccq}%\n{ether_result}.\n'
        
        #------------------------------------------------------------------
        lista = ""
        if len(dhcp) != 0:
            for conectados in dhcp:
                # print(json.dumps(conectados))
                if "host-name" in conectados:
                    lista += f"El equipo conectado con ip {conectados['address']} seria el {conectados['host-name']}.\n"
                    # print(f"El equipo conectado con ip {conectados['address']} seria el {conectados['host-name']}")
                else:
                    lista += f"El equipo conectado con ip {conectados['address']} no posee host-name.\n"
                    # print(f"El equipo conectado con ip {conectados['address']} no posee host-name")
                
        else:
            lista = "no hay nadie conectado"
        
        print(resultadoa,lista)
        return resultadoa + lista
    except:
        return f'Ocurrio algun error al conectar con {ip}'