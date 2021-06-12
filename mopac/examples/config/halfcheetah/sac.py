params = {
    'type': 'SAC',
    'universe': 'gym',
    'domain': 'HalfCheetah',
    'task': 'v2',

    'log_dir': '~/ray_mopac/',
    'exp_name': 'entropysac',

    'kwargs': {
        'epoch_length': 1000,
        'train_every_n_steps': 1,
        'n_train_repeat': 40,
        'eval_render_mode': None,
        'eval_n_episodes': 1,
        'eval_deterministic': True,
    }
}
