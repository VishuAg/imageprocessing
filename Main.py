from library.altitudeCal import get_elevation_from_open_meteo
from library.dayCalculator import get_day_from_date_in_hindi
from library.imageimporter import add_text_with_translucent_background
from library.locationCalculator import getLocationName
from library.randomTimeCalculator import generate_random_time_ist
from library.getOutputFileName import rename_file_with_text
from library.getInputsFromCSV import get_lat_lon_from_xlsx
import asyncio
async def main():
    font_path = "/Users/vishnuagrawal/Desktop/Project/font/Noto_Sans_Devanagari/NotoSansDevanagari-VariableFont_wdth,wght.ttf" 
    text = []
    excelSheetPath="/Users/vishnuagrawal/Desktop/Project/data/directions/co-ordinate_bagbahara.xlsx"
    lat, long = get_lat_lon_from_xlsx(excelSheetPath, "Sheet1", 1, 'B')
    date="01.02.2024"
    loc = await getLocationName(lat, long);
    text.append(loc)
    text.append(f"Latitude {lat}°")
    text.append(f"Longitude {long}°")
    timeInIst, timeInGst= generate_random_time_ist()
    text.append(f"Local {timeInIst}")
    text.append(f"GMT {timeInGst}")
    text.append(f"Altitude {get_elevation_from_open_meteo(lat, long)} मीटर")
    text.append(f"{get_day_from_date_in_hindi(date)}, {date}")
    input_image_location = "/Users/vishnuagrawal/Desktop/Project/data/InputImages/image1.jpg"
    output_image_dir = "/Users/vishnuagrawal/Desktop/Project/data/OutputImages"
    output_image_location = rename_file_with_text(input_image_location, output_image_dir)
    add_text_with_translucent_background(input_image_location, output_image_location, text, font_path)
asyncio.run(main())