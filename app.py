from flask import Flask, request, send_from_directory

app = Flask(__name__)

@app.route('/')
def formulario():
    return send_from_directory('.', 'Formulario.html')

@app.route('/examen', methods=['POST'])
def examen():
    datos = request.form.to_dict()

    print("Datos recibidos:")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

    with open("file.csv", "a", encoding="utf-8") as f_csv, open("file.txt", "a", encoding="utf-8") as f_txt:
        fila = ",".join([f'{valor}' for valor in datos.values()]) + "\n"
        f_csv.write(fila)
        f_txt.write(fila)

    return "Datos recibidos y guardados correctamente."

if __name__ == '__main__':
    app.run(debug=True)
