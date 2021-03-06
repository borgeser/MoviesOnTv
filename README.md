# MoviesOnTv

The purpose of this repository is to warn you by email when a movie/show of your choice is scheduled on TV.

Yeah I know, Netflix, streaming... But not all movies are available on those platforms and I want to play it legally.

## Configuration

You'll need a Trello account to get the movies you want to search.
You'll also need a gmail account to send your mails. 
And you have to choose a recipient for those mails.

So the environments variables are used on this project:
* GMAIL_USERNAME: the username of your gmail account
* GMAIL_PASSWORD: the password of your gmail account
* EMAIL_RECIPIENT: the email address of the recipient of your mails
* TRELLO_API_KEY : the api key of your Trello account. See [here](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/) for more information.
* TRELLO_API_TOKEN : the api token of your Trello account.
* TRELLO_API_LIST_ID : the id of the list in Trello where you store the movies to search. 

By default the project fetches the French TV programs. You can modify the code in `programs_fetcher.py` for other program grids. 

## Deployment

`python main.py` will fetch the movies and print the results in the console.

`python routine.py` will do the job: fetch the movies and send an email if there is at least one movie scheduled on TV.
You can call it manually or (better) automatically with cron or some cloud scheduler.

Personally I use [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler).
