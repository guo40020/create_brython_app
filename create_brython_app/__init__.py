import os
import shutil


def main():
    app_name = input('App name[new_app]: ')
    if app_name == '' or '\\' in app_name or '/' in app_name:
        app_name = 'new_app'
    os.mkdir(app_name)
    os.chdir(app_name)
    os.mkdir('static')
    os.mkdir('eel')

    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(current_path, 'template.html'), 'r') as html:
        html_template = html.read()
        html_template = html_template.replace('{{app_name}}', app_name)
        with open('static/index.html', 'w') as index:
            index.write(html_template)
    shutil.copy(os.path.join(current_path, 'brython.min.js'), 'static')
    shutil.copy(os.path.join(current_path, 'brython_stdlib.js'), 'static')
    shutil.copy(os.path.join(current_path, 'eel.js'), 'eel')
    with open('main.py', 'w') as main:
        main.write('import eel\n\n\neel.init(\'static\')\neel.start(\'index.html\')')
