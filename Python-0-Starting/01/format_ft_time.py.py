from datetime import datetime

current_time = datetime.now()
formatted_time = current_time.strftime("%b %d %Y")

epoch_time = datetime(1970, 1, 1)

seconds_since_epoch = (current_time - epoch_time).total_seconds()
scientific_notation = "{:.0e}".format(seconds_since_epoch)
formatted_seconds = '{:,.0f}'.format(seconds_since_epoch)

string_seconds = str(formatted_seconds)

print("Seconds since January 1, 1970: " + string_seconds + " or " + scientific_notation + " in scientific notation")
print(formatted_time)