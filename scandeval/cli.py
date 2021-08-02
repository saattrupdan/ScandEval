'''Command-line interface for benchmarking'''

import click
from typing import Tuple

from .benchmark import Benchmark


@click.command()
@click.option('model_id', '-m',
              default=None,
              show_default=True,
              multiple=True,
              help='The HuggingFace model ID of the model(s) to be '
                   'benchmarked. If not specified then all models will be '
                   'benchmarked, filtered by `language` and `task`.')
@click.option('--dataset', '-d',
              default=None,
              show_default=True,
              multiple=True,
              help='The name of the benchmark dataset. If not specified then '
                   'all datasets will be benchmarked.')
@click.option('--language', '-l',
              default=['da' ,'sv', 'no'],
              show_default=True,
              multiple=True,
              help='The languages to benchmark. Only relevant if `model_id` '
                   'is not specified.')
@click.option('--task', '-t',
              default=['fill-mask',
                       'token-classification',
                       'text-classification'],
              show_default=True,
              multiple=True,
              help='The tasks to benchmark. Only relevant if `model_id` '
                   'is not specified.')
@click.option('--num_finetunings', '-n',
              default=10,
              show_default=True,
              help='The number of times a language model should be '
                   'finetuned.')
@click.option('--verbose', '-v',
              is_flag=True,
              show_default=True,
              help='Whether extra input should be outputted during '
                   'benchmarking')
def benchmark(model_id: Tuple[str],
              dataset: Tuple[str],
              language: Tuple[str],
              task: Tuple[str],
              num_finetunings: int,
              verbose: bool = False):
    '''Benchmark language models on Scandinavian language tasks.'''
    benchmarker = Benchmark(languages=language, tasks=task, verbose=verbose)
    benchmarker(model_ids=None if len(model_id) == 0 else model_id,
                datasets=None if len(dataset) == 0 else dataset,
                num_finetunings=num_finetunings)