#!/usr/bin/python3

import json
import uuid
import time
from selenium.webdriver.support.ui import Select, WebDriverWait

# read in search
def search_settings_read():
    try:
        with open('settings/searches.json') as f:
            return(json.load(f))
    except Exception:
        return None

# read in dealer searches
def search_dealer_read():
    try:
        with open('settings/dealer_search.txt') as f:
            lines = f.readlines()
            lines = [line.rstrip() for line in lines]
            return(lines)
    except Exception:
        return None

# generate a uuid and trim it
def gen_unique():
    return str(uuid.uuid4()).split('-')[0]

def run_car_offer():
    settings = search_settings_read()
    car_offer = True if settings['car_offer'] == "yes" else False
    return car_offer


# put all info in the correct order
def format_entry(entry):
    car = []
    # vin
    car.append(entry[8])
    # year
    car.append(entry[0])
    # make/model
    car.append(entry[1])
    # mileage
    car.append(entry[3])
    # exterior color
    car.append(entry[6])
    # transmission
    car.append(entry[2])
    # drive
    car.append(entry[28])
    # engine
    car.append(entry[27])
    # leather
    car.append(entry[10])
    # moonroof
    car.append(entry[9])
    # navigation
    car.append(entry[11])
    # accident(carfax)
    car.append(entry[24])
    # accident(cargurus)
    car.append(entry[19])
    # dealer info
    car.append(entry[13])
    # price
    car.append(entry[4])
    # offer
    car.append(entry[29])
    # profit
    car.append("-")
    # name
    car.append(entry[15])
    # phone
    car.append(entry[14])
    # notes
    car.append("-")
    # car link
    car.append(entry[12])
    # dealership town
    car.append(entry[16])
    # disatnce from zip
    car.append(entry[17])
    # below/above mk
    car.append(entry[21])
    # fuel
    car.append(entry[26])
    # compare to mk
    car.append(entry[22])
    # interior
    car.append(entry[7])
    # days on cargurus
    car.append(entry[18])
    # title cargurus
    car.append(entry[20])
    # title carfax
    car.append(entry[25])
    # trim
    car.append(entry[23])
    return car

def get_prefix(search):
    model = search['model'] if search['model'] else ""
    make = search['make'] if search['make'] else ""
    if model:
        prefix = "{}".format(model)
    elif make:
        prefix = "{}".format(make)
    else:
        prefix = "all"
    return(prefix)

def get_dealer_name(search):
    try:
        prefix = search.strip('https://www.cargurus.com/Cars/m-')
    except Exception:
        prefix = None
    return prefix

def check_get_key(dict, key):
    if key in dict.keys():
        return dict[key]
    else:
        return ""

def fancysleep(secs):
    for i in range(secs, 0, -1):
        print(f"Sleeping: {i}", end="\r", flush=True)
        time.sleep(1)

def wait_for_page_to_load(driver, timeout=30):
    WebDriverWait(driver, timeout).until(lambda driver: driver.execute_script('return \
        document.readyState') == 'complete')

def select_from_drop_down(driver, element, text):
    _find = driver.find_element_by_id(element)
    _find.click()
    _select = Select(_find)
    _select.select_by_visible_text(text)
