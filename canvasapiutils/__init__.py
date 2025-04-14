# canvasapi_addon/__init__.py

from canvasapi import Canvas
import datetime
import requests
import os

def print_obj(obj):
    for name in obj.__dict__:
        if name != 'attributes':
            print(name, ":", getattr(obj, name))

def print_dict(dic):
    for key, value in dic.items():
        print(key, ":", value)

def get_date_from_string(date_string):
    if date_string is None:
        return None
    date_string = date_string.replace("T", "-")
    date_data = date_string.split("-")
    time_data = date_data[3].split(":")
    return datetime.datetime(int(date_data[0]), int(date_data[1]), int(date_data[2]), int(time_data[0]), int(time_data[1]))

def get_days_ago(past_date, present_date=datetime.datetime.now()):
    return (present_date - past_date).days

def get_current_academic_year():
    now = datetime.datetime.now()
    year = now.year
    if now.month < 7:
        year -= 1
    return year

def get_enrollment_term_ids(canvas, years):
    term_id_list = []
    if isinstance(years, (int, str)):
        years = [years]

    terms = canvas.get_account(3).get_enrollment_terms()
    for term in terms:
        for year in years:
            if str(year) in term.name:
                term_id_list.append(term.id)
    return term_id_list

def canvas_get(url, req_data, page=1, res_data=None):
    if res_data is None:
        res_data = []

    req_data['per_page'] = 100
    req_data['page'] = page

    response = requests.get(url, params=req_data)
    if response.status_code == 200:
        data = response.json()
        res_data.extend(data)

        link_header = response.headers.get('Link', None)
        if link_header:
            next_link = next((link for link in link_header.split(',') if 'rel="next"' in link), None)
            if next_link:
                next_page = int(next_link[next_link.find('page=') + 5:next_link.find('&')])
                return canvas_get(url, req_data, next_page, res_data)

    return res_data

def init_canvas(api_key=None, url=None):
    if api_key is None:
        api_key = os.getenv("CANVAS_API_KEY")
    if not api_key:
        raise ValueError("CANVAS_API_KEY is not set.")

    if url is None:
        url = os.getenv("CANVAS_API_URL")
    if not url:
        raise ValueError("CANVAS_API_URL is not set.")
    return Canvas(url, api_key)

__all__ = [
    'print_obj', 'print_dict', 'get_date_from_string', 'get_days_ago',
    'get_current_academic_year', 'get_enrollment_term_ids', 'canvas_get', 'init_canvas'
]
