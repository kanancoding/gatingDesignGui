import csv

def savecsv_gating(filename,data):
    gating_header = ['Head', 'LossFactor', 'FlowRate', 'CastingHeight_P', 'TotalCasting_C', 'Name', 'Area', 'Width', 'Height']
    # writing to csv file 
    with open(filename, 'w', encoding='UTF8', newline='') as csvfile: 
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
        # writing the fields 
        csvwriter.writerow(gating_header)
        csvwriter.writerows(data)

def savecsv_riser(riser_file,riser_data):
    riser_header = ['Material','CastingWt','CastingMod','ColdRiser',
                            'NeckMod','RiserMod',
                            'NeckW','NeckH','NeckL',
                            'RiserBase','RiserTop','RiserH','RiserWt','RiserFeed']
    with open(riser_file, 'w', encoding='UTF8', newline='') as csvfile: 
        csvwriter = csv.writer(csvfile) 
        csvwriter.writerow(riser_header)
        csvwriter.writerows(riser_data)