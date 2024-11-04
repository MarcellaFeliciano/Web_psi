from database import get_connection


class Emprestimo:
    def __init__(self, user, book, data):
        self.user = user
        self.book = book
        self.data = data
        
    def save(self):
        conn = get_connection()
        conn.execute("INSERT INTO emprestimos(emp_user_id, emp_book_id, emp_data) values(?,?,?)", (self.user, self.book, self.data))
        conn.commit()
        conn.close()
        return True
    
    @classmethod
    def all(cls):
        conn = get_connection()
        emprestimos = conn.execute("SELECT * FROM emprestimos").fetchall()
        return emprestimos
    

