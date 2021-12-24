from typing import Any, List, Optional 

from pydantic import BaseModel
from classification_model.processing.validation import BettingDataInputSchema


class PredictionResults(BaseModel):
    errors: Optional[Any]
    version: str 
    predictions: Optional[List[bool]]
    probabilities: Optional[List[float]]


class MultipleBettingDataInputs(BaseModel):
    inputs: List[BettingDataInputSchema]

    class Config:
        schema_extra = {
            "example": {
                "inputs": [
                   {
                       'q1_diff': -9,
                        'q2_diff': -18,
                        'q3_diff': -9,
                        'improved_score': True,
                        'score_change': 6,
                        'q1_first': False,
                        'q1_second': False,
                        'q2_first': False,
                        'q2_second': False,
                        'q3_first': True,
                        'q3_second': True,
                        'avg_score_diff': -9.793893129770993,
                        'max_score_diff_pos': 1,
                        'max_score_diff_neg': -19,
                        'pct_3p': 0.4827586206896552,
                        'pct_fg': 0.5238095238095238,
                        'pct_3p_reg': 0.1,
                        'pct_fg_reg': 0.05,
                        'underdog_odds': 2.0,
                        'p1_plays': False,
                        'p2_plays': False,
                        'p3_plays': False
                    }
                ]
            }
        }
