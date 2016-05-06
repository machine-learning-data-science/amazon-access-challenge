# amazon-access-challenge
Our solution to Kaggle's Amazon Access Challenge.

## How to Run
Since we have saved the output of all of our individual models, it is easy to run the ensemble by itself. From the top level directory, simply run:

```bash
$ python rankedavg.py submission
```

The `submission` command line argument is the name of the file. The result will be saved to `output/submission.csv`
