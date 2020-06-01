# snapshot
Demo Project to manage AWS EC2 instances snapshots

## about

This prject is a demo, and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

shotty uses the configuration file created by the ASW cli. e.g.

'aws configure --profile shotty'

## running

'pipenv run "python shotty/shotty.py <command> <subcommand> <--project=PROJECT>"'

*command* is instances, volumes, or Snapshots
*subcommand* depends on commands
*project* is option
