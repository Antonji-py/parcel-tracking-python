import requests
import json


class UpsParcel:
    def __init__(self, tracking_number):
        self.tracking_number = tracking_number

        self.get_data()

    def get_tracking_number(self):
        return self.tracking_number

    def get_data(self):
        response = requests.get(f"https://tracking.pb.com/api/{self.tracking_number}")

        self.json = json.loads(response.text)

    def get_latest_event(self):
        latest_event = self.json["trackingDataResponseList"][0]["currentStatus"]

        info = latest_event["eventDescription"]
        date = latest_event["eventDate"]
        time = latest_event["eventTime"]

        location_city = latest_event["eventLocation"]["city"]
        location_country = latest_event["eventLocation"]["country"]

        location = f"{location_city}, {location_country}"

        data = {
            "info": info,
            "date": date,
            "time": time,
            "location": location
        }

        return data

    def get_all_events(self):
        all_events = self.json["trackingDataResponseList"][0]["scanHistory"]
        data = []

        for event in all_events:
            info = event["eventDescription"]
            date = event["eventDate"]
            time = event["eventTime"]

            location_city = event["eventLocation"]["city"]
            location_country = event["eventLocation"]["country"]

            location = f"{location_city}, {location_country}"

            part_data = {
                "info": info,
                "date": date,
                "time": time,
                "location": location
            }

            data.append(part_data)

        return data

    def get_current_status(self):
        status = self.json["trackingDataResponseList"][0]["currentStatus"]["packageStatus"]

        return status

    def get_parcel_weight(self):
        weight = self.json["trackingDataResponseList"][0]["size"]["weight"]
        unit = self.json["trackingDataResponseList"][0]["size"]["weightUnit"]

        package_weight = f"{weight} {unit}"

        return package_weight

    def get_delivery_location(self):
        delivery_location = self.json["trackingDataResponseList"][0]["deliveryLocation"]

        return delivery_location

    def get_estimated_delivery_date(self):
        estimated_delivery_date = self.json["trackingDataResponseList"][0]["estimatedDeliveryDate"]

        if estimated_delivery_date == "":
            estimated_delivery_date = None

        return estimated_delivery_date

    def get_delivery_date(self):
        delivery_date = self.json["trackingDataResponseList"][0]["deliveryDate"]

        if delivery_date == "":
            delivery_date = None

        return delivery_date