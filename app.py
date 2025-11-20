from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'una_clave_secreta_muy_larga_y_compleja_1234567890'

@app.route('/')
def index():
    return render_template('index.html')

# gasto energetico
@app.route('/gastoenergetico', methods=['GET', 'POST'])
def gastoenergetico():
    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        edad = int(request.form['edad'])
        genero = request.form['genero']
        actividad = float(request.form['actividad'])

        if genero == 'hombre':
            tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
        else:
            tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)

        resultado = round(tmb * actividad, 2)
        tmb = round(tmb, 2)

        return render_template('gastoenergetico.html', tmb=tmb, resultado=resultado)

    return render_template('gastoenergetico.html')

@app.route('/calculadoras')
def calculadoras():
    return render_template('calculadoras.html')

# 💪 IMC
@app.route('/imc', methods=['GET', 'POST'])
def imc():
    resultado = None
    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura = float(request.form['altura']) / 100
        imc = peso / (altura ** 2)

        if imc < 18.5:
            estado = "Bajo peso"
        elif imc < 25:
            estado = "Normal"
        elif imc < 30:
            estado = "Sobrepeso"
        else:
            estado = "Obesidad"

        resultado = f"Tu IMC es {imc:.2f} ({estado})"
    return render_template('imc.html', resultado=resultado)

# 🔥 TMB
@app.route('/tmb', methods=['GET', 'POST'])
def tmb():
    resultado = None
    if request.method == 'POST':
        sexo = request.form['sexo']
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])
        edad = int(request.form['edad'])

        if sexo == "masculino":
            tmb = 88.36 + (13.4 * peso) + (4.8 * altura) - (5.7 * edad)
        else:
            tmb = 447.6 + (9.2 * peso) + (3.1 * altura) - (4.3 * edad)

        resultado = f"Tu TMB es {tmb:.2f} calorías/día"
    return render_template('tmb.html', resultado=resultado)

# 🏃‍♂ Gasto Calórico Total
@app.route('/gct', methods=['GET', 'POST'])
def gct():
    resultado = None
    if request.method == 'POST':
        tmb = float(request.form['tmb'])
        actividad = float(request.form['actividad'])
        gct = tmb * actividad
        resultado = f"Tu Gasto Calórico Total es {gct:.2f} calorías/día"
    return render_template('gct.html', resultado=resultado)

# ⚖ Peso Ideal
@app.route('/pesoideal', methods=['GET', 'POST'])
def pesoideal():
    resultado = None
    if request.method == 'POST':
        altura = float(request.form['altura']) / 100
        genero = request.form['genero']
        if genero == "masculino":
            peso_ideal = 22 * (altura ** 2)
        else:
            peso_ideal = 21 * (altura ** 2)
        resultado = f"Tu peso ideal aproximado es {peso_ideal:.1f} kg"
    return render_template('pesoideal.html', resultado=resultado)

# 🥗 Macronutrientes
@app.route('/macronutrientes', methods=['GET', 'POST'])
def macronutrientes():
    resultado = None
    if request.method == 'POST':
        calorias = float(request.form['calorias'])
        proteinas = (calorias * 0.3) / 4
        grasas = (calorias * 0.25) / 9
        carbohidratos = (calorias * 0.45) / 4
        resultado = f"Proteínas: {proteinas:.1f}g | Grasas: {grasas:.1f}g | Carbohidratos: {carbohidratos:.1f}g"
    return render_template('macronutrientes.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
