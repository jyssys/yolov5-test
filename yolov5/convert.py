from glob import glob
from sklearn.model_selection import train_test_split

img_list = glob('dataset/export/images/*.jpg')

train_img_list, val_img_list = train_test_split(img_list, test_size = 0.2, random_state = 2000)

with open('dataset/train.txt', 'w') as f:
  f.write('\n'.join(train_img_list) + '\n')

with open('dataset/val.txt', 'w') as f:
  f.write('\n'.join(val_img_list) + '\n')
  
import yaml

with open('dataset/data.yaml', 'r') as f:
  data = yaml.safe_load(f)

print(data)

data['train'] = 'dataset/train.txt'
data['val'] = 'dataset/val.txt'

with open('dataset/data.yaml', 'w') as f:
  yaml.dump(data, f)

print(data)