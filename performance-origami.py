def origami(height, width, height_folds, width_folds):
    if height_folds:
        height = round(height / 2,1)
        if height > 0.1:
            print('{}cm*{}'.format(height, width))
            origami(height, width, height_folds=False, width_folds=True)
    if height_folds:
        width =  round(width / 2,1)
        if width > 0.1:
            print('{}cm*{}'.format(height, width))
            origami(height, width, height_folds=True, width_folds=False)
    




height = 20
width = 20
origami(height, width, height_folds=True, width_folds=False)