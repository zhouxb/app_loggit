==============================================
app_loggit: log for project template
==============================================

Provides log to a project template.

INSTALL
============
1. Install Project Template

  django-admin.py startproject --template=https://github.com/zhouxb/project_template/zipball/master [project_name]

2. Install App Account

  pip install https://github.com/zhouxb/app_loggit/zipball/master

3. Add account to INSTALLED_APPS in settings.py

  INSTALLED_APPS = {

    ...

    loggit,

  }

4. Add loggit url in urls.py

  url(r'loggit/', include('loggit.urls')),

5. Create DB

  python manage.py schemamigration loggit --init

  python manage.py migrate loggit

