import csv

def csv_to_dict(csv_file):
    '''(file) -> list

    returns a list of dictionary items extracted from file in CSV format

    Precondition: file is a file in CSV format with the 1st row being headers.

    Usage: csv_file = 'your_file.csv'
           data = csv_to_dict(csv_file)

           for item in data:
             print(item)

    >>>fetch_csv()
    {Something:something, somethingelse:somethingelse}
    '''
    data_dict = []
    
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        
        for row in csv_reader:
            data_dict.append(row)
    
    return data_dict
