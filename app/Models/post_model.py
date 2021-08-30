from datetime import datetime 

class Post:
    def __init__(self, id: int, title: str, author: str, tags: list[str], content: str, updated_at: str = None):
        self._id = id
        self.created_at = datetime.utcnow()
        self.updated_at = updated_at
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content
               

    def __str__(self):
        return f"id: {self.id}, author: {self.author}, title: {self.title}, content: {self.content}, tags: {self.tags}"
   
    
    
