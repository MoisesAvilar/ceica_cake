# Projeto API Django RESTful

Este projeto é uma API Django RESTful para gerenciamento de clientes e vendas, com suporte a autenticação via JWT.

## Modelos

### Customer

O modelo `Customer` representa os clientes da aplicação.

- **name**: Nome do cliente.
- **phone_number**: Número de telefone do cliente no formato (XX) XXXXX-XXXX.
- **birthday**: Data de nascimento do cliente.
- **bought**: Total de compras realizadas pelo cliente.

### Sale

O modelo `Sale` representa as vendas realizadas na aplicação.

- **product**: Produto vendido;
- **product_description**: Descrição do produto (gerada automaticamente).
- **price**: Preço unitário do produto.
- **quantity**: Quantidade vendida.
- **customer**: Cliente associado à venda.
- **data_hour**: Data e hora da venda.
- **payment_status**: Status do pagamento (Pendente/Pago).
- **total**: Total da venda (calculado automaticamente).

## Autenticação JWT

A autenticação JWT (JSON Web Token) é utilizada para autenticar e autorizar solicitações na API.

## Como Utilizar

1. Clone este repositório.
2. Instale as dependências utilizando `pip install -r requirements.txt`.
3. Execute as migrações do banco de dados com `python manage.py migrate`.
4. Inicie o servidor de desenvolvimento com `python manage.py runserver`.

A API estará disponível em `http://localhost:8000/`.

## Rotas Disponíveis

- `/customers/`: Endpoint para listar e criar clientes.
- `/customers/<id>/`: Endpoint para detalhar, atualizar e excluir clientes.
- `/sales/`: Endpoint para listar e criar vendas.
- `/sales/<id>/`: Endpoint para detalhar, atualizar e excluir vendas.

Para utilizar os endpoints que requerem autenticação JWT, inclua o token JWT no cabeçalho `Authorization`.

## Requisitos do Sistema

- Python 3.x
- Django 3.x
- Django REST Framework
- JWT
- Outras dependências listadas em `requirements.txt`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um problema ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

