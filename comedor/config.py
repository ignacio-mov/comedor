import os

URL_BASE = 'https://www.crecercontigo.com/agendadigitalcat'
URL_LOGIN = f'{URL_BASE}/mcole_login.php'

DEFAULT_UA = 'Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0'
USER_AGENT = os.environ.get('USER_AGENT') or DEFAULT_UA

LOG_LEVEL = os.environ['LOG_LEVEL']

USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
