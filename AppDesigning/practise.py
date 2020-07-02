"""from django.contrib.staticfiles import finders

APP_LABEL = 'app_youre_looking_at'
FILE_NAME = 'file_name_you_want_to_read_or_write.ext'

stores = finders.AppDirectoriesFinder(app_names={APP_LABEL}).storages
print(f'Here it is: {stores[APP_LABEL].path(FILE_NAME)}')"""
import numpy as np

arr=np.array(['a','a','a','a','a','a','a','a'])
for i in arr:
    print(i)




"""
arr=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

print(arr)
sliced=arr[:2 ,::2]
print(sliced)
indexed=arr[[1,2,2,0],
            [2,1,0,1]]
print(indexed)

"""