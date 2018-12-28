from time import gmtime, strftime
from inspect import getframeinfo, stack
import os
from .constants import STYLE_DICT, LOG_LEVELS_DICT

def style_list_to_str(style_list):
	if len(style_list) == 2:
		return '\33[{};{}m'.format(
			STYLE_DICT[style_list[0]], 
			STYLE_DICT[style_list[1]])
	elif len(style_list) == 1:
		return '\33[{}m'.format(STYLE_DICT[style_list[0]])
	else:
		return '\33[0m'

def upgrade_config(config):
	# convert style from words to codes
	for level in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
		for i in range(0, len(config[level]['outputs'])):
			if config[level]['outputs'][i]['type'] == 'console':
				config[level]['outputs'][i]['style'] = style_list_to_str(config[level]['outputs'][i]['style'])

	# rewrite logging level from enviromental variable
	try:
		config["level"] = os.getenv('LOGGING_LEVEL', 'DEBUG')
	except e:
		pass

	# convert level from word to number
	config["level"] = LOG_LEVELS_DICT[config["level"]]

	return config

def fill_template(template, caller, d, message, style):
	# fills template with actual values
	template = str(template)
	
	# add date
	while '{date}' in template:
		template = template.replace('{date}', strftime("%Y-%m-%d %H:%M:%S", gmtime()))

	# add file and line from where logging was called
	while '{file}' in template:
		template = template.replace('{file}', '{}:{}'.format(caller.filename, caller.lineno))

	# add logging mode like 'DEGUG'
	while '{mode}' in template:
		template = template.replace('{mode}', d['mode'])
		
	# add start text styling
	while '{style}' in template:
		template = template.replace('{style}', str(style))

	# add close text styling
	while '{endstyle}' in template:
		if style == '':
			template = template.replace('{endstyle}', '')
		else:
			template = template.replace('{endstyle}', '\33[0m')

	# add message
	while '{message}' in template:
		template = template.replace('{message}', message)

	return template