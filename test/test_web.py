import json
import os
import re
from contextlib import contextmanager
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union
from unittest import TestCase
from unittest.mock import patch

import yaml
from fastapi.testclient import TestClient
from pydantic import BaseModel, Extra

from crittercarousel.api.application import CritterApplication

FOLDER = os.path.dirname(__file__)

BASE_URL = "http://localhost:8888/api/v1"

class WebTestCaseInfo(BaseModel):
    description: str
    method: str
    resource: str
    expect_rc: int
    expect_data: Union[str, List, Dict]
    critter_dt: Optional[List[int]] = []
    event_dt: Optional[List[int]] = []
    status_dt: Optional[List[int]] = []

    class Config:
        extra = Extra.ignore

class WebTest(TestCase):
                
    def load_info(self, name, sequence=False):

        path = os.path.join(FOLDER, name)

        with open(path) as f:
            data = yaml.safe_load(f)

        if sequence:
            return [WebTestCaseInfo(**x) for x in data]
        
        return WebTestCaseInfo(**data)
    
    def api_request(self, client, info:WebTestCaseInfo):

        url = f"{BASE_URL}/{info.resource}"

        expect_data = info.expect_data

        expect_text = isinstance(expect_data, str)

        expect_list = isinstance(expect_data, list)

        expect_lines = re.split("\r?\n", expect_data if expect_text else json.dumps(expect_data, indent=4, sort_keys=True))

        response = client.request(method=info.method, url=url)

        actual_data = str(response.content, encoding="UTF-8") if expect_text else response.json()

        actual_lines = re.split("\r?\n", actual_data if expect_text else json.dumps(actual_data, indent=4, sort_keys=True))

        print()
        print(f"description: {info.description}")
        print(f"method:      {info.method}")
        print(f"resource:    {info.resource}")
        print(f"url:         {url}")
        print(f"actual_rc:   {response.status_code}")
        print(f"expect_rc:   {info.expect_rc}")
        print(f"actual_lines:")
        for line in actual_lines:
            print(f"    {line}")
        print(f"expect_lines:")
        for line in expect_lines:
            print(f"    {line}")
        print()


        self.assertEqual(response.status_code, info.expect_rc)

        if expect_text:
            self.assertEqual(actual_data, expect_data)
        elif expect_list:
            self.assertListEqual(actual_data, expect_data)
        else:
            self.assertDictEqual(actual_data, expect_data)

    def datetime_generator(self, reference_datetime, offset_list):

        for offset in offset_list:
            yield reference_datetime + timedelta(minutes=offset)
        while True:
            yield None

    @contextmanager
    def mock_datetime(self, path, side_effect):

        with patch(f"{path}.datetime") as mock_datetime:

            mock_datetime.now.side_effect = side_effect

            mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)

            yield mock_datetime

    def test_sequences(self):

        sequence_list = [
            "test_init",
            "test_users",
            "test_species",
            "test_critters",
            "test_events",
            "test_status",
            "test_lifecycle",
        ]

        critter_mock = "crittercarousel.api.services._spawn_critter_service"
        event_mock = "crittercarousel.api.services._post_event_service"
        status_mock = "crittercarousel.api.models._status_model"

        reference_datetime = datetime(year=2020, month=1, day=1, hour=0, minute=0, second=0)


        app = CritterApplication()
       
        client = TestClient(app, raise_server_exceptions=False)

        for test_sequence in sequence_list:

            info_list = self.load_info(f"{test_sequence}.yaml", sequence=True)

            for info in info_list:

                critter_datetimes = self.datetime_generator(reference_datetime, info.critter_dt)
                event_datetimes = self.datetime_generator(reference_datetime, info.event_dt)
                status_datetimes = self.datetime_generator(reference_datetime, info.status_dt)

                with self.mock_datetime(critter_mock, critter_datetimes):
                    with self.mock_datetime(event_mock, event_datetimes):
                        with self.mock_datetime(status_mock, status_datetimes):
                            self.api_request(client, info)
