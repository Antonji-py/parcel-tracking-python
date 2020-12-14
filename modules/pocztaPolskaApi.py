import requests

from bs4 import BeautifulSoup


class PocztaPolskaParcel:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number

        self.get_data()

    def get_tracking_number(self):
        return self.tracking_number

    def get_data(self):
        with requests.Session() as s:
            headers = {"X-Requested-With": "XMLHttpRequest"}

            s.get(f"https://emonitoring.poczta-polska.pl/?numer={self.tracking_number}")

            cookies = s.cookies.get_dict()
            phpsessid = cookies["PHPSESSID"]

            data = {
                "s": phpsessid,
                "n": self.tracking_number,
                "l": ""
            }

            response = s.post("https://emonitoring.poczta-polska.pl/wssClient.php", data=data, headers=headers)
            self.soup = BeautifulSoup(response.text, "lxml")

    def get_latest_event(self):
        tds = self.soup.find_all("td")

        latest_event = tds[-3:]
        timestamp = latest_event[1].text.split()

        info = latest_event[0].text.strip()
        date = timestamp[0]
        time = timestamp[1]
        location = latest_event[2].text.strip()

        data = {
            "info": info,
            "date": date,
            "time": time,
            "location": location
        }

        return data

    def get_all_events(self):
        tds = self.soup.find_all("td")
        all_events = tds[18:]

        data = []

        current_event = []
        count = 1
        for event in all_events:
            if count <= 3:
                current_event.append(event.text)
                count += 1
            else:
                current_event = []
                current_event.append(event.text)
                count = 2

            if count == 4:
                timestamp = current_event[1].split()

                info = current_event[0].strip()
                date = timestamp[0]
                time = timestamp[1]
                location = current_event[2].strip()

                part_data = {
                    "info": info,
                    "date": date,
                    "time": time,
                    "location": location
                }

                data.append(part_data)

        return data

    def get_posting_date(self):
        tds = self.soup.find_all("td")
        posting_date = tds[3].text

        return posting_date

    def get_delivery_service(self):
        tds = self.soup.find_all("td")
        service = tds[5].text

        return service

    def get_posting_post_office(self):
        tds = self.soup.find_all("td")
        posting_post = tds[11].text

        return posting_post

    def get_parcel_size(self):
        tds = self.soup.find_all("td")
        parcel_size = tds[13].text

        return parcel_size

    def get_parcel_weight(self):
        tds = self.soup.find_all("td")
        parcel_weight = tds[17].text

        return parcel_weight