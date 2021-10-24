# R3-SoftwareTask2-ZacharyCote
 
To complete this project, two .py files were needed. 

The first file, input.py, which acts as the client. It uses the msvcrt commands to read values from the keyboard. This file also includes code for the TCP, which allows for the keyboard inputs to be sent to the server. 


The second file is the output.py file, which acts as the server. It uses the TCP to receive data from the client, and then uses a series of if statements to process the data and produce the correct output depending on the keypress sent by the client. The server can recognise numbers from 0 to 5 to set the speed of the moter and it recognizes 'w, a, s, d' keyboard inputs and uses them to output motor directions and speeds to move the rover forwars, backword, turn left, or turn right. 


The two programs are working as expected and are producing the correct output.


Link to video demo: https://drive.google.com/file/d/10XwXQgymCDeWgf9pT7fjg6O2OwbV_iBM/view?usp=sharing
