from .constants import DEFAULT_CONFIG
from . import utils
import datetime
import os
from inspect import getframeinfo, stack
import json

# load configs
config = DEFAULT_CONFIG

# upgrade configs to work with it
config = utils.upgrade_config(config)

def log(fn):
	def wrapper(message):
		d = fn(message)
		caller = getframeinfo(stack()[1][0])

		if config['level'] <= d['level']:
			for output in config[d['mode']]['outputs']:
				# log in console
				if output['type'] == 'console':
					print(utils.fill_template(
							config['log_template'], 
							caller, 
							d, 
							message, 
							output['style']
							))
	return wrapper

@log
def debug(message):
	d = {
		'mode': 'DEBUG',
		'level': 0
	}
	return d

@log
def info(message):
	d = {
		'mode': 'INFO',
		'level': 1
	}
	return d	

@log
def warning(message):
	d = {
		'mode': 'WARNING',
		'level': 2
	}
	return d

@log
def error(message):
	d = {
		'mode': 'ERROR',
		'level': 3
	}
	return d

@log
def critical(message):
	d = {
		'mode': 'CRITICAL',
		'level': 4
	}
	return d

@log
def info_forced(message):
	d = {
		'mode': 'INFO',
		'level': 99
	}
	return d

# FIX ME: use dlogging-light here
# info_forced('Current logging configuration is\n{}'.format(json.dumps(config, indent=2)))
