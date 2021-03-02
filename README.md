# MoviesOnTv

The purpose of this repository is to warn you by email when a movie/show of your choice is scheduled on TV.

Yeah I know, Netflix, streaming... But not all movies are available on those platforms and I want to play it legally.

## Configuration

You'll need a gmail account to send your mails. And you have to choose a recipient for those mails.

So three environments variables are used on this project:
* GMAIL_USERNAME: the username of your gmail account (the one which will send you emails)
* GMAIL_PASSWORD: the password of your gmail account
* EMAIL_RECIPIENT: the email of the recipient of your mails

You can modify the list of movies you want to follow in the variable `movies_to_search` in `routine.py`.

By default the project fetches the French TV programs. You can modify the code in `controller.py` for other program grids. 

## Deployment

`python routine.py` will do the job.
You can call it manually or (better) automatically with cron or some cloud scheduler.

Personally I use [Heroku Scheduler](https://devcenter.heroku.com/articles/scheduler).

## Next step

* Extract the movies titles in a simple and accessible "database"
* Replace main() function by something useful
