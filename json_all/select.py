import os
import json

directory = '/mnt/petrelfs/mengfanqing/Physical_bench/json_all'
jsons = os.listdir(directory)
for json_file in jsons:
    if json_file == 'select.py':
        continue
    json_path = os.path.join(directory,json_file)
    print(json_file)
    with open(json_path,'r') as f:
        data = json.load(f)
    
    result = []
    for data_tmp in data:
        new_dict = {
            'prompt': data_tmp['scene'],
            'normal': data_tmp['normal'],
            'grading': data_tmp['grading'],
            'law': data_tmp['law'],
            'DALLE3': data_tmp['DALLE3'],
            'DALLE2': data_tmp['DALLE2'],
            'Mid': data_tmp['Mid'],
            'Gemini': data_tmp['Gemini'],
        }

        result.append(new_dict)
    
    with open(os.path.join(directory,json_file),'w') as f:
        json.dump(result,f,indent=4)

# zip -r /mnt/petrelfs/mengfanqing/Physical_bench/images_all/Gemini_images_chem.zip /mnt/petrelfs/mengfanqing/Physical_bench/Gemini_images_chem