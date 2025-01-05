from openpyxl import load_workbook

    
def get_lat_lon_from_xlsx(file_path, sheet_name, row, colForLatLong, colForDate):
    # Load workbook and sheet
    wb = load_workbook(file_path)
    sheet = wb[sheet_name]
    
    # Get latitude and longitude from the specified cells

    lat, lon = sheet[f"{colForLatLong}{row}"].value.split(",")
    date = sheet[f"{colForDate}{row}"].value
    lat = lat.replace(" ", "")
    lon = lon.replace(" ", "")
    return lat, lon, date

# Example usage
# file_path = "/Users/vishnuagrawal/Desktop/Project/data/directions/co-ordinate_bagbahara.xlsx"
# sheet_name = "White"
# latitude, longitude, Date = get_lat_lon_from_xlsx(file_path, sheet_name, 1, 'B', 'C')
# print(f"Latitude: {latitude}, Longitude: {longitude}")

