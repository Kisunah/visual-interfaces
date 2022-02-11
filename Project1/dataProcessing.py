import os
import glob
import pandas as pd

os.chdir('C:/Users/sethc/Desktop/visual-interfaces/data')

extension = 'csv'
allFilenames = [i for i in glob.glob('*.{}'.format(extension))]

combinedCsv = pd.concat([pd.read_csv(f) for f in allFilenames])
combinedCsv.to_csv('aqiData.csv', index=False, encoding='utf-8-sig')