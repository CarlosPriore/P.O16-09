class Aluno:
    """Representa um aluno no sistema acadêmico."""

    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        self.notas: list[float] = []
        

    def adicionar_nota(self, nota: float) -> None:
        """Adiciona uma nota à lista de notas do aluno."""

        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print(f"Nota Somente Permitida a Parmera")


     def calcular_media(self) -> float:
        """Calcular a media das notas"""

        return sum(self.notas) / len(self.notas) if self.notas else 0.0


    def situacao(self) -> str:
        """Retorna a situação de aprovado ou reprovado doaluno"""

        media = self.calcular_media()
        return "Aprovadoo" if media >=7.0 else "Se Fudeu"




    aluno1 = Aluno("Fulano", 20)
    aluno1.adicionar_nota(8)
    aluno1.adicionar_nota(9)
    aluno1.adicionar_nota(10)