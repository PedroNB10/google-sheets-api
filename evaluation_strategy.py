# evaluation_strategy.py
from abc import ABC, abstractmethod
import math

class EvaluationStrategy(ABC):
    @abstractmethod
    def evaluate(self, student_data):
        pass
    

class AttendanceEvaluation(EvaluationStrategy):
    def evaluate(self, missed_classes, total_classes):
        if missed_classes > total_classes * 0.25 and total_classes > 0:
            return 'Reprovado por Falta', 0
        return None, None

class GradeEvaluation(EvaluationStrategy):
    def evaluate(self, average):
        if average < 50:
            return 'Reprovado por Nota', 0
        elif 50 <= average < 70:
            return 'Exame Final', math.ceil(100 - average)
        else:
            return 'Aprovado', 0
