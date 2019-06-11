import serial
import requests
serial_port = '/dev/ttyUSB0';
baud_rate = 9600; #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt";

output_file = open(write_to_file_path, "w+");
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline();
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    print(line);
    
    #создание dictionary для использования JSON
    data = {'x': float(line[3:12]),
            'y': float(line[17:]),
            'z': 0
    }

    #output_file.write(line);
    print(data)
    r = requests.post("http://gisis.cf/api/gps/", json=data)
    print(r)
