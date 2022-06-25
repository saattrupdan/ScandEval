"""Question-answering benchmark dataset."""

import logging
from typing import Dict, Optional

from datasets import Dataset
from transformers import DefaultDataCollator, PreTrainedTokenizerBase

from .benchmark_dataset import BenchmarkDataset
from .exceptions import InvalidBenchmark

logger = logging.getLogger(__name__)


class QABenchmark(BenchmarkDataset):
    """Question-answering benchmark dataset.

    Args:
        dataset_config (DatasetConfig):
            The dataset configuration.
        benchmark_config (BenchmarkConfig):
            The benchmark configuration.

    Attributes:
        dataset_config (DatasetConfig):
            The configuration of the dataset.
        benchmark_config (BenchmarkConfig):
            The configuration of the benchmark.
    """

    def _compute_metrics(
        self, predictions_and_labels: tuple, id2label: Optional[list] = None
    ) -> Dict[str, float]:
        """Compute the metrics needed for evaluation.

        Args:
            predictions_and_labels (pair of arrays):
                The first array contains the probability predictions and the second
                array contains the true labels.
            id2label (list or None, optional):
                Conversion of indices to labels. Defaults to None.

        Returns:
            dict:
                A dictionary with the names of the metrics as keys and the metric
                values as values.
        """
        raise NotImplementedError

    def _preprocess_data(self, dataset: Dataset, framework: str, **kwargs) -> Dataset:
        """Preprocess a dataset by tokenizing and aligning the labels.

        Args:
            dataset (HuggingFace dataset):
                The dataset to preprocess.
            kwargs:
                Extra keyword arguments containing objects used in preprocessing the
                dataset.

        Returns:
            HuggingFace dataset: The preprocessed dataset.
        """
        raise NotImplementedError

    def _load_data_collator(self, tokenizer: Optional[PreTrainedTokenizerBase] = None):
        """Load the data collator used to prepare samples during finetuning.

        Args:
            tokenizer (HuggingFace tokenizer or None, optional):
                A pretrained tokenizer. Can be None if the tokenizer is not used in the
                initialisation of the data collator. Defaults to None.

        Returns:
            HuggingFace data collator:
                The data collator.
        """
        return DefaultDataCollator(tokenizer)

    def _get_spacy_predictions_and_labels(self, model, dataset: Dataset) -> tuple:
        """Get predictions from SpaCy model on dataset.

        Args:
            model (SpaCy model):
                The model.
            dataset (HuggingFace dataset):
                The dataset.

        Returns:
            A pair of arrays:
                The first array contains the probability predictions and the second
                array contains the true labels.
        """
        raise InvalidBenchmark(
            "Evaluation of question-answering tasks "
            "for SpaCy models is not yet implemented."
        )