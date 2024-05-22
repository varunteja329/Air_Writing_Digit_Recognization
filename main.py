import pandas as pd
import numpy as np
import time
import serial
import csv


arduino_port = "COM5"  # Change to the correct port
baud = 9600  # Change to the baud rate used in your Arduino code
fileName = "data.csv"

# Open a serial connection to the Arduino
ser = serial.Serial(arduino_port, baud,)

# Open a CSV file for writing
with open(fileName, mode='w', newline='') as data_file:
    data_writer = csv.writer(data_file)

    try:
        while True:
            # Read a line of data from the Arduino
            data = ser.readline().decode('utf-8').strip()

            # Convert data to a list of values (assuming comma-separated values)
            values = data.split(',')

            # Write the values to the CSV file
            data_writer.writerow(values)

    except KeyboardInterrupt:
        # Close the serial connection when the user interrupts the program
        ser.close()


# Read the CSV file into a DataFrame
import pandas as pd
import numpy as np

data = pd.read_csv(r'C:\Users\nimma\PycharmProjects\pythonProject\data.csv')


# Calculate the number of rows in the original DataFrame
total_rows = len(data)

# Calculate the number of rows in each part
part_size = total_rows // 4
re=total_rows % 4

# Split the original DataFrame into 4 parts
part1 = data.iloc[:part_size]
part2 = data.iloc[part_size:2*part_size]
part3 = data.iloc[2*part_size:3*part_size]
part4 = data.iloc[3*part_size:total_rows]

# Save each part as a separate CSV file
part1.to_csv('part1.csv', index=False)
part2.to_csv('part2.csv', index=False,header=False)
part3.to_csv('part3.csv', index=False,header=False)
part4.to_csv('part4.csv', index=False,header=False)

data1 = pd.read_csv(r'C:\Users\nimma\PycharmProjects\pythonProject\part1.csv')

# Calculate mean, min, max, and RMS values for each column
column_means1 = data1.mean()
column_mins1 = data1.min()
column_maxs1 = data1.max()
column_rms1 = np.sqrt((data1 ** 2).mean())
# Combine all statistics into a single Series
result_series = pd.concat([column_means1,column_mins1, column_maxs1, column_rms1])

# Create a new DataFrame to store the results as a single row
results = pd.DataFrame(result_series.values.reshape(1, -1))

# Save the results to a new CSV file

data2 = pd.read_csv(r'C:\Users\nimma\PycharmProjects\pythonProject\part2.csv')

# Calculate mean, min, max, and RMS values for each column
column_means2 = data2.mean()
column_mins2 = data2.min()
column_maxs2 = data2.max()
column_rms2 = np.sqrt((data2 ** 2).mean())

# Combine all statistics into a single Series
result_series1 = pd.concat([column_means2,column_mins2, column_maxs2, column_rms2])

# Create a new DataFrame to store the results as a single row
results1 = pd.DataFrame(result_series1.values.reshape(1, -1))
data3 = pd.read_csv(r'C:\Users\nimma\PycharmProjects\pythonProject\part3.csv')

# Calculate mean, min, max, and RMS values for each column
column_means3 = data3.mean()
column_mins3 = data3.min()
column_maxs3 = data3.max()
column_rms3 = np.sqrt((data3 ** 2).mean())

# Combine all statistics into a single Series
result_series2 = pd.concat([column_means3,column_mins3, column_maxs3, column_rms3])

# Create a new DataFrame to store the results as a single row
results2 = pd.DataFrame(result_series2.values.reshape(1, -1))

data4 = pd.read_csv(r'C:\Users\nimma\PycharmProjects\pythonProject\part4.csv')

# Calculate mean, min, max, and RMS values for each column
column_means4 = data4.mean()
column_mins4 = data4.min()
column_maxs4 = data4.max()
column_rms4 = np.sqrt((data4 ** 2).mean())

# Combine all statistics into a single Series
result_series3 = pd.concat([column_means4,column_mins4, column_maxs4, column_rms4])

# Create a new DataFrame to store the results as a single row
results3 = pd.DataFrame(result_series3.values.reshape(1, -1))

result_data = pd.concat([results, results1,results2,results3], axis=1,ignore_index=True)
# Save the results to a new CSV file

result_data.to_csv('summary_results.csv',index=False)