Some future tasks:

- Configure and set stage and prod env, also move secrets to ENV file/secrets' manager service
- Connect stat. functions to some serverless service (e.g AWS lambda functions)
- Improve logging output and fix file creation
- Extract the plotting functionality to some more generic logic (another decorator?)
- Fix the data to be case-insensitive (Now one must use the exact casing as the DB)
- Add CICD
- Design and improve the data storage, currently the records are dated from the beginning of the data collection, 
  while the stat. are currently going far as 14 days back only
