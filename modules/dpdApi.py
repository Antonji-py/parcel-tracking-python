import requests

from bs4 import BeautifulSoup


class DpdParcel:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number

        self.get_data()

    def get_tracking_number(self):
        return self.tracking_number

    def get_data(self):
        headers = {"X-Requested-With": "XMLHttpRequest"}
        data = {
            "q": self.tracking_number,
            "typ": 1
        }

        find_package = requests.post("https://tracktrace.dpd.com.pl/findPackage", data=data, headers=headers)
        self.soup = BeautifulSoup(find_package.text, "lxml")

    def get_latest_event(self):
        trs = self.soup.find("tr")

        # for tr in trs:
        tds = trs.find_all("td")

        date = tds[0].text
        time = tds[1].text
        info = tds[2].text.strip().replace("\xa0", " ")
        location = tds[3].text

        data = {
            "info": info,
            "date": date,
            "time": time,
            "location": location
        }

        return data

    def get_all_events(self):
        trs = self.soup.find_all("tr")

        data = []

        for tr in trs:
            tds = tr.find_all("td")

            date = tds[0].text
            time = tds[1].text
            info = tds[2].text.strip().replace("\xa0", " ")
            location = tds[3].text

            part_data = {
                "info": info,
                "date": date,
                "time": time,
                "location": location
            }

            data.append(part_data)

        return data

    def get_cod_value(self):
        cod_value = " "

        cod_field = self.soup.find("span", {"class": "input input-text"})
        try:
            cod_value_list = cod_field.text.split()

            return cod_value.join(cod_value_list)
        except:
            return None