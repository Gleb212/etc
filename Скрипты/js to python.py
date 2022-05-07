import js2py

tmp = """var SpeechRecognition = new (window.SpeechRecognition || window.webkitSpeechRecognition || window.mozSpeechRecognition || window.msSpeechRecognition)();"""

js2py.eval_js(tmp)
