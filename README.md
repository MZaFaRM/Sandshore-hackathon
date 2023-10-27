# Sandshore-hackathon

This is the Backend Django project of [Basith-P's](https://github.com/Basith-P/) [Empman](https://github.com/Basith-P/Empman) that provides a REST API for managing employees made within a day and a bit more as part of my attempt at [Codestorm Hackathon](devfolio.co/gta-sandshores/) organised by [μLearn Foundation](https://mulearn.org/).

This project at the time of writing this readme is live at [PythonAnywhere](http://muhammedzafar.pythonanywhere.com/).

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MZaFaRM/Sandshore-hackathon.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Make database migrations:

```bash
python manage.py makemigrations
```

4. Apply database migrations:

```bash
python manage.py migrate
```

## Usage

1. Start the development server:

```bash
python manage.py runserver
```

2. Access the API at `http://localhost:8000/api/`.

## API Endpoints

### Departments

- `GET /api/departments/`: Retrieve all departments
- `GET /api/departments/{id}/`: Retrieve a single department
- `POST /api/departments/`: Create a new department
- `PUT /api/departments/{id}/`: Update an existing department
- `DELETE /api/departments/{id}/`: Delete an existing department

### Employees

- `GET /api/employees/`: Retrieve all employees
- `GET /api/employees/{id}/`: Retrieve a single employee
- `POST /api/employees/`: Create a new employee
- `PUT /api/employees/{id}/`: Update an existing employee
- `DELETE /api/employees/{id}/`: Delete an existing employee

## Contributing

Contributions are always welcome! If you have any suggestions or find any bugs, please open an issue or a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django REST framework](https://www.django-rest-framework.org/)
- [MySQL](https://mysql.com/)