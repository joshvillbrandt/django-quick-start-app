django-quick-start-app
======================

This is a Django app template to help you get up and running quickly.

# Setup

By this point, you should already have a Django project set up. Fix that first if you don't. Once you do, run the command below replacing app_name with the name of your new app.

If you are new do Django or haven't used django-quick-start-app, you might want to name your app 'polls' since this quick start app includes the polls models from the Django tutorial. Don't worry though, as soon as you are ready to start your own model, you can make a new app just as easily.

    cd project
    python manage.py startapp --template=https://github.com/joshvillbrandt/django-quick-start-project/archive/master.zip app_name

# Get to work

To use an app in a Django project, you first need to add the app name to the end of the INSTALLED_APPS list in your projects settings.py file. It should look like this:

    'app_name',

Next, you'll want to create some models and views associated with your app. The basic polls models as described in the Django tutorials (https://docs.djangoproject.com/en/dev/intro/tutorial01/) is included as a template. To change the polls model to something of your own, you'll need to edit code in app_name/models.py, app_name/views.py, and app_name/admin.py.

You will also want to point to your views by setting up the app_name/urls.py file. Then don't forget to include your app's urls.py file in the urlpatterns of your projects main urls.py file like so:

    url(r'^app_name/', include('app_name.urls'), namespace="app_name"),

Once you have your everything set up, add the tables to your database and start the server:

    python manage.py syncdb
    python manage.py runserver 0.0.0.0:8080

You can then view your polls app by going to http://localhost:8080/app_name/. The admin interface should also be available at http://localhost:8080/admin/.