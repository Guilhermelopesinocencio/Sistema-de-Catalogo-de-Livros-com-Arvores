class Livro:
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"[{self.id}] {self.titulo} - {self.autor}"
