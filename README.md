# 🌐 Personal Portfolio Website

A personal portfolio website built with **HTML** and **CSS**, with **Bootstrap** used **only for error pages**, and **Django** for the backend.  
It showcases my work, experience, skills, and projects, along with a **custom-built contact form** that connects to the Django backend.

🚀 **Live Site:**  [Visit my portfolio](https://deepankar619.pythonanywhere.com/)

---

## 🚀 Features

- 🎨 **Modern UI** built with custom CSS  
- 📂 **Portfolio Sections**  
  - 🏠 **Home** – Introduction & landing page  
  - 👤 **About** – Personal details & background  
  - 💼 **Experience** – Work history & achievements  
  - 🛠️ **Skills** – Technical skills & tools  
  - 📑 **Projects** – Highlighted personal & professional projects  
  - ✉️ **Contact** – **Manually created form** with backend logic in `views.py`  
- ⚡ **Form Handling**  
  - ✔️ Saves valid submissions as objects in the database  
  - ❌ Rejects invalid data and renders **Bootstrap-based custom error pages**  
- ☁️ **Deployed online** using PythonAnywhere  

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (custom styling), Bootstrap (error pages only)  
- **Backend:** Django (Python)  
- **Database:** SQLite (default)  
- **Hosting:** PythonAnywhere  

---

## ⚙️ Setup Instructions

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/portfolio-website.git
   cd portfolio-website
2. **Create and activate a vitual environment**
   ```bash
   python -m venv venv
   # On Linux/Mac
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Apply database migrations**
   ```bash
   python manage.py migrate
5. **Start the development server**
   ```bash
   python manage.py runserver
6. **Open the website in your browser**
   http://127.0.0.1:8000/
   
---

## 📌 Roadmap / Future Improvements

- 🔄 Make website **fully responsive** using CSS and Bootstrap utilities  
- 📊 Add more detailed project descriptions with images & links  
- ✨ Enhance UI/UX with animations and smooth navigation  

---

✨ Feel free to fork this repo and use it as a base for your own portfolio!

