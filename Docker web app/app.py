from flask import Flask
from flask import render_template
from flask import request
from docker import *

app = Flask('menu')
app.static_folder = 'static'


@app.route('/')
def home():
    return render_template('docker.html')

@app.route('/docker')
def docker():
    return render_template('docker.html')


@app.route('/docker-static-output', methods=['GET'])
def docker_static_output():
    y = request.args.get('option')
    if y=='1':
        output = doc_version()
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif y=='2':
        return render_template('op-input.html', x='2', input=2, input1=['IMAGE NAME', 'CONTAINER NAME'], input2=['image', 'name'], title='Details')
    elif y=='3':
        return render_template('op-input.html', x='3', input=1, input1=['IMAGE NAME'], input2=['image'], title='Details')
    elif y=='4':
        output = docker_ps()
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif y=='5':
        output = docker_ps_all()
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif y=='6':
        output = docker_images()
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif y=='7':
        return render_template('op-input.html', x='7', input=1, input1=['CONTAINER NAME/ID'], input2=['name'], title='Details')
    elif y=='8':
        return render_template('op-input.html', x='8', input=1, input1=['CONTAINER NAME/ID'], input2=['name'], title='Details')
    elif y=='9':
        return render_template('op-input.html', x='9', input=1, input1=['CONTAINER NAME/ID'], input2=['name'], title='Details')
    elif y=='10':
        output = docker_rm_all()
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif y=='11':
        output = docker_stop_all()
        return render_template('default-op.html', op=output, title='OUTPUT')

@app.route('/docker-dynamic-op', methods=['GET'])
def docker_dynamic_op():
    x = request.args.get('x')
    if x=='2':
        image = request.args.get('image')
        name = request.args.get('name')
        output = docker_run(image, name)
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif x=='3':
        image = request.args.get('image')
        output = docker_pull(image)
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif x=='7':
        name = request.args.get('name')
        output = docker_start(name)
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif x=='8':
        name = request.args.get('name')
        output = docker_stop(name)
        return render_template('default-op.html', op=output, title='OUTPUT')
    elif x=='9':
        name = request.args.get('name')
        output = docker_rm(name)
        return render_template('default-op.html', op=output, title='OUTPUT')

app.run(debug=True)
