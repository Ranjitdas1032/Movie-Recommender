# 🎬 Movie Recommender

**Movie Recommender** is a Django-based full-stack web application that allows users to sign up, log in, explore movies, and view detailed movie metadata such as cast, director, box office collection, and critical ratings like Rotten Tomatoes. Built with a structured database and scalable architecture, it provides a smooth and interactive user experience.

---

## 🚀 Features

- 🔐 **User Authentication**: Signup, Login, Logout
- 🎥 **Movie Listings**: Browse a curated list of movies with posters and release dates
- 🧠 **Detailed Movie Insights**:
  - 🎭 Cast & Director
  - 💰 Box Office Collections
  - 🍅 Rotten Tomatoes Ratings
- 💬 **User Comments**: Registered users can leave comments on movies
- 📁 **Efficient Data Modeling**: Built using relational databases for maintainability and scalability

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (can be upgraded to PostgreSQL/MySQL)
- **Version Control**: Git, GitHub

---

## 📊 Database Design

This project uses a well-structured ER model with multiple relationships to manage movies, users, and metadata efficiently.

### 🗂️ Core Tables

#### 🎞️ `Movies`
- Name, Poster, Date of Release
- Category, Director ID, Box Office Collection
- Rating ID, Actors ID, Rotten Tomatoes references

#### 👤 `User`
- User ID, Name, Email, Password
- Can write multiple comments

#### 👨‍🎤 `Actors`
- Actor ID, Name, Gender, Total Movies
- Many-to-many relation with movies via `Role`

#### 🎬 `Director`
- Director ID, Name
- One-to-many relation with Movies

#### 💬 `Comments`
- Comment ID, Content, User ID
- Linked to both Movie and User

#### 🏷️ `Category`
- Category ID, Type (e.g., Action, Drama)

#### ⭐ `Rating`
- Rating ID, Type (e.g., PG-13, R)

#### 🍅 `Rotten Tomatoes`
- ActorsID, RatingID, Score Type

### 🔄 Relationships

- `Movies` ↔ `Actors`: Many-to-Many via `Role`
- `Movies` ↔ `Director`: One-to-Many
- `Movies` ↔ `Rating`, `Category`, `Rotten Tomatoes`: Many-to-One
- `Users` ↔ `Comments` ↔ `Movies`: One-to-Many (both directions)

>![ER Diagram](https://raw.githubusercontent.com/Ranjitdas1032/Movie-Recommender/main/static/images/ERdiagram.png)

---

## 🧪 Installation & Setup

1. **Clone the repo**:
   ```bash
   git clone https://github.com/Ranjitdas1032/Movie-Recommender.git
   cd Movie-Recommender
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Start the development server:

bash
Copy
Edit
python manage.py runserver
📷 Screenshots
(Add screenshots of movie listings, detail view, and user login here)

📈 Future Enhancements
🔍 Search, filters, and sorting

🎞️ Trailer embedding (YouTube, etc.)

🤖 AI-based movie recommendation engine

🌐 Third-party API integration (IMDb, TMDB)

📱 Mobile responsive UI

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

📬 Contact
Ranjit Das
📧 ranjitdas1032@gmail.com
🔗 LinkedIn
💻 GitHub

📝 License
This project is licensed under the MIT License.
