

'''2GISNavigationSimplifier prints out duration and length of your route.
The input is: lat and lon of point 1 then lat and lon of point 2.
Works with pedestrians and transport.
If 2 gis changes their website code it wont be working, maybe it already happened. I dunno'''

import requests

def get_transport_duration_by_2_points(lat1: float, lon1: float, lat2: float, lon2: float):

    public_transport_url = 'https://catalog.api.2gis.ru/ctx/2.0/moscow?key=rurbbn3446'

    json_payload = f'{{"locale":"ru","enable_schedule":false,"source":{{"point"\
:{{"lat":{lat1},"lon":{lon1}}}, "name":"Source"}},"target":{{"point":{{"lat"\
:{lat2},"lon":{lon2}}},"name":"Target"}},"transport":["bus","trolleybus","tram"\
,"shuttle_bus","metro","suburban_train","funicular_railway","monorail",\
"river_transport","cable_car","light_rail","premetro","light_metro","aeroexpress"\
,"pedestrian","mcc","mcd"],"purpose":"routeSearch"}}'
    response = requests.post(public_transport_url, json_payload).json()
    return response[0].get('total_duration')


def get_pedestrian_duration_by_2_points(lat1: float, lon1: float, lat2: float, lon2: float):

    pedestrian_url = 'https://catalog.api.2gis.ru/pedestrian/4.0.0/moscow?key=rurbbn3446'

    json_payload = f'{{"locale":"ru","point_a_name":"Source","point_b_name":"Target"\
,"points":[{{"type":"pedo","x":{lon1},"y":{lat1},"object_id":""}},{{"type":"pedo","x"\
:{lon2},"y":{lat2},"object_id":""}}],"type":"pedestrian","purpose":"autoSearch"}}'
    response = requests.post(pedestrian_url, json_payload).json()
    return response.get('result')[0].get('total_duration')


def get_pedestrian_length_by_2_points(lat1: float, lon1: float, lat2: float, lon2: float):

    pedestrian_url = 'https://catalog.api.2gis.ru/pedestrian/4.0.0/moscow?key=rurbbn3446'

    json_payload = f'{{"locale":"ru","point_a_name":"Source","point_b_name":"Target"\
,"points":[{{"type":"pedo","x":{lon1},"y":{lat1},"object_id":""}},{{"type":"pedo","x"\
:{lon2},"y":{lat2},"object_id":""}}],"type":"pedestrian","purpose":"autoSearch"}}'
    response = requests.post(pedestrian_url, json_payload).json()
    return response.get('result')[0].get('total_distance')

