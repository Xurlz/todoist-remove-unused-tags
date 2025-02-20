# -*- coding: utf-8 -*-

import pytest
import os
from ttc import TodoistUnusedTagsRemover
from ttc import Token
import requests


class MockResponse:
    text = open('mock-response-text.json','r').read()

def test_getallprojects_response(monkeypatch,capsys):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

    monkeypatch.setenv('TODOIST_API_TOKEN', 'foo')

  
    assert TodoistUnusedTagsRemover().getAllProjects() == open('projects-expected-response.json','r').read()

def test_main_method(monkeypatch,capsys):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

    monkeypatch.setenv('TODOIST_API_TOKEN', 'foo')
    TodoistUnusedTagsRemover().main()
    assert capsys.readouterr().out == open('main-expected-stdout.txt','r').read()

test_data = [
    ('foo',{'Authorization':'Bearer foo'}),
    ('bar',{'Authorization':'Bearer bar'})
]

@pytest.mark.parametrize('api_token,expected',test_data)
def test_gettoken_method(monkeypatch,api_token,expected):
    monkeypatch.setenv('TODOIST_API_TOKEN', api_token)

    result = TodoistUnusedTagsRemover().getToken()

    assert type(result) is Token
    assert result.toDict() == expected


