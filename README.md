# Weekend-travel

The project ranks weekend places to visit in a specific city based on Google review ratings, time needed to visit, and other factors. The ranking is performed using pandas library.

## Libraries Used
- **pandas**: Used for data manipulation and analysis

## Instructions to run the code
1. **Install Dependencies**: Make sure you have python installed on your system. You can download it from [python.org](https://www.python.org/downloads/). The code relies on the pandas library, which can be installed using pip:
```python
pip install pandas
```
2. **Download the Dataset**: Place the CSV file containing the dataset in same directory as the Python Script
3. **Run the code**: Execute the Python script `Travel.py`. You can do this via the command line:
```python
python Travel.py
```
This will print the top weekend places to visit in the specified city based on the provided dataset.
4. **Customisation** You can customise the weights assigned to different feature for ranking by modifying the `weights` dictionary in the `rank_weekend_places` function.

## Sample Output
upon running the code, you'll see the top ranked places to visit in the specified city along with their names, types and scores
