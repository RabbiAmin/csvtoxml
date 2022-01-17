import csv
f = open('Dummy.csv') #reading csv file
csv_f =  csv.reader(f)
data = []
for row in csv_f:
    data.append(row) #storing row data as individual list
f.close()

print(data[1:]) #printing all the rows except header

#def convert_row(row):
 #   return """<Strict>
  #  <TripID> %$</TripID>
   # <TimeStamp>%$</TimeStamp>
    #<Speed>%$</Speed>
    #<Acceleration>%$</Acceleration>
    #<Heading>%$</Heading>
    #<HeadingChange>%$</HeadingChange>
    #<Latitude>%$</Latitude>
    #<Longitude>%$</Longitude>
    #<Annotation>%$</Annotation>
    #<SegmentType>%$</SegmentType>
    #</Strict>""" %$ (row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],)

def convert_row(row):
    return """<Strict>
    <TripID> %s</TripID>
    <TimeStamp>%s</TimeStamp>
    <Speed>%s</Speed>
    <Acceleration>%s</Acceleration>
    <Heading>%s</Heading>
    <HeadingChange>%s</HeadingChange>
    <Latitude>%s</Latitude>
    <Longitude>%s</Longitude>
    <Annotation>%s</Annotation>
    <SegmentType>%s</SegmentType>
    </Strict>""" % (row[0], row[1], row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])


with open ('output.xml','w') as f:
    f.write('\n'.join([convert_row(row) for row in data]))