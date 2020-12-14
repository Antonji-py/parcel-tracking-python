from modules.dpdApi import DpdParcel
from modules.pocztaPolskaApi import PocztaPolskaParcel
from modules.upsApi import UpsParcel
from modules.inPostApi import InPostParcel


dpd_parcel = DpdParcel("TRACKING NUMBER")

latest_event = dpd_parcel.get_latest_event()
all_events = dpd_parcel.get_all_events()
cod_value = dpd_parcel.get_cod_value()


poczta_polska_parcel = PocztaPolskaParcel("TRACKING NUMBER")

latest_event = poczta_polska_parcel.get_latest_event()
all_events = poczta_polska_parcel.get_all_events()
posting_date = poczta_polska_parcel.get_posting_date()
delivery_service = poczta_polska_parcel.get_delivery_service()
posting_post_office = poczta_polska_parcel.get_posting_post_office()
parcel_size = poczta_polska_parcel.get_parcel_size()
poczta_polska_parcel.get_parcel_weight()


ups_parcel = UpsParcel("TRACKING NUMBER")

latest_event = ups_parcel.get_latest_event()
all_events = ups_parcel.get_all_events()
location = ups_parcel.get_delivery_location()
status = ups_parcel.get_current_status()
weight = ups_parcel.get_parcel_weight()
estimated = ups_parcel.get_estimated_delivery_date()
date = ups_parcel.get_delivery_date()


inpost_parcel = InPostParcel("TRACKING NUMBER")

latest_event = inpost_parcel.get_latest_event()
all_events = inpost_parcel.get_all_events()
description = inpost_parcel.get_machine_description("dropoff")
description = inpost_parcel.get_machine_description("target")
target_machine_code = inpost_parcel.get_target_machine_code()
dropoff_machine_code = inpost_parcel.get_dropoff_machine_code()
parcel_size = inpost_parcel.get_parcel_size()
last_update_date = inpost_parcel.get_last_update_date()