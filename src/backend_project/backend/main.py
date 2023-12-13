from datetime import datetime, date, time
import os
import shutil

def main():

    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Backend running at {formatted_date}.")

    app_folder_path = "/app/data"
    if (not os.path.exists(app_folder_path)):
        print(f"Creating \"{app_folder_path}\".")
        os.makedirs(app_folder_path)
    
    alt_formatted_date = now.strftime("%Y%m%d_%H%M%S")
    filename = f"{alt_formatted_date}.html"
    filepath = os.path.join(app_folder_path, filename)

    print(f"Creating \"{filepath}\".")
    with open(filepath, "w") as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write("<head>\n")
        file.write("   <meta charset=\"UTF-8\">\n")
        file.write("   <title>Report</title>\n")
        file.write("</head>\n")
        file.write("<body>\n")
        file.write(f"   <p>This report generated at {formatted_date}.</p>\n")
        file.write("</body>\n")
        file.write("</html>\n")

    alt_filepath = os.path.join(app_folder_path, "report.html")
    print(f"Creating \"{alt_filepath}\".")
    shutil.copy2(filepath, alt_filepath)

    print("Backend complete.")

if __name__ == "__main__":
    main()