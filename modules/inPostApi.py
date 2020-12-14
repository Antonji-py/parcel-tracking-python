import requests
import json


class InPostParcel:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number

        self.get_data()

    def get_tracking_number(self):
        return self.tracking_number

    def get_data(self):
        headers = {"X-Requested-With": "XMLHttpRequest"}

        response = requests.get(f"https://inpost.pl/shipx-proxy/?number={self.tracking_number}", headers=headers)

        self.json = json.loads(response.text)

    def get_latest_event(self):
        latest_event = self.json["tracking_details"][0]

        info = latest_event["status"]
        date = latest_event["datetime"].split("T")[0]
        time = latest_event["datetime"].split("T")[1].split(".")[0]
        location = latest_event["agency"]

        data = {
            "info": info,
            "date": date,
            "time": time,
            "location": location
        }

        return data

    def get_all_events(self):
        all_events = self.json["tracking_details"]

        data = []

        for event in all_events:
            info = event["status"]
            date = event["datetime"].split("T")[0]
            time = event["datetime"].split("T")[1].split(".")[0]
            location = event["agency"]

            part_data = {
                "info": info,
                "date": date,
                "time": time,
                "location": location
            }

            data.append(part_data)

        return data

    def get_last_update_date(self):
        last_update = self.json["updated_at"]

        date = last_update.split("T")[0]
        time = last_update.split("T")[1].split(".")[0]

        data = {
            "date": date,
            "time": time
        }

        return data

    def get_parcel_size(self):
        size = self.json["custom_attributes"]["size"]

        return size

    def get_target_machine_code(self):
        target_machine = self.json["custom_attributes"]["target_machine_id"]

        return target_machine

    def get_dropoff_machine_code(self):
        dropoff_machine = self.json["custom_attributes"]["dropoff_machine_id"]

        return dropoff_machine

    def get_machine_description(self, machine_type):
        if machine_type == "dropoff":
            machine_type = "target_machine_detail"
        elif machine_type == "target":
            machine_type = "dropoff_machine_detail"

        machine_detail = self.json["custom_attributes"][machine_type]["location_description"]

        return machine_detail