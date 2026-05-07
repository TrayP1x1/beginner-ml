from dataclasses import dataclass

@dataclass
class ScoreRow:
    name: str
    math_score: float
    python_score: float

    @property
    def average_score(self) -> float:  
        return (self.math_score + self.python_score) / 2
    
score = ScoreRow("menos", 7.5, 8.3)
print(score.average_score)