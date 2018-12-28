DEFAULT_CONFIG = {
  "log_template": "[{date}][{file}]{style}[{mode}]{endstyle} - {message}",
  "file_template": "{}:{}",
  "level": "DEBUG",
  "DEBUG": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold"
        ]
      }
    ]
  },
  "INFO": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold",
          "cyan"
        ]
      }    
    ]
  },
  "WARNING": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold",
          "yellow"
        ]
      }
    ]
  },
  "ERROR": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold",
          "red"
        ]
      }
    ]
  },
  "CRITICAL": {
    "outputs": [
      {
        "type": "console",
        "style": [
          "bold",
          "red_background"
        ]
      }
    ]
  }
}

STYLE_DICT = {
	"bold": "1",
	"cyan": "96",
	"yellow": "93",
	"red": "91",
	"red_background": "101"
}

LOG_LEVELS_DICT = {
	"DEBUG": 0,
	"INFO": 1,
	"WARNING": 2,
	"ERROR": 3,
	"CRITICAL": 4,
	"INFO_FORCED": 99
}