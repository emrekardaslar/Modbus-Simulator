from pymodbus3.client.sync import ModbusTcpClient

client = ModbusTcpClient('127.0.0.1', 5021)
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result.bits[0])
client.close()