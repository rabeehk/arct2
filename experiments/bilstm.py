"""Baseline BiLSTM model."""
from util import training, experiments
from arct import bilstm


def run():
    args = training.Args(
        experiment_name=__name__.split('.')[-1],
        use_bert=False,
        tune_embeds=True,
        annealing_factor=0.1,
        num_train_epochs=20,
        train_batch_size=32)
    model_constructor = bilstm.BiLSTM
    grid_space = {
        'learning_rate': [
            0.3, 0.2, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04, 0.03],
        'dropout_prob': [0., 0.1],
        'hidden_size': [128, 256, 512]}
    experiments.run(
        args=args,
        model_constructor=model_constructor,
        data_loaders_constructor=bilstm.DataLoaders,
        grid_space=grid_space,
        n_experiments=20)
