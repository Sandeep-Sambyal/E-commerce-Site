from django.contrib.staticfiles import finders

APP_LABEL = 'app_youre_looking_at'
FILE_NAME = 'file_name_you_want_to_read_or_write.ext'

stores = finders.AppDirectoriesFinder(app_names={APP_LABEL}).storages
print(f'Here it is: {stores[APP_LABEL].path(FILE_NAME)}')