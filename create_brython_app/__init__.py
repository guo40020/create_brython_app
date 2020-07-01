import os
import shutil


def create():
    app_name = input('App name[new_app]: ')
    if app_name == '' or '\\' in app_name or '/' in app_name:
        app_name = 'new_app'
    os.mkdir(app_name)
    os.chdir(app_name)
    os.mkdir('src')
    os.mkdir('src/python')
    os.mkdir('dependencies')
    os.mkdir('eel')

    current_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(current_path, 'template.html'), 'r') as html:
        html_template = html.read()
        html_template = html_template.replace('{{app_name}}', app_name)
        with open('src/index.html', 'w') as index:
            index.write(html_template)
    shutil.copy(os.path.join(current_path, 'brython.min.js'), 'dependencies')
    shutil.copy(os.path.join(current_path, 'brython_stdlib.js'), 'dependencies')
    shutil.copy(os.path.join(current_path, 'styleHelper.css'), 'dependencies')
    shutil.copy(os.path.join(current_path, 'tailwind.min.css'), 'dependencies')
    shutil.copy(os.path.join(current_path, 'eel.js'), 'eel')
    shutil.copy(os.path.join(current_path, 'demo.py'), 'src/python')
    shutil.copytree(os.path.join(current_path, 'browser'), 'src/python/browser')

    with open('main.py', 'w') as main:
        main.write(
'''import eel


eel.init('')
eel.start('src/index.html')'''
        )
