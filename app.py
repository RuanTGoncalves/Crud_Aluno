from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos armazenada na memória (sem banco de dados)
produtos = []
proximo_id = 1


@app.route('/')
def listar():
    return render_template('listar.html', produtos=produtos)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        global proximo_id

        nome = request.form['nome']
        categoria = request.form['categoria']
        preco = request.form['preco']
        quantidade = request.form['quantidade']

        produto = {
            'id': proximo_id,
            'nome': nome,
            'categoria': categoria,
            'preco': preco,
            'quantidade': quantidade
        }

        produtos.append(produto)
        proximo_id += 1

        return redirect(url_for('listar'))

    return render_template('adicionar.html')


@app.route('/editar/<int:produto_id>', methods=['GET', 'POST'])
def editar(produto_id):
    produto = None
    for p in produtos:
        if p['id'] == produto_id:
            produto = p
            break

    if produto is None:
        return redirect(url_for('listar'))

    if request.method == 'POST':
        produto['nome'] = request.form['nome']
        produto['categoria'] = request.form['categoria']
        produto['preco'] = request.form['preco']
        produto['quantidade'] = request.form['quantidade']

        return redirect(url_for('listar'))

    return render_template('editar.html', produto=produto)


@app.route('/remover/<int:produto_id>')
def remover(produto_id):
    for p in produtos:
        if p['id'] == produto_id:
            produtos.remove(p)
            break

    return redirect(url_for('listar'))


if __name__ == '__main__':
    app.run(debug=True)
