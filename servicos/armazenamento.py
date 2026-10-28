"""
Módulo de conexão com banco de dados analítico.
"""

class ConexaoArmazem:
    def __init__(self, host: str, porta: int, usuario: str):
        self.host = host
        self.porta = porta
        self.usuario = usuario
        self.conectado = False

    def conectar(self) -> str:
        if not self.host or not self.usuario:
            return "FALHA: Credenciais incompletas."
        self.conectado = True
        return f"CONECTADO: {self.usuario}@{self.host}:{self.porta}"
