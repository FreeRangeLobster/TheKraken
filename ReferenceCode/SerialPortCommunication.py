import serial
import time
#ser = serial.Serial('COM9')  # open serial port
#print(ser.name)         # check which port was really used
#ser.write(b'hello')     # write a string
#ser.close()             # close port

with serial.Serial('COM10', 9600, timeout=1) as ser:
    x = ser.read(20)          # read one byte
    ser.write(b'$')  # write a string
    s = ser.read(10)        # read up to ten bytes (timeout)
    line = ser.readline()   # read a '\n' terminated line
    #input = input(">> ")
    print(line)

    input_t=1
    while 1 :
        # get keyboard input
        input_t = input(">> ")
            # Python 3 users
            # input = input(">> ")
        if input_t == 'exit':
            ser.close()
            exit()
        else:
            # send the character to the device
            # (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
            input_t=input_t + "\r\n"


            #ser.write(input_t.encode())
            ser.write(input_t.encode())

            #out.decode('utf-8')



            out = ''
            # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            while ser.inWaiting() > 0:
                line = ser.readline()
                out = out + str(line) + "\r\n"
                #print (">>", line)
                #out = ser.read(20)
                #out = str(out)
                #print (">>", out)

            if out != '':
                print (">>", out)
                #print(out.decode('utf-8'))