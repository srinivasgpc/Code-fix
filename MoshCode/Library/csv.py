import csv


#write

with open("data.csv", "w") as file: # eleminate close syntax

    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product#id", "price_id"])
    writer.writerow([1000, 1 ,5 ])
    writer.writerow([1001, 2, 15])

#read

with open("data.csv") as file: # eleminate close syntax

    reader = csv.writer(file)
    #print(list(reader))
    for row in reader:
        print(row)

