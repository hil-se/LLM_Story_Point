# Usergrid – OpenAI RQ3 pairwise

To add **usergrid** to the RQ3 OpenAI results:

1. Run **`research questions/openai_rq3_zero_shot_pairwise.ipynb`** for dataset **usergrid** (pairwise input: `pairwise prediction/dataset/usergrid_pairwise.csv`).
2. Save the output CSV into this folder with a name like:  
   `openai_pairwise_zero_shot_usergrid_pairwise_YYYYMMDD_HHMMSS.csv`
3. Re-run **`research questions/RQ3_compute_accuracy.ipynb`** and the RQ3 batch summary script so **batch_summary_openai_rq3.csv** includes usergrid.
