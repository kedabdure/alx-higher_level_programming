# ALX - Higher Level Programming 🚀

Welcome to the **Higher Level Programming** track at ALX! This repository marks the transition from low-level systems programming to the world of high-level abstraction. Here, programs are shorter, more expressive, and powered by interpreters.

This journey covers **Python**, **SQL**, **JavaScript**, **C**, and **Shell scripting**, focusing on Object-Oriented Programming (OOP), Data Structures, and Database Integration.

---

## 🛠️ Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![SQL](https://img.shields.io/badge/sql-%2300758F.svg?style=for-the-badge&logo=mysql&logoColor=white)
![Shell Script](https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white)
![C](https://img.shields.io/badge/c-%2300599C.svg?style=for-the-badge&logo=c&logoColor=white)

---

## 📚 Project Roadmap

### 🐍 Python Fundamentals & Data Structures
Mastering the core of Python, from basic syntax to complex data management.

| Project | Highlights |
| :--- | :--- |
| **[0x00-Hello World](./0x00-python-hello_world)** | First steps: formatting output and string manipulation. |
| **[0x01-If/Else & Loops](./0x01-python-if_else_loops_functions)** | Logic flow control and the introduction of Python functions. |
| **[0x02-Import/Modules](./0x02-python-import_modules)** | Code modularity and reusability through script imports. |
| **[0x03-Data Structures](./0x03-python-data_structures)** | Working with Lists, Stacks, Queues, and Tuples. |
| **[0x04-Advanced Data](./0x04-python-more_data_structures)** | Sets, Dictionaries, and functional programming (Map, Filter, Lambda). |
| **[0x05-Exceptions](./0x05-python-exceptions)** | Robust error handling using built-in and custom exceptions. |

### 🏛️ Object-Oriented Programming (OOP)
Organizing code through data encapsulation, abstraction, inheritance, and polymorphism.

*   **[0x06-Python Classes](./0x06-python_classes)**: The blueprint of OOP—Attributes and Methods.
*   **[0x07-Test Driven Development](./0x07-python-test_driven_development)**: Using the `doctest` module to verify logic before implementation.
*   **[0x08-More Classes](./0x08-python-more_classes)**: Advanced practice with class structures.
*   **[0x09-Everything is an Object](./0x09-python-everything_is_object)**: Understanding how Python treats every piece of data.
*   **[0x0A-Inheritance](./0x0A-Python-Inheritance)**: Implementing Parent/Super classes and Subclasses.
*   **[0x0C-Almost a Circle](./0x0C-python-almost_a_circle)**: The ultimate review project—covering JSON, Unittests, Class Methods, and Serialization.

### 💾 Databases & Persistence
Bridging the gap between Python and Structured Data.

*   **[0x0D-SQL Introduction](./0x0D-SQL_introduction)**: Deep dive into MySQL, DDL/DML, Joins, and Relational Database design.
*   **[0x0F-Object Relational Mapping](./0x0F-python-object_relational_mapping)**: The evolution from raw SQL queries (`MySQLdb`) to Object-Oriented database management (`SQLAlchemy`).

> **Comparison: Raw SQL vs ORM**
> ```python
> # Without ORM (Raw SQL)
> cur.execute("SELECT * FROM states ORDER BY id ASC")
> 
> # With ORM (Pythonic)
> session.query(State).order_by(State.id).all()
> ```

### 🌐 Web & JavaScript
Expanding into the interactivity of the web.

*   **[0x12-JavaScript Warm-up](./0x12-javascript-warm_up)**: Syntax basics, scope (`var`, `let`, `const`), and control structures.
*   **[0x13-JS Objects & Closures](./0x13-javascript_objects_scopes_closures)**: Mastering Prototypes, Closures, and the `this` keyword.
*   **[0x10 & 0x11-Networking](./0x10-python-network_0)**: Exploring HTTP, Cookies, and URL fetching with `urllib` and `curl`.

---

## 📂 Repository Structure
*   **Python Scripts**: Found in `0x00` through `0x0F` (and networking).
*   **SQL Scripts**: Found in `0x0D`.
*   **JS Scripts**: Found in `0x12` and `0x13`.
*   **Documentation**: Includes `README.md` for each project directory detailing specific tasks.

## 🚀 Getting Started
To run any of these programs, clone the repository and ensure you have the required interpreters (Python 3, Node.js, MySQL) installed.

```bash
git clone https://github.com/your_username/alx-higher_level_programming.git
cd alx-higher_level_programming
