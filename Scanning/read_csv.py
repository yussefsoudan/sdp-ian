import csv 

def read_query_output():
    flight_id = ""
    with open('barcodes.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(row)
                flight_id = row
                line_count += 1
         
    #details = query_db(flight_id[0])
    #print(details)
    return(flight_id)
