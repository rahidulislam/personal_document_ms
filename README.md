# personal_document_ms

## create virtual environment
cd personal_document_ms\
python3 -m venv venv

## activate virtual environment
source venv/bin/activate

## install package
pip install -r requirements.txt

## run make migrations and migrate
python manage.py makemigrations\
python manage.py migrate

## run server
python manage.py runserver

### Import API Collection in Insomnia Rest Client (personal-doc-ms.json).
`Application > Preferences > Data > Import Data`

### Read api endpoints for api information