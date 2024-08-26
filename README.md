# python-rabitmq-template

this repo will be a template repo for python apps that use rabitmq as a message broker.

## repo structure

    ├── README.md
    ├── requirements.txt
    ├── src
    │   ├── __init__.py
    │   ├── app.py
    │   ├── consumer.py
    │   ├── producer.py
    │   └── rabbitmq.py
    └── tests
        ├── __init__.py
        ├── test_app.py
        ├── test_consumer.py
        ├── test_producer.py
        └── test_rabbitmq.py

## usage

1. Create a virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

3. Run the producer

   ```bash
   python src/producer.py
   ```

4. Run the consumer

   ```bash
   python src/consumer.py
   ```

5. Run tests
   ```bash
   pytest tests
   ```

## references

- [RabbitMQ](https://www.rabbitmq.com/)
- [pika](https://pika.readthedocs.io/en/stable/)
- [pytest](https://docs.pytest.org/en/stable/)
- [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/)
- [pytest-mock](
