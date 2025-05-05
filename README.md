# URL Shortener Service 

This project is a simple **URL Shortener** built using **FastAPI** and **MongoDB**. It allows you to:

- Generate a short code for a given URL
- Redirect to the original URL using the short code
- Update the destination of a short code
- Delete a short code

---

## 📁 Project Structure
Backend/
├── app/
│ ├── routes/
│ │ └── network.py # API endpoints
│ ├── config.py # Configuration (if needed)
│ ├── database.py # MongoDB connection and collection setup
│ ├── main.py # FastAPI app entry point
│ ├── models.py # Pydantic models/schemas
│ ├── services.py # Business logic for CRUD operations
│ └── utils.py # Utility functions (e.g. short code generator)


---

## 🛠️ Requirements

- Python 3.8+
- MongoDB (running locally or accessible remotely)

### Install dependencies

```bash
pip install -r requirements.txt

### How to Run the Project

cd Backend
uvicorn app.main:app --reload

http://127.0.0.1:8000/docs




###Notes 

Ensure MongoDB is running before starting the app.

You can customize the database URI and name in database.py.


