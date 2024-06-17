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
    
    length = len(lanes) # GET TOTAL LANES
    row = 31
    for indx in range(length):
        lane = lanes[indx]

        sheet["A{row}".format(row=row)] = lane[0]   # ESTIMATED ID
        sheet["B{row}".format(row=row)] = lane[5]   # ORIGIN CITY
        sheet["C{row}".format(row=row)] = lane[7]   # ORIGIN STATE
        sheet["D{row}".format(row=row)] = lane[1]   # ORIGIN ZIP
        sheet["E{row}".format(row=row)] = "USA"     # ORIGIN COUNTRY
        sheet["F{row}".format(row=row)] = lane[6]   # DESINATION CITY
        sheet["G{row}".format(row=row)] = lane[8]   # DESINATION STATE
        sheet["H{row}".format(row=row)] = lane[2]   # DESTINATION ZIP
        sheet["I{row}".format(row=row)] = "USA"     # DESTINATION COUNTRY
        sheet["J{row}".format(row=row)] = lane[9]   # DISTANCE
        sheet["K{row}".format(row=row)] = 1     # VOLUMEN
        sheet["L{row}".format(row=row)] = "DM"  # ROUTE TYPE
        sheet["M{row}".format(row=row)] = "DV"  # MODE
        sheet["N{row}".format(row=row)] = "N"   # CONTROL TYPE
        sheet["O{row}".format(row=row)] = 53    # EQUIPMENT SIZE
        sheet["P{row}".format(row=row)] = "R"   # SERVICE LEVEL
        sheet["Q{row}".format(row=row)] = "OB"  # MOVEMENT TYPE
        sheet["R{row}".format(row=row)] = "C"   # RATE TYPE
        sheet["S{row}".format(row=row)] = "ABC" # SERVICE PROVIDER TYPE
        sheet["T{row}".format(row=row)] = "N"   # HAZARDUS MATERIAL
        row += 1 #ROW MUST START IN 31
    
    workbook.save(dest_path)
    
    