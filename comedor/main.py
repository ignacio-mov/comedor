from time import sleep

from comedor import app

import requests
from bs4 import BeautifulSoup

from comedor.config import URL_LOGIN, URL_BASE, PASSWORD, USER


@app.route('/comida', methods=['GET'])
def comida():

    s = init_session()
    app.logger.debug('Sesion iniciada')

    response = do_login(s, USER, PASSWORD)
    app.logger.info(f'login response {response.status_code}')

    # get main page
    soup = BeautifulSoup(response.text, 'html.parser')
    while soup.find('meta', attrs={'http-equiv': 'refresh'}):
        app.logger.info(f'refresh {soup.text} -> {soup.a["href"]}')
        sleep(1)
        r = s.get(f"{URL_BASE}/{soup.a['href']}")
        soup = BeautifulSoup(r.text, 'html.parser')

    # Read current day data
    row = soup.find('div', {'id': 'DNV'}).tr  # First row of table under DIV with id='DNV'

    # First column = date of the information, 2nd = information
    info_date = row.td.text
    info_str = row.td.next_sibling.text

    # Returns info for current day if exists
    return info_str if info_date == str_today() else None


def init_session():
    # Init session
    s = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux ppc64le; rv:75.0) Gecko/20100101 Firefox/75.0',
    }
    s.headers.update(headers)
    return s


def do_login(session, user, pw):
    # get login page
    r = session.get(URL_LOGIN)
    soup = BeautifulSoup(r.text, 'html.parser')

    # send login form
    action = soup.form['action']
    payload = {'cto': user, 'pw': pw}
    return session.post(f'{URL_BASE}/{action}', data=payload)


def str_today():
    from datetime import date
    fecha = date.today()
    return fecha.strftime('%d-%m-%Y')
