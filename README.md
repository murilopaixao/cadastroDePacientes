# cadastroDePacientes

## Instalação 

```bash
git clone git@github.com:murilopaixao/cadastroDePacientes.git
cd cadastroDePacientes
python -m venv venv
source venv/bin/activate
pip -r requirements.txt
```

```bash
cat <<EOF | tee .env
FLASK_APP=app
FLASK_DEBUG=1
FLASK_RUN_PORT=5000
FLASK_RUN_HOST=0.0.0.0
EOF
```

## Iniciando o projeto

```bash
source venv/bin/activate
flask run
```

http://localhost:5000