#!/usr/bin/env python3
"""
This is an example to train a task with ERWR algorithm.

Here it runs CartpoleEnv on ERWR with 100 iterations.

Results:
    AverageReturn: 100
    RiseTime: itr 34
"""
from garage.baselines import LinearFeatureBaseline
from garage.tf.algos import ERWR
from garage.tf.envs import TfEnv
from garage.tf.policies import CategoricalMLPPolicy
from garage.runners import LocalRunner

with LocalRunner() as runner:
    env = TfEnv(env_name="CartPole-v1")

    policy = CategoricalMLPPolicy(
        name="policy", env_spec=env.spec, hidden_sizes=(32, 32))

    baseline = LinearFeatureBaseline(env_spec=env.spec)

    algo = ERWR(
        env=env,
        policy=policy,
        baseline=baseline,
        max_path_length=100,
        discount=0.99)

    runner.setup(algo=algo, env=env)

    runner.train(n_epochs=100, batch_size=10000, plot=True)
