import serial, time

port_p26 = "COM10"
baud_p26 = 9600

# meter sends the pressure data in response to command
command_p26 = "?IP\r\n"

ser_p26 = serial.Serial(port_p26, baud_p26, timeout=1)

output_file = "SerialLogger_P26.txt"
comment = ""

date = time.localtime()
date = str(date[2]) + "." + str(date[1]) + "." + str(date[0])
file = open(output_file, "a")
header = "\n" + "* * * *\n\n" + output_file + "\n" + "Halstrup-Walcher P26 " + date
if len(comment) > 0:
    header += "\n" + comment
header += "\n\n" + "* * * *\n\n"
print(header)
file.write(header)
file.close()

try:
    while True:
        ser_p26.reset_input_buffer()
        ser_p26.write(command_p26.encode())
        p26_press = ""
        p26_press = ser_p26.readline().decode().rstrip()[3:-3]
        if p26_press[0] == " ":
            p26_press = p26_press[1:]

        date = time.localtime()
        act_date = str(date[2]) + "." + str(date[1]) + "." + str(date[0])
        act_time = str(date[3]) + ":" + str(date[4]) + ":" + str(date[5])

        file = open(output_file, "a")
        output_data = act_date + "," + act_time + ",pressure," + p26_press + ",Pa"
        print(output_data)
        file.write(output_data + "\n")
        file.close()
except KeyboardInterrupt:
    file.close()
