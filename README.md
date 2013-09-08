django-quick-start-app
======================

This is a Django app template to help you get up and running quickly.

The django-quick-start-app template gets everything in order so you can start coding what is unique to your app. A basic template builds on base.html (from [django-quick-start-project](http://github.com/joshvillbrandt/django-quick-start-project) or elsewhere.) Empty app.js and app.css files are already included in the template. Just install and start coding!

# Setup

By this point, you should already have a Django project set up. If you haven't, check out [django-quick-start-project](http://github.com/joshvillbrandt/django-quick-start-project). Once you do, run the command below replacing app_name with the name of your new app.

    cd project
    python manage.py startapp --template=https://github.com/joshvillbrandt/django-quick-start-app/archive/master.zip --extension=py,html app_name

# Get to work

To use an app in a Django project, you first need to add the app name to the end of the INSTALLED_APPS list in your projects settings.py file. It should look like this:

    'app_name',

Next, you'll want to create some models and views associated with your app. The basic polls models as described in the [Django tutorials](https://docs.djangoproject.com/en/dev/intro/tutorial01/) is already include, so if you want to see some models in action, no changes are required.

If you do want to make some changes of your own, you will want to edit code in app_name/models.py, app_name/views.py, app_name/urls.py, and app_name/admin.py. Also, don't forget to include your app's urls.py file in the urlpatterns of your projects main urls.py file like so:

    url(r'^app_name/', include('app_name.urls', namespace="app_name")),

Once you have your everything set up, add the new tables to your database and start the server:

    python manage.py syncdb
    python manage.py runserver 0.0.0.0:8080

You can then view your polls app by going to http://localhost:8080/app_name/. The admin interface should also be available at http://localhost:8080/admin/.
