# amazon-access-challenge
Our solution to Kaggle's Amazon Access Challenge.

- [Running the Code](#how-to-run)

## How to Run
> Note: You must have [XGBoost](https://xgboost.readthedocs.io/en/latest/) installed in order to re-run the models. If you just wish to run the final ensemble, you do not need the library installed.

Since we have saved the output of all of our individual models, it is easy to run the ensemble by itself. From the top level directory, simply run:

```bash
$ python rankedavg.py submission
```

The `submission` command line argument is the name of the file. The result will be saved to `output/submission.csv`

If you wish to re-train the models, use the following steps:

**1. Run the starter code logistic regression**

First move into the `reference-code` directory.

```bash
$ cd reference-code/
```

Then, run the file.

```bash
$ python starter.py
```

When you are prompted to enter a name for the submission file, enter: `starter_submission`

**2. Run our models**

Go back to the top level directory.

```bash
$ python models.py
```

**3. Now you can run `rankedavg.py` again to get the final ensembled submission**
