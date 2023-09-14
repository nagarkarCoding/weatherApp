# weatherApp
# To fetch weather data for a given city
# Ensure you have python installed in your notebook and the appropriate PATH system variable is set 
# to access python executable from any directory in the notebook.


python -m venv myenv       # Create a virtual environment
source myenv/bin/activate # Activate the virtual environment (Linux/Mac)
myenv\Scripts\activate    # Activate the virtual environment (Windows)

python.exe -m pip install --upgrade pip
pip install django
pip install requests

django-admin startproject weatherAppProject
cd .\weatherAppProject\
python .\manage.py startapp weatherApp

Open the `settings.py` file in your project directory (`projectname/settings.py`) and add your app to the `INSTALLED_APPS` list:
```python
   INSTALLED_APPS = [
       # ...
       'weatherApp',
       # ...
   ]
 ```

python manage.py makemigrations
python manage.py migrate

# Run development server 
Start the Django development server to preview your app:

```
python manage.py runserver
```

By default, the server runs at `http://127.0.0.1:8000/`. Open your web browser and navigate to this URL to see your app in action.

# create login user credentials
python project.py createsuperuser