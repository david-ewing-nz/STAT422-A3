# Configuration set for baseline and one-variable-at-a-time analysis

# from the optima run we define the baseline:
# [I 2025-05-23 04:06:01,900] Trial 17 finished with value: 0.7390999794006348 and parameters: {'filters': 128, 'kernel_size': 4, 'dense_units': 256, 'batch_size': 32, 'optimizer': 'nadam'}. Best is trial 17 with value: 0.7390999794006348.

configs = [
    
    {'run': 'baseline',             'optimizer': 'nadam',    'batch_size': 32, 'epochs': 12,  'filters': 128, 'kernel_size': 4, 'dense_units': 256}
]

# Training control parameter variations
configs += [
    {'run': 'optimizer : sgd',      'optimizer': 'sgd',     'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 128},
    {'run': 'optimizer : rmsprop',  'optimizer': 'rmsprop', 'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 128},
    {'run': 'optimizer : nadam',    'optimizer': 'adam',    'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 128},

    {'run': 'batch_size : 32',      'optimizer': 'adam',    'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 128},
    {'run': 'batch_size : 128',     'optimizer': 'adam',    'batch_size': 128,'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 128},

    {'run': 'epochs : 10',          'optimizer': 'adam',    'batch_size': 64, 'epochs': 10,  'filters': 64, 'kernel_size': 5, 'dense_units': 128},
 #  {'run': 'epochs : 8',           'optimizer': 'adam',    'batch_size': 64, 'epochs': 8,  'filters': 64, 'kernel_size': 5, 'dense_units': 128},
    {'run': 'epochs : 15',          'optimizer': 'adam',    'batch_size': 64, 'epochs': 12, 'filters': 64, 'kernel_size': 5, 'dense_units': 128} 

 #  {'run': 'learning_rate : 0.0001','optimizer': 'adam',   'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 128},
 #  {'run': 'learning_rate : 0.01',  'optimizer': 'adam',   'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 128}
]

# Hyperparameter variations
configs += [
    {'run': 'kernel_size : 3',      'optimizer': 'adam',    'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 3, 'dense_units': 128},
    {'run': 'kernel_size : 4',      'optimizer': 'adam',    'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 4, 'dense_units': 128},

    {'run': 'filters : 32',         'optimizer': 'adam',    'batch_size': 64, 'epochs': 12,  'filters': 32, 'kernel_size': 5, 'dense_units': 128},
    {'run': 'filters : 128',        'optimizer': 'adam',    'batch_size': 64, 'epochs': 12,  'filters': 128,'kernel_size': 5, 'dense_units': 128},

    {'run': 'dense_units : 64',     'optimizer': 'adam',    'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 64},
    {'run': 'dense_units : 256',    'optimizer': 'adam',    'batch_size': 64, 'epochs': 12,  'filters': 64, 'kernel_size': 5, 'dense_units': 256}
]
