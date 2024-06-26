import logging
from datasets import Dataset
from torch import nn

from .args import TrainingArguments


logger = logging.getLogger(__name__)


def evaluate(
        model: nn.Module,
        eval_set: Dataset,
        training_args: TrainingArguments,
        **kwargs,
):
    """Evaluate on eval dataset."""
