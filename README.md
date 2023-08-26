# Twitter Data Pipeline using Airflow and AWS S3

This project is designed to extract data from Twitter using the Twitter API and load it into an AWS S3 bucket in CSV format. The pipeline is managed and orchestrated using Airflow.

🌟 For those who crave more, discover the **Advanced Twitter Data Pipeline** [right here](https://github.com/kishlayjeet/Zomato-Twitter-Sentiment-Analysis-Data-Pipeline). 🌟

## Architecture

![Architecture Image](https://imgur.com/mAjDOxl.png)

- [Twitter API](https://developer.twitter.com/en/docs/twitter-api)
- [Apache Airflow](https://airflow.apache.org)
- [Amazon S3](https://aws.amazon.com/s3/)

The Twitter API is used to collect data from Twitter. The data collected from the Twitter API is saved locally before being transferred to the landing bucket on AWS S3. The ETL jobs are written in Python and scheduled in Apache Airflow.

## Environment Setup

### Hardware Used

I used a local machine with the following specifications:

```bash
  Ubuntu OS
  4 vCores, 4 GiB Memory
  Storage: 32 GiB
```

### Prerequisites

- A Twitter developer account and API key
- An AWS account and S3 bucket set up
- Python 3
- Airflow
- tweepy
- pandas
- boto3

## Installation

1. Clone the repository

```bash
git clone https://github.com/kishlayjeet/Twitter-Data-Pipeline-using-Airflow-and-AWS-S3.git
```

2. Install the required packages

```bash
pip install -r requirements.txt
```

3. Create a `config.py` file in the root directory of the project and add the following variables:

```python
AccessKey = "[Your Twitter API key]"
AccessSecret = "[Your Twitter API secret key]"
BearerToken = "[Your Twitter API bearer token]"
ConsumerKey = "[Your Twitter access token]"
ConsumerSecret = "[Your Twitter access token secret]"

KEY = "[Your AWS access key]"
SECRET = "[Your AWS secret key]"
```

4. Update the `airflow.cfg` file to point to your `config.py` file and set the appropriate S3 bucket name.

## Usage

1. Start the Airflow webserver

```bash
airflow standalone
```

![Airflow Server](https://imgur.com/RM9bEZb.png)

2. Access Airflow through your browser using the default `8080` port.

3. In the Airflow UI, enable the `twitter_data_pipeline` DAG.

4. The pipeline will run on the schedule defined in the DAG and load the data into the specified S3 bucket in CSV format.

Example output:

| user     | username  | text                                            | like_count | reply_count | retweet_count | created_at                |
| :------- | :-------- | :---------------------------------------------- | :--------- | :---------- | :------------ | :------------------------ |
| elonmusk | Elon Musk | Je me souviens Pluto 🥹                          | 23794      | 4036        | 1802          | 2023-01-21 09:07:40+00:00 |
| elonmusk | Elon Musk | Twitter is the source of truth                  | 35278      | 2525        | 3756          | 2023-01-21 08:25:50+00:00 |
| elonmusk | Elon Musk | Notes Extremely important                       | 1116       | 74          | 75            | 2023-01-21 07:19:35+00:00 |
| elonmusk | Elon Musk | I’m reviewing it next week for possible release | 2134       | 166         | 165           | 2023-01-21 03:13:31+00:00 |
| elonmusk | Elon Musk | The debt trend is 🤯🤯                          | 2255       | 314         | 193           | 2023-01-21 00:27:49+00:00 |

## Notes

- The pipeline is currently set to extract data from a specific Twitter handle. You can update the `run_twitter_etl` function in `dags/twitter_etl.py` to extract data from other sources.
- The pipeline is currently set to load the data into a specific S3 bucket. You can update the `bucket_name` variable in `dags/twitter_etl.py` to load the data into other S3 buckets or in a different format.
- The pipeline is currently scheduled to run every seven days. You can update the `schedule_interval` in the DAG to run more or less frequently.

## Extras

- You can also check the output dataframe for a specific task by using `xcom_pull` from the `task_instance`.
- You can also check the S3 CSV file using the S3 bucket URL.
- You can also set up Airflow on other cloud platforms like GCP and Azure.

## Error Handling and Troubleshooting

- Airflow provides a UI for monitoring the status of tasks and DAG runs. In case of task failure, the UI displays the error message and the traceback, which can be used to troubleshoot the issue.
- Airflow also provides the option to retry failed tasks a certain number of times before marking them as failures. This can be configured in the DAG definition.
- In the `run_twitter_etl` function in `dags/twitter_etl.py`, you can include try-except blocks to catch and handle any errors that may occur while extracting data from the Twitter API.
- In case of issues with the S3 bucket, such as access denied or invalid credentials, check if the `config.py` file contains the correct AWS access key and secret key, and that the S3 bucket name is correctly configured in the `twitter_etl.py` file.
- Logs for the pipeline can also be found in the `logs/` directory. These logs can be useful in troubleshooting issues with the pipeline.

## Conclusion

In conclusion, this project provides a detailed guide on how to build a data pipeline using Airflow to extract data from the Twitter API, process it using pandas, and load it into an AWS S3 bucket in CSV format. By following the step-by-step instructions in this README, you should be able to set up and run the pipeline successfully.

## Important Considerations

It is important to note that this project is intended for educational or testing purposes. Before using the data in production, it is crucial to comply with Twitter's terms of service and any other relevant laws and regulations. It is also important to consider data privacy, security, and compliance in any production implementation.

## Future Enhancements

This project provides a solid foundation that can be further enhanced by adding more functionalities such as data cleaning, transformation, and analysis. It can also be integrated with other systems and services, such as data warehousing, machine learning, and visualization tools, to enable more advanced use cases.

## Author

Thank you for using this data pipeline. If you have any questions, suggestions, or feedback, please don't hesitate to contact me at contact.kishlayjeet@gmail.com.
