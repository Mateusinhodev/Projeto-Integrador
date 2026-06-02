# ==========================================
# CLASSE PROFESSOR
# ==========================================

class Professor:
    def __init__(self, id_professor, nome, email, senha_hash):
        self.id_professor = id_professor
        self.nome = nome
        self.email = email
        self.senha_hash = senha_hash

    def exibir_dados(self):
        print(f"Professor: {self.nome}")
        print(f"E-mail: {self.email}")


# ==========================================
# CLASSE DISCIPLINA
# ==========================================

class Disciplina:
    def __init__(self, id_disciplina, nome_disciplina, area_conhecimento):
        self.id_disciplina = id_disciplina
        self.nome_disciplina = nome_disciplina
        self.area_conhecimento = area_conhecimento

    def exibir_disciplina(self):
        print(f"Disciplina: {self.nome_disciplina}")
        print(f"Área: {self.area_conhecimento}")


# ==========================================
# CLASSE SERIE
# ==========================================

class Serie:
    def __init__(self, id_serie, nome_serie, nivel):
        self.id_serie = id_serie
        self.nome_serie = nome_serie
        self.nivel = nivel

    def exibir_serie(self):
        print(f"Série: {self.nome_serie}")
        print(f"Nível: {self.nivel}")


# ==========================================
# CLASSE ATIVIDADE
# ==========================================

class Atividade:
    def __init__(self, titulo, conteudo, metodologia,
                 objetivos, professor, disciplina, serie):
        
        self.titulo = titulo
        self.conteudo = conteudo
        self.metodologia = metodologia
        self.objetivos = objetivos

        # Relacionamentos
        self.professor = professor
        self.disciplina = disciplina
        self.serie = serie

    def exibir_atividade(self):
        print("\n===== ATIVIDADE =====")
        print(f"Título: {self.titulo}")
        print(f"Conteúdo: {self.conteudo}")
        print(f"Metodologia: {self.metodologia}")
        print(f"Objetivos: {self.objetivos}")
        print(f"Professor: {self.professor.nome}")
        print(f"Disciplina: {self.disciplina.nome_disciplina}")
        print(f"Série: {self.serie.nome_serie}")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

# Criando objetos
professor = Professor(
    1,
    "Idomeneu",
    "idomeneu@mail.com",
    "123456"
)

disciplina = Disciplina(
    1,
    "Física",
    "Ciências da Natureza"
)

serie = Serie(
    1,
    "2º Ano",
    "Ensino Médio"
)

atividade = Atividade(
    "Leis de Newton",
    "Estudo das três leis do movimento.",
    "Aula expositiva e resolução de exercícios.",
    "Compreender os princípios da mecânica clássica.",
    professor,
    disciplina,
    serie
)

# Executando métodos
atividade.exibir_atividade()