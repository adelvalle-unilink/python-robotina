import shutil

from datetime import datetime
from openpyxl import load_workbook


def copy_excel_template(lanes):
    time = datetime.now()
    new_book_name = time.strftime("%m-%d-%Y-%H-%M-%S")
    dest_path = "docs/{book_name}.xlsx".format(book_name=new_book_name)
    
    shutil.copy("main_template.xlsx", dest_path)
    
    workbook = load_workbook(filename=dest_path)
    sheet = workbook.worksheets[0]
    
    for indx, lane in enumerate(lanes):
        row = indx + 1
        sheet["A3{row}".format(row=row)] = lane[0]   # ESTIMATED ID
        sheet["B3{row}".format(row=row)] = lane[5]   # ORIGIN CITY
        sheet["C3{row}".format(row=row)] = lane[7]   # ORIGIN STATE
        sheet["D3{row}".format(row=row)] = lane[1]   # ORIGIN ZIP
        sheet["E3{row}".format(row=row)] = "USA"     # ORIGIN COUNTRY
        sheet["F3{row}".format(row=row)] = lane[6]   # DESINATION CITY
        sheet["G3{row}".format(row=row)] = lane[8]   # DESINATION STATE
        sheet["H3{row}".format(row=row)] = lane[2]   # DESTINATION ZIP
        sheet["I3{row}".format(row=row)] = "USA"     # DESTINATION COUNTRY
        sheet["J3{row}".format(row=row)] = lane[9]   # DISTANCE
        sheet["K3{row}".format(row=row)] = 1     # VOLUMEN
        sheet["L3{row}".format(row=row)] = "DM"  # ROUTE TYPE
        sheet["M3{row}".format(row=row)] = "DV"  # MODE
        sheet["N3{row}".format(row=row)] = "N"   # CONTROL TYPE
        sheet["O3{row}".format(row=row)] = 53    # EQUIPMENT SIZE
        sheet["P3{row}".format(row=row)] = "R"   # SERVICE LEVEL
        sheet["Q3{row}".format(row=row)] = "OB"  # MOVEMENT TYPE
        sheet["R3{row}".format(row=row)] = "C"   # RATE TYPE
        sheet["S3{row}".format(row=row)] = "ABC" # SERVICE PROVIDER TYPE
        sheet["T3{row}".format(row=row)] = "N"   # HAZARDUS MATERIAL
    
    workbook.save(dest_path)
    
    