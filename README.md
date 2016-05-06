# amazon-access-challenge
Our solution to Kaggle's Amazon Access Challenge.

## How to Run
Since we have saved the output of all of our individual models, it is easy to run the ensemble by itself. From the top level directory, simply run:

```bash
$ python rankedavg.py submission
```

The `submission` command line argument is the name of the file. The result will be saved to `output/submission.csv`

If you wish to re-train the models, use the following steps:

- Run the starter code logistic regression

```bash
$ python reference-code/starter.py
```

When you are prompted to enter a name for the submission file, enter: `starter_submission`

- Run our models

```bash
$ python models.py
```

Then you can run `rankedavg.py` again to get the final ensembled submission.
