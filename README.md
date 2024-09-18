# HoopSoup
## Objective:
- Create an API for basketball-reference.com's per-season player stats.
### Problem:
- basketball-reference (bbref) is a go-to source for basketball statistics. **However**, bbref simply provides the data to view through its website without common developer resources, meaning that viewing, gathering, aggregating data provided can be difficult.
## Tech:
- Python 3
- MongoDB (Atlas)
- GraphQL (Graphene, GrapheneMongo)
#### Run it locally
Prerequisites:
1. If you do not have Python installed you can install [here](https://www.python.org/downloads/)
2. This project runs MongoDB using [Atlas (free)](https://www.mongodb.com/cloud/atlas/register) - I don't think the hosting service matters...but I set my instance up to use AWS
3. You will need to create an `.env` file at the top level (e.g. `/HoopSoup/.env`) where you will need to define variables `MONGO_USER`, `MONGO_PASSWORD`, and `MONGO_CONNECTION_STRING` - you can get your connection string from Atlas (replace username and password with `{mongo_user}` and `{mongo_password}` in `.env`'s `MONGO_CONNECTION_STRING`)
4. install Python dependencies
   ```
   > pip install -r requirements.txt
   ```

Popuating MongoDB:
1. to populate your MongoDB database you can run the `BbrefScraper.py` script
   
   ```
   > python -m scrapers.BbrefScraper --metric=per_g --start=2024 --end=2024 --source=url --debug
   ```
   - `metric` defines the specific metric we want to pull data for
   - `start` defines the start of the years range we want to start with to pull data for
   - `end` defines the end (inclusive) of the years range to pull data for
   - `source` defines where to pull data from. `url` will pull from Bbref site. `html` will read in html files saved from using `--debug`
   - `--debug` will save html files and json stats files to provide some visibility in what the scraper is pulling and parsing. it bypasses saving to the database
   - you can use `--help` to view further info

Running the GraphQL API:
1. to run the GraphQL API simply run the command
   ```
   > python -m api.graphql.api
   ```
2. You should now be able to go to `27.0.0.1:5000/graphql` for the interactive GraphiQL interface and begin querying data!
3. example query that will query for Doncic's Per Game stats for the 2022 season:
```
{
    allPerG(season: 2022,name: "doncic") {
        edges {
            node {
                season
                name
                stats {
                    fga
                    fg
                    fg2a
                    fg2
                    fg3a
                    fg3
                }
            }
        }
    }
}
```