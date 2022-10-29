import requests
import math
import h3
import os
import json
import sys
import jellyfish

THIS_FILE = os.path.dirname(os.path.abspath(__file__))
PROJ_FILE = os.path.abspath(os.path.join(THIS_FILE, "../"))
sys.path.insert(0, PROJ_FILE)

from database.db_methods import DbMethods

class FindPatners:
    def __init__(self, start_latitude, start_longitude, dest_latitude, dest_longitude) -> None:
        self.start_latitude = start_latitude
        self.start_longitude = start_longitude
        self.dest_latitude = dest_latitude
        self.dest_longitude = dest_longitude
        self.config = self._read_config()
        self.db = DbMethods()
        
    def _get_cached_route(self):
        if result := self.db.route_search_db(starting=(self.start_latitude, self.start_longitude), destination=(self.dest_latitude, self.dest_longitude),):
            print("Cached route")
            result_in_string = result[0][4]
            return json.loads(result_in_string)
        return False
    
    def _get_route(self) -> dict:
        result = self._get_cached_route()
        if not result:
            print("Not in Cached Route")
            url = f"https://maps.googleapis.com/maps/api/directions/json?origin={self.start_latitude}%2C{self.start_longitude}&destination={self.dest_latitude}%2C{self.dest_longitude}&key=AIzaSyBRCBv1g2bhMCxviR1JYWYicWIfHyQMVCQ"
            response = requests.request("GET", url=url, headers={}, data={})
            return response.json(), False
        return result, True
    
    def _read_config(self):
        path = f"{PROJ_FILE}/FindPatners/config.json"
        with open(path, "rb") as f:
            return json.load(f)
    
    def _distance(self, coords_1, coords_2):
        return h3.point_dist(coords_1, coords_2, unit="m")

    def _recursion(self, start_location, end_location):
        location = self._midpoint(start_location, end_location)
        if self._distance(start_location, location) < self._threshold:
            self.store.append(start_location)
        else:
            self._recursion(start_location, location)
        if self._distance(location, end_location) < self._threshold:
            self.store.append(location)
        else:
            self._recursion(location, end_location)
    
    def _traverse_route(self, route):
        _buffer_distance = 0
        try:
            _steps = route["routes"][0]["legs"][0]["steps"]
        except Exception as e:
            pass
        self._threshold = route["routes"][0]["legs"][0]["distance"]["value"] * 0.1
        for idx, _step in enumerate(_steps):
            if idx == 0:
                self.store.append(
                    (_step["end_location"]["lat"], _step["end_location"]["lng"])
                )
            if _buffer_distance > self._threshold:
                _buffer_distance = 0
                self.store.append(
                    (_step["start_location"]["lat"], _step["start_location"]["lng"])
                )
            if _step["distance"]["value"] < self._threshold / 2:
                _buffer_distance += _step["distance"]["value"]
            if (
                _step["distance"]["value"] > self._threshold / 2 and _step["distance"]["value"] < self._threshold
            ):
                _buffer_distance = 0
                self.store.append(
                    (_step["end_location"]["lat"], _step["end_location"]["lng"])
                )
            if _step["distance"]["value"] > self._threshold:
                _buffer_distance = 0
                self._recursion(
                    start_location=(
                        _step["start_location"]["lat"],
                        _step["start_location"]["lng"],
                    ),
                    end_location=(
                        _step["end_location"]["lat"],
                        _step["end_location"]["lng"],
                    ),
                )
                self.store.append(
                    (_step["end_location"]["lat"],
                    _step["end_location"]["lng"])
                )
        # checking for the end point
        if self.store[-1] != (route["routes"][0]["legs"][0]["end_location"]["lat"], route["routes"][0]["legs"][0]["end_location"]["lng"],):
            self.store.append(
                (
                    route["routes"][0]["legs"][0]["end_location"]["lat"],
                    route["routes"][0]["legs"][0]["end_location"]["lng"],
                )
            )
        if self.store[0] != (route["routes"][0]["legs"][0]["start_location"]["lat"], route["routes"][0]["legs"][0]["start_location"]["lng"],):
            self.store.insert(
                0,
                (
                    route["routes"][0]["legs"][0]["start_location"]["lat"],
                    route["routes"][0]["legs"][0]["start_location"]["lng"],
                ),
            )
            
    def _points_in_between(self) -> None:
        self.store = []
        route, boolean_val = self._get_route()
        if boolean_val:
            self.store = route
            return 
        self._traverse_route(route=route)
        self.store = [[x1, x2] for x1, x2 in self.store]
        self.db.route_insert_db(
            source=(self.start_latitude, self.start_longitude),
            destination=(self.dest_latitude, self.dest_longitude),
            list=str(self.store),
        )
        return
    
    def _midpoint(self, start_location, end_location):
        x1, y1 = start_location
        x2, y2 = end_location
        return round((x1 + x2) / 2, 6), round((y1 + y2) / 2, 6)

    def _get_cache_result(self, location, keyword):
        
        if cache := self.db.location_search_db(
            lat=location[0], log=location[1], keyword=keyword
        ):
            print("Getting the result from cache")
            filename = cache[0][3]
            with open(f"{PROJ_FILE}{filename}", "rb") as f:
                return json.load(f)
        else:
            return False
    
    def search(self, location, keywords) -> list:
        x, y = location
        total_filtered_results = []
        for keyword in keywords:
            filtered_results = []
            # implementing caching
            results = self._get_cache_result(
                location=location, keyword=keyword)
            if not results:
                print("Not in Cache")
                url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={x}%2C{y}&radius={self.config['radius']}&type=&keyword={keyword}&key=AIzaSyBRCBv1g2bhMCxviR1JYWYicWIfHyQMVCQ"
                response = requests.request("GET", url, headers={}, data={})
                results = response.json()
                print(results)
                filename_to_save = self._save_in_cache(
                    results=results, location=location, keyword=keyword
                )
                self.db.location_insert_db(
                    lat=location[0],
                    log=location[1],
                    keyword=keyword,
                    filename=filename_to_save,
                )

            # filtering the results < 5000 m
            for result in results["results"]:
                if (
                    int(
                        self._distance(
                            location,
                            (
                                result["geometry"]["location"]["lat"],
                                result["geometry"]["location"]["lng"],
                            ),
                        )
                    )
                    < self.config["filteration_radius"]
                ):
                    filtered_results.append(result)

            total_filtered_results.extend(filtered_results)

        return total_filtered_results
    
    def _get_keywords(self) -> list:
        return self.config["patner_types"]

    def _save_in_cache(self, results, location, keyword):
        filename = f"/cache_location_results/{location[0]}_{location[1]}_{keyword}.json"
        json_object = json.dumps(results, indent=4)
        with open(PROJ_FILE + filename, "w") as outfile:
            outfile.write(json_object)
        return filename
    
    def _find_patners_exist(self, search_results) -> list:
        finds = []
        for data in search_results:
            for our_patners in self.config["list_of_patners"]:
                sim = jellyfish.jaro_similarity(data["name"], our_patners)
                if sim > 0.8:
                    finds.append((data["name"], data["geometry"]["location"]))
        return finds
    def get_place(self) -> list:
        final_res = [] # Final Result to be returned
        keywords = self._get_keywords()
        self._points_in_between()
        for storage in self.store:
            search_res = self.search(location=(storage[0],storage[1]), keywords=keywords)
            if res := self._find_patners_exist(search_res):
                final_res.extend(res)
        return final_res

if __name__ == "__main__":
    obj = FindPatners(17.449146, 78.349206, 28.704400, 77.102500)
    print(obj.get_place())