import pytest
import requests
import json
import allure

#testing valid login
def test_login_valid(supply_url):
	url = supply_url + "/login/" 
	data = {'email':'eve.holt@reqres.in','password':'cityslicka'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 200, resp.text
	assert j['token'] == "QpwL5tke4Pnpja7X4", resp.text


#testing login with no password
def test_login_no_password(supply_url):
	url = supply_url + "/login/" 
	data = {'email':'test@test.com'}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing password", resp.text


# testing login with no email
def test_login_no_email(supply_url):
	url = supply_url + "/login/" 
	data = {}
	resp = requests.post(url, data=data)
	j = json.loads(resp.text)
	assert resp.status_code == 400, resp.text
	assert j['error'] == "Missing email or username", resp.text