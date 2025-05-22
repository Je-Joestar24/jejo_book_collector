# JEJO BOOK COLLECTOR

A modern web application for collecting and managing your favorite books. Built with Django and styled with custom CSS, this application provides a seamless experience for book enthusiasts to organize their reading collection.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

1. Clone the repository:
```bash
git clone https://Je-Joestar24/jejo_book_collector.git
cd jejo_book_collector
```

2. Create and activate virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

The application will be available at `http://localhost:8000`

## 📖 How to Use

### User Features

1. **Authentication**
   - Sign up for a new account
   - Log in to access your collection
   - Update your profile information

2. **Book Collection**
   - Search for books using the search bar
   - Add books to your collection
   - View your collected books
   - Remove books from your collection
   - View book details

3. **Recent Views**
   - Track your recently viewed books
   - Quick access to your last viewed books

4. **Profile Management**
   - View your profile information
   - Update your personal details
   - Change username and email

## 🛠️ Technologies Used

### Backend
- **Django**: Web framework
- **Python**: Programming language
- **SQLite**: Database (development)
- **Django ORM**: Database management

### Frontend
- **HTML5**: Markup language
- **CSS3**: Styling
  - Custom CSS with BEM methodology
  - CSS Grid and Flexbox for layouts
  - CSS Variables for theming
  - Responsive design
- **Semantic HTML**: For accessibility
- **ARIA Labels**: For better accessibility
- **javascript**: JS for Minor functionalities

### Features
- Responsive design
- Semantic HTML structure
- Accessibility support
- Clean and modern UI
- Efficient data management
- User authentication
- Book collection management
- Recent views tracking

## 🎨 Theme Colors

The application uses a carefully selected color palette:
- Primary Green: #7FB77E
- Primary Blue: #B1D7B4
- Primary Light: #F7F6DC
- Secondary Green: #90C8AC
- Secondary Blue: #C4DFAA
- Accent Pastel: #FFD9B7
- Text Dark: #2C3333
- Text Light: #F7F6DC

## 🔒 Security Features

- CSRF protection
- User authentication
- Secure password handling
- Protected routes
- Input validation

## 📱 Responsive Design

The application is fully responsive and works on:
- Desktop computers
- Tablets
- Mobile phones

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 👥 Authors

- Jejomar Parrilla - Initial work

## 🙏 Acknowledgments

- Django Documentation
- Google Books API
- All contributors and supporters
