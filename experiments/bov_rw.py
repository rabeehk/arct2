"""Bag of Vectors model just matching reasons to warrants."""
from util import training, experiments
from arct import bov


def run():
    args = training.Args(
        experiment_name=__name__.split('.')[-1],
        use_bert=False,
        n_train_epochs=3,
        hidden_size=300,
        train_batch_size=32,
        tune_embeds=True,
        reduce_op='sum')
    model_constructor = bov.BOV_RW
    grid_space = {
        'learning_rate': [0.3, 0.2, 0.1, 0.09, 0.08],
        'dropout_prob': [0., 0.1]}
    experiments.run(
        args=args,
        model_constructor=model_constructor,
        data_loaders_constructor=bov.DataLoaders,
        grid_space=grid_space,
        n_experiments=20)
