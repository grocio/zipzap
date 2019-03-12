# -*- coding:utf-8 -*-
#!/usr/bin/env python

target_extension = '.wav'

import os
import zipfile

current_path = os.getcwd()
folder_name = os.path.basename(current_path)
file_name_li = os.listdir(current_path)

with zipfile.ZipFile('comp_{}.zip'.format(folder_name), 'w') as new_zip:
	for file_name in file_name_li: 
		if file_name.endswith(target_extension):
			new_zip.write(file_name)
