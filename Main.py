from library.altitudeCal import get_elevation_from_open_meteo
from library.dayCalculator import get_day_from_date_in_hindi
from library.imageimporter import add_text_with_translucent_background
from library.locationCalculator import getLocationName
from library.randomTimeCalculator import generate_random_time_ist
from library.getOutputFileName import rename_file_with_text
from library.getInputsFromCSV import get_lat_lon_from_xlsx
import os

font_path = "/Users/vishnuagrawal/Desktop/Project/font/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf" 
text = []
excelSheetPath="/Users/vishnuagrawal/Desktop/Project/data/directions/co-ordinate_bagbahara.xlsx"
folderPaths = ["/Users/vishnuagrawal/Desktop/Project/data/InputImages/White","/Users/vishnuagrawal/Desktop/Project/data/InputImages/Pink","/Users/vishnuagrawal/Desktop/Project/data/InputImages/Grey","/Users/vishnuagrawal/Desktop/Project/data/InputImages/Blue"]
outputImagesDirectories = ["/Users/vishnuagrawal/Desktop/Project/data/OutputImages/White","/Users/vishnuagrawal/Desktop/Project/data/OutputImages/Pink", "/Users/vishnuagrawal/Desktop/Project/data/OutputImages/Grey", "/Users/vishnuagrawal/Desktop/Project/data/OutputImages/Blue"]
Sheets = ["White", "Pink", "Grey", "Blue"]
i=0
j=-1

for folder_path in folderPaths:
    j = j + 1
    i = 1
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):  # Add more image extensions if needed
            input_image_location = os.path.join(folder_path, filename)
        else: continue
        lat, long, date = get_lat_lon_from_xlsx(excelSheetPath, Sheets[j], i, 'B', 'C')
        i = i + 1
        loc = getLocationName(lat, long)
        text = []
        text.append(f"                                 {loc}                           ")
        # text.append("")
        text.append(f"Latitude                                                  Longitude")
        text.append(f"{lat}°                                              {long}°")
        timeInIst, timeInGst= generate_random_time_ist()
        # text.append("")
        text.append(f"Local {timeInIst}                                  Altitude {get_elevation_from_open_meteo(lat, long)} मीटर")
        text.append(f"GMT {timeInGst}                                   {get_day_from_date_in_hindi(date)}, {date}")
        # text.append(f"Altitude {get_elevation_from_open_meteo(lat, long)} मीटर")
        # text.append(f"{get_day_from_date_in_hindi(date)}, {date}")
    
        output_image_location = rename_file_with_text(input_image_location, outputImagesDirectories[j])
        add_text_with_translucent_background(input_image_location, output_image_location, text, font_path)
