# jobfairproject
to install django
follow this link
https://docs.djangoproject.com/en/2.1/howto/windows/
or
check whether python is installed and path is set up
-go to command prompt and run command : python --version
if not running then install python (if not already installed) and set up the environment variable through control panel in windows

then go to control panel-system and security - system - advanced system setting- environment variable - system variable - path - new-then paste the path of the python program folder
now run this command :
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

Then run the following:
python get-pip.py

set up the environment variable through control panel for pip [folder name is python/script]:
pip install virtualenvwrapper-win

Then create a virtual environment for your project:

mkvirtualenv myproject
then run :
workon myproject

In the command prompt, ensure your virtual environment is active, and execute the following command:

pip install django
then:
pip install django-crispy-forms

After the installation has completed, you can verify your Django installation by executing django-admin --version in the
command prompt.


after Installation
go to the jobfair project folder and run the command : 
python manage.py runserver

then open browser and type:
localhost:8000
u will be able to see the web pages
