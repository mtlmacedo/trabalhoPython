No Windows:

    python -m venv venv
    venv\Scripts\activate
    pip install flask transformers torch pillow
No macOS/Linux:

    python3 -m venv venv
    source venv/bin/activate

    pip install flask transformers torch pillow

Com o ambiente virtual ativado e as dependências instaladas, execute o servidor Flask:

    python app.py

O servidor Flask será iniciado e estará disponível em http://localhost:5000.
