import os
import datetime

data_input_catalog = r'c:\temp\data_input'
data_output_catalog = r'c:\temp\data_output'

today = datetime.datetime.today()
today_output_catalog = os.path.join(data_output_catalog,today.strftime("%Y-%m-%d"))

is_input_catalog_ok = os.path.isdir(data_input_catalog)

# output folder must exist
is_output_catalog_ok = os.path.isdir(data_output_catalog)

# today output catalog cannot exist
is_today_output_catalog_ok = not (os.path.isdir(today_output_catalog)) and \
                             not (os.path.isfile(today_output_catalog))

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print('Conditions met! We can continue!')
else:
    print('Prerequisites not met! Check the paths!')

