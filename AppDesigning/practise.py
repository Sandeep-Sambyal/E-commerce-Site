from ecart.models import Order
import _sqlite3


try:
    sqllite=_sqlite3.connect(Order)
    cursor=sqllite.cursor()
    print("connected to SQLLITE")
    insert="""insert into Order  (name,email) values ('TEsT','TEst@test.com')"""
    count=cursor.execute(insert)
    sqllite.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()
except _sqlite3.error as error:
    print("Failed to insert data into sqlite table", error)

finally:
    if (sqllite):
        sqllite.close()
        print("The SQLite connection is closed")




"""from django.contrib.staticfiles import finders
 from ec
APP_LABEL = 'app_youre_looking_at'
FILE_NAME = 'file_name_you_want_to_read_or_write.ext'

stores = finders.AppDirectoriesFinder(app_names={APP_LABEL}).storages
print(f'Here it is: {stores[APP_LABEL].path(FILE_NAME)}')
import numpy as np

arr=np.array(['a','a','a','a','a','a','a','a'])
for i in arr:
    print(i)"""




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