import csv
import math
from decimal import Decimal
from unesco.models import Category,Iso,Region,States,Site


def run():
    csv_file = "test.csv"
    fhand    = open(csv_file)
    reader   = csv.reader(fhand)
    # skip the header
    next(reader)
    
    
    Category.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    States.objects.all().delete()
    Site.objects.all().delete()
    counter = 1
    for row in reader:
#name,description,justification,year,longitude,latitude,area_hectares,category,states,region,iso

        #print(row[7])
        try:
            cate = row[7]
            c,created = Category.objects.get_or_create(name=row[7])
        except:
            cate = None
            c,created = Category.objects.get_or_create(name=row[7])

#print(row[7])
        try:
            stat = row[8]
            s,created = States.objects.get_or_create(name = stat)
        except:
            stat = None
            s,created = States.objects.get_or_create(name = stat)

#print(row[7])
        try:
            reg = row[9]
            r,created = Region.objects.get_or_create(name=reg)
        except:
            reg = None
            r,created = Region.objects.get_or_create(name=reg)

#print(row[7])
        try:
            is_o = row[10]
            i,created = Iso.objects.get_or_create(name=is_o)
        except:
            is_o = None
            i,created = Iso.objects.get_or_create(name=is_o)
        
        
        
        name = row[0]
        description = row[1]
        try:
            justification = row[2]
        except:
            justification = None 
        year  = row[3]
        longi = row[4]
        lati  = row[5]
        area  = row[6]
        state = Site(name=name,description=description,justification=justification,year=year,longitude=longi,latitude=lati,area_hectares=area,category=c,states=s,region=r,iso=i)
        state.save()
        print("-----------")        
 
       